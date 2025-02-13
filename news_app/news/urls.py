from django.urls import path
from .views import *
from . import views
from .views import terms_and_conditions,contact_page
from .views import  ads_txt
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('search/', Search.as_view(), name='search'),
    path('post/<slug:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('terms-and-conditions/', terms_and_conditions, name='terms_and_conditions'),
    path('contact/', contact_page, name='contact_page'),
    path("ads.txt", ads_txt),

]
