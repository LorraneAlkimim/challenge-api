from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from amcom_project.core.views import (
    CustomerViewset,
    SellerViewset,
    ProductViewset,
    SaleViewset,
    SaleCreateViewset,
    SaleUpdateViewset,
    CommissionViewset,
)


router = routers.DefaultRouter()
router.register(r"customers", CustomerViewset)
router.register(r"sellers", SellerViewset)
router.register(r"products", ProductViewset)
router.register(r"sales", SaleViewset)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/create_sale/", SaleCreateViewset.as_view()),
    path("api/update_sale/<int:invoice_code>/", SaleUpdateViewset.as_view()),
    path("api/commissions/", CommissionViewset.as_view()),
]
