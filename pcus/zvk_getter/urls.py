from django.urls import path

from .views import get_all_zvk


urlpatterns = [
    path('', get_all_zvk, name='all_zvk'),
    # path('viewed/', get_viewed_zvk, name='viewed_zvk'),
    # path('gen/', get_gen_zvk, name='gen_zvk'),
]
