from django.http import HttpRequest
from django.http import HttpResponse
from requests import request
#import urllib2
import pdb
def students_proc(request):
		PORTAL_URL = "http://"+request.META['HTTP_HOST']+'/'#+request.META['PWD']+'/'
		#import pdb; pdb.set_trace()
		return {'PORTAL_URL':PORTAL_URL}