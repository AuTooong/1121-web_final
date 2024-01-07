from django.shortcuts import render
from .models import IP, Owner
from django.template import loader
from django.http import HttpResponse

def overview(request):
  ip_query = request.GET.get('ip_query')
  if ip_query:
    results = IP.objects.filter(ip__icontains=ip_query)
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

def owner_detail(request, owner_id):
  owner = Owner.objects.get(pk=owner_id)
  template = loader.get_template('owner_detail.html')
  context = {
    'owners': owner,
  }
  return HttpResponse(template.render(context, request))
