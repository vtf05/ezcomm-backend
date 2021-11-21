from .views import Notice_PostViewSet , CommentViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter  # we can use custom routers


router = SimpleRouter()
router.register('notice_post', Notice_PostViewSet)
router.register('comments',CommentViewSet)
urlpatterns = router.urls


