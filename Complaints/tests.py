from django.test import TestCase

from django.test import TestCase
from django.core.urlresolvers import reverse, resolve
from Database.models import User,Student,Faculty,Alumni,Connections, Complaints
from django.shortcuts import redirect


class Complaint_Not_Logged_In_TestCase(TestCase):

    #For url /Complaints/
    #If user is not logged in he/she will be redirected to login page
    def test_Complaint_list_view(self):
        url = reverse("viewComplaints")
        resp = self.client.get(url)
        self.assertEqual(resp.url.split('?')[0] , reverse("login"))


    #For url /Complaints/post/
    #If user is not logged in he/she will be redirected to login page
    def test_Complaint_post(self):
        url = reverse("postComplaint")
        resp = self.client.get(url)
        self.assertEqual(resp.url.split('?')[0] , reverse("login"))




class Complaint_Logged_In_TestCase(TestCase):
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


        Complaint1=Complaints.objects.create(complaint_info='Test1',
                                                  created_by=user1
                                                )

        Complaint2 = Complaints.objects.create(complaint_info='Test2',
                                                    created_by=user1
                                                    )

        Complaint3 = Complaints.objects.create(complaint_info='Test3',
                                                created_by=user3
                                                    )

    # For url /Complaints/
    # Checking whether all data is coming or not
    def test_Complaint_list_view_count(self):
        self.client.login(username='jacob1', password='top_secret')
        url = reverse("viewComplaints")
        resp = self.client.get(url, follow=True)

        self.assertEqual(resp.status_code, 200)

        self.assertEqual(len(resp.context['complaints']), 2)

    # For url /Complaints/1/viewComplaint
    # Checking whether all data is coming correctly or not
    def test_Complaint_view(self):
        self.client.login(username='jacob1', password='top_secret')
        url = reverse("viewComplaint", kwargs={'pk':1})
        resp = self.client.get(url, follow=True)

        self.assertEqual(resp.status_code, 200)

        Complaint1=Complaints.objects.get(pk=1)

        self.assertEquals(Complaint1.complaint_info,resp.context[0]['complaint'].complaint_info)
        self.assertEquals(Complaint1.created_by, resp.context[0]['complaint'].created_by)


    # For url /Complaints/1/
    # Checking whether all data is coming correctly or not
    def test_Complaint_update(self):
        self.client.login(username='jacob1', password='top_secret')
        url = reverse("updateComplaint", kwargs={'pk':1})
        resp = self.client.get(url, follow=True)

        self.assertEqual(resp.status_code, 200)


    # For url /Complaints/1/
    # Checking whether an unauthorised user can update an Complaint or not
    def test_Complaint_update_false(self):
        self.client.login(username='jacob1', password='top_secret')
        url = reverse("updateComplaint", kwargs={'pk':3})
        resp = self.client.get(url, follow=True)

        self.assertNotEqual(resp.status_code,200)

        self.assertEqual(resp.status_code, 404)


    # For url /Complaints/1/delete
    # Checking whether a user is able to delete an Complaint or not
    def test_Complaint_delete(self):
        self.client.login(username='jacob1', password='top_secret')
        url = reverse("deleteComplaint", kwargs={'pk':1})
        resp = self.client.get(url, follow=True)

        self.assertEqual(resp.status_code, 200)

        oppo=Complaints.objects.all()

        self.assertEquals(len(oppo),2)


    # For url /Complaints/1/delete
    # Checking whether an unauthorised user can delete an Complaint or not
    def test_Complaint_delete_false(self):
        self.client.login(username='jacob1', password='top_secret')
        url = reverse("deleteComplaint", kwargs={'pk':3})
        resp = self.client.get(url, follow=True)

        self.assertNotEqual(resp.status_code,200)

        self.assertEqual(resp.status_code, 404)