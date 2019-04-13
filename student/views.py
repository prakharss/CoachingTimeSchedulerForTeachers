from student.forms import *
from django.shortcuts import render
from teacher.models import *
from django.contrib.auth.models import User
# Create your views here.
def student(request,str=None):
	days = ['monday', 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday', 'sunday']
	obj=[]
	cnt=0
	for d in days:
		for j in range(1,7):
			temp=Management.objects.get(userid=str,day=d,slotid=j)
			obj.insert(cnt,temp)
			cnt=cnt+1

	user = User.objects.get(username=str)
	form = StudentDetails()
	context = {
		"stu": obj,
		"username": str,
		"email": user.email,
		"form": form,
		}

	return render(request,"student.html",context)

def submit_student(request,str=None):
	days = ['monday', 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday', 'sunday']
	cnt = ['mon1', 'mon2','mon3','mon4','mon5','mon6','tue1','tue2','tue3','tue4','tue5','tue6','wed1','wed2','wed3','wed4','wed5','wed6','thu1','thu2','thu3','thu4','thu5','thu6','fri1','fri2','fri3','fri4','fri5','fri6','sat1','sat2','sat3','sat4','sat5','sat6','sun1','sun2','sun3','sun4','sun5','sun6']
	obj_ignore=[]
	obj_accept=[]
	i=j=k=chk=0
	for d in days:
		for j in range(1,7):
			student = Management.objects.get(userid=str,day=d,slotid=j)

			if request.POST.get(cnt[k])!=None and int(request.POST.get(cnt[k])) == int(j) and student.bookingstatus ==1:
				obj_ignore.insert(i,student)
				i=i+1
				chk=1

			if request.POST.get(cnt[k])!=None and int(request.POST.get(cnt[k])) == int(j) and student.bookingstatus ==0:
				obj_accept.insert(j,student)
				j=j+1
				student.bookingstatus =  1
				student.studentname = request.POST.get('name')
				student.studentemail = request.POST.get('email')
				student.save()

			k=k+1;
			
	
	context = {
		"username": str,
		"obj_ignore": obj_ignore,
		"obj_accept": obj_accept,
		"chk": chk,
		}
	
	return render(request,"submit_student.html",context)