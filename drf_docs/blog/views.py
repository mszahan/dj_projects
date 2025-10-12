from rest_framework import viewsets
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



