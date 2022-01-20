from coupon.models import Coupon
from rest_framework import status
from rest_framework.generics import ListAPIView,ListCreateAPIView, CreateAPIView
from .serializer import Coupon_ListSerializer, Coupon_ApplySerializer,Add_CouponSerializer 
from rest_framework.response import Response
from datetime import datetime
from datetime import timedelta
import datetime   
from django.utils import timezone
from rest_framework.views import APIView


class Coupon_List(ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = Coupon_ListSerializer
    
    def get(self,request):
        coupon = Coupon.objects.all()
        serializer = Coupon_ListSerializer(coupon,many=True)
        return Response({'status':'200','msg':'Coupon Lists','data':serializer.data})

class Coupon_Apply(CreateAPIView):
    queryset =  Coupon.objects.all()
    serializer_class = Coupon_ApplySerializer
    
    def post(self, request):
        coupon_code = request.data.get('code')
        print(coupon_code)
        if coupon_code:
            try:
                now = timezone.now()
                coupon =  Coupon.objects.get(code__iexact = coupon_code,valid_from__lte =now,valid_to__gte=now,is_active = True)
                if coupon.can_use():
                    coupon.num_used += 1
                    coupon.save()
                    if coupon.num_used == coupon.num_available:
                        coupon.is_active = False
                        coupon.save()
                    return Response({'msg':'Appy Coupon Successfully','discount':coupon.discount})

            except Coupon.DoesNotExist:
                return Response({'msg':'Coupon not valid'})
        else:
            return Response({'msg':'coupon code Field is requreid'})

        return Response({'msg':'Coupon Expired'})       


class Add_Coupon(ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = Add_CouponSerializer
    def post(self, request):
        code = request.data.get('code')
        valid_from = request.data.get('valid_from')
        valid_to = request.data.get('valid_to')
        num_available = request.data.get('num_available')
        amount = request.data.get('amount')
        amount_type = request.data.get('amount_type')
        if(code== '' or code == None)  or (valid_from== '' or valid_from == None) or (amount== '' or amount == None)   or (valid_to== '' or valid_to == None) or (num_available== '' or num_available == None) or (amount_type== '' or amount_type == None): 
            return Response({'msg':'Please enter full detail'})
        if Coupon.objects.filter(code__iexact = code).exists():
            return Response({'msg':'coupon with this code already exists.'})
        if amount_type == '1':
            coupon_obj = Coupon.objects.create(code =code,valid_from =valid_from,valid_to=valid_to,num_available=num_available,amount=amount,is_active =True,amount_type ="Fixed Amount",coupon_type ="Public")
            coupon_obj.save()
        else:
            coupon_obj = Coupon.objects.create(code =code,valid_from =valid_from,valid_to=valid_to,num_available=num_available,amount=amount,is_active =True,amount_type ="Percentage",coupon_type ="Public")
            coupon_obj.save()    
        serializer = Add_CouponSerializer(coupon_obj)
        return Response({'msg':'coupon code Created','data':serializer.data}) 
    
      


