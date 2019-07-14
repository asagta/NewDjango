from django.shortcuts import render  
from NewProject.forms import EmployeeForm 
from django.shortcuts import redirect 
from django.http import HttpResponse  
from django.template import loader  
import os
  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                template = loader.get_template('index.html')
                data = request.POST.get('eid')
                print(data)
                html = "<html><body><h3>Now Data is %s.</h3></body></html>" % data
                name = {  'question':data} 
                return HttpResponse(template.render(name))  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})    