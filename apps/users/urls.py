from django.urls import path
from .views import (
    UserList,
    UserDetail,
)

app_name = 'users_section'

urlpatterns = [
    path('teachers/', UserList.as_view(), name='teachers_list'),
    path('teacher/<slug:slug>', UserDetail.as_view(), name='teacher_detail'),
]
