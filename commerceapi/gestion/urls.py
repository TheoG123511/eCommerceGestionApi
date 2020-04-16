from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [path('', views.DocsView.as_view()),
               path("product/", views.ProductList.as_view(), name="viewAllProduct"),
               path("update/product/<int:pk>", views.ProductDetail.as_view(), name="UpdateProduct"),
               path("order/", views.OrderList.as_view()),
               path("update/order/<int:pk>", views.OrderUpdate.as_view()),
               path("order/details/<int:order__customer__id>/<int:order__id>", views.OrderDetail.as_view()),
               path("add/img/", views.ProductImageList.as_view()),
               path("customer/", views.CustomerList.as_view()),
               path("contact/", views.ContactList.as_view()),
               path("contact/<int:pk>", views.ContactDelete.as_view()),
               path("address/", views.AddressList.as_view()),
               path("address/<int:customer>", views.AddressCustomerDetails.as_view()),
               path("address/order/<int:customer>/<int:pk>", views.AddressOrderDetails.as_view()),
               path("subcategory/", views.SubCategoryList.as_view())]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
