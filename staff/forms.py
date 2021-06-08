from django.forms import *
from user.models import *
from .models import *


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput(attrs={'required': True}), label= 'Password')

    class Meta:
        model= User
        fields = ('staff_id', 'first_name', 'last_name', 'user_type', 'password')

    def clean_staff_id(self):
        staff_id = self.cleaned_data.get('staff_id')

        try:
            User.objects.get(staff_id=staff_id)
            raise ValidationError('Staff with this staff id already exist')
        except User.DoesNotExist:
            pass
        return staff_id


class UserFormUpdate(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'user_type',)