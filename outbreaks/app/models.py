from django.db import models

# Create your models here.

class Notices(models.Model):
    id = models.AutoField('ID',primary_key=True)
    title = models.CharField('Title',max_length=100, null=False)
    detail = models.CharField('Details',max_length=125,null=False)
    create_time = models.CharField('Create Time',db_column='create_time',max_length=19)
    class Meta:
        db_table = 'notices' 

class Statistics(models.Model):
    id = models.AutoField('ID',primary_key=True)
    create_time = models.CharField('Create Time',db_column='create_time',max_length=19)
    confirm =  models.IntegerField('Confirmed Cases',null=False)
    heal = models.IntegerField('Healed Cases',null=False)
    dead = models.IntegerField('Dead Cases',null=False)
    nowConfirm = models.IntegerField('Currently Confirmed Cases',db_column='now_confirm',null=False)
    class Meta:
        db_table = 'statistics'

class User(models.Model):
    id = models.AutoField('ID',primary_key=True)
    userName = models.CharField('Username',db_column='User Name',max_length=32,null=False)
    password = models.CharField('Password',max_length=32,null=False)
    name = models.CharField('Name',max_length=32,null=False)
    gender = models.CharField('Gender', max_length=2, null=False)
    age = models.IntegerField('Age',null=False)
    phone = models.CharField('Phone',max_length=11,null=False)
    address = models.CharField('Address',max_length=100,null=False)
    type = models.IntegerField('Type',null=False) 
    class Meta:
        db_table = 'user'


class Checklog(models.Model):
    id = models.AutoField('ID',primary_key=True)
    create_time = models.CharField('Create Time',db_column='create_time',max_length=19)
    detail = models.CharField('Details',max_length=125,null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, db_column='user_id',null=False)
    class Meta:
        db_table = 'check_log'

class VaccinateLog(models.Model):
    id = models.AutoField('ID',primary_key=True)
    name = models.CharField('Name',max_length=32,null=False)
    card = models.CharField('Card ID',max_length=32,null=False)
    phone = models.CharField('Phone',max_length=11,null=False)
    address = models.CharField('Address',max_length=100,null=False)
    details = models.CharField('Details',max_length=125,null=False)
    vaccinateNo = models.CharField('Number of Vaccination',db_column='vaccinate_no',max_length=32,null=False)
    vaccinateTime = models.CharField('Vaccination Time', db_column='vaccinate_time',max_length=19,null=False)
    use = models.ForeignKey(User,on_delete=models.CASCADE, db_column='user_id',null=False)
    class Meta:
        db_table = 'vaccinate_log'


class AbnormityLog(models.Model):
    id = models.AutoField('ID',primary_key=True)
    create_time = models.CharField('Create Time',db_column='create_time',max_length=19)
    details = models.CharField('Details',max_length=125,null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, db_column='user_id',null=False)
    class Meta:
        db_table = 'abnormity_log'
