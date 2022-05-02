from django.shortcuts import redirect, render
from myapp.forms import *
from myapp.models import *
from django.http import HttpResponse
from reportlab.pdfgen    import canvas
import datetime
# Create your views here.
def home(request):
    if request.method=='POST':
        form=patient_details(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            clinicName=request.POST['clinicName']
            clinicLogo=request.FILES['clinicLogo']
            physicianName=request.POST['physicianName']
            physicianContact=request.POST['physicianContact']
            pfname=request.POST['pfname']
            plname=request.POST['plname']
            pdob=request.POST['pdob']
            pcontact=request.POST['pcontact']
            complaint=request.POST['complaint']
            consultation=request.POST['consultation']
            saved_list=[clinicName,physicianName,physicianContact,pfname,plname,pdob,pcontact,complaint,consultation]
            request.session['saved_list']=saved_list
            x=str(clinicLogo)
            logo=x.replace(" ","_")
            request.session['logo']=logo
            return redirect(pdf_dw)
        else:
            print("Error from invalid")
    return render(request,'home.html')


#from reportlab.lib.utils import ImageReader

#from django.http import FileResponse
#from reportlab.pdfgen import canvas
#import os,random
#path = os.path.realpath(os.path.dirname(__file__))
def pdf_dw(request):                                  
    li=request.session['saved_list']
    response = HttpResponse(content_type='application/pdf')  
    #response['Content-Disposition'] = 'attachment; filename="CR_"'+li[4]+'"_"'+li[3]+'".pdf"'
    p = canvas.Canvas(response,)
    p.drawBoundary(0,60,50,470,730)
    y=request.session['logo']
    x="Media/workshop/logo/"+y
    p.drawImage(x,500,785,60,60)
    p.setFont("Times-Roman", 30)  
    p.drawString(80,740, li[0]) 
    p.setFont("Times-Roman",17)  
    p.drawString(80,700, 'Physician Name')  
    p.drawString(220,700,'=')
    p.drawString(255,700,li[1])
    p.drawString(80,680, 'Physician Contact')  
    p.drawString(220,680,'=')
    p.drawString(255,680,li[2])    
    p.drawString(80,660, 'Patient First Name')  
    p.drawString(220,660,'=')
    p.drawString(255,660,li[3])
    p.drawString(80,640, 'Patient Last Name')  
    p.drawString(220,640,'=')
    p.drawString(255,640,li[4])
    p.drawString(80,620, 'Patient DOB')  
    p.drawString(220,620,'=')
    p.drawString(255,620,li[5])
    p.drawString(80,600, 'Patient Contact')  
    p.drawString(220,600,'=')
    p.drawString(255,600,li[6])  
    p.drawString(80,550, 'Chief Complaint')  
    p.setFont("Times-Roman",14) 
    p.drawString(80,530,li[7]) 
    p.setFont("Times-Roman",17)
    p.drawString(80,350, 'Consultation Note')
    p.setFont("Times-Roman",14) 
    p.drawString(80,330,li[8])
    p.setFont("Times-Roman",11) 
    x = datetime.datetime.now()
    y=x.strftime("%d %b %Y %H:%M")
    p.drawString(320,20,"This report is generated on "+y)    
    p.showPage()  
    p.save()  
    return response   


