from django import template

from staff.models import Request
from vehicle.models import Vehicle

register = template.Library()


@register.simple_tag()
def percen():
    num = Vehicle.objects.filter(available=True).count()
    total = Vehicle.objects.all().count()
    percentage_avail = (num/total) * 100
    percentage_unavail = 100 - percentage_avail
    return {
        'percentage_avail' : percentage_avail,
        'percentage_unavail': percentage_unavail,
        'num': num
    }


@register.simple_tag()
def cars_on_road_percen():
    cor = Vehicle.objects.filter(on_road=True).count()
    total = Vehicle.objects.all().count()
    percentage_avail = (cor / total) * 100
    percentage_unavail = 100 - percentage_avail
    return {
        'percentage_avail' : percentage_avail,
        'percentage_unavail': percentage_unavail,
        'cor':cor
    }


@register.simple_tag()
def cars_maintain_percen():
    com = Vehicle.objects.filter(sent_for_maintenance=True).count()
    total = Vehicle.objects.all().count()
    percentage_avail = (com / total) * 100
    percentage_unavail = 100 - percentage_avail
    return {
        'percentage_avail' : percentage_avail,
        'percentage_unavail': percentage_unavail,
        'com':com
    }


@register.simple_tag(takes_context=True)
def reqs_percen(context):
    reqs = Request.objects.all().count()
    total = Vehicle.objects.all().count()
    percentage_avail = (int(reqs) / total) * 100
    percentage_unavail = 100 - percentage_avail
    return {
        'percentage_avail': percentage_avail,
        'percentage_unavail': percentage_unavail,
        'reqs': reqs
    }