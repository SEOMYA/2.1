from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from autosalon.views import cars_list, car_detail, car_sales


urlpatterns = [
    path('cars/', cars_list, name='list'),
    path('cars/<int:car_id>/', car_detail, name='details'),
    path('cars/<int:car_id>/sales/', car_sales, name='sales')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)