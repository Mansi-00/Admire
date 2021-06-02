from django.db import models

# Create your models here.

class t1(models.Model):
    s_name = models.CharField("Student Name", default="", null=True, blank=True, max_length=200)
    s_eno = models.PositiveIntegerField("Student Enrollment", default="0")
    s_email = models.EmailField("Student Email ID",default="", null=True, blank=True, max_length=200)
    s_con = models.IntegerField("Student Contact Number", default="0")
    s_add = models.TextField("Student Address", default="")

    def __str__(self):
        return self.s_email