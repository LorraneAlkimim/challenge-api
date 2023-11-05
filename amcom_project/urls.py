from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from amcom_project.core.views import CustomerViewset


router = routers.DefaultRouter()
router.register(r'customers', CustomerViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
