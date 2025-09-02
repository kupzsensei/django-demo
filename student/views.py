from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response

# Create your views here.
class StudentView(APIView):
    # model.object.query
    def get(self, request):
        # List of Student model
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset , many=True)

        return Response(serializer.data)

    def post(self, request):
        # def sanitizer(value):
        #     while "  " in value:
        #         value = value.replace("  ", " ")

        data = request.data

        data['first_name'] = data['first_name'].title()
        data['last_name'] = data['last_name'].title()
        data['middle_name'] = data['middle_name'].title()
        
        # data['first_name'] = sanitizer(data['first_name'])
        # data['last_name'] = sanitizer(data['last_name'])
        # data['middle_name'] = sanitizer(data['middle_name'])

        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

class StudentRetrieveUpdateDelete(APIView):
    def get(self, request, pk): # pk = Primary Key
        # Retrieve
        queryset = Student.objects.get(id=pk)
        # get student where id = 5
        serializer = StudentSerializer(queryset)

        return Response(serializer.data)
    
    def patch(self, request, pk):
        
        instance = Student.objects.get(id=pk)

        serializer = StudentSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({f"Successfully updated: {serializer.data}"})
        
        return Response(serializer.errors)

    def delete(self, request, pk):
        instance = Student.objects.get(id=pk)

        serializer = StudentSerializer(instance)

        instance.delete()
        return Response({f"Successfully deleted: {serializer.data}"})