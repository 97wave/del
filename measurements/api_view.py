  
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from measurements.serializers import ProjectModelSerializer
from measurements.models import Project


class ProjectApiView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
