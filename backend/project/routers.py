from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet, ProductGenericViewSet


###########################################

router = DefaultRouter()

router.register('products', ProductViewSet, basename='products')
# router.register('products', ProductGenericViewSet, basename='products')


# print(router.urls)
# [
    # <URLPattern '^$' [name='api-root']>, 
    # <URLPattern '^products/$' [name='products-list']>, 
    # <URLPattern '^products\.(?P<format>[a-z0-9]+)/?$' [name='products-list']>, 
    # <URLPattern '^products/(?P<pk>[^/.]+)/$' [name='products-detail']>, 
    # <URLPattern '^products/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$' [name='products-detail']>, 
    # <URLPattern '^\.(?P<format>[a-z0-9]+)/?$' [name='api-root']>
    # ]

urlpatterns = router.urls
