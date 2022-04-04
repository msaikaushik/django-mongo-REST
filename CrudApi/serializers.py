from rest_framework import serializers 
from CrudApi.models import User#, Interests, Recommendations
 
class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('id',
                  'name',
                  'data')