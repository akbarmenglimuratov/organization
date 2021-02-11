from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import *

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'title': 'Успешная авторизация!',
            'code': 202,
            'message': 'Пользователь успешно авторизован!',
            'payload': {
                'auth_token': token.key,
            }
        })

    # def get_all_data(self,request):
    #     queryset = Organization.objects.all()
    #     pk = None
    #     if self.user.organization_user.organization_id is not None:
    #         pk = self.user.organization_user.organization_id.id
    #     organization = get_object_or_404(queryset, pk = pk)
    #     serializer = OrganizationSerializer(organization)
    #     return serializer.data



class ProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self,request):
        queryset = User.objects.get(username = request.user)
        serializer = UserProfileSerializer(queryset)
        return Response(serializer.data, status = 200)