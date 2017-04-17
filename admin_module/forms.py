from django import forms
from django.core import validators
from  Database.models import  Event,User,Student,Faculty,Alumni
from django.forms.models import inlineformset_factory
class EventForm(forms.ModelForm):
    class Meta():
        model=Event
        fields='__all__'
    '''event_name = forms.CharField()
    event_info= forms.CharField(widget=forms.Textarea)
    expiration_date=forms.DateField()
    createdBy=forms.CharField()
    event_news_flag=forms.BooleanField()
    created_date=forms.DateField()
    updated_date=forms.DateField()
    active_flag=forms.BooleanField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])'''

class UserEditForm(forms.ModelForm):
    class Meta:
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type_flag']


class StudentForm(forms.ModelForm):
    class Meta:
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type_flag',
                  'branch_name', 'course_name']


class FacultyForm(forms.ModelForm):
    class Meta:
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type_flag',
                  'department_name', 'designation']


class AlumniForm(forms.ModelForm):
    class Meta:
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type_flag',
                  'branch_name', 'course_name']

class UserForm(forms.ModelForm):
    class Meta():
        def getUser(self):
            user = User.objects.get(pk=self.user_id)
            print user.phone_number
            print user.user_type_flag
            # fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type_flag']
            if (user.user_type_flag == Alumni):
                model = Alumni
                fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type_flag',
                          'branch_name', 'course_name']


            elif (user.user_type_flag == Faculty):
                model = Faculty
                fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type_flag',
                          'department_name', 'designation']

            elif (user.user_type_flag == Student):
                model = Student
                fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type_flag',
                          'branch_name', 'course_name']

            else:
                fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type_flag']

        model=User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type_flag']

