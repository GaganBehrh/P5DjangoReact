from rest_framework import generics
from blog.models import Post

class PostSerializer(serializer.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','author','excerpt','content','status')
