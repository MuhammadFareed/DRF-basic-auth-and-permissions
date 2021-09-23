from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from .custom_permissions import MyPermissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermissions]

    
# class StudentModelViewSet2(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [AllowAny]


# class StudentModelViewSet3(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAdminUser]



##########      For Function Based Views       ##############

# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# @authentication_classes([SessionAuthentication])
# @permission_classes([MyPermissions])
# def student_api(req, pk=None)
