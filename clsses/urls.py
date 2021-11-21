from .views import AssignmentViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter  # we can use custom routers


router = SimpleRouter()
router.register('Assignment',AssignmentViewSet)
urlpatterns = router.urls


