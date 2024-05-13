from rest_framework import serializers
from .models import Repair,Enterprise

class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = '__all__'


class AdminRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair
        fields = '__all__'

class TechnicianRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair
        fields = ['repair_id','customer_name','technician_profit']

class StaffRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repair
        fields = ['repair_id','customer_name']

