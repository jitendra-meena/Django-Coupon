FROM python:3.6-slim
RUN mkdir /Coupon Management System
WORKDIR /Coupon Management System/CouponSystem
ADD . /Coupon Management System/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0:8000
