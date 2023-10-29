from django.contrib import admin
from .models import Category
from .models import Course
from .models import Lesson
from .models import comment
from .models import Rating,Tag




admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(comment)
admin.site.register(Rating)
admin.site.register(Tag)

# Register your models here.
