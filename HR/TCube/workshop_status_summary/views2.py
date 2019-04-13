from django.shortcuts import render
from datetime import datetime as dt
from django.db import connection
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from models import *
import MySQLdb
# Create your views here.
db_host="localhost"
db_username="root"
db_password=""
db_db="tcube"


query_to_execute="""
set global sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
set session sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
"""

def show_reports(request):
    return render(request,"reports.html")


def show_w_s_s(request):
    try:
        db = MySQLdb.connect(db_host,db_username,db_password,db_db)
        cursor = db.cursor()
        cursor.execute(query_to_execute)
        if request.method=="GET":         #convert to post afterwards
            startdate= request.GET.get("startdate")
            enddate= request.GET.get("enddate") 
            if(startdate):
                startdate= startdate.encode('ascii','ignore')
            if(enddate):
                enddate= enddate.encode('ascii','ignore')
        

            if ((startdate == None or startdate=="") and (enddate == None or startdate=="")):
                #nothing
                #print "one"
            
                qy="select p.workshop ,name,DATE_FORMAT(p.startdate, '%d %M %Y') as startdate1,DATE_FORMAT(p.enddate, '%d %M %Y') as enddate1, sum(if( status in ('Approved','Elig. Approved','Request Approved') ,count,0)) 'Approved',sum(if(status in ('','1','Cancelled','incomplete','Request Verified','Waiting','Waitlisted','Withdrawn') or status is null,count,0)) 'Cancelled',sum( if (status in ( 'Confirmed','Moodle Accessed','Request Confirmed'),count,0)) 'Confirmed',sum(if(status ='Completed',count,0)) 'Certified',sum(if(status in ( 'Registration Invalid','Rejected'),count,0)) 'Invalid',sum(if(status in ( 'enrolled','Prov. Enrolled','Registered','Request Registered'),count,0)) 'Registered',sum(count) Total from participant_status p, workshops w where workshop=w.workshopid and workshop > 0 group by p.workshop,p.name order by p.startdate desc"
                cursor.execute(qy)
                #print qy
                data = cursor.fetchall()
        

            elif (startdate == None or startdate==""):
                #Only end
                #print "two"
    
                argm = "select p.workshop ,name,DATE_FORMAT(p.startdate, '%%d %%M %%Y') as startdate1 , DATE_FORMAT(p.enddate, '%%d %%M %%Y') as enddate1, sum(if( status in ('Approved','Elig. Approved','Request Approved') ,count,0)) 'Approved',sum(if(status in ('','1','Cancelled','incomplete','Request Verified','Waiting','Waitlisted','Withdrawn') or status is null,count,0)) 'Cancelled' ,sum(if(status in ( 'Confirmed','Moodle Accessed','Request Confirmed'),count,0)) 'Confirmed' ,sum(if(status ='Completed',count,0)) 'Certified',sum(if(status in ( 'Registration Invalid','Rejected'),count,0)) 'Invalid' ,sum(if(status in ( 'enrolled','Prov. Enrolled','Registered','Request Registered'),count,0)) 'Registered' ,sum(count) Total from participant_status p, workshops w where workshop=w.workshopid and workshop > 0 and w.startdate >= STR_TO_DATE(%s,'%%m/%%d/%%Y') group by p.workshop,p.name order by p.startdate desc"
                cursor.execute(argm,(str(enddate)))
                data = cursor.fetchall()
            

            elif (enddate == None or enddate==""):
                #Only start
                #print "three"
    
                argm = "select p.workshop ,name,DATE_FORMAT(p.startdate, '%%d %%M %%Y') as startdate1, DATE_FORMAT(p.enddate, '%%d %%M %%Y') as enddate1, sum(if( status in ('Approved','Elig. Approved','Request Approved') ,count,0)) 'Approved',sum(if(status in ('','1','Cancelled','incomplete','Request Verified','Waiting','Waitlisted','Withdrawn')  or status is null,count,0)) 'Cancelled' ,sum(if(status in ( 'Confirmed','Moodle Accessed','Request Confirmed'),count,0)) 'Confirmed',sum(if(status ='Completed',count,0)) 'Certified',sum(if(status in ( 'Registration Invalid','Rejected'),count,0)) 'Invalid',sum(if(status in ( 'enrolled','Prov. Enrolled','Registered','Request Registered'),count,0)) 'Registered',sum(count) Total from participant_status p, workshops w where workshop=w.workshopid and workshop > 0 and  w.startdate <= STR_TO_DATE(%s,'%%m/%%d/%%Y') group by p.workshop,p.name order by p.startdate desc"
                cursor.execute(argm,(str(startdate)))
                data = cursor.fetchall()    
            
            
            else: 
                #Both given
                #print "four"
    
                argm = "select p.workshop ,name,DATE_FORMAT(p.startdate, '%%d %%M %%Y') as startdate1 , DATE_FORMAT(p.enddate, '%%d %%M %%Y') as enddate1, sum(if( status in ('Approved','Elig. Approved','Request Approved') ,count,0)) 'Approved',sum(if(status in ('','1','Cancelled','incomplete','Request Verified','Waiting','Waitlisted','Withdrawn') or status is null,count,0)) 'Cancelled' ,sum(if(status in ( 'Confirmed','Moodle Accessed','Request Confirmed'),count,0)) 'Confirmed' ,sum(if(status ='Completed',count,0)) 'Certified',sum(if(status in ( 'Registration Invalid','Rejected'),count,0)) 'Invalid' ,sum(if(status in ( 'enrolled','Prov. Enrolled','Registered','Request Registered'),count,0)) 'Registered' ,sum(count) Total from participant_status p, workshops w where workshop=w.workshopid and workshop > 0 and w.startdate >= STR_TO_DATE(%s,'%%m/%%d/%%Y') and w.startdate <= STR_TO_DATE(%s,'%%m/%%d/%%Y') group by p.workshop,p.name order by p.startdate desc"
                cursor.execute(argm,(str(startdate),str(enddate)))
                data = cursor.fetchall()
            
        
            #print data
    
            context = {"result": data,}
            cursor.close()
            return render(request,"workshop_status_summary.html",context)
    except Exception as error:
        cursor.close()
        return HttpResponse(str(error.message))
        

def login_not_register(request):
    try:
        db = MySQLdb.connect(db_host,db_username,db_password,db_db)
        cursor = db.cursor()
        cursor.execute(query_to_execute)
        cursor.execute("select login.login_id, login.login_name,person.firstname,person.lastname ,institute.institutename from login, person,institute  where person.personid=login.login_id and institute.idinstitute=person.instituteid and  not exists (select contextid from participant where participant.contextid=login.login_id) and login.usertypeid=1")
        data = cursor.fetchall()
        for each in data:       
            #print each
            pass
    
        context = {
                "result": data,
              }
        cursor.close()
        return render(request,"login_not_register.html",context)
    except Exception as error:
        cursor.close()
        return HttpResponse(str(error.message))
    

def invite_not_register(request):
    try:
        db = MySQLdb.connect(db_host,db_username,db_password,db_db)
        cursor = db.cursor()
        cursor.execute(query_to_execute)
        cursor.execute("select pud.userinterfaceid,         pud.email,pud.workshopid,pud.firstname,pud.lastname,pud.rcid,pud.institutename from partuserdata pud where status='valid' and not exists (select  c.email from accomodation a,participant p,context c where a.participantid=p.participantid and p.contextid=c.idcontext and status != 'Cancelled' and pud.workshopid=a.workshopid and pud.email=c.email)")
        data = cursor.fetchall()
        context = {
                "result": data,
            }
        cursor.close()
        return render(request,"invite_not_register.html",context)
    except Exception as error:
        cursor.close()
        return HttpResponse(str(error.message))
    

def enable_disable(request):
    try:
        db = MySQLdb.connect(db_host,db_username,db_password,db_db)
        cursor = db.cursor()
        cursor.execute(query_to_execute)
        if request.method == 'POST':
            uid=request.POST.get("uid")
            uid=long(uid)
            #print (uid)

            cursor.execute("update partuserdata set userinterfaceid="+ str(-1*uid)+" WHERE userinterfaceid="+str(uid)+"")
            cursor.execute("select * from partuserdata where userinterfaceid=" + str(-1*uid))
            data = cursor.fetchall()
            db.commit()
            cursor.close()
            return HttpResponseRedirect("../")      
    except Exception as error:
        cursor.close()
        return HttpResponse(str(error.message))
    

        
def show_w_d(request):
    try:
        db = MySQLdb.connect(db_host,db_username,db_password,db_db)
        cursor = db.cursor()
        cursor.execute(query_to_execute)
        if request.method=="GET":         #convert to post afterwards
            startdate= request.GET.get("startdate")
            enddate= request.GET.get("enddate")
            if(startdate):
                startdate= startdate.encode('ascii','ignore')
            if(enddate):
                enddate= enddate.encode('ascii','ignore')
        
            if((startdate == None or startdate=="") and (enddate == None or startdate=="")):
                qy="select w.workshopid,w.workshopname,w.categorycode,count(distinct a.rcid ) rc, count(distinct instituteid) as 'intstituteid',count(distinct city) as 'city', count(distinct state) as 'state', sum(Female) as 'female',sum(otherg) as 'other_gender',count(*) as total, sum(Male) as 'male',sum(unknown_exp) as 'unknown_exp', sum(less_than_2) as 'exp_less_than_2',sum(2_to_10) as 'exp_2_to_10',sum(greater_than_10) as 'exp_greater_than_10', sum(Doctorate) as 'doctorate',sum(PostGraduate) as 'postgraduate',sum(Graduate) as 'graduate',sum(Diploma) as 'diploma',sum(others) as 'others' from confirmed_participants a , workshops w where a.workshopid = w.workshopid and w.workshopid > 0 and a.participantid in (select participantid from participant where status IN ('Confirmed','Moodle Accessed','Request Confirmed','Completed')) group by w.workshopid, w.workshopname ,w.categorycode order by w.startdate desc"
                cursor.execute(qy)
                data = cursor.fetchall()

            elif (startdate == None or startdate==""):
                argm = "select w.workshopid,w.workshopname,w.categorycode,count(distinct a.rcid ) rc, count(distinct instituteid) as 'intstituteid',count(distinct city) as 'city', count(distinct state) as 'state', sum(Female) as 'female',sum(otherg) as 'other_gender',count(*) as total, sum(Male) as 'male',sum(unknown_exp) as 'unknown_exp', sum(less_than_2) as 'exp_less_than_2',sum(2_to_10) as 'exp_2_to_10',sum(greater_than_10) as 'exp_greater_than_10', sum(Doctorate) as 'doctorate',sum(PostGraduate) as 'postgraduate',sum(Graduate) as 'graduate',sum(Diploma) as 'diploma',sum(others) as 'others' from confirmed_participants a , workshops w where a.workshopid = w.workshopid and w.workshopid > 0 and w.startdate <= STR_TO_DATE(%s,'%%m/%%d/%%Y') and a.participantid in (select participantid from participant where status IN ('Confirmed','Moodle Accessed','Request Confirmed','Completed')) group by w.workshopid, w.workshopname ,w.categorycode order by w.startdate desc"
                cursor.execute(argm,(str(enddate)))
                data = cursor.fetchall()


            elif (enddate == None or enddate==""):
                argm = "select w.workshopid,w.workshopname,w.categorycode,count(distinct a.rcid ) rc, count(distinct instituteid) as 'intstituteid',count(distinct city) as 'city', count(distinct state) as 'state', sum(Female) as 'female',sum(otherg) as 'other_gender',count(*) as total, sum(Male) as 'male',sum(unknown_exp) as 'unknown_exp', sum(less_than_2) as 'exp_less_than_2',sum(2_to_10) as 'exp_2_to_10',sum(greater_than_10) as 'exp_greater_than_10', sum(Doctorate) as 'doctorate',sum(PostGraduate) as 'postgraduate',sum(Graduate) as 'graduate',sum(Diploma) as 'diploma',sum(others) as 'others' from confirmed_participants a , workshops w where a.workshopid = w.workshopid and w.workshopid > 0 and w.startdate >= STR_TO_DATE(%s,'%%m/%%d/%%Y') and a.participantid in (select participantid from participant where status IN ('Confirmed','Moodle Accessed','Request Confirmed','Completed')) group by w.workshopid, w.workshopname ,w.categorycode order by w.startdate desc"
                cursor.execute(argm,(str(startdate)))
                data = cursor.fetchall()    
            
            else:
                argm = "select w.workshopid,w.workshopname,w.categorycode,count(distinct a.rcid ) rc, count(distinct instituteid) as 'intstituteid',count(distinct city) as 'city', count(distinct state) as 'state', sum(Female) as 'female',sum(otherg) as 'other_gender',count(*) as total, sum(Male) as 'male',sum(unknown_exp) as 'unknown_exp', sum(less_than_2) as 'exp_less_than_2',sum(2_to_10) as 'exp_2_to_10',sum(greater_than_10) as 'exp_greater_than_10', sum(Doctorate) as 'doctorate',sum(PostGraduate) as 'postgraduate',sum(Graduate) as 'graduate',sum(Diploma) as 'diploma',sum(others) as 'others' from confirmed_participants a , workshops w where a.workshopid = w.workshopid and w.workshopid > 0 and w.startdate >= STR_TO_DATE(%s,'%%m/%%d/%%Y') and w.startdate <= STR_TO_DATE(%s,'%%m/%%d/%%Y') and a.participantid in (select participantid from participant where status IN ('Confirmed','Moodle Accessed','Request Confirmed','Completed')) group by w.workshopid, w.workshopname ,w.categorycode order by w.startdate desc"   
                cursor.execute(argm,(str(startdate),str(enddate)))
                data = cursor.fetchall()

            #print data 

            context = {
                    "result": data,
                  }
            
            return render(request,"workshop_diversity.html",context)
        cursor.close()
        return HttpResponseRedirect("")         
    except Exception as error:
        cursor.close()
        return HttpResponse(str(error.message))

def ws_p_wise(request):
    try:
        db = MySQLdb.connect(db_host,db_username,db_password,db_db)
        cursor = db.cursor()
        cursor.execute(query_to_execute)
        qy="select count(distinct(a.workshopid)) as workshopCount, pa.personid,p.genderinfo,concat(p.firstname,' ',p.lastname) as name from participant pa left join accomodation a on pa.participantid = a.participantid left join person p on pa.personid=p.personid where pa.status in ('Confirmed','Completed', 'Moodle Accessed', 'Request Confirmed')  group by pa.personid order by pa.personid"
        cursor.execute(qy)
        data = cursor.fetchall()

        context = {
                "result": data,
              }
        cursor.close()
        return render(request,"total_ws_by_participant_wise.html",context)      
    except Exception as error:
        cursor.close()
        return HttpResponse(str(error.message))

def ws_i_wise(request):
    try:
        db = MySQLdb.connect(db_host,db_username,db_password,db_db)
        cursor = db.cursor()
        cursor.execute(query_to_execute)
        argm = "select count(distinct(a.workshopid)) as workshopCount,pa.instituteid,i.institutename from participant pa,accomodation a, institute i where  pa.instituteid = i.idInstitute and a.participantid = pa.participantid and i.isActive IN (1,0,-1) and pa.status in ('Confirmed','Completed','Moodle Accessed', 'Request Confirmed')  group by pa.instituteid  order by pa.instituteid"
        cursor.execute(argm)
        data = cursor.fetchall()


        context = {
                "result": data,
              }
        cursor.close()
        return render(request,"total_ws_by_institute_wise.html",context)        
    except Exception as error:
        cursor.close()
        return HttpResponse(str(error.message))
    
def show_state_wise(request):
    try:
        db = MySQLdb.connect(db_host,db_username,db_password,db_db)
        cursor = db.cursor()
        cursor.execute(query_to_execute)
        if request.method=="GET":         #convert to post afterwards
            startdate= request.GET.get("startdate")
            enddate= request.GET.get("enddate")
            if(startdate):
                startdate= startdate.encode('ascii','ignore')
            if(enddate):
                enddate= enddate.encode('ascii','ignore')

            if((startdate == None or startdate=="") and (enddate == None or startdate=="")):
                qy="select s.state, count(distinct rcid) as 'rcid',count(distinct workshopid) as 'workshopid', count(distinct c.instituteid) as 'instituteid',count(participantid) as 'participantid' ,sum(Male) as 'Male',sum(Female) as 'female',sum(otherg) as 'other_gender',count(*) as total, sum(unknown_exp) as 'unknown_exp',sum(less_than_2) as 'exp_less_than_2',sum(2_to_10) as 'exp_2_to_10',sum(greater_than_10) as 'exp_greater_than_10', sum(Doctorate) as 'doctorate',sum(PostGraduate) as 'postgraduate',sum(Graduate) as 'graduate',sum(Diploma) as 'diploma',sum(others) as 'others' from confirmed_participants c,remotecenter r,state s where r.remotecenterid = c.rcid and s.stateid=r.state group by r.state order by s.state"
                cursor.execute(qy)
                data = cursor.fetchall()

            elif (startdate == None or startdate==""):
                argm = "select s.state, count(distinct rcid) as 'rcid',count(distinct c.workshopid) as 'workshopid', count(distinct c.instituteid) as 'instituteid',count(participantid) as 'participantid',sum(Male) as 'Male',sum(Female) as 'female',sum(otherg) as 'other_gender',count(*) as total, sum(unknown_exp) as 'unknown_exp',sum(less_than_2) as 'exp_less_than_2',sum(2_to_10) as 'exp_2_to_10',sum(greater_than_10) as 'exp_greater_than_10', sum(Doctorate) as 'doctorate', sum(PostGraduate) as 'postgraduate',sum(Graduate) as 'graduate',sum(Diploma) as 'diploma', sum(others) as 'others' from confirmed_participants c,remotecenter r,state s, workshops w where c.workshopid=w.workshopid and w.workshopid > 0 and  w.startdate <= STR_TO_DATE(%s,'%%m/%%d/%%Y')  and r.remotecenterid = c.rcid and s.stateid=r.state group by r.state order by s.state"
                cursor.execute(argm,(str(enddate)))
                data = cursor.fetchall()


            elif (enddate == None or enddate==""):
                argm = "select s.state, count(distinct rcid) as 'rcid',count(distinct c.workshopid) as 'workshopid', count(distinct c.instituteid) as 'instituteid',count(participantid) as 'participantid',sum(Male) as 'Male',sum(Female) as 'female',sum(otherg) as 'other_gender',count(*) as total, sum(unknown_exp) as 'unknown_exp',sum(less_than_2) as 'exp_less_than_2',sum(2_to_10) as 'exp_2_to_10',sum(greater_than_10) as 'exp_greater_than_10', sum(Doctorate) as 'doctorate', sum(PostGraduate) as 'postgraduate',sum(Graduate) as 'graduate',sum(Diploma) as 'diploma', sum(others) as 'others' from confirmed_participants c,remotecenter r,state s, workshops w where c.workshopid=w.workshopid and w.workshopid > 0 and w.startdate >= STR_TO_DATE(%s,'%%m/%%d/%%Y')  and r.remotecenterid = c.rcid and s.stateid=r.state group by r.state order by s.state"
                cursor.execute(argm,(str(startdate)))
                data = cursor.fetchall()    
            
            else:
                argm = "select s.state, count(distinct rcid) as 'rcid',count(distinct c.workshopid) as 'workshopid', count(distinct c.instituteid) as 'instituteid',count(participantid) as 'participantid',sum(Male) as 'Male',sum(Female) as 'female',sum(otherg) as 'other_gender',count(*) as total, sum(unknown_exp) as 'unknown_exp',sum(less_than_2) as 'exp_less_than_2',sum(2_to_10) as 'exp_2_to_10',sum(greater_than_10) as 'exp_greater_than_10', sum(Doctorate) as 'doctorate', sum(PostGraduate) as 'postgraduate',sum(Graduate) as 'graduate',sum(Diploma) as 'diploma', sum(others) as 'others' from confirmed_participants c,remotecenter r,state s, workshops w where c.workshopid=w.workshopid and w.workshopid > 0 and w.startdate >= STR_TO_DATE(%s,'%%m/%%d/%%Y')  and w.startdate <= STR_TO_DATE(%s,'%%m/%%d/%%Y')  and r.remotecenterid = c.rcid and s.stateid=r.state group by r.state order by s.state"
                cursor.execute(argm,(str(startdate),str(enddate)))
                data = cursor.fetchall()

            #print data     

            context = {
                    "result": data,
                  }
            
            return render(request,"state_wise_summary.html",context)
        cursor.close()
        return HttpResponseRedirect("")                 

    except Exception as error:
        cursor.close()
        return HttpResponse(str(error.message))

def show_rc_wise(request):
    try:
        db = MySQLdb.connect(db_host,db_username,db_password,db_db)
        cursor = db.cursor()
        cursor.execute(query_to_execute)
        if request.GET:         #convert to post afterwards
            startdate= request.GET.get("startdate")
            enddate= request.GET.get("enddate")
            if(startdate):
                startdate= startdate.encode('ascii','ignore')
            if(enddate):
                enddate= enddate.encode('ascii','ignore')
    

            if((startdate == None or startdate=="") and (enddate == None or startdate=="")):
                qy="select rcid, remotecentername ,s.state,ci.city, count(distinct c.workshopid) as 'workshopid', count(distinct c.instituteid) as 'instituteid',count(participantid) as 'participantid',sum(Male) as 'Male',sum(Female) as 'female',sum(otherg) as 'other_gender',count(*) as total,sum(unknown_exp) as 'unknown_exp', sum(less_than_2) as 'exp_less_than_2',sum(2_to_10) as 'exp_2_to_10',sum(greater_than_10) as 'exp_greater_than_10', sum(Doctorate) as 'doctorate',sum(PostGraduate) as 'postgraduate',sum(Graduate) as 'graduate',sum(Diploma) as 'diploma',sum(others) as 'others' from confirmed_participants c,remotecenter r,state s,city ci where r.remotecenterid = c.rcid and r.state=s.stateid and r.city=ci.cityid group by (case when rcid in (0,-1) then \"Unknown\" else rcid end)"
                #print qy
                cursor.execute(qy)
                data = cursor.fetchall()

            elif (startdate == None or startdate==""):
                argm = "select rcid, remotecentername,s.state,ci.city, count(distinct c.workshopid) as 'workshopid', count(distinct c.instituteid) as 'instituteid',count(participantid) as 'participantid',sum(Male) as 'Male',sum(Female) as 'female',sum(otherg) as 'other_gender',count(*) as total,sum(unknown_exp) as 'unknown_exp', sum(less_than_2) as 'exp_less_than_2',sum(2_to_10) as 'exp_2_to_10',sum(greater_than_10) as 'exp_greater_than_10', sum(Doctorate) as 'doctorate',sum(PostGraduate) as 'postgraduate',sum(Graduate) as 'graduate',sum(Diploma) as 'diploma',sum(others) as 'others' from confirmed_participants c,remotecenter r,state s,city ci, workshops w where c.workshopid=w.workshopid and w.workshopid > 0 and w.startdate <= STR_TO_DATE(%s,'%%m/%%d/%%Y') and r.remotecenterid = c.rcid and r.state=s.stateid and r.city=ci.cityid group by (case when rcid in (0,-1) then \"Unknown\" else rcid end)"
                cursor.execute(argm,(str(enddate)))
                data = cursor.fetchall()


            elif (enddate == None or enddate==""):
                argm = "select rcid, remotecentername,s.state,ci.city, count(distinct c.workshopid) as 'workshopid', count(distinct c.instituteid) as 'instituteid',count(participantid) as 'participantid',sum(Male) as 'Male',sum(Female) as 'female',sum(otherg) as 'other_gender',count(*) as total,sum(unknown_exp) as 'unknown_exp', sum(less_than_2) as 'exp_less_than_2',sum(2_to_10) as 'exp_2_to_10',sum(greater_than_10) as 'exp_greater_than_10', sum(Doctorate) as 'doctorate',sum(PostGraduate) as 'postgraduate',sum(Graduate) as 'graduate',sum(Diploma) as 'diploma',sum(others) as 'others' from confirmed_participants c,remotecenter r,state s,city ci, workshops w where c.workshopid=w.workshopid and w.workshopid > 0 and w.startdate >= STR_TO_DATE(%s,'%%m/%%d/%%Y') and r.remotecenterid = c.rcid and r.state=s.stateid and r.city=ci.cityid group by (case when rcid in (0,-1) then \"Unknown\" else rcid end)"
                cursor.execute(argm,(str(startdate)))
                data = cursor.fetchall()    
            
            else:
                argm = "select rcid, remotecentername,s.state,ci.city, count(distinct c.workshopid) as 'workshopid', count(distinct c.instituteid) as 'instituteid',count(participantid) as 'participantid',sum(Male) as 'Male',sum(Female) as 'female',sum(otherg) as 'other_gender',count(*) as total,sum(unknown_exp) as 'unknown_exp', sum(less_than_2) as 'exp_less_than_2',sum(2_to_10) as 'exp_2_to_10',sum(greater_than_10) as 'exp_greater_than_10', sum(Doctorate) as 'doctorate',sum(PostGraduate) as 'postgraduate',sum(Graduate) as 'graduate',sum(Diploma) as 'diploma',sum(others) as 'others' from confirmed_participants c,remotecenter r,state s,city ci, workshops w where c.workshopid=w.workshopid and w.workshopid > 0 and w.startdate >= STR_TO_DATE(%s,'%%m/%%d/%%Y') and w.startdate <= STR_TO_DATE(%s,'%%m/%%d/%%Y') and r.remotecenterid = c.rcid and r.state=s.stateid and r.city=ci.cityid group by (case when rcid in (0,-1) then \"Unknown\" else rcid end)"
                cursor.execute(argm,(str(startdate),str(enddate)))
                data = cursor.fetchall()

            #print data     

            context = {
                    "result": data,
                  }
            
            return render(request,"remote_centre_wise.html",context)
        cursor.close()
        return HttpResponseRedirect("")     

    except Exception as error:
        cursor.close()
        return HttpResponse(str(error.message))
    
