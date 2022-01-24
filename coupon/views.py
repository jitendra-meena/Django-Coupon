from django.http import HttpResponse
from django.shortcuts import render
import logging
logger = logging.getLogger(__name__)
from django.http import HttpResponse
from .tasks import create_task


def home(request):
    create_task.delay()
    return HttpResponse("Done")