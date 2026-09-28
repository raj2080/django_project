from django.shortcuts import render
from .models import Student
# Create your views here.
#from django.http import HttpResponse

def home(request):
    #return HttpResponse("Hello Django")
    
    context = {
        'title' : 'Student System test',
        'header' : 'Student Management System rrr',
        'paragraphs':["this is first paragraph","this is second paragraph","this is third paragraph"]
    }




    #print(context)
    print("METHOD:", request.method)
    print("PATH:", request.path)
    print("GET:", request.GET)
    print("POST:", request.POST)
    print("COOKIES:", request.COOKIES)
    print("HEADERS:", request.headers)
    print("USER:", request.user)


    for paragraph in context['paragraphs']:
        print(paragraph)


#So you're telling Django: 
#"Take this request, load students/home.html, give that template the context data, and create a response."

    return render(request,"students/home.html",context)



def aboutus(request):
    #return HttpResponse("Hello Django")
    context = {
        'ipaddress': "http://127.0.0.1:8000/students/aboutus"
    }

    return render(request,"students/aboutus.html",context)

def list_students(request):
    students = Student.objects.all()

    context = {
        "stds" : students,
        "header":"list of students in database",
        "title" :"Student List"
    }

    return render(request,"students/list_student.html",context)