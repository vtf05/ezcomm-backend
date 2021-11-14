from .views import WalletViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter  # we can use custom routers


router = SimpleRouter()
router.register('wallet', WalletViewSet)
urlpatterns = router.urls


