from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from AlumniManagement import settings
from Database.models import User,Connections,Student,Faculty,Alumni
from django.db.models import  Q
from Connect.views import get_user_details,find_connections

def view(request):

    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL, request.path)

    all_data=Connections.objects.filter(follower__username=request.user.username)

    context = {'all_data': all_data, "type_of_user": 'Contacts'}
    return render(request, 'AlumniManagement/viewContacts.html', context)



def viewContacts(request):
    if not request.user.is_authenticated:
        return redirect(settings.LOGIN_URL, request.path)

    user=User.objects.filter(username=request.POST['view'])[0]
    type_of_user=user.user_type_flag
    row_set= get_user_details(request.POST['view'],type_of_user)

    connection = find_connections(request.user.username, row_set)
    context = {"user_data": zip(row_set, connection), "type_of_user": type_of_user}
    return render(request, 'AlumniManagement/view.html', context)

def deleteContact(request):
    follower_id=request.user.username
    following_id=request.POST['unfollow']
    Connections.objects.filter(follower__username=follower_id,following__username=following_id).delete()

    return redirect('listContacts')
