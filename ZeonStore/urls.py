"""ZeonStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

import others.views
from others.views import AboutUsViewSet
from product import views
from product.views import CollectionProductViewSet

router = DefaultRouter()
router.register(r'product', views.ProductViewSet, 'product')
router.register(r'about_us', AboutUsViewSet, 'about_Us')
router.register(r'collection', views.CollectionViewSet, 'collection' )
router.register(r'collectionproduct', views.CollectionProductViewSet, 'collectionproduct' )  #
router.register(r'news', others.views.NewsViewSet, 'news')  # новости
router.register(r'help', others.views.HelpingViewSet, 'help') # помощь

urlpatterns = [
    path('admin/', admin.site.urls),
    path (r'ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/similar_product/<int:pk>/', views.filter, name='filter'),
    path('api/v1/collection_product/<int:pk>', views.collection_products), #    показывает 12 товаров из одной коллекции
    path('api/v1/news_product/', views.new_products),  # показывает 5 товаров со статусом новинки

]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    # path ('api-auth/',include('rest_framework.urls')),
    # path('api/v1/about_us', include('others.urls')),
    # path('api/v1/', include('product.urls'))




# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)
