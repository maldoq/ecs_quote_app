from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('connexion/', views.login_page, name='login'),
    path('carte/<int:user_id>/', views.quote_card, name='quote_card'),
    path('telecharger/<int:user_id>/', views.download_card, name='download_card'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )