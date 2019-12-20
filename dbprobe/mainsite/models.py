# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver






class Crew(models.Model):
    id = models.BigAutoField(primary_key=True)
    p_name = models.CharField(max_length=255)


    # login = models.CharField(max_length=255)
    # psswrd = models.CharField(max_length=255)

    p_bio = models.CharField(max_length=500)
    p_status = models.CharField(max_length=7, blank=True, null=True)
    pers_pic = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Crew'

    def __str__(self):
        return self.p_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew, models.DO_NOTHING, blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class CrewRes(models.Model):
    id = models.BigAutoField(primary_key=True)
    crew = models.ForeignKey(Crew, models.DO_NOTHING)
    res = models.ForeignKey('Research', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Crew_Res'


# https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/
class CrewSpec(models.Model):
    id = models.BigAutoField(primary_key=True)
    crew = models.ForeignKey(Crew, models.DO_NOTHING)
    spec = models.ForeignKey('Specializations', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Crew_Spec'


class Modules(models.Model):
    id = models.BigAutoField(primary_key=True)
    mod_name = models.CharField(max_length=255)
    mod_description = models.CharField(max_length=500)
    mod_status = models.CharField(max_length=7, blank=True, null=True)
    mod_pic = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Modules'
    
    def __str__(self):
        return self.mod_name


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(Crew, models.DO_NOTHING)
    res = models.ForeignKey('Research', models.DO_NOTHING)
    title = models.CharField(max_length=255)
    n_date = models.DateTimeField(blank=True, null=True)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'News'


class Newsletter(models.Model):
    id = models.BigAutoField(primary_key=True)
    s_mail = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Newsletter'


class ResSpec(models.Model):
    id = models.BigAutoField(primary_key=True)
    res = models.ForeignKey('Research', models.DO_NOTHING)
    spec = models.ForeignKey('Specializations', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Res_Spec'


class Research(models.Model):
    id = models.BigAutoField(primary_key=True)
    r_topic = models.CharField(max_length=50)
    mod = models.ForeignKey(Modules, models.DO_NOTHING, blank=True, null=True)
    r_status = models.CharField(max_length=13) # 'pending valid','pending team','in progress','finished'
    prop_name = models.CharField(max_length=30)
    prop_mail = models.CharField(max_length=50)
    r_message = models.CharField(max_length=800)

    class Meta:
        managed = False
        db_table = 'Research'

    def __str__(self):
        return self.r_topic

class Specializations(models.Model):
    id = models.BigAutoField(primary_key=True)
    sp_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Specializations'
    
    def __str__(self):
        return self.sp_name


class Tourism(models.Model):
    id = models.BigAutoField(primary_key=True)
    t_name = models.CharField(max_length=30)
    personal = models.IntegerField(blank=True, null=True)
    t_mail = models.CharField(max_length=50)
    t_message = models.CharField(max_length=500) 
    
    class Meta:
        managed = False
        db_table = 'Tourism'

