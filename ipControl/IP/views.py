from django.shortcuts import render
from .models import IP
from django.template import loader
from django.http import HttpResponse

def overview(request):
  all_ip = IP.objects.all()
  template = loader.get_template('overview.html')
  context = {
    'all_ip': all_ip,
  }
  return HttpResponse(template.render(context, request))
