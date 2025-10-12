from django.utils import timezone
from rest_framework import viewsets,  status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import Post
from .serializers import PostSerializer



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        """
        Show only published posts to unauthenticated users.
        Admin can see all posts
        """
        if self.action == 'list' and not self.request.user.is_staff:
            return Post.objects.filter(is_published=True)
        return Post.objects.all()
    
    def get_permissions(self):
        """
        Apply different permission based on the action
        """
        if self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'retrive':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
    @action(detail=False, methods=['get'])
    def recent(self, request):
        """
        Return the 3 most recent published posts.
        URL: /posts/recent
        you can change url to url_path='latest'
        """
        recent_posts = Post.objects.filter(is_published=True).order_by('-id')[:3]
        serializer = self.get_serializer(recent_posts, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def publish(self, request, pk=None):
        """
        Publish specific post.
        URL: /posts/{id}/publish
        """
        post = self.get_object()
        post.is_published = True
        post.save()
        return Response({'status': 'post published'}, status=status.HTTP_200_OK)



