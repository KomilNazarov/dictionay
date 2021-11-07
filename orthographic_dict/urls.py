from django.urls import path
from orthographic_dict import views


urlpatterns = [
    path('category/', views.CategoryListAPIViews.as_view(), name='navbar-menyu'),
    path('words/', views.WordRetrieveAPIViews.as_view(), name='words-list'),
    path('word/<int:id>', views.WordDetailAPIView.as_view(), name='detail-word'),

]
