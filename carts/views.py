from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user, ordered=False).first()
        queryset = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        user = request.user
        cart,_ = Cart.objects.get_or_create(user=user, ordered=False)

        product = Product.objects.get(id=data.get('product'))
        price = product.price
        quantity = data.get('quantity')
        cart_item = CartItem(cart=cart, user=user, product=product, price=price, quantity=quantity)
        cart_item.save()

        total_price = 0
        cart_item = CartItem.objects.filter(user=user, cart=cart.id)
        for items in cart_item:
            total_price += items.price
        cart.total_price = total_price
        cart.save()

        serializer = CartItemSerializer(cart_item, many=True)
        return Response(serializer.data)
        # return Response({'success': 'Items Added to your cart'})

    def put(self, request):
        data = request.data
        user = request.user
        cart = Cart.objects.get(user=user, ordered=False)
        cart_item = CartItem.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()

        total_price = 0
        cart_item = CartItem.objects.filter(user=user, cart=cart.id)
        for items in cart_item:
            total_price += items.price
        cart.total_price = total_price
        cart.save()

        serializer = CartItemSerializer(cart_item, many=True)
        return Response(serializer.data)
        # return Response({'success': 'Items Updated'})


    def delete(self, request):
        user = request.user
        data = request.data

        cart_item = CartItem.objects.get(id=data.get('id'))
        cart_item.delete()

        cart = Cart.objects.filter(user=user, ordered=False).first()
        queryset = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        return Response(serializer.data)


class OrderAPI(APIView):

    def get(self, request):
        queryset = Orders.objects.filter(user=request.user)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)


