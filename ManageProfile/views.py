from django.shortcuts import render
from django.http import HttpResponse
from  django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from Database.models import User,Alumni,Student,Faculty
from  django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@login_required
def view(request):
    context = {}
    return render(request, 'AlumniManagement/profile.html', context)

@login_required
def editProfile(request):
    return HttpResponse('<h1>Jai Guru Umesh !!!</h1>')


def get_profile_update_model(type_of_user):
    if type_of_user=='student':
        model=Student
        fields=['user_id__first_name','user_id__last_name','user_id__email','user_id__phone_number','user_id__profile_dp','user_id__introduction']
    elif type_of_user=='alumni':
        model = Alumni
        fields = ['user_id__first_name', 'user_id__last_name', 'user_id__email', 'user_id__phone_number','user_id__profile_dp', 'user_id__introduction','current_organization_name','designation','role','work_phone']
    elif type_of_user=='faculty':
        model = Student
        fields = ['user_id__first_name', 'user_id__last_name', 'user_id__email', 'user_id__phone_number','user_id__profile_dp', 'user_id__introduction','designation']

    return model,fields


class ProfileUpdate(UpdateView):
    model=''
    fields=''

    # def __init__(self, *args, **kwargs):

        # super(ProfileUpdate, self).__init__(*args, **kwargs)


    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        self.model, self.fields = get_profile_update_model(self.request.user.user_type_flag)
        obj = super(ProfileUpdate, self).get_object()

        if not obj.pk == self.request.user.pk:
            raise Http404
        return obj

    def form_valid(self, form):
        if form.instance.number_of_vacancy < 0:
            form.instance.number_of_vacancy=0
        return super(ProfileUpdate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileUpdate, self).dispatch(*args, **kwargs)