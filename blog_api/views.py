from rest_framework import generics
from blog.models import Post
from .serializer import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class=PostSerializer
class PostDetail(generics.RetrieveDestroyAPIView):
    pass
