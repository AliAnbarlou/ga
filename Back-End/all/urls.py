from django.urls import reverse , path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.all_home, name='all_page'),
    path('<int:blog_id>/', views.det_view, name="det"),
    path('detail/<int:blog_id>/', views.det_view, name='detail'),
    path('search/',view=views.search,name='search'),
    
]
