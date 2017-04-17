from django.shortcuts import render
from django.http import HttpResponse

from Database.models import User,Student,Faculty,Alumni,Connections
from django.template import loader
from django.db.models import  Q
from django.shortcuts import redirect
from AlumniManagement import settings
from django.contrib.auth.decorators import login_required

def get_row_set(type_of_user):
    if type_of_user=='student':
        row_set=Student.objects.all()
    elif type_of_user=='alumni':
        row_set = Alumni.objects.all()
    elif type_of_user=='faculty':
        row_set = Faculty.objects.all()

    return row_set


def get_search_fields(type_of_user):

    if type_of_user=='student':
        search_fields = ['department_name', 'branch_name', 'course_name', 'admission_date','user_id__email','user_id__first_name','user_id__last_name']
    elif type_of_user=='alumni':
        search_fields = ['department_name', 'branch_name', 'course_name', 'admission_date','passout_date','current_organization_name','designation','role','user_id__email','user_id__first_name','user_id__last_name']
    elif type_of_user=='faculty':
        search_fields = ['department_name', 'designation','user_id__email','user_id__first_name','user_id__last_name']

    return search_fields


def get_filtered_row_set(type_of_user,search_term):

    search_fields=get_search_fields(type_of_user)

    queries = [Q(**{str(f + '__icontains'): search_term}) for f in search_fields]

    qs = Q()
    for query in queries:
        qs = qs | (query & (Q(**{'active_flag': True})))

    if type_of_user=='student':
        user = Student.objects.filter(qs)
    elif type_of_user=='alumni':
        user = Alumni.objects.filter(qs)
    elif type_of_user=='faculty':
        user = Faculty.objects.filter(qs)

    return user

@login_required
def connect(request,type_of_user):

    row_set=get_row_set(type_of_user)

    #excluding current user
    row_set=row_set.exclude(user_id__username = request.user.username)

    connection=find_connections(request.user.username,row_set)

    context={"all_data":zip(row_set, connection) ,"type_of_user":type_of_user}
    return render(request, 'AlumniManagement/connectNew.html',context)


def find_connections(follower,rowset):

    connection=[]
    for user in rowset:
        try:
            data=Connections.objects.filter(follower__username=follower,following__username=user.user_id.username)
        except:
            pass

        if len(data)==0:
            connection.append(0)
        else:
            connection.append(1)
    return connection

@login_required
def search(request,type_of_user):

    # if not request.user.is_authenticated:
        # return redirect(settings.LOGIN_URL, request.path)

    try:
        query=request.GET['search_box']
    except:
        query=''

    if not query:
        return redirect('connect',type_of_user)
    else:
        row_set=get_filtered_row_set(type_of_user,query)

    #excluding current user
    row_set=row_set.exclude(user_id__username = request.user.username)

    connection = find_connections(request.user.username, row_set)
    context = {"all_data": zip(row_set, connection), "type_of_user": type_of_user}
    return render(request, 'AlumniManagement/connectNew.html', context)


@login_required
def view(request,type_of_user):

    # if not request.user.is_authenticated:
    #     return redirect(settings.LOGIN_URL, request.path)

    row_set= get_user_details(request.POST['view'],type_of_user)
    connection = find_connections(request.user.username, row_set)
    context = {"user_data": zip(row_set, connection), "type_of_user": type_of_user}
    return render(request, 'AlumniManagement/view.html', context)


def get_user_details(user_id,type_of_user):

    if type_of_user=='student':
        row_set=Student.objects.filter(user_id__username=user_id)
    elif type_of_user=='alumni':
        row_set = Alumni.objects.filter(user_id__username=user_id)
    elif type_of_user=='faculty':
        row_set = Faculty.objects.filter(user_id__username=user_id)

    return row_set


@login_required
def add_to_contacts(request,type_of_user):

    follower_id = request.user.username
    following_id = request.POST['add']

    follower= User.objects.get(username=follower_id)
    following=User.objects.get(username=following_id)

    connection = Connections(follower=follower,following=following)
    connection.save()

    return redirect('connect',type_of_user)

@login_required
def delete_contact(request,type_of_user):
    follower_id=request.user.username
    following_id=request.POST['unfollow']
    Connections.objects.filter(follower__username=follower_id,following__username=following_id).delete()

    return redirect('connect', type_of_user)


def home(request):
    context = {}
    return render(request, 'AlumniManagement/index.html', context)

def about(request):
    context={}
    return render(request, 'AlumniManagement/about.html', context)

def contact_us(request):
    context={}
    return render(request, 'AlumniManagement/contact_us.html', context)