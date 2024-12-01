from rest_framework import generics

from comment.api.v1.serializers import CommentSerializer
from comment.models import Comment
from rest_framework.permissions import IsAuthenticated


class CommentList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter()
