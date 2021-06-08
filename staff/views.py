import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView
from staff.forms import UserForm, UserFormUpdate
from staff.models import Request, Staff
from user.models import User
from vehicle.models import Vehicle, Branches


def add_staff(request):
    user = User.objects.all()
    form = UserForm

    context = {
        'users': user,
        'form' : form
    }

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.instance.set_password(form.instance.password)
            form.save()
        Staff.objects.create(
            staff=form.instance
        )
    return redirect(reverse_lazy('vehicle:general_manager_view'))


def staff_view(request):
    requests=Request.objects.all()
    context = {
        'requests':requests
    }
    return render(request, 'vehicle/staff_page.html', context)


def change_user_type(request, id):
    queryset = User.objects.get(id=id)
    form = UserFormUpdate(instance=queryset)

    context = {
        'queryset':queryset,
        'form':form
    }

    if request.method == 'POST':
        form = UserFormUpdate(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
        return redirect(reverse_lazy('vehicle:manager_staff_list'))
    return render(request, 'vehicle/staff_update.html', context)


def make_request(request):
    reason = request.POST.get('reason')
    day_needed = request.POST.get('day_needed')
    cdate = datetime.datetime.strptime(day_needed, "%Y-%m-%d").date()
    request_by = Staff.objects.get(staff=request.user)
    if request.method == "POST":
        new_request = Request.objects.create(
            requested_by=request_by,
            reason=reason,
            day_needed=cdate,
            response='Pending',
        )
    return redirect(reverse_lazy('staff:staff_view'))


def staff_respond_request(request, id):
    requestt = Request.objects.get(id=id)

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'receive':
            requestt.vehicle_assigned.available = False
            requestt.time_received = timezone.now()
            requestt.response = 'VehReceived'
            requestt.save()
            return redirect(reverse_lazy('staff:staff_view'))

        elif form_type == 'return':
            requestt.response = 'Completed'
            requestt.save()
            return redirect(reverse_lazy('staff:staff_view'))

        elif form_type == 'cancel':
            requestt.response = 'Canceled'
            requestt.save()
            return redirect(reverse_lazy('staff:staff_view'))
    return redirect(reverse_lazy('staff:staff_view'))