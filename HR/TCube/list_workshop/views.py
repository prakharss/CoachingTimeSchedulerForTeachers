from django.shortcuts import render
from .models import *

# Create your views here.
def allworkshops(request,rcid=None):
	workshop=Workshops.objects.all()
	coordinatorw=[]
	mainw=[]
	selfsustainedw=[]
	for each in workshop:
		if(int(each.categorycode)==4 and int(each.workshopid)>=0):
			coordinatorw.append(each)
		elif(int(each.categorycode)==5 and int(each.workshopid)>=0):
			mainw.append(each)
		elif(int(each.categorycode)==6 and int(each.workshopid)>=0):
			selfsustainedw.append(each)	
	cws=len(coordinatorw)
	mws=len(mainw)
	ssws=len(selfsustainedw)
	tot=cws+mws+ssws
	context = {
			"coordinatorw": coordinatorw,
			"mainw": mainw,
			"selfsustainedw": selfsustainedw,
			"cws": cws,
			"mws": mws,
			"ssws": ssws,
			"tot":tot,
			}
	return render(request, "allworkshops.html" ,context)

def introworkshop(request,wsid=None):
	workshop=Workshops.objects.get(workshopid=wsid)
	workshopcoordinators=WorkshopCoordinator.objects.filter(workshopid=wsid)
	wscoordinators=[]
	for each in workshopcoordinators:
		each.rcname=Remotecenter.objects.get(remotecenterid=each.rcid).remotecentername
		wscoordinators.append(each)
	length=len(wscoordinators)
	context = {
			"wscoordinators": wscoordinators,
			"workshop": workshop,
			"length":length,
			}
	return render(request, "workshopintro.html" ,context)

def download(request,wsid=None):
	downld=Downloads.objects.filter(workshopid=wsid)
	workshop=Workshops.objects.get(workshopid=wsid)
	context = {
			"downld": downld,
			"workshop": workshop,
			}
	return render(request, "download.html" ,context)