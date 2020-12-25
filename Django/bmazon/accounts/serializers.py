from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class RegistrationSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    password2 = serializers.CharField(
            style={'input_type': 'password'},
            write_only=True
        )

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'address', 'country', 'city',
                  'postal_code', 'account_type', 'user', 'password2')
        depth = 1

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            address=self.validated_data['address'],
            country=self.validated_data['country'],
            city=self.validated_data['city'],
            postal_code=self.validated_data['postal_code'],
            account_type=self.validated_data['account_type'],
        )
        password = self.validated_data['user']['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({
                'password': 'Passwords must match'
            })
        new_user = User.objects.create_user(
            username=self.validated_data['user']['username'],
            password=self.validated_data['user']['password'],
        )
        account.user = new_user
        account.save()      # calling the actual save method, not the one overriden
        return account


class UpdateProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'address', 'country', 'city',
                  'postal_code', 'account_type', 'user')
        depth = 1


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                "password": "Password fields didn't match"
            })
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({
                "old_password": "Old password is not correct"
            })
        return value

    def update(self, user, validated_data):
        user.set_password(validated_data['password'])
        user.save()
        return user
