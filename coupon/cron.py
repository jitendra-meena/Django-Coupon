

from django.http import HttpResponse
import datetime

import logging
logger = logging.getLogger(__name__)

def my_cron_job():
    
    logger.info("Coupon Active for Private Members ")
