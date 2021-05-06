from rest_framework import serializers

from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    profile_image=serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)
    class Meta:
        model=Author
        fields=['first_name', 'last_name', 'bio', 'profile_image', 'joined_on']