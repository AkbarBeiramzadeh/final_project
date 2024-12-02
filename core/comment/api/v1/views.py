from rest_framework import generics
from rest_framework import viewsets
from comment.api.v1.serializers import CommentSerializer
from comment.models import Comment
from rest_framework.permissions import IsAuthenticated


class CommentList(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

