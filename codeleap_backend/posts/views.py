from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


class PostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all().order_by("-created_datetime")
    serializer_class = PostSerializer
