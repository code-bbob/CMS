from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import Repair
from rest_framework.response import Response
from .serializers import AdminRepairSerializer,TechnicianRepairSerializer,StaffRepairSerializer
from .permissions import check_status
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.
class RepairView(APIView):
    permission_classes= [IsAuthenticated]
    def get(self,request):
        user = request.user
        enterprise = user.enterprise.first()
        print(enterprise)
        repairs = Repair.objects.filter(enterprise_repairs__name=enterprise)
        print(repairs)
        status = check_status(user)
        print(status)
        if status == "Admin":
            serializer = AdminRepairSerializer(repairs,many=True)
        elif status == "Technicians":
            serializer = TechnicianRepairSerializer(repairs,many=True)
        else:
            serializer = StaffRepairSerializer(repairs,many=True)
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        serializer = AdminRepairSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg":"Successful"})
        
    def patch(self,request):
        repair_id = request.data.get('repair_id',None)
        repair = Repair.objects.get(repair_id=repair_id)
        data=request.data
        if repair:
            serializer = AdminRepairSerializer(repair, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"No repair found"})