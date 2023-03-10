from rest_framework import serializers
from blog.models import Post
#serializer file is used to convert into frontend(JSON/XML) and backend () readable form
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','author','excerpt','content','status')
