from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.template import loader,Context,Template
from .models import *
from models import Context as Contxt
from . import globals
from django.db import connection
from django.core import serializers
import json,datetime,os
from django.conf import settings
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage,EmailMultiAlternatives,send_mail
from django.core.urlresolvers import reverse
import role_manage.models as role_manage_models

#to display the details of participants in the selected workshop
def status_manage(request,wsid=None,n=None,rcid=None):
    #role_id=5
    page_id=63
    try:
	role_id=request.session['role_id']
    except Exception:
	role_id=0
    if(role_manage_models.check_page_permission(role_id,page_id)):
	    globals.init()
	    accomo=[]
	    facetofaceintr=Workshops.objects.get(workshopid=wsid).facetofaceintrif_available
	    if(int(rcid)==0 and facetofaceintr==0):
		accomo=Accomodation.objects.filter(workshopid=wsid)
		flag=0
		check=0
	    elif(int(rcid)==0 and facetofaceintr==1):
		accomo=Accomodation.objects.filter(workshopid=wsid)
		flag=1
		check=0
	    else:    
		if(facetofaceintr==0):
		    accomos=Accomodation.objects.filter(workshopid=wsid)

		    for each in accomos:
		        if(each.participantid.contextid.state == int(rcid)):
		            accomo.append(each)
		    qs=State.objects.get(stateid=rcid)
		    flag=0
		else:
		    accomo=Accomodation.objects.filter(workshopid=wsid,instituteid=rcid)
		    qs=Remotecenter.objects.get(remotecenterid=rcid)
		    flag=1
		check=1
	    state=State.objects.all()
	    wshop=Workshops.objects.get(workshopid=wsid)
	    i=0
	    requestregistered=0
	    requestinvalid=0
	    requestapproved=0
	    confirmed=0
	    completed=0
	    cancelled=0
	    accepted=0
	    allstatus=len(accomo)
	    for each in accomo:
		status=each.participantid.status
		if(status=='Request Registered'):
		    requestregistered+=1
		elif(status=='Registration Invalid'):
		    requestinvalid+=1
		elif(status=='Request Approved'):
		    requestapproved+=1
		elif(status=='Confirmed'):
		    confirmed+=1
		elif(status=='Completed'):
		    completed+=1
		elif(status=='Cancelled'):
		    cancelled+=1
		elif(status=='Accepted'):
		    accepted+=1
	    acco=[]
	    if(int(n)==0):
		for each in accomo:
		        acco.append(each)
	    elif(int(n)==1):
		for each in accomo:
		    if(each.participantid.status=='Request Registered'):
		        acco.append(each)
	    elif(int(n)==2):
		for each in accomo:
		    if(each.participantid.status=='Registration Invalid'):
		        acco.append(each)
	    elif(int(n)==3):
		for each in accomo:
		    if(each.participantid.status=='Request Approved'):
		        acco.append(each)
	    elif(int(n)==4):
		for each in accomo:
		    if(each.participantid.status=='Confirmed'):
		        acco.append(each)
	    elif(int(n)==5):
		for each in accomo:
		    if(each.participantid.status=='Completed'):
		        acco.append(each)
	    elif(int(n)==6):
		for each in accomo:
		    if(each.participantid.status=='Cancelled'):
		        acco.append(each)
	    elif(int(n)==7):
		for each in accomo:
		    if(each.participantid.status=='Accepted'):
		        acco.append(each)
	    object_list=[]
	    qrcc=Remotecentercapacity.objects.filter(workshopid=wsid).order_by('rcid')
	    for each in qrcc:
		try:
		       x=Remotecenter.objects.get(remotecenterid=each.rcid)
		       each.remotecentername=x.remotecentername
		except Remotecenter.DoesNotExist:
		       each.remotecentername='NA'
	    for each in acco:
		try:
		       qletter=Letter.objects.get(participantid=each.participantid.participantid)
		       each.letter=qletter.letter
		except Letter.DoesNotExist:
		       each.letter='NA'
		try:
		       qinstitute=Institute.objects.get(idinstitute=each.participantid.personid.instituteid)
		       each.institutename=qinstitute.institutename
		except Institute.DoesNotExist:
		       each.institutename='NA'
		try:
		       qstate=State.objects.get(stateid=each.participantid.contextid.state)
		       each.state=qstate.state
		except State.DoesNotExist:
		       each.state='NA'
		try:
		       qstatusmatrix=StatusMatrix.objects.get(initialstatus=each.participantid.status)
		       each.registered=qstatusmatrix.registered
		       each.invalid=qstatusmatrix.invalid
		       each.approved=qstatusmatrix.approved
		       each.confirmed=qstatusmatrix.confirmed
		       each.completed=qstatusmatrix.completed
		       each.cancelled=qstatusmatrix.cancelled
		except StatusMatrix.DoesNotExist:
		       each.registered='N'
		       each.invalid='N'
		       each.approved='N'
		       each.confirmed='N'
		       each.completed='N'
		       each.cancelled='N'
		try:
		       x=Remotecenter.objects.get(remotecenterid=each.instituteid)
		       each.remotecentername=x.remotecentername
		except Remotecenter.DoesNotExist:
		       each.remotecentername='NA'
		each.regtime=acco[i].participantid.regtime
		each.status=acco[i].participantid.status
		each.firstname=acco[i].participantid.personid.firstname
		each.lastname=acco[i].participantid.personid.lastname
		each.experience=acco[i].participantid.personid.experience
		each.image=acco[i].participantid.personid.image
		each.qualification=acco[i].participantid.personid.qualification
		each.email=acco[i].participantid.contextid.email
		each.mobile=acco[i].participantid.contextid.mobile
		try:
		       each.designation=(Lookups.objects.get(category='designation',code=each.participantid.personid.designation)).description
		except Lookups.DoesNotExist:
		       each.designation='NA'
		try:
		       each.stream=(Lookups.objects.get(category='Stream',code=each.participantid.personid.streamid)).description
		except Lookups.DoesNotExist:
		       each.stream='NA'
		each.certificate=Participant.objects.get(participantid=each.participantid.participantid).eligible_for_certificate
		each.payment=Participant.objects.get(participantid=each.participantid.participantid).payment
		i+=1
		object_list.append(each)
	    invalidReasons=Lookups.objects.filter(category='INVALID_RC',isactive=1)
	    if(check==1):
		context = {
		    "object_list": object_list,
		    "wsid": wsid,
		    "rcid": rcid,
		    "num":n,
		    "qrcc": qrcc,
		    "qs": qs,
		    "rr": requestregistered,
		    "ri": requestinvalid,
		    "ra": requestapproved,
		    "con": confirmed,
		    "com": completed,
		    "can": cancelled,
		    "ac": accepted,
		    "al": allstatus,
		    "check": check,
		    "wshop": wshop,
		    "state":state,
		    "flag": flag,
		    "listReasons":invalidReasons,
		    }
	    else:
		context = {
		    "object_list": object_list,
		    "wsid": wsid,
		    "rcid": rcid,
		    "num":n,
		    "qrcc": qrcc,
		    "rr": requestregistered,
		    "ri": requestinvalid,
		    "ra": requestapproved,
		    "con": confirmed,
		    "com": completed,
		    "can": cancelled,
		    "ac": accepted,
		    "al": allstatus,
		    "check": check,
		    "wshop": wshop,
		    "state":state,
		    "flag": flag,
		    "listReasons":invalidReasons,
		    }
	    context.update(globals.myList)
	    return render(request,"statusManagement.html",context)
    else:
	    storePrevUrl(request,HttpRequest.build_absolute_uri(request))
    	    return HttpResponseRedirect("/")	    

#to select the workshop for update status
def status(request):
	#role_id=5
	page_id=62
	try:
		role_id=request.session['role_id']
	except Exception:
		role_id=0
	if(role_manage_models.check_page_permission(role_id,page_id)):
		globals.init()
		queryset=Workshops.objects.filter(startdate__gt = '2015-07-01').order_by('startdate');
		context = {
			"object_list": queryset,
			}
		context.update(globals.myList)
		return render(request, "updateStatus.html", context)
	else:
		storePrevUrl(request,HttpRequest.build_absolute_uri(request))
    	    	return HttpResponseRedirect("/")	    

#for the button View Seats
def viewRCCapacity(request,wsid,n):
	#role_id=5
	page_id=64
	try:
		role_id=request.session['role_id']
	except Exception:
		role_id=0
	if(role_manage_models.check_page_permission(role_id,page_id)):
		globals.init()
		qs=Workshops.objects.get(workshopid=wsid)
		rcc=Remotecentercapacity.objects.filter(workshopid=wsid)
		ans=[]
		for each in rcc:
			x=Remotecenter.objects.get(remotecenterid=each.rcid)
			each.rcname=x.remotecentername
			each.rcstate=x.state.state
			seat=Accomodation.objects.filter(workshopid=wsid,instituteid=each.rcid)
			acco=Accomodation.objects.filter(workshopid=wsid,accomodation='Yes',instituteid=each.rcid)
			i=0
			j=0
			for each1 in acco:
				if(each1.participantid.status!='Cancelled'):
					i+=1
			for each1 in seat:
				if(each1.participantid.status!='Cancelled'):
					j+=1
			each.acco_booked=i
			each.seats_booked=j
			each.seats_remain=each.available_seats-j
			ans.append(each)
		if(n=='0'):
			context = {
				"wsid":wsid,
				"object_list": ans,
				"workshopname":qs.workshopname,
				"startdate":qs.startdate,
				"enddate":qs.enddate,
				}
		elif(n=='1'):
			ans1=[]
			for each in ans:
				if(each.seats_booked==0):
					ans1.append(each)
			context = {
				"wsid":wsid,
				"object_list": ans1,
				"workshopname":qs.workshopname,
				"startdate":qs.startdate,
				"enddate":qs.enddate,
				}
		elif(n=='2'):
			ans2=[]
			for each in ans:
				if(each.seats_booked>0 and each.seats_booked<=5):
					ans2.append(each)
			context = {
				"wsid":wsid,
				"object_list": ans2,
				"workshopname":qs.workshopname,
				"startdate":qs.startdate,
				"enddate":qs.enddate,
				}
		elif(n=='3'):
			ans3=[]
			for each in ans:
				if(each.seats_remain>=0 and each.seats_remain<=5):
					ans3.append(each)
			context = {
				"wsid":wsid,
				"object_list": ans3,
				"workshopname":qs.workshopname,
				"startdate":qs.startdate,
				"enddate":qs.enddate,
				}
		elif(n=='4'):
			ans4=[]
			for each in ans:
				if(each.seats_remain<0):
					ans4.append(each)
			context = {
				"wsid":wsid,
				"object_list": ans4,
				"workshopname":qs.workshopname,
				"startdate":qs.startdate,
				"enddate":qs.enddate,
				}
		context.update(globals.myList)
		return render(request, "viewRCList.html", context)
	else:
		storePrevUrl(request,HttpRequest.build_absolute_uri(request))
		return HttpResponseRedirect("/")

#to change the status of participant
def changeStatus(request):
	pid=int(request.GET["pid"])
	btnid=request.GET["btnid"]
	wsid=int(request.GET["wsid"])
	rc_payment=Workshops.objects.get(workshopid=wsid).rc_payment_if_required
	wsname=Workshops.objects.get(workshopid=wsid).workshopname
	contextId=Participant.objects.get(participantid=pid).contextid.idcontext
	emailId=Contxt.objects.get(idcontext=contextId).email
	personId=Participant.objects.get(participantid=pid).personid.personid
	name=Person.objects.get(personid=personId).firstname
	q=Participant.objects.filter(participantid=pid)
	cursor = connection.cursor()
	if(btnid=='approvedButton'):
		cursor.execute("UPDATE participant SET status = 'Request Approved' WHERE participantid = %s",[pid])
		if(rc_payment==1):
			subject="Payment at Remote Center"
			from_email=settings.EMAIL_HOST_USER
			#to=[emailId]
			to=['goyalsakshi020@gmail.com']
			plaintext = get_template('ver_mail_selfSustained.txt')
			html = get_template('ver_mail_selfSustained.html')
			d = Context({ 'name':name , 'wsname':wsname })
			text_content = plaintext.render(d)
			html_content = html.render(d)
			msg = EmailMultiAlternatives(subject, text_content, from_email, to)
			msg.attach_alternative(html_content, "text/html")
			#msg.send()
		else:
			subject="Registration Confirmed"
			from_email=settings.EMAIL_HOST_USER
			#to=[emailId]
			to=['goyalsakshi020@gmail.com']
			plaintext = get_template('req_approved.txt')
			html = get_template('req_approved.html')
			d = Context({ 'name':name , 'wsname':wsname })
			text_content = plaintext.render(d)
			html_content = html.render(d)
			msg = EmailMultiAlternatives(subject, text_content, from_email, to)
			msg.attach_alternative(html_content, "text/html")
			#msg.send()
	if(btnid=='confirmedButton'):
		cursor.execute("UPDATE participant SET status = 'Confirmed' WHERE participantid = %s",[pid])
		if(rc_payment==1):
			subject="Registration Confirmed"
			from_email=settings.EMAIL_HOST_USER
			#to=[emailId]
			to=['goyalsakshi020@gmail.com']
			plaintext = get_template('req_approved.txt')
			html = get_template('req_approved.html')
			d = Context({ 'name':name , 'wsname':wsname })
			text_content = plaintext.render(d)
			html_content = html.render(d)
			msg = EmailMultiAlternatives(subject, text_content, from_email, to)
			msg.attach_alternative(html_content, "text/html")
			#msg.send()
	if(btnid=='invalidButton'):
		cursor.execute("UPDATE participant SET status = 'Registration Invalid' WHERE participantid = %s",[pid])
	if(btnid=='completedButton'):
		cursor.execute("UPDATE participant SET status = 'Completed' WHERE participantid = %s",[pid])
		'''f = open('logFile.txt','w')
		f.write('Participant id:'+ str(pid)+' Action Performed:'+ str(btnid)+' Workshop id:' +str(wsid)+' Time:' +str(datetime.datetime.now())+'\n')
		f.close()'''
	if(btnid=='cancelledButton'):
		cursor.execute("UPDATE participant SET status = 'Cancelled' WHERE participantid = %s",[pid])
	qsDict=serializers.serialize('json',q)
	data={"selected_qs":json.loads(qsDict)}
	return HttpResponse(json.dumps(data), content_type="application/json")

#to send mail if invalid button is clicked
def sendMail(request):
	reasons = request.GET.get('arr_reasons')
	r=reasons.split(',')
	pid=request.GET.get('pid')
	wsid=request.GET.get('wsid')
	#cursor = connection.cursor()
	#cursor.execute("UPDATE participant SET status = 'Registration Invalid' WHERE participantid = %s",[pid])
	wsname=Workshops.objects.get(workshopid=wsid).workshopname
	status=Participant.objects.get(participantid=pid).status
	contextId=Participant.objects.get(participantid=pid).contextid.idcontext
	emailId=Contxt.objects.get(idcontext=contextId).email
	personId=Participant.objects.get(participantid=pid).personid.personid
	name=Person.objects.get(personid=personId).firstname
	invalidReasons=Lookups.objects.filter(category='INVALID_RC',isactive=1)
	participantreason=Participantreasons()
	participantreason.workshopid=wsid
	participantreason.participantid=Participant.objects.get(participantid=pid)
	participantreason.status=status
	participantreason.reasons=reasons
	participantreason.last_update=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	participantreason.save()
	#code to send mail
	subject="Registration Invalid Reason"
	from_email=settings.EMAIL_HOST_USER
	#to=[emailId]
	to=['goyalsakshi020@gmail.com']
	plaintext = get_template('reg_invalid.txt')
	html = get_template('reg_invalid.html')
	d = Context({ 'name':name , 'message':r , 'wsname':wsname })
	text_content = plaintext.render(d)
	html_content = html.render(d)
	msg = EmailMultiAlternatives(subject, text_content, from_email, to)
	msg.attach_alternative(html_content, "text/html")
	#msg.send()
	qsDict=serializers.serialize('json',invalidReasons)
	data={"selected_qs":json.loads(qsDict)}
	return HttpResponse(json.dumps(data), content_type="application/json")

#to load the details of last remote center in the dropdown
def loadLastRC(request):
	wsid=int(request.GET["wsid"])
	facetofaceintr=Workshops.objects.get(workshopid=wsid).facetofaceintrif_available
	if(facetofaceintr==1):
		queryset=Remotecentercapacity.objects.filter(workshopid=wsid).order_by('rcid')
		qsDict=serializers.serialize('json',queryset)
		data={"selected_qs":json.loads(qsDict)}
		return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		queryset=Workshops.objects.filter(workshopid=wsid)
		qsDict=serializers.serialize('json',queryset)
		data={"selected_qs":json.loads(qsDict)}
		return HttpResponse(json.dumps(data), content_type="application/json")

#to send mail on cancel
def sendMailCancel(request):
	pid=request.GET.get('pid')
	wsid=request.GET.get('wsid')
	#cursor = connection.cursor()
	#cursor.execute("UPDATE participant SET status = 'Cancelled' WHERE participantid = %s",[pid])
	wsname=Workshops.objects.get(workshopid=wsid).workshopname
	contextId=Participant.objects.get(participantid=pid).contextid.idcontext
	emailId=Contxt.objects.get(idcontext=contextId).email
	personId=Participant.objects.get(participantid=pid).personid.personid
	name=Person.objects.get(personid=personId).firstname
	invalidReasons=Lookups.objects.filter(category='INVALID_RC',isactive=1)
	subject="Registration Cancelled"
	from_email=settings.EMAIL_HOST_USER
	#to=[emailId]
	to=['goyalsakshi020@gmail.com']
	plaintext = get_template('cancelled.txt')
	html = get_template('cancelled.html')
	d = Context({ 'name':name , 'wsname':wsname })
	text_content = plaintext.render(d)
	html_content = html.render(d)
	msg = EmailMultiAlternatives(subject, text_content, from_email, to)
	msg.attach_alternative(html_content, "text/html")
	#msg.send()
	qsDict=serializers.serialize('json',invalidReasons)
	data={"selected_qs":json.loads(qsDict)}
	return HttpResponse(json.dumps(data), content_type="application/json")

#to show id of participant
def showPhoto(request,pid):
	perid=Participant.objects.get(participantid=pid).personid.personid
	img=Person.objects.get(personid=perid).image
	try:
		########If the images are in static folder in statusManagement folder######
		'''dir = os.path.dirname(__file__)
		filename = os.path.join(dir, '/static/images/'+img)
		image_data=open(filename,"rb").read()'''
		########If the images are in static folder of TCube, then the absolute path should be given.#######
		image_data=open("/home/TCube/TCube/static/images/"+img, "rb").read()
		return HttpResponse(image_data, content_type="image/png")
	except IOError:
		return HttpResponse("ID not available in the specified location.")

#to show letter of participant
def showLetter(request,pid,wsid):
	img=Letter.objects.get(participantid=pid,workshopid=wsid).letter
	try:
		########If the images are in static folder in statusManagement folder######
		'''dir = os.path.dirname(__file__)
		filename = os.path.join(dir, '/static/images/'+img)
		image_data=open(filename,"rb").read()'''
		########If the images are in static folder of TCube, then the absolute path should be given.#######
		image_data = open("/home/TCube/TCube/static/images/"+img, "rb").read()
    		return HttpResponse(image_data, content_type="image/png")
	except IOError:
		return HttpResponse("Letter not available in the specified location.")

def storePrevUrl(request,url):
    request.session['prevUrl'] = url
