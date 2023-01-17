from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=100)
    jop = models.CharField(max_length=100)
    subtitel = models.CharField(max_length=300)
    image = models.ImageField(upload_to='about/')
    from_adress = models.CharField( max_length=100)
    lives_in = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    cv = models.FileField(upload_to='cv',help_text='upload you cv')
    def __str__(self):
        return self.name


SKILL_TYPE = (
    ('Coding','Coding'),
    ('Design','Design')
)


class Skills(models.Model):
    skill = models.CharField(max_length=100)
    percentage = models.IntegerField()
    type = models.CharField( max_length=10,choices=SKILL_TYPE)

    def __str__(self):
        return self.skill


class Education(models.Model):
    year = models.IntegerField()
    titel = models.CharField ( max_length=100)
    place = models.CharField( max_length=50)
    description = models.CharField(max_length=300)
   # last = models.BooleanField(default=False)

    def __str__(self):
        return self.titel

        
    class Meta:
        ordering = ('-year',)    

class Experience(models.Model):
    year = models.IntegerField()
    titel = models.CharField ( max_length=100)
    place = models.CharField( max_length=50)
    description = models.CharField(max_length=300)
   # last = models.BooleanField(default=False)

    def __str__(self):
        return self.titel


class Service(models.Model):
    icon = models.CharField(max_length=20)
    titel = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.titel

class Projects(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project/')
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.name