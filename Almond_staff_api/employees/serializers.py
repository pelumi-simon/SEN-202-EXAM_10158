from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street_address1', 'street_address2', 'street_address3', 'house_number','city','state','country','postal_code' ]
