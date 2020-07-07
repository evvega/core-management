# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .models import *
from .serializers import *
from .filters import *


class UserViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    ordering_fields = '__all__'

    @action(methods=['get'], detail=False)
    def current_user(self, request):
        """
        Returns current user authenticated
        """
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.data)


class FacultyViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    filter_class = FacultyFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    ordering_fields = '__all__'


class ProgramViewSet(viewsets.ModelViewSet):
    """

    """

    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    filter_class = ProgramFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    ordering_fields = '__all__'


class ScheduleModelViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = ScheduleModel.objects.all()
    serializer_class = ScheduleModelSerializer
    filter_class = ScheduleModelFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    ordering_fields = '__all__'


class PromotionModelViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = PromotionModel.objects.all()
    serializer_class = PromotionModelSerializer
    filter_class = PromotionModelFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    ordering_fields = '__all__'


class AccountModelViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = AccountModel.objects.all()
    serializer_class = AccountModelSerializer
    filter_class = AccountModelFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    ordering_fields = '__all__'


class ModuleConfigViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = ModuleConfig.objects.all()
    serializer_class = ModuleConfigSerializer
    filter_class = ModuleConfigFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    ordering_fields = '__all__'


class RolConfigViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = RolConfig.objects.all()
    serializer_class = RolConfigSerializer
    filter_class = RolConfigFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    ordering_fields = '__all__'


class RolUserViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = RolUser.objects.all()
    serializer_class = RolUserSerializer
    filter_class = RolUserFilter
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    ordering_fields = '__all__'