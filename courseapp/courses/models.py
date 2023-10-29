from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_date = models.DateField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now=True, null=True)
    active = models.BooleanField(default=True)
    subject = models.CharField(max_length=100, null=False)


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


# Create your models here.


class Course(BaseModel):
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to ='Course/%Y/%m', default=None)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.subject

    class Meta:
        unique_together = ('subject', 'category')


class Lesson(BaseModel):
    image = models.ImageField(upload_to ='Lesson/%Y/%m', default=None)
    content = RichTextField()
    content = RichTextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')

    class Meta:
        unique_together = ('subject', 'course')


class Tag(BaseModel):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class comment(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now=True, null=True)
    content = models.TextField(null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Rating(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
