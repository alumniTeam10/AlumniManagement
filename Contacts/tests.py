from django.test import TestCase
from django.core.urlresolvers import reverse, resolve
from Database.models import User,Student,Faculty,Alumni,Connections
from django.shortcuts import redirect


class Contacts_Not_Logged_In_TestCase(TestCase):

    #For url /Contacts/
    #If user is not logged in he/she will be redirected to login page
    def test_contacts_list_view(self):
        url = reverse("listContacts")
        resp = self.client.get(url)
        self.assertEqual(resp.url.split('?')[0] , reverse("login"))


    #For url /Contacts/view/
    #If user is not logged in he/she will be redirected to login page
    def test_contacts_view_contacts(self):
        url = reverse("viewContacts")
        resp = self.client.get(url)
        self.assertEqual(resp.url.split('?')[0] , reverse("login"))

    # For url /Contacts/deleteContact/
    # If user is not logged in he/she will be redirected to login page
    def test_connect_faculty(self):
        url = reverse("deleteContact")
        resp = self.client.get(url)
        self.assertEqual(resp.url.split('?')[0], reverse("login"))



class Connect_Logged_In_TestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='jacob1',
                                        email='jacob@gmail.com',
                                        password='top_secret',
                                        first_name='Jacob',
                                        last_name='Sen',
                                        user_type_flag='student'
                                        )

        user2 = User.objects.create_user(username='jacob2',
                                        email='jacob@gmail.com',
                                        password='top_secret',
                                        first_name='Jacob',
                                        last_name='Sen',
                                        user_type_flag='student'
                                        )

        user3 = User.objects.create_user(username='jacob3',
                                        email='jacob@gmail.com',
                                        password='top_secret',
                                        first_name='Jacob',
                                        last_name='Sen',
                                        user_type_flag='alumni'
                                        )

        user4 = User.objects.create_user(username='jacob4',
                                        email='jacob@gmail.com',
                                        password='top_secret',
                                        first_name='Jacob',
                                        last_name='Sen',
                                        user_type_flag='faculty'
                                        )

        user5 = User.objects.create_user(username='jacob5',
                                         email='jacob@gmail.com',
                                         password='top_secret',
                                         first_name='Jacob',
                                         last_name='Sen',
                                         user_type_flag='student'
                                         )

        student1=Student.objects.create(user_id=user1,
                                        department_name='Cse',
                                        branch_name='Cse',
                                        course_name='MTech',
                                        admission_date='2017-03-27'
                                        )

        student2 = Student.objects.create(user_id=user2,
                                          department_name='Cse',
                                          branch_name='Cse',
                                          course_name='MTech',
                                          admission_date='2017-03-27'
                                          )

        student3 = Student.objects.create(user_id=user5,
                                          department_name='IT',
                                          branch_name='IT',
                                          course_name='MTech',
                                          admission_date='2017-03-27'
                                          )

        alumni1 = Alumni.objects.create(user_id=user3,
                                         department_name='IT',
                                         branch_name='IT',
                                         course_name='MTech',
                                         admission_date='2017-03-27',
                                         passout_date='2017-03-27'
                                        )

        faculty1 = Faculty.objects.create(user_id=user4,
                                         department_name='IT'
                                         )

        connection1=Connections.objects.create(follower=user1,
                                               following=user2)

        connection2 = Connections.objects.create(follower=user1,
                                                 following=user3)

    # For url /Contacts/
    # simple check for 200 status code
    # checking that user is not redirected to login, when he/she is logged in
    def test_connect_student_simple(self):
        self.client.login(username='jacob1', password='top_secret')
        url = reverse("listContacts")
        resp = self.client.get(url, follow=True)
        self.assertEqual(resp.status_code, 200)


    # For url /Connect/student/
    # checking whether the number of student displayed are correct or not
    def test_connect_student_count(self):
        self.client.login(username='jacob1', password='top_secret')
        url = reverse("listContacts")
        resp = self.client.get(url, follow=True)

        self.assertEqual(len(resp.context['all_data']), 2)