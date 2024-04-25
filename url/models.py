from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)
    role=models.CharField(max_length=100,null=False)
    photo=models.ImageField(blank=True,upload_to='photos/')
    phone=models.CharField(max_length=10,null=False)
    email=models.EmailField(null=False)
    district=models.CharField(max_length=100,null=False)
    state=models.CharField(max_length=100,null=False)
    social=models.URLField(null=False)
    summary=models.TextField(null=False)
    username=models.CharField(max_length=100,null=False,unique=True)
    password=models.CharField(max_length=100,null=False)

class Education(models.Model):
    id=models.AutoField(primary_key=True)
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    qualification1=models.CharField(max_length=100,null=False)
    college1=models.CharField(max_length=100,null=False)
    start1=models.CharField(max_length=4,null=False)
    stop1=models.CharField(max_length=4,null=True)
    score1=models.DecimalField(max_digits=3,decimal_places=2)
    qualification2=models.CharField(max_length=100,null=False)
    college2=models.CharField(max_length=100,null=False)
    start2=models.CharField(max_length=4,null=False)
    stop2=models.CharField(max_length=4,null=False)
    score2=models.DecimalField(max_digits=4,decimal_places=2)
    qualification3=models.CharField(max_length=100,null=False)
    college3=models.CharField(max_length=100,null=False)
    start3=models.CharField(max_length=4,null=False)
    stop3=models.CharField(max_length=4,null=False)
    score3=models.DecimalField(max_digits=4,decimal_places=2)

class Skill(models.Model):
    id=models.AutoField(primary_key=True)
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    technical=models.TextField(null=False)
    soft=models.TextField(null=False)

class Experience(models.Model):
    id=models.AutoField(primary_key=True)
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    job1=models.CharField(max_length=100,null=False)
    company1=models.CharField(max_length=100,null=False)
    start1=models.CharField(max_length=20,null=False)
    stop1=models.CharField(max_length=20,null=True)
    mode1=models.CharField(max_length=7,null=False)
    desc1=models.TextField(null=False)
    tech1=models.CharField(max_length=100,null=False)
    job2=models.CharField(max_length=100,null=True)
    company2=models.CharField(max_length=100,null=True)
    start2=models.CharField(max_length=20,null=True)
    stop2=models.CharField(max_length=20,null=True)
    mode2=models.CharField(max_length=7,null=True)
    desc2=models.TextField(null=True)
    tech2=models.CharField(max_length=100,null=True)
    job3=models.CharField(max_length=100,null=True)
    company3=models.CharField(max_length=100,null=True)
    start3=models.CharField(max_length=20,null=True)
    stop3=models.CharField(max_length=20,null=True)
    mode3=models.CharField(max_length=7,null=True)
    desc3=models.TextField(null=True)
    tech3=models.CharField(max_length=100,null=True)
    job4=models.CharField(max_length=100,null=True)
    company4=models.CharField(max_length=100,null=True)
    start4=models.CharField(max_length=20,null=True)
    stop4=models.CharField(max_length=20,null=True)
    mode4=models.CharField(max_length=7,null=True)
    desc4=models.TextField(null=True)
    tech4=models.CharField(max_length=100,null=True)
    job5=models.CharField(max_length=100,null=True)
    company5=models.CharField(max_length=100,null=True)
    start5=models.CharField(max_length=20,null=True)
    stop5=models.CharField(max_length=20,null=True)
    mode5=models.CharField(max_length=7,null=True)
    desc5=models.TextField(null=True)
    tech5=models.CharField(max_length=100,null=True)

class Project(models.Model):
    id=models.AutoField(primary_key=True)
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    project1=models.CharField(max_length=100,null=False)
    start1=models.CharField(max_length=20,null=False)
    stop1=models.CharField(max_length=20,null=False)
    desc1=models.TextField(null=False)
    tech1=models.CharField(max_length=100,null=False)
    project2=models.CharField(max_length=100,null=True)
    start2=models.CharField(max_length=20,null=True)
    stop2=models.CharField(max_length=20,null=True)
    desc2=models.TextField(null=True)
    tech2=models.CharField(max_length=100,null=True)
    project3=models.CharField(max_length=100,null=True)
    start3=models.CharField(max_length=20,null=True)
    stop3=models.CharField(max_length=20,null=True)
    desc3=models.TextField(null=True)
    tech3=models.CharField(max_length=100,null=True)
    project4=models.CharField(max_length=100,null=True)
    start4=models.CharField(max_length=20,null=True)
    stop4=models.CharField(max_length=20,null=True)
    desc4=models.TextField(null=True)
    tech4=models.CharField(max_length=100,null=True)
    project5=models.CharField(max_length=100,null=True)
    start5=models.CharField(max_length=20,null=True)
    stop5=models.CharField(max_length=20,null=True)
    desc5=models.TextField(null=True)
    tech5=models.CharField(max_length=100,null=True)

class Certificate(models.Model):
    id=models.AutoField(primary_key=True)
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    certificate1=models.CharField(max_length=100,null=False)
    certificate2=models.CharField(max_length=100,null=True)
    certificate3=models.CharField(max_length=100,null=True)
    certificate4=models.CharField(max_length=100,null=True)
    certificate5=models.CharField(max_length=100,null=True)
    certificate6=models.CharField(max_length=100,null=True)
    certificate7=models.CharField(max_length=100,null=True)
    certificate8=models.CharField(max_length=100,null=True)
    certificate9=models.CharField(max_length=100,null=True)
    certificate10=models.CharField(max_length=100,null=True)

class Job(models.Model):
    id=models.AutoField(primary_key=True)
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField(max_length=2500)
    desc=models.JSONField()
    resume=models.ImageField(null=True,blank=True,upload_to='images/')