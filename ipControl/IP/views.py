from django.shortcuts import render
from .models import IP
from django.template import loader
from django.http import HttpResponse

def overview(request):
  ip_query = request.GET.get('ip_query')
  if ip_query:
    results = IP.objects.filter(ip__icontains=ip_query)
  else:
    results = IP.objects.all()
  template = loader.get_template('overview.html')
  context = {
    'ip_query': ip_query,
    'results': results
  }
  return HttpResponse(template.render(context, request))
