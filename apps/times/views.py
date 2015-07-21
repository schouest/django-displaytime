from django.http import HttpResponse, Http404
from django.shortcuts import render
from time import localtime
def index(request):
	time = localtime()
	context = {'year':time.tm_year,
				'month':time.tm_mon,
				'day':time.tm_mday,
				'hour':time.tm_hour,
				'min':time.tm_min,
	}
	if context['hour'] >= 12:
		context['meridian'] = "PM"
		if context['hour'] != 12:
			context['hour'] -= 12
	else: 
		context['meridian'] = "AM"
		if context['hour'] == 0:
			context['hour'] = 12

	return render(request, 'times/index.html',context)
