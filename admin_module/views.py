from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.http import Http404
from sympy.functions.elementary.complexes import re
from django.contrib.auth.decorators import login_required
from django.utils.decorators import  method_decorator
from django.urls import reverse_lazy
from Database.models import Event,User,Student,Alumni,Faculty
from  admin_module.forms import EventForm,UserForm
from django.shortcuts import redirect
from AlumniManagement import settings
from django.forms import inlineformset_factory
from django.db.models import prefetch_related_objects
from .forms import forms
from django.db.models import  Q
def get_filtered_row_set(search_term,uid):
    search_fields = fields = ['name', 'info', 'createdBy__username', 'created_date']

    fields = [f for f in search_fields]
    queries = [Q(**{str(f + '__icontains'): search_term}) for f in fields]

    qs = Q()
    for query in queries:
        qs = qs | query

    qs = qs & (Q(**{'active_flag': True})) & (Q(**{'createdBy':uid}))

    events = Event.objects.filter(qs)

    return events
# Create your views here.
class EventDelete(DeleteView):
    model=Event

    def get_success_url(self):
        obj = super(EventDelete,self).get_object()


        if obj.event_news_flag==True:
           # print obj.event_info
            success_url=reverse_lazy("view-event")
        else:
            success_url = reverse_lazy("view-news")
        return success_url

@login_required
def view_event(request):
    event_list=Event.objects.all()
    eventsList=[]

    for eve in event_list:
        if eve.event_news_flag==True:
            eventsList.append(eve)
        event_dict={'event_name':eventsList}
    return render(request,'AlumniManagement/viewEvent.html',context=event_dict)
    #return render(request,'web/index.html')






@login_required
def view_news(request):
    news_List=Event.objects.all()
    newsList=[]
    for news in news_List:
        if news.event_news_flag==False:

            newsList.append(news)
        news_dict={'news_name':newsList}
    return render(request,'AlumniManagement/viewNews.html',context=news_dict)

@login_required
def createEvent(request):
    model = Event
    fields=['event_name','event_info','createdBy','event_news_flag']
    def get_object(self,form):
        user=self.request.user.ADMIN

        i
    def form_valid(self,form):
        user=self.request.user.ADMIN
        return super(createEvent,self).form_valid(form)
    @method_decorator(login_required)
    def dispatch(self,*args,**kwargs):
        return super(createEvent,self).dispatch(*args,**kwargs)


    #return render(request,'AlumniManagement/event_form.html')
@login_required
def form_name_view(request):
    form=EventForm()

    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            if form.cleaned_data['event_news_flag']==True:
                return view_event(request)
            else:
                return view_news(request)
            #print (" event_news_flag"+form.cleaned_data['event_news_flag'])
    return render(request,'AlumniManagement/event_formpage.html',{'form':form})

@login_required
def createUser(request):
    form=UserForm()
    if request.method =='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return viewUsers(request)
    return render(request,'AlumniManagement/user_formpage.html',{'form':form})


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy("view-event")

@login_required
def viewEvent(request,pk):

    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL, request.path)

    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        raise Http404("The Event you are searching for does not exists")

    return render(
        request,
        'AlumniManagement/viewEvent.html'

    )


class EventUpdate(UpdateView):
    news_event_flag = False
    model = Event
    fields = ['name','info']
    template_name_suffix = '_update_form'


    def get_success_url(self):
        obj = super(EventUpdate,self).get_object()


        if obj.event_news_flag==True:
           # print obj.event_info
            success_url=reverse_lazy("view-event")
        else:
            success_url = reverse_lazy("view-news")
        return success_url


class UserUpdate(UpdateView):
    model=User
    form=UserForm
    #template_name= 'AlumniManagement/user_update_form.html'
    '''def get_queryset(self):
    if self.request.user.user_type_flag=='Student' :
        return Student
    if self.request.user.user_type_flag=='Faculty':
        return Faculty
    if self.request.user.user_type_flag=='Alumni':
        return Alumni'''

    fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type_flag',

             ]
    template_name_suffix = '_update_form'


    success_url = reverse_lazy("view-users")


def manage_user(request, id):
    user = User.objects.get(kwargs=id)
    UserInlineFormSet = inlineformset_factory(User, Student,Faculty,Alumni ,fields=('username','first_name','last_name','email','phone_number'))
    if request.method == "POST":
        formset = BookInlineFormSet(request.POST, request.FILES, instance=user)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(user.get_absolute_url())
    else:
        formset = UserInlineFormSet(instance=user)
    return render(request, 'AlumniManagement/user_update_form.html', {'formset': formset})

def viewUsers(request):
    user_list=User.objects.all()
    userList=[]

    for user in user_list:
        userList.append(user)
        user_dict={'user_name':userList}
    return render(request,'AlumniManagement/viewUsers.html',context=user_dict)


@login_required
def searchEvent(request):

    try:
        query=request.GET['search_box']
    except:
        query=''

    if not query:
        return redirect('view-event')
    else:
        event=get_filtered_row_set(query,request.user.pk)

    return render(
        request,
        'AlumniManagement/viewEvent.html',
        context={'event_name': event, }
    )

@login_required
def searchNews(request):

    try:
        query=request.GET['search_box']
    except:
        query=''

    if not query:
        return redirect('view-news')
    else:
        news=get_filtered_row_set(query,request.user.pk)

    return render(
        request,
        'AlumniManagement/viewNews.html',
        context={'news_name': news, }
    )



def manageUser(request,self):
    #user=User.objects.get(pk=self.id)
    #print user.phone_number
    UserformSet=inlineformset_factory(User,Student,fields=('department_name','branch_name',))
    if request.method=="POST":
        formset=UserformSet(request.POST,request.FILES,instance=user)
        if formset.is_valid():
            formset.save()
            success_url = reverse_lazy("view-users")
            return success_url
    else:
           formset=UserformSet(instance=user)

    return render(request,'AlumniManagement/user_update.html',{'formset':formset})