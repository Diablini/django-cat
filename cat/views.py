#encoding:utf-8

from django.template.loader import get_template
from django.template import Template, Context, RequestContext
from django.shortcuts import *
from django.http import HttpResponse

# views

def homepage(request):
	t = get_template('homepage.html')
	c = RequestContext(request,{
		'page_title':'Cats.bg',
		})
	html = t.render(c)
	return HttpResponse(html)


	

	
	
	

	
	
	
		
		
