from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.generics import UpdateAPIView, RetrieveUpdateDestroyAPIView

from accounts.serializers import RegistrationSerializer, UpdateProfileSerializer
from accounts.models import Account


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered a new user"
            data['email'] = account.email
            data['username'] = account.user.username
        else:
            data = serializer.errors
        return Response(data)


class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class AccountRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Account.objects.all()
    lookup_field = 'account_id'
    serializer_class = UpdateProfileSerializer

    def delete(self, request, *args, **kwargs):
        account_id = request.data.get('account_id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('account_data_{}'.format(account_id))
        return response

    def update(self, request, *args, **kwargs):
        account_id = self.kwargs['account_id']
        account = Account.objects.get(pk=account_id)
        serializer = UpdateProfileSerializer(
            account,
            data=request.data,
            partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)