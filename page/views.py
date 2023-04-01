from django.shortcuts import render,redirect
from .models import Members,Courses
    






def index(request):
    return render(request, 'pages/index.html',{'cour':Courses.objects.all()})
def member(request):
    return render(request , 'pages/member.html' ,{'Mem':Members.objects.all()})

def courses(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        price = request.POST.get('price')
        memberCourse = Courses(label=title ,price = price, description=desc)
        memberCourse.save()
        return redirect('pages/courses.html')
    else:
        return render(request , 'pages/courses.html',{'cour':Courses.objects.all()} )

    


    
