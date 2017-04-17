from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse

class User(AbstractUser):
    phone_number=models.CharField(max_length=12, null=True, blank=True)
    secret_question=models.CharField(max_length=100, null=True, blank=True)
    secret_question_answer=models.CharField(max_length=150, null=True, blank=True)
    create_date=models.DateField(auto_now_add=True,null=True)
    update_date=models.DateField(auto_now=True,null=True)
    profile_dp=models.FileField(default='def.jpg')
    introduction=models.TextField(max_length=3000, null=True,blank=True)

    ADMIN='admin'
    STUDENT='student'
    ALUMNI='alumni'
    FACULTY='faculty'

    USER_TYPE_FLAG_CHOICES=(
        (ADMIN, 'Admin'),
        (STUDENT, 'Student'),
        (ALUMNI, 'Alumni'),
        (FACULTY, 'Faculty'),
        )

    user_type_flag = models.CharField(max_length=10,choices=USER_TYPE_FLAG_CHOICES, default=ALUMNI)

    def __str__(self):
        return self.username



class Student(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

    CSE = 'Cse'
    IT = 'IT'
    MECHANICAL = 'Mechanical'
    CIVIL = 'Civil'
    ELECTRICAL='Electrical'
    ELECTRONICS='Electronics'


    DEPARTMENT_NAME_CHOICES = (
        (CSE, 'Cse'),
        (IT, 'IT'),
        (MECHANICAL, 'Mechanical'),
        (CIVIL, 'Civil'),
        (ELECTRICAL,'Electrical'),
        (ELECTRONICS,'Electronics')
    )

    department_name=models.CharField(max_length=50,choices=DEPARTMENT_NAME_CHOICES, default=CSE)

    CSE_BRANCH = 'Cse'
    IT_BRANCH = 'IT'
    MECHANICAL_BRANCH = 'Mechanical'
    CIVIL_BRANCH = 'Civil'
    ELECTRICAL_BRANCH = 'Electrical'
    ELECTRONICS_BRANCH = 'Electronics'

    BRANCH_NAME_CHOICES = (
        (CSE_BRANCH, 'Cse'),
        (IT_BRANCH, 'IT'),
        (MECHANICAL_BRANCH, 'Mechanical'),
        (CIVIL_BRANCH, 'Civil'),
        (ELECTRICAL_BRANCH, 'Electrical'),
        (ELECTRONICS_BRANCH, 'Electronics')
    )

    branch_name=models.CharField(max_length=50,choices=BRANCH_NAME_CHOICES, default=CSE_BRANCH)

    MTECH='MTech'
    BTECH='BTech'
    MS='MS'

    COURSE_NAME_CHOICES=(
        (MTECH,'MTech'),
        (BTECH,'BTech'),
        (MS,'MS')
    )

    course_name=models.CharField(max_length=40,choices=COURSE_NAME_CHOICES, default=BTECH)

    admission_date=models.DateField()
    create_date = models.DateField(auto_now_add=True,blank=True)
    update_date = models.DateField(auto_now=True,blank=True)
    active_flag=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('viewUser',kwargs={'pk':self.pk})


class Alumni(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    CSE = 'Cse'
    IT = 'IT'
    MECHANICAL = 'Mechanical'
    CIVIL = 'Civil'
    ELECTRICAL = 'Electrical'
    ELECTRONICS = 'Electronics'

    DEPARTMENT_NAME_CHOICES = (
        (CSE, 'Cse'),
        (IT, 'IT'),
        (MECHANICAL, 'Mechanical'),
        (CIVIL, 'Civil'),
        (ELECTRICAL, 'Electrical'),
        (ELECTRONICS, 'Electronics')
    )

    department_name = models.CharField(max_length=50, choices=DEPARTMENT_NAME_CHOICES, default=CSE)

    CSE_BRANCH = 'Cse'
    IT_BRANCH = 'IT'
    MECHANICAL_BRANCH = 'Mechanical'
    CIVIL_BRANCH = 'Civil'
    ELECTRICAL_BRANCH = 'Electrical'
    ELECTRONICS_BRANCH = 'Electronics'

    BRANCH_NAME_CHOICES = (
        (CSE_BRANCH, 'Cse'),
        (IT_BRANCH, 'IT'),
        (MECHANICAL_BRANCH, 'Mechanical'),
        (CIVIL_BRANCH, 'Civil'),
        (ELECTRICAL_BRANCH, 'Electrical'),
        (ELECTRONICS_BRANCH, 'Electronics')
    )

    branch_name = models.CharField(max_length=50, choices=BRANCH_NAME_CHOICES, default=CSE_BRANCH)

    MTECH = 'MTech'
    BTECH = 'BTech'
    MS = 'MS'

    COURSE_NAME_CHOICES = (
        (MTECH, 'MTech'),
        (BTECH, 'BTech'),
        (MS, 'MS')
    )

    course_name = models.CharField(max_length=40, choices=COURSE_NAME_CHOICES, default=BTECH)

    admission_date=models.DateField()
    passout_date = models.DateField()

    current_organization_name=models.CharField(max_length=50,null=True,blank=True)
    designation=models.CharField(max_length=50,null=True,blank=True)
    role=models.CharField(max_length=50,null=True,blank=True)
    work_phone=models.CharField(max_length=12,null=True,blank=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    active_flag=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('viewUser',kwargs={'pk':self.pk})


class Faculty(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

    CSE = 'Cse'
    IT = 'IT'
    MECHANICAL = 'Mechanical'
    CIVIL = 'Civil'
    ELECTRICAL = 'Electrical'
    ELECTRONICS = 'Electronics'

    DEPARTMENT_NAME_CHOICES = (
        (CSE, 'Cse'),
        (IT, 'IT'),
        (MECHANICAL, 'Mechanical'),
        (CIVIL, 'Civil'),
        (ELECTRICAL, 'Electrical'),
        (ELECTRONICS, 'Electronics')
    )

    department_name = models.CharField(max_length=50, choices=DEPARTMENT_NAME_CHOICES, default=CSE)

    designation = models.CharField(max_length=50, null=True,blank=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    active_flag = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('viewUser',kwargs={'pk':self.pk})

class Connections(models.Model):
    follower = models.ForeignKey(User,related_name='follower', on_delete=models.CASCADE)
    following = models.ForeignKey(User,related_name='following',on_delete=models.CASCADE)


class Opportunities(models.Model):
    opportunity_info = models.TextField(max_length=1000)
    number_of_vacancy = models.IntegerField(null=True,blank=True)
    expiration_date=models.DateField(null=True,blank=True)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    active_flag = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('viewOpportunity',kwargs={'pk':self.pk})


class Complaints(models.Model):
    TECHNICAL = 'technical'
    FINANCIAL = 'financial'
    ACADEMIC = 'academic'
    OTHER='other'

    COMPLAINT_CATEGORY_CHOICES = (
        (TECHNICAL, 'Technical'),
        (FINANCIAL, 'Financial'),
        (ACADEMIC, 'Academic'),
        (OTHER,'Other')
    )

    complaint_category = models.CharField(max_length=50, choices=COMPLAINT_CATEGORY_CHOICES, default=TECHNICAL)
    complaint_info = models.TextField(max_length=1000)
    acknowledge_flag = models.BooleanField(default=False)
    solution_info = models.TextField(editable=True)
    created_by = models.ForeignKey(User)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    active_flag = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('viewComplaint',kwargs={'pk':self.pk})


class Event(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField(editable=True)
    expiration_date = models.DateField(auto_now=True)
    createdBy = models.ForeignKey(User)
    event_news_flag = models.BooleanField()
    created_date = models.DateField(auto_now=True)
    updated_date = models.DateField(auto_now=True)
    active_flag = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('viewEvent',kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

class Emails(models.Model):
    name=models.CharField(max_length=50)
    email_id=models.EmailField()