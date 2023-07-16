
from configparser import SafeConfigParser

# importing pandas
import pandas as pd
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.db.models import Count, Sum, Value
from django.http import HttpResponse
from django.shortcuts import (  # allows us to redirect user to another page
    redirect, render)

from .models import (Mid_1_1, Mid_1_2, Mid_2_1, Mid_2_2, Mid_3_1, Mid_3_2,
                     Mid_4_1, Mid_4_2, Results_1_1, Results_1_2, Results_2_1,
                     Results_2_2, Results_3_1, Results_3_2, Results_4_1,
                     Results_4_2, Student,Internships,Projects,Courses,Extracircular)


# ur views here.
def index(request):
    return render(request,'index.html')



@login_required
def update(request):
    
    SGPA=[]
    CG=[]
    credits=[]
    if request.method =='POST':
            students=Student.objects.all()
            for i in students:
                if Results_1_1.objects.filter(Htno = i.roll_no).exists() :
                    s=0
                    data1=Results_1_1.objects.filter(Htno=i.roll_no)
                    for j in data1:
                        s=s+j.Credits*j.Grade_Points
                    k=Results_1_1.objects.filter(Htno=i.roll_no).aggregate(C=Sum('Credits'))
                    S1=round(s/k['C'],2)
                    i.SGPA_1_1 = S1
                    i.save()
                    SGPA.append(S1)
                    credits.append(k['C'])

                if Results_1_2.objects.filter(Htno = i.roll_no).exists() :
                    s=0
                    data1=Results_1_2.objects.filter(Htno=i.roll_no)
                    for j in data1:
                        s=s+j.Credits*j.Grade_Points
                    k=Results_1_2.objects.filter(Htno=i.roll_no).aggregate(C=Sum('Credits'))
                    S2=round(s/k['C'],2)
                    i.SGPA_1_2 = S2
                    i.save()
                    SGPA.append(S2)
                    credits.append(k['C'])

                if Results_2_1.objects.filter(Htno = i.roll_no).exists() :
                    s=0
                    data1=Results_2_1.objects.filter(Htno=i.roll_no)
                    for j in data1:
                        s=s+j.Credits*j.Grade_Points
                    k=Results_2_1.objects.filter(Htno=i.roll_no).aggregate(C=Sum('Credits'))
                    S3=round(s/k['C'],2)
                    i.SGPA_2_1 = S3
                    i.save()
                    SGPA.append(S3)
                    credits.append(k['C'])

                if Results_2_2.objects.filter(Htno = i.roll_no).exists() :
                    s=0
                    data1=Results_2_2.objects.filter(Htno=i.roll_no)
                    for j in data1:
                        s=s+j.Credits*j.Grade_Points
                    k=Results_2_2.objects.filter(Htno=i.roll_no).aggregate(C=Sum('Credits'))
                    S4=round(s/k['C'],2)
                    i.SGPA_2_2 = S4
                    i.save()
                    SGPA.append(S4)
                    credits.append(k['C'])

                if Results_3_1.objects.filter(Htno = i.roll_no).exists() :
                    s=0
                    data1=Results_3_1.objects.filter(Htno=i.roll_no)
                    for j in data1:
                        s=s+j.Credits*j.Grade_Points
                    k=Results_3_1.objects.filter(Htno=i.roll_no).aggregate(C=Sum('Credits'))
                    S5=round(s/k['C'],2)
                    i.SGPA_3_1 = S5
                    i.save()
                    SGPA.append(S5)
                    credits.append(k['C'])

                if Results_3_2.objects.filter(Htno = i.roll_no).exists() :
                    s=0
                    data1=Results_3_2.objects.filter(Htno=i.roll_no)
                    for j in data1:
                        s=s+j.Credits*j.Grade_Points
                    k=Results_3_2.objects.filter(Htno=i.roll_no).aggregate(C=Sum('Credits'))
                    S6=round(s/k['C'],2)
                    i.SGPA_3_2 = S6
                    i.save()
                    SGPA.append(S6)
                    credits.append(k['C'])

                if Results_4_1.objects.filter(Htno = i.roll_no).exists() :
                    s=0
                    data1=Results_4_1.objects.filter(Htno=i.roll_no)
                    for j in data1:
                        s=s+j.Credits*j.Grade_Points
                    k=Results_4_1.objects.filter(Htno=i.roll_no).aggregate(C=Sum('Credits'))
                    S7=round(s/k['C'],2)
                    i.SGPA_4_1 = S7
                    i.save()
                    SGPA.append(S7)
                    credits.append(k['C'])

                if Results_4_2.objects.filter(Htno = i.roll_no).exists() :
                    s=0
                    data1=Results_4_2.objects.filter(Htno=i.roll_no)
                    for j in data1:
                        s=s+j.Credits*j.Grade_Points
                    k=Results_4_2.objects.filter(Htno=i.roll_no).aggregate(C=Sum('Credits'))
                    S8=round(s/k['C'],2)
                    i.SGPA_4_2 = S8
                    i.save()
                    SGPA.append(S8)
                    credits.append(k['C'])
                messages.info(request, 'Updated Successfully')

                CG = [SGPA[i]*credits[i] for i in range(len(SGPA))]
                if (sum(credits)!=0):
                     i.CGPA = round(sum(CG)/sum(credits),2)
                     i.save()

                if Internships.objects.filter(HTNO = i.roll_no).exists() :
                    data1=Internships.objects.filter(HTNO=i.roll_no)
            
                    k=Internships.objects.filter(HTNO=i.roll_no).aggregate(C=Count('HTNO'))
                    i.Internships =k['C'] 
                    i.save()
                messages.info(request, 'Updated Successfully')

                if Courses.objects.filter(HTNO = i.roll_no).exists() :
                    data1=Courses.objects.filter(HTNO=i.roll_no)
            
                    k=Courses.objects.filter(HTNO=i.roll_no).aggregate(C=Count('HTNO'))
                    i.Courses =k['C'] 
                    i.save()
                
                if Projects.objects.filter(HTNO = i.roll_no).exists() :
                    data1=Projects.objects.filter(HTNO=i.roll_no)
            
                    k=Projects.objects.filter(HTNO=i.roll_no).aggregate(C=Count('HTNO'))
                    i.Projects =k['C'] 
                    i.save()

                if Extracircular.objects.filter(HTNO = i.roll_no).exists() :
                    data1=Extracircular.objects.filter(HTNO=i.roll_no)
            
                    k=Extracircular.objects.filter(HTNO=i.roll_no).aggregate(C=Count('HTNO'))
                    i.Extracircular =k['C'] 
                    i.save()
                messages.info(request, 'Updated Successfully')

                

                CG = [SGPA[i]*credits[i] for i in range(len(SGPA))]
                if (sum(credits)!=0):
                     i.CGPA = round(sum(CG)/sum(credits),2)
                     i.save()
                    

    return render(request, 'update.html') 
    
@login_required
def results(request):
   # items=Student.objects.all().values()
    #df=pd.DataFrame(items)
    # Sem marks
    
    context1={}
    context2={}
    context3={}
    context4={}
    CGPA=[]
    SGPA1={}
    students=[]
    midmarks1={}
    midmarks2={}
    midmarks3={}
    midmarks4={}
    topscore={}
    sect={}
    Internship=[]
    Course=[]
    Project=[]
    Extracir=[]
    backlogs={}
    
    if request.method =='POST':
        roll= request.POST['roll']
        roll_no=[j for j in str(roll)]
        if Student.objects.filter(roll_no=roll).exists():
            st=Student.objects.filter(roll_no=roll)
            top=Student.objects.all()
            students.append(st)

            if Internships.objects.filter(HTNO = roll).exists() :
                    data1 =Internships.objects.filter(HTNO=roll)
                    Internship.append(data1)
                    


            if Courses.objects.filter(HTNO  = roll).exists() :
                    data1 =Courses.objects.filter(HTNO=roll)
                    Course.append(data1)
                    


            if Projects.objects.filter(HTNO  = roll).exists() :
                    data1 =Projects.objects.filter(HTNO=roll)
                    Project.append(data1)
                  

            if Extracircular.objects.filter(HTNO  = roll).exists() :
                    data1 =Extracircular.objects.filter(HTNO=roll)
                    Extracir.append(data1)
                  

            if Results_1_1.objects.filter(Htno = roll).exists() :
                    data1 =Results_1_1.objects.filter(Htno=roll)
                    Fail=Results_1_1.objects.filter(Htno=roll,Grade='F')
                    backlogs['1_1']=Fail
                    context1['1_1']=data1
                    for i in st:
                       SGPA1['1_1']=i.SGPA_1_1
                    sect1=[]
                    for i in top:
                        Htno=[j for j in str(i.roll_no)]
                        
                        if(Htno[0:2]==roll_no[0:2] and Htno[4:6]==roll_no[4:6]):
                                  sect1.append(i.SGPA_1_1)  

                    #semtop['1_1']= max(sect1)
                          
                    
            
            #2ND
  
            if Results_1_2.objects.filter(Htno = roll).exists() :
                    data1 =Results_1_2.objects.filter(Htno=roll)
                    context1['1_2']=data1
                    Fail=Results_1_2.objects.filter(Htno=roll,Grade='F')
                    backlogs['1_2']=Fail
                    for i in st:
                       SGPA1['1_2']=i.SGPA_1_2
                    sect1=[]
                    for i in top:
                        Htno=[j for j in str(i.roll_no)]
                        if(Htno[0:2]==roll_no[0:2] and Htno[4:6]==roll_no[4:6]):
                                  sect1.append(i.SGPA_1_2)  

                    #semtop['1_2']= max(sect1)                    
                   
            
            # 3RD
            if Results_2_1.objects.filter(Htno = roll).exists() :
                    data1 =Results_2_1.objects.filter(Htno=roll)
                    context2['2_1']=data1
                    Fail=Results_2_1.objects.filter(Htno=roll,Grade='F')
                    backlogs['2_1']=Fail
                    for i in st:
                       SGPA1['2_1']=i.SGPA_2_1
                    sect1=[]
                    for i in top:
                        Htno=[j for j in str(i.roll_no)]
                        if(roll_no[4:6]=='5A'):
                            if((Htno[0:2]==roll_no[0:2] and Htno[4:6]==roll_no[4:6]) or (int(Htno[0:2])+1==int(roll_no[0:2]) and Htno[6:8]== roll_no[6:8]) ):
                                  sect1.append(i.SGPA_2_1)
                        else:
                            if(Htno[0:2]==roll_no[0:2] and Htno[4:6]==roll_no[4:6]):
                                  sect1.append(i.SGPA_2_1)  

                                    

            if Results_2_2.objects.filter(Htno = roll).exists() :
                    data1 =Results_2_2.objects.filter(Htno=roll)
                    context2['2_2']=data1
                    Fail=Results_2_2.objects.filter(Htno=roll,Grade='F')
                    backlogs['2_2']=Fail
                    for i in st:
                       SGPA1['2_2']=i.SGPA_2_2
                    sect1=[]
                    for i in top:
                        Htno=[j for j in str(i.roll_no)]
                        if(roll_no[4:6]=='5A'):
                            if((Htno[0:2]==roll_no[0:2] and Htno[4:6]==roll_no[4:6]) or (int(Htno[0:2])+1==int(roll_no[0:2]) and Htno[6:8]== roll_no[6:8]) ):
                                  sect1.append(i.SGPA_2_2)
                        else:
                            if(Htno[0:2]==roll_no[0:2] and Htno[4:6]==roll_no[4:6]):
                                  sect1.append(i.SGPA_2_2)  
                  
            
            if Results_3_1.objects.filter(Htno = roll).exists() :
                    data1 =Results_3_1.objects.filter(Htno=roll)
                    context3['3_1']=data1
                    Fail=Results_3_1.objects.filter(Htno=roll,Grade='F')
                    backlogs['3_1']=Fail
                    for i in st:
                       SGPA1['3_1']=i.SGPA_3_1
                    sect1=[]
                    for i in top:
                        Htno=[j for j in str(i.roll_no)]
                        if(roll_no[4:6]=='5A'):
                            if((Htno[0:2]==roll_no[0:2] and Htno[4:6]==roll_no[4:6]) or (int(Htno[0:2])+1==int(roll_no[0:2]) and Htno[6:8]== roll_no[6:8]) ):
                                  sect1.append(i.SGPA_3_1)
                        else:
                            if(Htno[0:2]==roll_no[0:2] and Htno[4:6]==roll_no[4:6]):
                                  sect1.append(i.SGPA_3_1)  
                  

            if Results_3_2.objects.filter(Htno = roll).exists() :
                    data1 =Results_3_2.objects.filter(Htno=roll)
                    context3['3_2']=data1
                    Fail=Results_3_2.objects.filter(Htno=roll,Grade='F')
                    backlogs['3_2']=Fail
                    for i in st:
                       SGPA1['3_2']=i.SGPA_3_2
                    sect1=[]
                    for i in top:
                        Htno=[j for j in str(i.roll_no)]
                        if(roll_no[4:6]=='5A'):
                            if((Htno[0:2]==roll_no[0:2] and Htno[4:6]==roll_no[4:6]) or (int(Htno[0:2])+1==int(roll_no[0:2]) and Htno[6:8]== roll_no[6:8]) ):
                                  sect1.append(i.SGPA_3_2)
                        else:
                            if(Htno[0:2]==roll_no[0:2] and Htno[4:6]==roll_no[4:6]):
                                  sect1.append(i.SGPA_3_2)  

                

            if Results_4_1.objects.filter(Htno = roll).exists() :
                    data1 =Results_4_1.objects.filter(Htno=roll)
                    context4['4_1']=data1
                    Fail=Results_4_1.objects.filter(Htno=roll,Grade='F')
                    backlogs['4_1']=Fail
                    for i in st:
                       SGPA1['4_1']=i.SGPA_4_1
                    sect1=[]
                    for i in top:
                        Htno=[j for j in str(i.roll_no)]
                        if(roll_no[4:6]=='5A'):
                            if((Htno[0:2]==roll_no[0:2] and Htno[4:6]==roll_no[4:6]) or (int(Htno[0:2])+1==int(roll_no[0:2]) and Htno[6:8]== roll_no[6:8]) ):
                                  sect1.append(i.SGPA_4_1)
                        else:
                            if(Htno[0:2]==roll_no[0:2] and Htno[4:6]==roll_no[4:6]):
                                  sect1.append(i.SGPA_4_1)  

                   

            if Results_4_2.objects.filter(Htno = roll).exists() :
                    data1 =Results_4_2.objects.filter(Htno=roll)
                    context4['4_2']=data1
                    Fail=Results_4_2.objects.filter(Htno=roll,Grade='F')
                    backlogs['4_2']=Fail
                    for i in st:
                       SGPA1['4_2']=i.SGPA_4_2
                    sect1=[]
                    for i in top:
                        Htno=[j for j in str(i.roll_no)]
                        if(roll_no[4:6]=='5A'):
                            if((Htno[0:2]==roll_no[0:2] and Htno[4:6]==roll_no[4:6]) or (int(Htno[0:2])+1==int(roll_no[0:2]) and Htno[6:8]== roll_no[6:8]) ):
                                  sect1.append(i.SGPA_4_2)
                        else:
                            if(Htno[0:2]==roll_no[0:2] and Htno[4:6]==roll_no[4:6]):
                                  sect1.append(i.SGPA_4_2)  

                    
            CGPA.append(Student.CGPA)
            roll_no=[j for j in str(roll)]
            for i in top:
                Htno=[j for j in str(i.roll_no)]
                if(roll_no[4:6]=='5A'):
                      if((Htno[0:2]==roll_no[0:2] and Htno[4:6]==roll_no[4:6]) or (int(Htno[0:2])+1==int(roll_no[0:2]) and Htno[6:8]== roll_no[6:8]) ):
                            sect[i.roll_no]=i.CGPA
                else:
                    if(Htno[0:2]==roll_no[0:2] and Htno[4:6]==roll_no[4:6]):
                            sect[i.roll_no]=i.CGPA
            
            topper=max(zip(sect.values(), sect.keys()))[1]
            topscore[topper]= max(zip(sect.values(), sect.keys()))[0]
          
            

            
            
            #sem_name={'sem':{'data1':S1,'data2':S2,'data3':S3,'data4':S4,'data5':S5,'data6':S6,'data7':S7,'data8':S8}}
            if  Mid_1_1.objects.filter(HTNO = roll).exists() :
                m1= Mid_1_1.objects.filter(HTNO = roll)
                midmarks1['1_1']=m1
            
            if  Mid_1_2.objects.filter(HTNO = roll).exists() :
                m2= Mid_1_2.objects.filter(HTNO = roll)
                midmarks1['1_2']=m2
            
            if  Mid_2_1.objects.filter(HTNO = roll).exists() :
                m3= Mid_2_1.objects.filter(HTNO = roll)
                midmarks2['2_1']=m3

            if  Mid_2_2.objects.filter(HTNO = roll).exists() :
                m4= Mid_2_2.objects.filter(HTNO = roll)
                midmarks2['2_2']=m4

            if  Mid_3_1.objects.filter(HTNO = roll).exists() :
                m5= Mid_3_1.objects.filter(HTNO = roll)
                midmarks3['3_1']=m5

            if  Mid_3_2.objects.filter(HTNO = roll).exists() :
                m6= Mid_3_2.objects.filter(HTNO = roll)
                midmarks3['3_2']=m6
            
            if  Mid_4_1.objects.filter(HTNO = roll).exists() :
                m7= Mid_4_1.objects.filter(HTNO = roll)
                midmarks4['4_1']=m7

            if  Mid_4_2.objects.filter(HTNO = roll).exists() :
                m8= Mid_4_2.objects.filter(HTNO = roll)
                midmarks4['4_2']=m8
            
           
            
           
    return render(request,"results.html",{'data1':context1,'data2':context2,'data3':context3,'data4':context4,'SGPA':SGPA1,'CGPA':CGPA,'student':students,'mid1':midmarks1,'mid2':midmarks2,'mid3':midmarks3,'mid4':midmarks4,
                       'topscore':topscore,'Internships':Internship,'Courses':Course,'Projects':Project,'Extracircular':Extracir,'backlogs':backlogs})



    

