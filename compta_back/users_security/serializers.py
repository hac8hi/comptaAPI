from rest_framework import serializers
from users_security.models import User, UserPermissions

class UserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPermissions
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class RegisterSerializer(serializers.ModelSerializer):
    permissions = UserPermissionsSerializer(many=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'full_name', 'role', 'company_id', 'password']
    
    def create(self, validated_data):
        permissions_data = validated_data.pop('permissions')
        user = User.objects.create_user(**validated_data)
        for perm_data in permissions_data:
            UserPermissions.objects.create(user_id=user, **perm_data)
        return user
    
    def update(self, instance, validated_data):
        permissions_data = validated_data.pop('permissions', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if permissions_data:
            instance.permissions.all().delete()
            for perm_data in permissions_data:
                UserPermissions.objects.create(user_id=instance, **perm_data)
        return instance