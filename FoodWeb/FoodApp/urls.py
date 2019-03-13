from django.conf.urls import url,include
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.views.static import serve
from django.urls import re_path


urlpatterns = [
    #--- Main Page ---#
    url('',views.Main,name='show'),
    url('MainCoursesPage',views.MainCoursesPage,name='MaincoursePage'),
    url('DrinkPage',views.DrinkPage,name='DrinkPage'),
    url('DessertPage',views.DessertPage,name='DessertPage'),



    #--- Dessert---#
    url('Dessert-1/',views.Dessert_1,name='FujiCoconut'),
    url('Dessert-2/',views.Dessert_2,name='TSUJIRI'),
    url('Dessert-6/',views.Dessert_3,name='Pancake'),
    url('Dessert-10/',views.Dessert_4,name='Potpuree'),

    #--- Drink---#
    url('Drink-3/',views.Drink_1,name='GAGA'),
    url('Drink-9/',views.Drink_2,name='TINPRESSO'),
    url('Drink-11/',views.Drink_3,name='GAGA'),
    url('Drink-12/',views.Drink_4,name='TINPRESSO'),



    #--- Main Course---#
    url('MainCourses-4',views.MainCourse_1,name='HN'),
    url('MainCourses-5',views.MainCourse_2,name='Lobster'),
    url('MainCourses-7',views.MainCourse_3,name='Taiwan'),
    url('MainCourses-8',views.MainCourse_4,name='Shuchi'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
            }),
    ]
