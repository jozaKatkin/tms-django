from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Student(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)

    group = models.ForeignKey('Group', null=True, on_delete=models.SET_NULL,
                              related_name='students')


class Diary(models.Model):
    avg_mark = models.IntegerField()

    student = models.OneToOneField(
        Student, null=True,
        related_name='diary',
        on_delete=models.SET_NULL,
    )


class Book(models.Model):
    name = models.CharField(max_length=100)
    pages = models.IntegerField()

    students = models.ManyToManyField("Student", related_name='books')
