from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from users.views import (
    CreateUserView,
    UserDetailView,
    ListUserView,
    TransactionCreateView,
)

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),

    path("add_user/", CreateUserView.as_view(), name="add-user"),
    path("get_user/<int:user_id>/", UserDetailView.as_view(), name="user-detail"),
    path("get_all_users/", ListUserView.as_view(), name="user-list"),
    path(
        "add_transaction/", TransactionCreateView.as_view(), name="transaction-create"
    ),
]
