

from django.http import HttpResponse
import datetime

import logging
logger = logging.getLogger(__name__)
# When Coupon Active alert private members for coupon
def my_cron_job():
    
    logger.info("Coupon Active for Private Members ")
