from django.shortcuts import render, redirect, get_object_or_404
from .models import IP, Owner
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
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

@login_required
def owner_detail(request, owner_id):
  owner = Owner.objects.get(pk=owner_id)
  template = loader.get_template('owner_detail.html')
  context = {
    'owners': owner,
  }
  return HttpResponse(template.render(context, request))

@login_required
def ip_edit(request, ip_str):
    ip = IP.objects.filter(ip=ip_str).first()
    owners = Owner.objects.all()
    message = None

    if request.method == 'POST':
        ip.service = request.POST.get('service')
        ip.product = request.POST.get('product')
        ip.os = request.POST.get('os')
        ip.unix_like = bool(request.POST.get('unix_like'))
        ip.owner_id = int(request.POST.get('owner_id'))
        ip.save()

        messages.success(request, '修改成功')

        # 重導向回 ip_edit
        return redirect('ip_edit', ip_str=ip.ip)

    template = loader.get_template('ip_edit.html')
    context = {
        'ip': ip,
        'owners': owners,

    }
    return HttpResponse(template.render(context, request))

@login_required
def owner_edit(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)

    if request.method == 'POST':
        owner.name = request.POST.get('name')
        owner.unit = request.POST.get('unit')
        owner.ext = request.POST.get('ext')
        owner.save()

        messages.success(request, '修改成功')

    template = loader.get_template('owner_edit.html')
    context = {
        'owner': owner,
    }
    return HttpResponse(template.render(context, request))
