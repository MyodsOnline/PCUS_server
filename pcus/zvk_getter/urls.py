from django.urls import path

from .views import get_all_zvk, get_gen_zvk, get_kolaes_zvk, get_laes_zvk, get_all_our


urlpatterns = [
    path('', get_all_zvk, name='all_zvk'),
    # path('viewed/', get_viewed_zvk, name='viewed_zvk'),
    path('gen/', get_gen_zvk, name='gen_zvk'),
    path('gen/kolaes/', get_kolaes_zvk, name='gen_kolaes'),
    path('gen/laes/', get_laes_zvk, name='gen_laes'),
    path('gen/test/', get_all_our, name='gen_test'),
]
