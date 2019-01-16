from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
def index(request):
    response = HttpResponse()
    response.write("<html><body style=background-color:lightblue>\n")
    response.write("<h1 style=color:blue;background-color:red>Employee Details</h1>")
    response.write("<hr>")
    elist = Employee.objects.all()
    for e in elist:
        link = "<a href=\'adminapp\info\%d\'>"%(e.id)
        response.write("%s<li>%s &nbsp %s</a></li>"%(link, e.first_name, e.last_name))
        response.write("<br></body></html>")
    return response

def details(request, eid="0"):
    response = HttpResponse()
    response.write("<html><body style=background-color:lightgreen>\n")
    try:
        e = Employee.objects.get(id=eid)
        response.write("<h1 style=color:blue;background-color:red>Details of Employee %s</h1><hr>\n"%e.first_name)
        response.write("<li>First Name:%s</li><br>"%e.first_name)
        response.write("<li>Last Name:%s</li><br>"%e.last_name)
        response.write("<li>Company:%s</li><br>" % e.company)
        response.write("<li>Email:%s</li><br>" % e.email)
        response.write("<li>Address:%s</li><br>" % e.address)
        response.write("<li>Salary:%s</li><br>" % e.salary)
        response.write("<li>Mobile number:%s</li><br>" % e.mobile)
    except Employee.DoesNotExist:response.write("Sorry,Employee details does not exist.")
    response.write("</body></html>")
    return response
    #return response
    #return tee
    #jdhsjkdkj

