from django.db import models
from django.contrib.auth.models import AbstractUser


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
    unique_together = 'subject,Lesson'
    description = models.TextField(null=True, blank=True)
    image = models.ImageField('Course/ %Y %m', default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    unique_together = 'subject,course'
    image = models.ImageField('Lesson/ %Y %m', default=None)
    content = models.TextField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Tag(BaseModel):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class tags(Tag):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='tag_%(class)s_related', on_delete=models.CASCADE)

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
