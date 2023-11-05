from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from amcom_project.core.views import CustomerViewset, SellerViewset


router = routers.DefaultRouter()
router.register(r'customers', CustomerViewset)
router.register(r'sellers', SellerViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
