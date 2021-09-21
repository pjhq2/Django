from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # 회원가입
    path('update/', views.update, name='update'),  # 회원정보 수정
    path('password/', views.change_password, name='change_password'),  # 비밀번호 변경
    path('delete/', views.delete, name='delete'),  # 회원탈퇴
    path('login/', views.login, name='login'),  # 로그인
    path('logout/', views.logout, name='logout'),  # 로그아웃

    path('<str:username>/', views.profile, name='profile'),  # 회원정보
]
