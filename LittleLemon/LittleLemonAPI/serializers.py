from rest_framework import serializers
from .models import Category, MenuItem, Cart, Order, OrderItem 
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator


class Userserializer(serializers.ModelSerializer): 
    class Meta: 
        model = User
        fields = ['id', 'username', 'email']


class Categoryserializer(serializers.ModelSerializer): 
    class Meta: 
        model = Category
        fields = ['id', 'slug', 'title']


class Menuitemserializers(serializers.ModelSerializer): 
    category = Categoryserializer(read_only = True)
    class Meta: 
        model = MenuItem
        fields = ['id', 'title', 'price', 'features', 'category']



class Cartserializer(serializers.ModelSerializer): 
    user = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(), 
        default = serializers.CurrentUserDefault()
    )

    def validate(self, attrs): 
        a  = attrs['quantity'] * attrs['unit_price']
        attrs['price'] = a
        return (attrs['price'])
    
    class Meta: 
        model = Cart
        fields = ['user', 'menuitem', 'quantity', 'unit_price', 'price']

        extra_kwargs = {
            'price' : {'read_only': True}
        } 

        validators = [
            UniqueTogetherValidator(
                queryset= Cart.objects.all(),
                fields=['user', 'menuitem']
            )
        ]

class Orderserializer(serializers.ModelSerializer): 
    user = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(), 
        default = serializers.CurrentUserDefault()
    )
    class Meta: 
        model = Order 
        fields = ['id', 'user', 'delivery_crew',  'status', 'total', 'date']

class Orderitemserializer(serializers.ModelSerializer): 
    order = Orderserializer(read_only = True, many= True)
    menuitem = Menuitemserializers(read_only = True, many= True)
    class Meta: 
        model = Orderserializer
        fields = ['order', 'menuitem', 'quantity', 'price']

        validators = [
            UniqueTogetherValidator(
                queryset= OrderItem.objects.all(),
                fields=['order', 'menuitem']
            )
        ]
