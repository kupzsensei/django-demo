from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response

# Create your views here.
class StudentView(APIView):
    # model.object.query
    def get(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset , many=True)

        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class StudentRetrieveUpdateDelete(APIView):
    def get(self, request, pk):
        queryset = Student.objects.get(id=pk)
        serializer = StudentSerializer(queryset)

        return Response(serializer.data)
    
    def delete(self, request, pk):
        instance = Student.objects.get(id=pk)

        serializer = StudentSerializer(instance)

        instance.delete()
        return Response({f"Successfully deleted: {serializer.data}"})

    def patch(self, request, pk):
        
        instance = Student.objects.get(id=pk)

        serializer = StudentSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({f"Successfully updated: {serializer.data}"})
        
        return Response(serializer.errors)

