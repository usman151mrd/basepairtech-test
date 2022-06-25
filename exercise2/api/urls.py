from rest_framework import routers
from api.views import SeriesViewSet

router = routers.DefaultRouter()
router.register(r'users', SeriesViewSet, basename='user')
urlpatterns = router.urls
