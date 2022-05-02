from django.urls import path
from .views import *

app_name = 'schools220'

urlpatterns = [
    path('managements/', ManagementsListView.as_view(), name='managements'),
    path('<int:pk>/', CoursesDetailView.as_view(), name='course_details'),
    path('gallery/', GalleryListView.as_view(), name='gallery'),
    path('staff/', StaffListView.as_view(), name='staff'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='detail'),
    path('about/', AboutTemplateViews.as_view(), name='about'),
    path('', HomeTemplateViews.as_view(), name='home'),
    path('contact/', ContactCreateView.as_view(), name='contact')

]
