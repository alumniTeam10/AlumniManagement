from django.shortcuts import render
from django.http import HttpResponse
from  django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from Database.models import User,Alumni,Student,Faculty,Opportunities,Emails,Connections
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


class OpportunityUpdate(UpdateView):
    model=Opportunities
    fields=['opportunity_info','number_of_vacancy','expiration_date','active_flag']

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(OpportunityUpdate, self).get_object()
        if not obj.posted_by == self.request.user:
            raise Http404
        return obj

    def form_valid(self, form):
        if form.instance.number_of_vacancy < 0:
            form.instance.number_of_vacancy=0
        return super(OpportunityUpdate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OpportunityUpdate, self).dispatch(*args, **kwargs)



class OpportunityCreate(CreateView):
    model = Opportunities
    fields = ['opportunity_info', 'number_of_vacancy', 'expiration_date', 'active_flag']

    def form_valid(self, form):
        user = self.request.user

        if form.instance.number_of_vacancy < 0:
            form.instance.number_of_vacancy=0

        form.instance.posted_by = user
        return super(OpportunityCreate, self).form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OpportunityCreate, self).dispatch(*args, **kwargs)


class OpportunityDelete(DeleteView):
    model = Opportunities
    success_url = reverse_lazy("viewOpportunities")

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(OpportunityDelete, self).get_object()
        if not obj.posted_by == self.request.user:
            raise Http404
        return obj

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OpportunityDelete, self).dispatch(*args, **kwargs)


@login_required
def viewOpportunities(request):

    try:
        opportunity = Opportunities.objects.all()
    except Opportunities.DoesNotExist:
        raise Http404("Keep visiting as of now no opportunities are posted")

    return render(
        request,
        'AlumniManagement/OpportunityListView.html',
        context={'opportunities': opportunity, }
    )

@login_required
def viewOpportunity(request,pk):

    try:
        opportunity = Opportunities.objects.get(pk=pk)
    except Opportunities.DoesNotExist:
        raise Http404("The Opportunity which you are searching for does not exists")

    return render(
        request,
        'AlumniManagement/OpportunityDetail.html',
        context={'opportunity': opportunity, }
    )

@login_required
def searchOpportunity(request):

    try:
        query=request.GET['search_box']
    except:
        query=''

    if not query:
        return redirect('viewOpportunities')
    else:
        opportunities=get_filtered_row_set(query)

    return render(
        request,
        'AlumniManagement/OpportunityListView.html',
        context={'opportunities': opportunities, }
    )

def get_filtered_row_set(search_term):
    search_fields = ['opportunity_info', 'posted_by__first_name','posted_by__last_name','posted_by__email']

    fields = [f for f in search_fields]
    queries = [Q(**{str(f + '__icontains'): search_term}) for f in fields]

    qs = Q()
    for query in queries:
        qs = qs | query

    qs = qs & (Q(**{'active_flag': True}))

    opportunities = Opportunities.objects.filter(qs)

    return opportunities


@receiver(post_save, sender=Opportunities)
def post_save_opportunities_send_mails(sender,instance, **kwargs):
    posted_by_id=instance.posted_by

    mailing_list=Connections.objects.filter(following=posted_by_id)

    recievers_mail_id=get_mail_ids_as_list(mailing_list)
    send_mails(recievers_mail_id,instance)



def get_mail_ids_as_list(mailing_list):

    mail_id_list=[]

    for conection in mailing_list:
        mail_id_list.append(conection.follower.email)

    return mail_id_list


def send_mails(recievers_mail_id,instance):
    subject = instance.posted_by.first_name + ' has posted in Opportunities'
    body = 'An opportunity has been posted by ' + instance.posted_by.first_name + ' ' + instance.posted_by.last_name + '. To view the complaint go to http://127.0.0.1:8000/Opportunity/' + (
    str)(instance.pk) + '/viewOpportunity/'
    email = EmailMessage(subject, body, to=recievers_mail_id)
    try:
        email.send()
    except:
        pass