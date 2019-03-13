from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from FoodApp.forms import PostForm,SubscribeEmail
from FoodApp.models import Post

#   ---- Main ----   # save email for subscibe
def Main(request):
    if request.method == "POST":
        form = SubscribeEmail(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/Main/')
    else:
        form = SubscribeEmail()
    return render(request,'Main.html',{'form':form})  

#   ---- Category ----   #
def DrinkPage(request):
    Post_list = Post.objects.filter(Category_id=1)
    return render(request,'DrinkPage.html',{'Post_list':Post_list})
def MainCoursesPage(request):
    Post_list = Post.objects.filter(Category_id=2)
    return render(request,'MainCoursesPage.html',{'Post_list':Post_list})
def DessertPage(request):
    Post_list = Post.objects.filter(Category_id=3)
    return render(request,'DessertPage.html',{'Post_list':Post_list})

#   ---- Dessert ----   #
def Dessert_1(request):
    Post_list = Post.objects.filter(id=1)
    return render(request,'Dessert/Dessert-1.html',{'Post_list':Post_list})
def Dessert_2(request):
    Post_list = Post.objects.filter(id=2)
    return render(request,'Dessert/Dessert-2.html',{'Post_list':Post_list})
def Dessert_3(request):
    Post_list = Post.objects.filter(id=6)
    return render(request,'Dessert/Dessert-6.html',{'Post_list':Post_list})
def Dessert_4(request):
    Post_list = Post.objects.filter(id=10)
    return render(request,'Dessert/Dessert-10.html',{'Post_list':Post_list})

#   ---- Drink ----   #
def Drink_1(request):
    Post_list = Post.objects.filter(id=3)
    return render(request,'Drink/Drink-3.html',{'Post_list':Post_list})
def Drink_2(request):
    Post_list = Post.objects.filter(id=9)
    return render(request,'Drink/Drink-9.html',{'Post_list':Post_list})
def Drink_3(request):
    Post_list = Post.objects.filter(id=11)
    return render(request,'Drink/Drink-11.html',{'Post_list':Post_list})
def Drink_4(request):
    Post_list = Post.objects.filter(id=12)
    return render(request,'Drink/Drink-12.html',{'Post_list':Post_list})

#   ---- MainCourse ----   #
def MainCourse_1(request):
    Post_list = Post.objects.filter(id=4)
    return render(request,'MainCourses/MainCourse-4.html',{'Post_list':Post_list})
def MainCourse_2(request):
    Post_list = Post.objects.filter(id=5)
    return render(request,'MainCourses/MainCourse-5.html',{'Post_list':Post_list})
def MainCourse_3(request):
    Post_list = Post.objects.filter(id=7)
    return render(request,'MainCourses/MainCourse-7.html',{'Post_list':Post_list})
def MainCourse_4(request):
    Post_list = Post.objects.filter(id=8)
    return render(request,'MainCourses/MainCourse-8.html',{'Post_list':Post_list})