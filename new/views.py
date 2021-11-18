from django.http import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
import xlwt
from .models import *

# Create your views here.
def home(request):
    a=Enter()
    
    b=Details.objects.all()
    c=Department.objects.all()
    
                
            
        
    if request.method=='POST':
        a=Enter(request.POST)
        if a.is_valid():
            c=a.save(commit=False)
            c.date=request.POST.get('date')
            c.save()
            messages.success(request,'created successfullly')
            return redirect('home')
        else:
            messages.error(request,'please Enter correct details')

    return render(request,'new/home.html',{'a':a})


def excel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment;filename="users.xls"'

    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Details')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['department','faculty_name']
    
    for col_num in range(len(columns)):
        ws.write(row_num,col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    # rows = Details.objects.values_list('department','faculty_name')
    # for row in rows:
    #     row_num+=1
    #     for col_num in range(len((row))):
    #         ws.write(row_num,col_num, row[col_num], font_style)
    rows = Details.objects.all().values_list('department','faculty_name')
    n=[]
    for i in rows:
        row_num+=1
        for j in range(len(i)):
            if i[0]==1:
                k='Mechanical'
                n.append((k,i[1]))
                ws.write(row_num,j, n[j], font_style)
                n.pop()
                break
                
                
            if i[0]==2:
                k='Civil'
                n.append((k,i[1]))
                ws.write(row_num,j, n[j], font_style)
                n.pop()
                break
            if i[0]==3:
                k='computer science engineering'
                n.append((k,i[1]))
                ws.write(row_num,j, n[j], font_style)
                n.pop()
                break
            if i[0]==4:
                k='EEE'
                n.append((k,i[1]))
                ws.write(row_num,j, n[j], font_style)
                n.pop()
                break
            if i[0]==5:
                k='ECE'
                n.append((k,i[1]))
                ws.write(row_num,j, n[j], font_style)
                n.pop()
                break
            if i[0]==6:
                k='IT'
                n.append((k,i[1]))
                ws.write(row_num,j, n[j], font_style)
                n.pop()
                break
            if i[0]==7:
                k='B.Pharmacy'
                n.append((k,i[1]))
                ws.write(row_num,j, n[j], font_style)
                n.pop()
                break
            
            
    wb.save(response)
    return response

        
def view(request):
    b=Details.objects.all()
    c=Department.objects.all()
    if request.method=='POST':
        return redirect('home')
    return render(request,'new/excel.html',{'b':b,'c':c})

