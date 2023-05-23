from django.shortcuts import render
from .models import *
from .forms import OrderCreateForm
from cart.cart import Cart
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
import razorpay
import random
from django.http import HttpResponse


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
     

        form = OrderCreateForm(request.POST,initial={'userid': request.user.id}, user=request.user)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            #cart.clear()
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm(initial={'userid': request.user.id}, user=request.user)
    return render(request, 'orders/order/create.html', {'form': form})


def order_payment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        orderid=request.POST.get("provider_order_id")
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.create(
            {"amount": float(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        order = Ordernow.objects.create(
            name=name, amount=amount, provider_order_id=razorpay_order['id']
        )
        order.save()
        o1=Order.objects.get(id=orderid)
        o1.paid=True
        o1.save()
        return render(
            request,
            "orders/order/payment.html",
            {
                "callback_url": "http://127.0.0.1:8000/orders/callback/",
                "razorpay_key": settings.RAZORPAY_KEY_ID,
                "order": order,
            },
        )
    return render(request, "orders/order/payment.html")


@csrf_exempt
def callback(request):
    cart = Cart(request)
    razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
    #    return client.utility.verify_payment_signature(response_data)

    if request.method == "POST":
        try:
            payment_id = request.POST.get("razorpay_payment_id", "")
            provider_order_id = request.POST.get("razorpay_order_id", "")
            signature_id = request.POST.get("razorpay_signature", "")
            params_dict={
                'razorpay_order_id':provider_order_id,
                'razorpay_payment_id':payment_id,
                'razorpay_signature':signature_id

            }
            print(params_dict)
            try:
                order = Ordernow.objects.get(provider_order_id=provider_order_id)
            except:
                return HttpResponse("505 not found inner")
            order.payment_id = payment_id
            order.signature_id = signature_id
            order.save()
            cart.clear()
            result=razorpay_client.utility.verify_payment_signature(params_dict)
            
            if result==True:
                amount=int(order.amount)
                
                try:
                   
                    '''res=razorpay_client.payment.capture(payment_id,{
                        "amount" : amount,
                        "currency" : "INR"
                        })
                    print(res)'''
                    order.status=PaymentStatus.SUCCESS
                    order.save()
                    return render(request, "orders/order/sucess.html")
                except:
                   
                    order.status=PaymentStatus.FAILURE
                    order.save()
                    return render(request, "orders/order/failure.html")
            else:
                
                order.status=PaymentStatus.FAILURE
                order.save()
                return render(request, "orders/order/failure.html")
        except:
            return HttpResponse("505 not found here")
        