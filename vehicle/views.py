from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView
from staff.forms import UserForm
from staff.models import Request, Staff
from user.models import User
from vehicle.forms import *
from vehicle.models import Vehicle, Branches
import datetime


def admin_layout(request):
    reqs = Request.objects.all()
    context = {
        'reqs': reqs
    }
    return render(request, 'layout/admin_layout.html', context)


def g_manager_view(request):
    form1 = UserForm
    form2 = BranchForm
    form3 = NewCarForm
    error = ''
    cars = Vehicle.objects.all()

    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'error': error,
        'cars': cars,
    }

    if request.method == 'POST':
        form = request.POST.get('form')
        if form == 'form2':
            form = BranchForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect(reverse_lazy('vehicle:general_manager_view'))

        elif form == 'form3':
            form = NewCarForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect(reverse_lazy('vehicle:general_manager_view'))
    return render(request, 'vehicle/g_manager_page.html', context)


def staff_list_gm(request):
    staff = User.objects.all()

    context = {
        'staff':staff,
    }
    return render(request, 'vehicle/g_manager_staff_list.html', context)


def make_manager(request, id):
    user = User.objects.get(id=id)
    branches = Branches.objects.all()
    if request.method == "POST":
        # try:
        #     staff = Staff.objects.get(staff=user)
        # except Staff.DoesNotExist:
        #     pass
        # staff = Staff.objects.get(staff=user)
        # for sth in branches:
        #     if staff.branch == sth:
        #         staff.branch = None
        user.user_type = "M"
    return redirect(reverse_lazy('vehicle:manager_staff_list'))


def branch_manager_view(request, id):
    branch_manager = User.objects.get(id=id)
    branch = Branches.objects.get(manager=branch_manager)
    cars = Vehicle.objects.filter(branch=branch)

    context = {
        'branch_manager':branch_manager,
        'branch':branch,
        'cars':cars,
    }
    return render(request, 'vehicle/b_manager_view.html', context)


def car_details(request, id):
    car = Vehicle.objects.get(id=id)
    branches = Branches.objects.all()
    form = MaintenanceForm
    maintenance_due_date = datetime.timedelta(days=30)

    context = {
        'car': car,
        'branches': branches,
        'form1': form,
        'last_maintain': '',
        'error': '',
    }
    try:
        diff = timezone.now() - car.last_maintained
        if car.last_maintained is None:
            context['last_maintain'] = ''
        elif diff > maintenance_due_date:
            context['error'] = 'This vehicle is due for maintenance'
        else:
            context['last_maintain'] = diff
    except:
        pass

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'make_m':
            form = MaintenanceForm(request.POST)
            if form.is_valid():
                form.instance.vehicle = car
                form.instance.approved_by = request.user
                car.sent_for_maintenance = True
                car.available = False
                car.save()
                form.save()
                return redirect(reverse_lazy('vehicle:car_details', kwargs={'id': id}))
        elif form_type == 'receive_m':
            form2 = MaintenanceReturnForm(request.POST)
            if form2.is_valid():
                form2.instance.received_by = request.user
                form2.save()
            car.last_maintained = form2.instance.date_created
            car.sent_for_maintenance = False
            car.available = True
            car.save()
            return redirect(reverse_lazy('vehicle:car_details', kwargs={'id': id}))
    return render(request, 'vehicle/car_details.html',context)


def assign_car_branch(request, id):
    car = Vehicle.objects.get(id=id)

    if request.method == "POST":
        branch = Branches.objects.get(id=request.POST.get('branch'))
        car.branch = branch
        car.save()
    return redirect(reverse_lazy('vehicle:car_details', kwargs={'id':id}))


def branch_list(request):
    branches = Branches.objects.all()

    context = {
        'branches':branches,
    }
    return render(request, 'vehicle/branches.html', context)


def branch_details(request, id):
    branch = Branches.objects.get(id=id)
    error = ''
    managers = User.objects.filter(user_type='M')
    cars = Vehicle.objects.filter(branch=branch)
    staff = User.objects.filter(user_type='St')
    staf = Staff.objects.filter(branch=branch, staff__user_type='St')

    context = {
        'branch': branch,
        'staff': staff,
        'managers': managers,
        'cars': cars,
        'staf':staf
    }
    if request.method == "POST":
        form_type = request.POST.get('form_type')
        try:
            user = User.objects.get(id=request.POST.get('user'))
            if branch.manager == user:
                error = "Staff already the branch manager"
                context['error'] = error
                return render(request, 'vehicle/branch_details.html', context)
        except User.DoesNotExist:
            pass
        if form_type == 'manager':
            user = User.objects.get(id=request.POST.get('user'))
            b = Branches.objects.all()
            for s in b:
                if s.manager == user:
                    error = f'Staff already the manager of {s.location} branch'
                    context['error'] = error
                    return render(request, 'vehicle/branch_details.html', context)

            branch.manager = user
            branch.save()

        elif form_type == 'staff':
            user = User.objects.get(id=request.POST.get('staff'))
            staff = Staff.objects.get(staff=user)
            if staff.branch == branch:
               error = 'Staff already in branch'
               context['error'] = error
               return render(request, 'vehicle/branch_details.html', context)
            staff.branch = branch
            staff.save()
    return render(request, 'vehicle/branch_details.html', context)


def remove_manager(request, id):
    branch = Branches.objects.get(id=id)

    if request.method == 'POST':
        if branch.manager:
            branch.manager = None
            branch.save()
    return redirect(reverse_lazy('vehicle:branch_details', kwargs={'id': id}))


def manager_request(request, id):
    branch = Branches.objects.get(id=id)
    requests = Request.objects.filter(requested_by__branch=branch)

    context = {
        'branch':branch,
        'requests':requests,
    }
    return render(request, 'vehicle/branch_reqs.html', context)


def respond_request(request, id):
    requestt = Request.objects.get(id=id)
    vehicles = Vehicle.objects.filter(branch=requestt.requested_by.branch)
    context = {
        'requestt':requestt,
        'vehicles':vehicles
    }
    if request.method == "POST":
        form_type = request.POST.get('form_type')

        if form_type == 'assign':
            vehicle = Vehicle.objects.get(id=request.POST.get('vehicle'))
            requestt.vehicle_assigned = vehicle
            requestt.response = 'Approved'
            vehicle.available = False
            vehicle.on_road = True
            requestt.vehicle_issued_by = request.user
            vehicle.save()
            requestt.save()
            return redirect(reverse_lazy('vehicle:respond_request', kwargs={'id':id}))

        elif form_type == 'decline':
            requestt.response = "Declined"
            requestt.save()
            return redirect(reverse_lazy('vehicle:respond_request', kwargs={'id': id}))

        elif form_type == 'complete':
            requestt.response = 'Received'
            requestt.time_of_return = timezone.now()
            requestt.vehicle_assigned.on_road = False
            requestt.vehicle_assigned.available = True
            requestt.save()
            return redirect(reverse_lazy('vehicle:respond_request', kwargs={'id': id}))
    return render(request, 'vehicle/respond_request.html', context)


def branch_staff_list(request, id):
    branch = Branches.objects.get(id=id)
    branch_staff = Staff.objects.filter(branch=branch, staff__user_type='St')
    context = {
        'branch':branch,
        'branch_staff':branch_staff,
    }
    return render(request, 'vehicle/branch_staff_list.html', context)


def all_req(request):
    req= Request.objects.all()
    context = {
        'reqs':req
    }
    return render(request, 'vehicle/all_reqs.html', context)