from django.shortcuts import render
from .models import *
# Create your views here.
def teacher(request):
	if str(request.user)=="AnonymousUser":
		return render(request,"loginfail.html")
	days = ['monday', 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday', 'sunday']
	obj=[]
	cnt=0
	for d in days:
		for j in range(1,7):
			temp=Management.objects.get(userid=request.user,day=d,slotid=j)
			obj.insert(cnt,temp)
			cnt=cnt+1
	context = {
		"stu": obj,
		}

	return render(request,"teacher.html",context)

def submit_teacher(request):
	if str(request.user)=="AnonymousUser":
		return render(request,"loginfail.html")
	days = ['monday', 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday', 'sunday']
	cnt = ['mon1', 'mon2','mon3','mon4','mon5','mon6','tue1','tue2','tue3','tue4','tue5','tue6','wed1','wed2','wed3','wed4','wed5','wed6','thu1','thu2','thu3','thu4','thu5','thu6','fri1','fri2','fri3','fri4','fri5','fri6','sat1','sat2','sat3','sat4','sat5','sat6','sun1','sun2','sun3','sun4','sun5','sun6']
	obj=[]
	k=0
	for d in days:
		for j in range(1,7):
			student = Management.objects.get(userid=request.user,day=d,slotid=j)
			obj.insert(k,student)
			student.time =  request.POST.get(cnt[k])
			student.save()
			k=k+1;

	context = {
		"stu": obj,
		}

	return render(request,"teacher.html",context)

def clear(request):
	if str(request.user)=="AnonymousUser":
		return render(request,"loginfail.html")
	days = ['monday', 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday', 'sunday']
	cnt = ['mon1', 'mon2','mon3','mon4','mon5','mon6','tue1','tue2','tue3','tue4','tue5','tue6','wed1','wed2','wed3','wed4','wed5','wed6','thu1','thu2','thu3','thu4','thu5','thu6','fri1','fri2','fri3','fri4','fri5','fri6','sat1','sat2','sat3','sat4','sat5','sat6','sun1','sun2','sun3','sun4','sun5','sun6']
	obj=[]
	k=0
	for d in days:
		for j in range(1,7):
			student = Management.objects.get(userid=request.user,day=d,slotid=j)
			obj.insert(k,student)
			student.bookingstatus=0
			student.studentname=''
			student.studentemail=''
			student.save()
			k=k+1

	context = {
		"stu": obj,
		}

	return render(request,"teacher.html",context)
                	
    

