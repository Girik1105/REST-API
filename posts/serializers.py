from rest_framework import serializers

from . import models 


from users.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    
    
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = models.Post
        fields = ("user", "content", "image", "timestamp", "id")
    
        # read_only_fields = ['user']

    def validate_content(self, value):
        if len(value) > 240:
            raise serializers.ValidationError("This is way to long")
        return value
    
    def validate(self, data):
        content = data.get("content", None)
        image = data.get("image", None)

        if content == "" and image == None:
            raise serializers.ValidationError("Image or content is required")
        
        return data 