#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from warehouse.models import Pipe

# Create your views here.

def start(request):
    pipes = Pipe.objects.all().order_by("GOST")
    return render(request, "warehouse_all.html", { "path": str(request.get_host()), "pipes": pipes})
