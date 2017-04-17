from django.shortcuts import render
from django.http import HttpResponse
from  django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from Database.models import User,Alumni,Student,Faculty,Opportunities,Complaints,Emails
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib.admin import widgets
from django import forms
from django.forms import extras
from django.db.models import  Q
from django.shortcuts import redirect
from AlumniManagement import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import EmailMessage


class ComplaintUpdate(UpdateView):
    model=Complaints
    fields=['complaint_category','complaint_info']


    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ComplaintUpdate, self).get_object()
        if ( not self.request.user.user_type_flag=='admin') and (not obj.created_by == self.request.user):
            raise Http404

        if self.request.user.user_type_flag=='admin':
            self.fields.append('solution_info')

        return obj

    def form_valid(self, form):

        return super(ComplaintUpdate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ComplaintUpdate, self).dispatch(*args, **kwargs)


class ComplaintCreate(CreateView):
    model = Complaints
    fields = ['complaint_category','complaint_info']

    def form_valid(self, form):
        user = self.request.user

        form.instance.created_by = user
        return super(ComplaintCreate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ComplaintCreate, self).dispatch(*args, **kwargs)


class ComplaintDelete(DeleteView):
    model = Complaints
    success_url = reverse_lazy("viewComplaints")

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ComplaintDelete, self).get_object()
        if not obj.created_by == self.request.user:
            raise Http404
        return obj

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ComplaintDelete, self).dispatch(*args, **kwargs)


@login_required
def viewComplaints(request):

    try:
        complaint = Complaints.objects.filter(created_by=request.user.pk)
    except Complaints.DoesNotExist:
        raise Http404("Keep visiting as of now no complaints are posted")

    return render(
        request,
        'AlumniManagement/ComplaintListView.html',
        context={'complaints': complaint, }
    )

@login_required
def viewComplaint(request,pk):

    try:
        complaint = Complaints.objects.get(pk=pk)
    except Complaints.DoesNotExist:
        raise Http404("The complaint which you are searching for does not exists")

    return render(
        request,
        'AlumniManagement/ComplaintDetail.html',
        context={'complaint': complaint, }
    )


@login_required
def searchComplaint(request):

    try:
        query=request.GET['search_box']
    except:
        query=''

    if not query:
        return redirect('viewComplaints')
    else:
        complaints=get_filtered_row_set(query,request.user.pk)

    return render(
        request,
        'AlumniManagement/ComplaintListView.html',
        context={'complaints': complaints, }
    )


def get_filtered_row_set(search_term,uid):
    search_fields = fields = ['complaint_info', 'solution_info', 'created_by__username', 'created_date']

    fields = [f for f in search_fields]
    queries = [Q(**{str(f + '__icontains'): search_term}) for f in fields]

    qs = Q()
    for query in queries:
        qs = qs | query

    qs = qs & (Q(**{'active_flag': True})) & (Q(**{'created_by':uid}))

    complaints = Complaints.objects.filter(qs)

    return complaints


@receiver(post_save, sender=Complaints)
def post_save_course_dosomething(sender,instance, **kwargs):
    complaint_category=instance.complaint_category

    emailId=Emails.objects.filter(name=complaint_category)
    recievers_mail_id = emailId[0].email_id
    subject='A complaint has been logged'
    body='A complaint has been logged by ' + instance.created_by.username + '. TO view the complaint go to http://127.0.0.1:8000/Complaints/' + (str)(instance.pk) +'/viewComplaint/'
    email = EmailMessage(subject, body, to=[recievers_mail_id])
    email.send()