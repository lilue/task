from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from .models import Student, Teacher
# Create your views here.


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    search_fields = []
    ordering_fields = ['id']
    ordering = ['id']


class TeacherSerializer(serializers.ModelSerializer):
    student_set = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    search_fields = []
    ordering_fields = ['id']
    ordering = ['id']



