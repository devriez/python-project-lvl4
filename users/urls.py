from django.urls import path
from users.views import UserListView, UserCreate, UserUpdate, UserDelete


urlpatterns = [
    path('', UserListView.as_view(), name='users-list'),
    path('create/', UserCreate.as_view(), name='user-create'),
    path('<int:pk>/update/', UserUpdate.as_view(), name='user-update'),
    path('<int:pk>/delete/', UserDelete.as_view(), name='user-delete'),
]
