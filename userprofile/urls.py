from .views import StudentProfileViewSet ,TeacherProfileViewSet ,UserViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter  # we can use custom routers


router = SimpleRouter()
router.register('StudentProfile',StudentProfileViewSet)
router.register('TeacherProfile',TeacherProfileViewSet)
router.register('users', UserViewSet )
urlpatterns = router.urls


