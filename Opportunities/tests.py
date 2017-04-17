from django.test import TestCase

from django.test import TestCase
from django.core.urlresolvers import reverse, resolve
from Database.models import User,Student,Faculty,Alumni,Connections, Opportunities
from django.shortcuts import redirect


class Opportunity_Not_Logged_In_TestCase(TestCase):

    #For url /Opportunities/
    #If user is not logged in he/she will be redirected to login page
    def test_opportunity_list_view(self):
        url = reverse("viewOpportunities")
        resp = self.client.get(url)
        self.assertEqual(resp.url.split('?')[0] , reverse("login"))


    #For url /Opportunities/post/
    #If user is not logged in he/she will be redirected to login page
    def test_opportunity_post(self):
        url = reverse("postOpportunity")
        resp = self.client.get(url)
        self.assertEqual(resp.url.split('?')[0] , reverse("login"))




class Opportunity_Logged_In_TestCase(TestCase):
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


        opportunity1=Opportunities.objects.create(opportunity_info='Test1',
                                                  number_of_vacancy=12,
                                                  posted_by=user1
                                                )

        opportunity2 = Opportunities.objects.create(opportunity_info='Test2',
                                                    number_of_vacancy=2,
                                                    posted_by=user1
                                                    )

        opportunity3 = Opportunities.objects.create(opportunity_info='Test3',
                                                    number_of_vacancy=12,
                                                    posted_by=user3
                                                    )

    # For url /Opportunities/
    # Checking whether all data is coming or not
    def test_opportunity_list_view_count(self):
        self.client.login(username='jacob1', password='top_secret')
        url = reverse("viewOpportunities")
        resp = self.client.get(url, follow=True)

        self.assertEqual(resp.status_code, 200)

        self.assertEqual(len(resp.context['opportunities']), 3)

    # For url /Opportunities/1/viewOpportunity
    # Checking whether all data is coming correctly or not
    def test_opportunity_view(self):
        self.client.login(username='jacob1', password='top_secret')
        url = reverse("viewOpportunity", kwargs={'pk':1})
        resp = self.client.get(url, follow=True)

        self.assertEqual(resp.status_code, 200)

        opportunity1=Opportunities.objects.get(pk=1)

        self.assertEquals(opportunity1.opportunity_info,resp.context[0]['opportunity'].opportunity_info)
        self.assertEquals(opportunity1.number_of_vacancy, resp.context[0]['opportunity'].number_of_vacancy)
        self.assertEquals(opportunity1.posted_by, resp.context[0]['opportunity'].posted_by)


    # For url /Opportunities/1/
    # Checking whether all data is coming correctly or not
    def test_opportunity_update(self):
        self.client.login(username='jacob1', password='top_secret')
        url = reverse("updateOpportunity", kwargs={'pk':1})
        resp = self.client.get(url, follow=True)

        self.assertEqual(resp.status_code, 200)


    # For url /Opportunities/1/
    # Checking whether an unauthorised user can update an opportunity or not
    def test_opportunity_update_false(self):
        self.client.login(username='jacob1', password='top_secret')
        url = reverse("updateOpportunity", kwargs={'pk':3})
        resp = self.client.get(url, follow=True)

        self.assertNotEqual(resp.status_code,200)

        self.assertEqual(resp.status_code, 404)


    # For url /Opportunities/1/delete
    # Checking whether a user is able to delete an opportunity or not
    def test_opportunity_delete(self):
        self.client.login(username='jacob1', password='top_secret')
        url = reverse("deleteOpportunity", kwargs={'pk':1})
        resp = self.client.get(url, follow=True)

        self.assertEqual(resp.status_code, 200)

        oppo=Opportunities.objects.all()

        self.assertEquals(len(oppo),2)


    # For url /Opportunities/1/delete
    # Checking whether an unauthorised user can delete an opportunity or not
    def test_opportunity_delete_false(self):
        self.client.login(username='jacob1', password='top_secret')
        url = reverse("deleteOpportunity", kwargs={'pk':3})
        resp = self.client.get(url, follow=True)

        self.assertNotEqual(resp.status_code,200)

        self.assertEqual(resp.status_code, 404)