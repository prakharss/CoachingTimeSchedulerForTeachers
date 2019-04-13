from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.contrib import messages
from django.template import loader,Context
from .models import *
from models import Context as Contxt
from django.db import connection
import json,datetime
from django.core import serializers
from . import globals
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage,EmailMultiAlternatives,send_mail
import role_manage.models as role_manage_models

#to show the workshops in dropdown
def manage(request):
	page_id=52
	#role_id=5
	try:
		role_id=request.session['role_id']
	except Exception:
		role_id=0	
	if(role_manage_models.check_page_permission(role_id,page_id)):
		globals.init() 
		d = datetime.date.today() - datetime.timedelta(days=90)
		resultset=Workshops.objects.raw('select workshopid,workshopname from workshops where workshopid>0 and startdate>%s order by startdate',[d])
		context={
			"objects":resultset,
		}
		context.update(globals.myList)
		return render(request,"manageRC.html",context)
	else:
		storePrevUrl(request,HttpRequest.build_absolute_uri(request))
		return HttpResponseRedirect("/")

#to show the details of RCs for selected workshop
def manageRC(request,workshopId=None):
	page_id=53
	#role_id=5
	try:
		role_id=request.session['role_id']
	except Exception:
		role_id=0
	if(role_manage_models.check_page_permission(role_id,page_id)):
		globals.init()
		ws=Workshops.objects.get(workshopid=workshopId)
		d = datetime.date.today() - datetime.timedelta(days=90)
		resultset=Workshops.objects.raw('select workshopid,workshopname from workshops where workshopid>0 and startdate>%s order by startdate',[d])
		queryset = Remotecentercapacity.objects.raw('SELECT * FROM remotecentercapacity where workshopid=%s and is_active=1 order by rcid',[workshopId])
		queryset1=[]
		for each in queryset:
			#x=Remotecenter.objects.get(remotecenterid=each.rcid)
			x=Remotecenter.objects.raw('select * from remotecenter where remotecenterid=%s',[each.rcid])
			for y in x:
				each.rcname=y.remotecentername
				queryset1.append(each)
		context = {
			"object_list": queryset1,
			"objects":resultset,
			"wsid":workshopId,
			"wsname":ws.workshopname,
			"workshop":ws,
			}
		context.update(globals.myList)
		return render(request, "manageRCCapacity.html", context)
	else:
		storePrevUrl(request,HttpRequest.build_absolute_uri(request))
		return HttpResponseRedirect("/")

#to save the added RC in database
def addRC(request,workshopId):
	page_id=49
	#role_id=5
	try:
		role_id=request.session['role_id']
	except Exception:
		role_id=0
	if(role_manage_models.check_page_permission(role_id,page_id)):
		globals.init()
		remotecentercap = Remotecentercapacity()
		remotecentercap.rcid = request.POST.get('rcId')
		#remotecentercap.workshopid = request.POST.get('workshopId')
		remotecentercap.workshopid=workshopId
		remotecentercap.available_seats = request.POST.get('seats')
		remotecentercap.available_accomo = request.POST.get('acco')
		remotecentercap.allotedrc=0
		if(request.POST.get('accoCost')!=''):
			remotecentercap.acco_cost = request.POST.get('accoCost')
		else:
			remotecentercap.acco_cost ='None'
		if(request.POST.get('foodCost')!=''):
			remotecentercap.food_cost = request.POST.get('foodCost')
		else:
			remotecentercap.food_cost ='None'
		queryset = Remotecentercapacity.objects.raw('SELECT * FROM remotecentercapacity where workshopid=%s and rcid=%s',[workshopId,request.POST.get('rcId')])
		q=Remotecenter.objects.raw('select * from remotecenter where remotecenterid=%s',[request.POST.get('rcId')])
		if(len(list(queryset))==0):
			remotecentercap.save()
			cursor = connection.cursor()
			cursor.execute("UPDATE remotecentercapacity SET is_active = 1 WHERE rcid = %s ",[request.POST.get('rcId')])
			context={"wsid":workshopId,}
			context.update(globals.myList)
			return render(request, "message.html", context)
		else:
			context={"wsid":workshopId,}
			context.update(globals.myList)
			return render(request,"rcAlreadyPresent.html",context)
	else:
		return HttpResponseRedirect("/")

#to show the page for adding new RC details
def add(request,workshopId):
	page_id=48
	#role_id=5
	try:
		role_id=request.session['role_id']
	except Exception:
		role_id=0
	if(role_manage_models.check_page_permission(role_id,page_id)):
		globals.init()
		queryset = Workshops.objects.raw('SELECT * FROM workshops where workshopid=%s',[workshopId])
		context = {
			"workshopId":workshopId,
			"workshopname":queryset[0].workshopname,
			"startdate":queryset[0].startdate,
			"enddate":queryset[0].enddate,
			"cc":queryset[0].categorycode,
			}
		context.update(globals.myList)
		return render(request,"addNewRC.html",context)
	else:
		storePrevUrl(request,HttpRequest.build_absolute_uri(request))
		return HttpResponseRedirect("/")

#to view RC details
def viewRC(request,wsid,n):
	page_id=60
	#role_id=5
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
		return render(request, "viewRCCapacity.html", context)
	else:
		storePrevUrl(request,HttpRequest.build_absolute_uri(request))
		return HttpResponseRedirect("/")

#to show the page to update RC details
def updateRC(request,wsId,rcId,availableSeats,availableAccomo,accoCost,foodCost):
	page_id=57
	#role_id=5
	try:
		role_id=request.session['role_id']
	except Exception:
		role_id=0
	if(role_manage_models.check_page_permission(role_id,page_id)):
		globals.init()
		qs=Workshops.objects.raw('SELECT * FROM workshops where workshopid=%s',[wsId])
		context = {
			"wsid":wsId,
			"rcid": rcId,
			"available_seats" : availableSeats,
			"available_accomo" : availableAccomo,
			"accoCost":accoCost,
			"foodCost":foodCost,
			"workshopname":qs[0].workshopname,
			"startdate":qs[0].startdate,
			"enddate":qs[0].enddate,
			"workshop":qs[0],
		}
		context.update(globals.myList)
		return render(request,"updateRCCapacity.html",context)
	else:
		storePrevUrl(request,HttpRequest.build_absolute_uri(request))
		return HttpResponseRedirect("/")	

#to save the updated RC info in database
def updateRCSuccess(request,wsid,rcId):
	page_id=58
	#role_id=5
	try:
		role_id=request.session['role_id']
	except Exception:
		role_id=0
	if(role_manage_models.check_page_permission(role_id,page_id)):
		globals.init()
		#remotecentercap = Remotecentercapacity()
		#remotecentercap.workshopid=wsid
		#remotecentercap.rcid=rcId
		available_seats = request.POST.get('seats')
		available_accomo = request.POST.get('accomo')
		acco_cost = request.POST.get('accoCost')
		food_cost = request.POST.get('foodCost')
		cursor = connection.cursor()
		cursor.execute("UPDATE remotecentercapacity SET available_seats = %s WHERE rcid = %s and workshopid=%s",[available_seats,rcId,wsid])
		cursor.execute("UPDATE remotecentercapacity SET available_accomo = %s WHERE rcid = %s and workshopid=%s",[available_accomo,rcId,wsid])
		cursor.execute("UPDATE remotecentercapacity SET acco_cost = %s WHERE rcid = %s and workshopid=%s", [acco_cost,rcId,wsid])
		cursor.execute("UPDATE remotecentercapacity SET food_cost = %s WHERE rcid = %s and workshopid=%s", [food_cost,rcId,wsid])
		context={"wsid":wsid,}
		context.update(globals.myList)
		return render(request,"updateMessage.html",context)
	else:
		return HttpResponseRedirect("/")	

#main page of RCC
def rCCInterface(request):
	page_id=55
	#role_id=1
	try:
		role_id=request.session['role_id']
	except Exception:
		role_id=0
	if(role_manage_models.check_page_permission(role_id,page_id)):
		globals.init()
		remcenter=Remotecenter.objects.filter(email=request.session["email"])
		qs=Workshops.objects.raw("select * from workshops where startdate > curdate() order by startdate")
		qs1=[]
		d = datetime.date.today() - datetime.timedelta(days=90)
		i=0
		for each in qs:
			x=Remotecentercapacity.objects.filter(workshopid=each.workshopid,rcid=remcenter[0].remotecenterid)
			if(len(list(x))!=0):
				each.is_declined=x[0].is_declined
				qs1.append(each)
			else:
				each.is_declined=0
				qs1.append(each)
		q=Workshops.objects.filter(startdate__gt=d,categorycode=7).order_by('startdate')
		context={
			"date":datetime.date.today(),
			"objects":qs1,
			"rcid":remcenter[0].remotecenterid,
			"objectSet":q,
		}
		context.update(globals.myList)
		return render(request,"RCCInterface.html",context)
	else:
		storePrevUrl(request,HttpRequest.build_absolute_uri(request))
		return HttpResponseRedirect("/")
	
#to show the page for filling RC capacity
def rCCapacityDetails(request,workshopid,rcid):
	page_id=51
	#role_id=1
	try:
		role_id=request.session['role_id']
	except Exception:
		role_id=0
	if(role_manage_models.check_page_permission(role_id,page_id)):
		globals.init()
		qs=Remotecentercapacity.objects.filter(workshopid=workshopid,rcid=rcid)
		if(len(list(qs))!=0):
			qs1=WorkshopCoordinator.objects.filter(workshopid=workshopid,rcid=rcid)
			context={
				"fcc":qs1[0].email,
				"objects": qs[0],
				"workshopid":workshopid,
				"rcid":rcid,
			}
			context.update(globals.myList)
			return render(request,"RCCapacityDetails.html",context)
		else:
			context={
				"objects":0,
				"workshopid":workshopid,
				"rcid":rcid,
			}
			context.update(globals.myList)
			return render(request,"RCCapacityDetails.html",context)
	else:
		storePrevUrl(request,HttpRequest.build_absolute_uri(request))
		return HttpResponseRedirect("/")

#to display message of RC added successfully
def message(request):
	page_id=47
	#role_id=5
	try:
		role_id=request.session['role_id']
	except Exception:
		role_id=0
	if(role_manage_models.check_page_permission(role_id,page_id)):
		globals.init()
		context={}
		context.update(globals.myList)
		return render(request,"message.html",{})
	else:
		storePrevUrl(request,HttpRequest.build_absolute_uri(request))
		return HttpResponseRedirect("/")

#to display message of RC updated successfully
def updateMessage(request):
	page_id=56
	#role_id=5
	try:
		role_id=request.session['role_id']
	except Exception:
		role_id=0
	if(role_manage_models.check_page_permission(role_id,page_id)):
		globals.init()
		context={}
		context.update(globals.myList)
		return render(request,"updateMessage.html",context)
	else:
		storePrevUrl(request,HttpRequest.build_absolute_uri(request))
		return HttpResponseRedirect("/")

#to check whether the RC can be deleted and if yes save in database
def deleteRC(request,wsid,rcid):
	page_id=50
	#role_id=5
	try:
		role_id=request.session['role_id']
	except Exception:
		role_id=0
	if(role_manage_models.check_page_permission(role_id,page_id)):
		globals.init()
		q=Accomodation.objects.raw('select * from accomodation where instituteid=%s and workshopid=%s',[rcid,wsid])
		for each in q:
			if (each.participantid.status!='Cancelled'):
				context={"wsid":wsid,}
				context.update(globals.myList)
				return render(request,'deleteError.html',context)
		cursor = connection.cursor()
	    	cursor.execute("UPDATE remotecentercapacity SET is_active = 0 WHERE rcid = %s", [rcid])
		resultset=Workshops.objects.raw('select workshopid,workshopname from workshops limit 15')
		context={
			"objects":resultset,
			"wsid":wsid,
		}
		context.update(globals.myList)
		return render(request,"deleteMessage.html",context)
	else:
	 	storePrevUrl(request,HttpRequest.build_absolute_uri(request))
		return HttpResponseRedirect("/")
	
#to save the capacity filled by RC in database
def capacityFilled(request):
	globals.init()
	remotecentercap = Remotecentercapacity()
	wsc=WorkshopCoordinator()
	remotecentercap.rcid = int(request.GET["rcid"])
	remotecentercap.workshopid=int(request.GET["wsid"])
	remotecentercap.available_seats = int(request.GET["seats"])
	remotecentercap.available_accomo = int(request.GET["acco"])
	remotecentercap.allotedrc=0
	remotecentercap.acco_cost = int(request.GET["accoCost"])
	remotecentercap.food_cost = int(request.GET["foodCost"])
	fcc=request.GET["fcc"]
	cntxt=Contxt.objects.get(email=fcc).idcontext
	wsc.workshopid=int(request.GET["wsid"])
	wsc.rcid=int(request.GET["rcid"])
	wsc.contextid=int(cntxt)
	wsc.email=fcc
	qs1=Remotecentercapacity.objects.filter(workshopid=int(request.GET["wsid"]),rcid=int(request.GET["rcid"]))
	qs=WorkshopCoordinator.objects.filter(workshopid=int(request.GET["wsid"]),rcid=int(request.GET["rcid"]))	
	wsc.save()
	if(len(list(qs1))!=0):
		cursor = connection.cursor()
		cursor.execute("UPDATE remotecentercapacity SET available_seats = %s WHERE rcid = %s and workshopid=%s",[int(request.GET["seats"]),int(request.GET["rcid"]),int(request.GET["wsid"])])
		cursor.execute("UPDATE remotecentercapacity SET available_accomo = %s WHERE rcid = %s and workshopid=%s",[int(request.GET["acco"]),int(request.GET["rcid"]),int(request.GET["wsid"])])
		cursor.execute("UPDATE remotecentercapacity SET acco_cost = %s WHERE rcid = %s and workshopid=%s",[int(request.GET["accoCost"]),int(request.GET["rcid"]),int(request.GET["wsid"])])
		cursor.execute("UPDATE remotecentercapacity SET food_cost = %s WHERE rcid = %s and workshopid=%s",[int(request.GET["foodCost"]),int(request.GET["rcid"]),int(request.GET["wsid"])])
	else:
		remotecentercap.save()
	qs=Login.objects.filter(login_name=fcc)
	qsDict=serializers.serialize('json',qs)
	data={"selected_qs":json.loads(qsDict)}
	return HttpResponse(json.dumps(data), content_type="application/json")

#to check whether the fcc email exists and if yes saving the info in database
def fillSeats(request):
	globals.init()
	wsid=int(request.GET["wsid"])
	rcid=int(request.GET["rcid"])
	acco=int(request.GET["acco"])
	seats=int(request.GET["seats"])
	accoCost=int(request.GET["accoCost"])
	foodCost=int(request.GET["foodCost"])
	fcc=request.GET["fcc"]
	qs=Login.objects.filter(login_name=fcc)
	qs1=WorkshopCoordinator.objects.filter(workshopid=int(request.GET["wsid"]),email=fcc)
	qsDict=serializers.serialize('json',qs)
	qsDict1=serializers.serialize('json',qs1)
	data={"selected_qs":json.loads(qsDict),"selected_qs1":json.loads(qsDict1)}
	return HttpResponse(json.dumps(data), content_type="application/json")

#to check whether the RC can be declined
def declineRC(request):
	wsid=int(request.GET["wsid"])
	#rcid=int(request.GET["rcid"])
	#qs=Remotecentercapacity.objects.filter(workshopid=wsid,rcid=rcid)
	qs=Accomodation.objects.filter(workshopid=wsid)
	qs1=[i for i in qs if i.participantid.status!='Cancelled']
	qsDict=serializers.serialize('json',qs1)
	ws=Workshops.objects.filter(workshopid=wsid)
	wsDict=serializers.serialize('json',ws)
	data={"selected_ws":json.loads(wsDict),"selected_qs":json.loads(qsDict)}
	return HttpResponse(json.dumps(data), content_type="application/json")

#to save the declined RC
def saveDeclinedRC(request):
	wsid=int(request.GET["wsid"])
	rcid=int(request.GET["rcid"])
	cursor = connection.cursor()
	cursor.execute("UPDATE remotecentercapacity SET is_declined=1 WHERE rcid = %s and workshopid=%s", [rcid,wsid])
	qs=Workshops.objects.filter(workshopid=wsid)
	qsDict=serializers.serialize('json',qs)
	data={"selected":json.loads(qsDict)}
	return HttpResponse(json.dumps(data), content_type="application/json")
	
#to send mail if a participant is rejected
def sendMail(request):
	reason = request.GET.get('reason')
	pid=request.GET.get('pid')
	wsid=request.GET.get('wsid')
	#cursor = connection.cursor()
	#cursor.execute("UPDATE participant SET status = 'Registration Invalid' WHERE participantid = %s",[pid])
	wsname=Workshops.objects.get(workshopid=wsid).workshopname
	contextId=Participant.objects.get(participantid=pid).contextid.idcontext
	emailId=Contxt.objects.get(idcontext=contextId).email
	personId=Participant.objects.get(participantid=pid).personid.personid
	name=Person.objects.get(personid=personId).firstname
	invalidReasons=Lookups.objects.filter(category='INVALID_RC',isactive=1)
	#code to send mail
	subject="Registration Rejection Reason"
	from_email=settings.EMAIL_HOST_USER
	#to=[emailId]
	to=['goyalsakshi020@gmail.com']
	plaintext = get_template('reject.txt')
	html = get_template('reject.html')
	d = Context({ 'name':name , 'message':reason , 'wsname':wsname })
	text_content = plaintext.render(d)
	html_content = html.render(d)
	msg = EmailMultiAlternatives(subject, text_content, from_email, to)
	msg.attach_alternative(html_content, "text/html")
	#msg.send()
	qsDict=serializers.serialize('json',invalidReasons)
	data={"selected_qs":json.loads(qsDict)}
	return HttpResponse(json.dumps(data), content_type="application/json")

#to show the page with list of participants in the RC
def manageparticipants(request,rcid,wsid):
	page_id=54
	#role_id=1
	try:
		role_id=request.session['role_id']
	except Exception:
		role_id=0
	if(role_manage_models.check_page_permission(role_id,page_id)):
		globals.init()
		qacco=Accomodation.objects.filter(workshopid=wsid,instituteid=rcid)
		wshop=Workshops.objects.get(workshopid=wsid)
		invalidReasons=Lookups.objects.filter(category='INVALID_RC',isactive=1)
		qmain=[]
		for each in qacco:
			if(each.participantid.status == 'Request Approved'):
				each.firstname = each.participantid.personid.firstname
				each.lastname = each.participantid.personid.lastname
				each.email = each.participantid.contextid.email
				qmain.append(each)
		context = {
			"object_list": qmain,
			"wshop": wshop,
			"listReasons":invalidReasons,
			}
		context.update(globals.myList)
		return render(request,"manageParticipants.html",context)
	else:
		storePrevUrl(request,HttpRequest.build_absolute_uri(request))
		return HttpResponseRedirect("/")

#to change the status of participant
def changeStatus(request):
	pid=int(request.GET["pid"])
	btnid=request.GET["btnid"]
	q=Participant.objects.filter(participantid=pid)
	cursor = connection.cursor()
	if(btnid=='acceptButton'):
		cursor.execute("UPDATE participant SET status = 'Accepted' WHERE participantid = %s",[pid])
	if(btnid=='rejectButton'):
		cursor.execute("UPDATE participant SET status = 'Registration Invalid' WHERE participantid = %s",[pid])
	qsDict=serializers.serialize('json',q)
	data={"selected_qs":json.loads(qsDict)}
	return HttpResponse(json.dumps(data), content_type="application/json")
	 
#to view the details of participants in that particular RC
def viewRCParticipants(request,wsid,n,rcid):
	page_id=61
	#role_id=1
	try:
		role_id=request.session['role_id']
	except Exception:
		role_id=0
	if(role_manage_models.check_page_permission(role_id,page_id)):
		globals.init()
		state=State.objects.all()
		wshop=Workshops.objects.get(workshopid=wsid)
		rcname=Remotecenter.objects.get(remotecenterid=rcid).remotecentername
		rr=0
		ri=0
		ra=0
		con=0
		com=0
		can=0
		acc=0
		accoQuerySet=Accomodation.objects.filter(workshopid=wsid,instituteid=rcid)
		al=len(accoQuerySet)
		queryset=[]
		for each in accoQuerySet:
			sta=each.participantid.status
			if(sta=='Request Registered'):
				rr+=1
			elif(sta=='Registration Invalid'):
				ri+=1
			elif(sta=='Request Approved'):
				ra+=1
			elif(sta=='Confirmed'):
				con+=1
			elif(sta=='Completed'):
				com+=1
			elif(sta=='Cancelled'):
				can+=1
			elif(sta=='Accepted'):
				acc+=1
			elif(sta=='Completed'):
				com+=1
		qs=[]
		if(int(n)==0):
			for each in accoQuerySet:
					qs.append(each)
		elif(int(n)==1):
			for each in accoQuerySet:
				if(each.participantid.status=='Request Registered'):
					qs.append(each)
		elif(int(n)==2):
			for each in accoQuerySet:
				if(each.participantid.status=='Registration Invalid'):
					qs.append(each)
		elif(int(n)==3):
			for each in accoQuerySet:
				if(each.participantid.status=='Request Approved'):
					qs.append(each)
		elif(int(n)==4):
			for each in accoQuerySet:
				if(each.participantid.status=='Confirmed'):
					qs.append(each)
		elif(int(n)==5):
			for each in accoQuerySet:
				if(each.participantid.status=='Completed'):
					qs.append(each)
		elif(int(n)==6):
			for each in accoQuerySet:
				if(each.participantid.status=='Cancelled'):
					qs.append(each)
		elif(int(n)==7):
			for each in accoQuerySet:
				if(each.participantid.status=='Accepted'):
					qs.append(each)
		for each in qs:
			each.firstname=each.participantid.personid.firstname
			each.lastname=each.participantid.personid.lastname
			each.gender=each.participantid.personid.genderinfo
			each.desig=each.designation=(Lookups.objects.get(category='designation',code=each.participantid.personid.designation)).description
			each.instituteid=Institute.objects.get(idinstitute=each.participantid.personid.instituteid).institutename
			each.mobNo=each.participantid.contextid.mobile
			each.email=each.participantid.contextid.email
			each.state=State.objects.get(stateid=each.participantid.contextid.state).state
			each.status=each.participantid.status
			queryset.append(each)
		context={"wshop":wshop,
			 "queryset":queryset,
			 "rcid":rcid,
			 "rcname":rcname,
			 "rr": rr,
			 "ri": ri,
			 "ra": ra,
			 "con": con,
			 "com": com,
			 "can": can,
			 "all":al,
			}
		context.update(globals.myList)
		return render(request,"viewRCParticipants.html",context)
	else:
		storePrevUrl(request,HttpRequest.build_absolute_uri(request))
		return HttpResponseRedirect("/")

#to view the program schedule of the workshop
def viewProgramSchedule(request,wsid):
	page_id=59
	#role_id=1
	try:
		role_id=request.session['role_id']
	except Exception:
		role_id=0
	if(role_manage_models.check_page_permission(role_id,page_id)):
		globals.init()
		wshop=Workshops.objects.get(workshopid=wsid)
		queryset=ProgramSchedule.objects.filter(workshopid=wsid)
		context={"queryset":queryset,
			 "wshop":wshop,                
			}
		context.update(globals.myList)
		return render(request,"viewProgramSchedule.html",context)
	else:
		storePrevUrl(request,HttpRequest.build_absolute_uri(request))
		return HttpResponseRedirect("/")
			
#index page
def RCCapacity(request):
	return render(request,"indexPage.html",{})

#to send mail to RC coordinators for filling capacity
def sendMail_RCCapacity(request):
	wsid=request.GET.get('wsid')
	wsname=Workshops.objects.get(workshopid=wsid).workshopname
	invalidReasons=Lookups.objects.filter(category='INVALID_RC',isactive=1)
	emails=[]
	qs=Remotecentercapacity.objects.filter(workshopid=wsid)
	q=Remotecenter.objects.filter(active=1)
	for each in q:
		for x in qs:
			if(each.remotecenterid!=x.rcid): 
				emails.append(each.email)
	subject="Reminder for filling remote center capacity"
	from_email=settings.EMAIL_HOST_USER
	#to=emails
	to=['goyalsakshi020@gmail.com']
	plaintext = get_template('RCCapacity.txt')
	html = get_template('RCCapacity.html')
	d = Context({ 'wsname':wsname })
	text_content = plaintext.render(d)
	html_content = html.render(d)
	msg = EmailMultiAlternatives(subject, text_content, from_email, to)
	msg.attach_alternative(html_content, "text/html")
	#msg.send()
	qsDict=serializers.serialize('json',invalidReasons)
	data={"selected_qs":json.loads(qsDict)}
	return HttpResponse(json.dumps(data), content_type="application/json")

def storePrevUrl(request,url):
    request.session['prevUrl'] = url
