from django.shortcuts import render
from .models import IP, Owner
from django.template import loader
from django.http import HttpResponse
from django.db.models import Q

def overview(request):
  ip_query = request.GET.get('ip_query')

  current_filter = request.GET.get('current_filter')
  if ip_query:
    results = IP.objects.filter(ip__icontains=ip_query)
    # if current_filter == "iot":
    #   results = results.filter(service="NAS")
    # if current_filter == "nas":
    #   results = results.filter(Q(service="印表機") | Q(name="攝影機"))
  else:
    results = IP.objects.all()
  owner = Owner.objects.all()
  template = loader.get_template('overview.html')
  context = {
    'ip_query': ip_query,
    'owners': owner,
    'results': results
  }
  return HttpResponse(template.render(context, request))
