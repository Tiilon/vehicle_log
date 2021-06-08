from django.forms import *
from vehicle.models import *


class BranchForm(ModelForm):
    class Meta:
        model = Branches
        fields = ('location',)

    def clean_location(self):
        location = self.cleaned_data.get('location')

        try:
            Branches.objects.get(location=location)
            raise ValidationError('This branch already exist')
        except Branches.DoesNotExist:
            pass
        return location


class MaintenanceForm(ModelForm):
    class Meta:
        model = Maintenance
        fields = ('reason',)


class MaintenanceReturnForm(ModelForm):
    class Meta:
        model = MaintenanceReturn
        fields = ('maintenance',)


class NewCarForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ('brand', 'name', 'colour', 'yr_of_manufacture', 'procurement_date', 'registration_number', 'image')

        widgets = {
            'procurement_date': DateInput(attrs={'type': 'date'}),
            'yr_of_manufacture': DateInput(attrs={'type': 'date'})
        }