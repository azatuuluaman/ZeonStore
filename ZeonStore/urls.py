from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
import Cart.views
import others.views
import product.views
from others.views import AboutUsViewSet
from product import views
from .swagger import url

router = DefaultRouter()
router.register(r'product', views.ProductViewSet, 'product')
router.register(r'about_us', AboutUsViewSet, 'about_Us')
router.register(r'collection', views.CollectionViewSet, 'collection')
router.register(r'collectionproduct', views.CollectionProductViewSet, 'collectionproduct')
router.register(r'news', others.views.NewsViewSet, 'news')  # новости
router.register(r'help', others.views.HelpingViewSet, 'help')  # помощь
router.register(r'publicoffer', others.views.PublicOfferViewSet, 'publicoffer')  # публичная оферта
router.register(r'footer', others.views.FooterViewSet, 'footer')  # футер
router.register(r'floatingbutton', others.views.FloatingButtonViewSet, 'floatingbutton', )
router.register(r'backcall', others.views.BackCallViewSet, 'backcall', )
router.register(r'favorites', product.views.FavoritesViewSet, 'favorites', )
router.register(r'cart', Cart.views.CartViewSet, 'cart',)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path(r'ckeditor/', include('ckeditor_uploader.urls')),
                  path('api/v1/', include(router.urls)),
                  path('api/v1/similar_product/<int:pk>/', views.filter, name='filter'),
                  path('api/v1/collection_product/<int:pk>', views.collection_products),  # показывает 12 товаров из одной коллекции
                  path('api/v1/news_product/', views.new_products),  # показывает 5 товаров со статусом новинки
                  path('product_search/', product.views.product_search),
                  path('mainpage/', product.views.mainpage),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += url
