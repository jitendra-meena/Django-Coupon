from coupon.models import Coupon
from rest_framework import status
from rest_framework.generics import ListAPIView,ListCreateAPIView, CreateAPIView
from .serializer import Coupon_ListSerializer, Coupon_UseSerializer 
from rest_framework.response import Response
from datetime import datetime
from datetime import timedelta
import datetime   

class Coupon_List(ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = Coupon_ListSerializer



class Coupon_Use(CreateAPIView):
    queryset =  Coupon.objects.all()
    serializer_class = Coupon_UseSerializer
    
    def post(self, request):
        coupon_code = request.data.get('code')
        print(coupon_code)
        if coupon_code:
            try:
                coupon =  Coupon.objects.get(code = coupon_code)
                current_date = datetime.datetime.now()
                expiry_date = coupon.valid_to
                if current_date.date() <= expiry_date.date():
                    print("This is valid date")
                    print(current_date.time(),expiry_date.time())
                    if current_date.time()<=expiry_date.time():
                        if coupon.can_use():
                            return Response({'discount':coupon.discount})

            except Coupon.DoesNotExist:
                return Response({'msg':'Coupon not valid'})
        else:
            print("Not ")
            return Response({'msg':'Coupon not valid'})

        return Response({'msg':'Appy Coupon Successfully'})       