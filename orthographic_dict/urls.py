from django.urls import path
from orthographic_dict import views


urlpatterns = [
    path('category/', views.CategoryListAPIViews.as_view(), name='navbar-menyu'),
    path('words/', views.WordRetrieveAPIViews.as_view(), name='search-list'),
    path('words/num', views.WordAPIViews.as_view(), name='count-words'),
    path('word/<int:id>', views.WordDetailAPIView.as_view(), name='detail-word'),
    path('user/info', views.UserRetriveAPIViews.as_view(), name='user-info'),
    path('rotation/create', views.RotationApiView.as_view(), name='rotation'),

]
