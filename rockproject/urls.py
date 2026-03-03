from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rockapi.views import (
    register_user, login_user,
    TypeView, RockView
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'types', TypeView, 'type')
router.register(r'rocks', RockView, 'rock')


@api_view(["GET"])
@permission_classes([AllowAny])
def api_root(request):
    return Response({"message": "Rock API is running"})

urlpatterns = [
    path('', api_root),
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
]
