from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from .models import StatusTweet, Tweet, Comment
from .serializers import StatusTweetSerializer, TweetSerializer, CommentSerializer, StatusCommentSerializer
from .permissions import IsTweetOwner, IsAuthorPermission


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorPermission]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    @action(methods=['POST'], detail=True)
    def leave_status(self, request, pk=None):
        serializer = StatusTweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                tweet=self.get_object(),
                profile=request.user.profile
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorPermission]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    @action(methods=['POST'], detail=True)
    def leave_status(self, request, pk=None):
        serializer = StatusCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                comment=self.get_object(),
                profile=request.user.profile
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

