from django.contrib.auth import get_user_model
from drf_spectacular.utils import OpenApiExample, extend_schema, OpenApiParameter, extend_schema_view
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Transaction
from users.serializers import UserSerializer, TransactionCreateSerializer

1


class APIRootView(APIView):
    @extend_schema(
        description="API root with list of available endpoints for User and Transaction management."
    )
    def get(self, request, *args, **kwargs):
        return Response({
            "register": "/api/register/",
            "token_obtain_pair": "/api/token/",
            "token_refresh": "/api/token/refresh/",
            "token_verify": "/api/token/verify/",
            "add_user": "/api/add_user/",
            "get_user": "/api/get_user/{user_id}/",
            "get_all_users": "/api/get_all_users/",
            "add_transaction": "/api/add_transaction/",
            "stats": "/api/stats/",
        })


@extend_schema(
    description="Creates a new user. Only accessible to admin users.",
    request=UserSerializer,
    responses={201: UserSerializer},
    examples=[
        OpenApiExample(
            "Example response",
            value={"id": 4},
            response_only=True
        )
    ]
)
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"id": user.id}, status=201)


@extend_schema(
    description="Retrieve details of a specific user by their ID.",
    responses={200: UserSerializer}
)
class UserDetailView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = "id"
    lookup_url_kwarg = "user_id"


@extend_schema(
    description="Retrieve a list of all users. Only accessible to authenticated users.",
    responses={200: UserSerializer(many=True)},
    examples=[
        OpenApiExample(
            "Example response",
            value=[
                {
                    "id": 1,
                    "username": "admin",
                    "email": "admin@admin.com",
                    "transactions": [
                        {
                            "id": 3,
                            "transaction_type": "Credit",
                            "amount": "23.00",
                            "created_at": "2024-10-09T09:33:00.478865Z"
                        }
                    ]
                },
                {
                    "id": 3,
                    "username": "Carl",
                    "transactions": [
                        {
                            "id": 4,
                            "transaction_type": "Transfer",
                            "amount": "34.00",
                            "created_at": "2024-10-09T09:33:09.283248Z"
                        },
                        {
                            "id": 11,
                            "transaction_type": "Credit",
                            "amount": "56.00",
                            "created_at": "2024-10-09T11:15:25.210798Z"
                        },
                        {
                            "id": 12,
                            "transaction_type": "Credit",
                            "amount": "32.00",
                            "created_at": "2024-10-09T11:15:26.676643Z"
                        }
                    ]
                },
            ],
            response_only=True
        )
    ]
)
class ListUserView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


@extend_schema(
    description="Create a new transaction linked to a user.",
    request=TransactionCreateSerializer,
    responses={201: TransactionCreateSerializer},
    examples=[
        OpenApiExample(
            "Example response",
            {
                "user_id": 1,
                "transaction_type": "debit",
                "amount": "34.00"
            },
            response_only=True
        )
    ]
)
class TransactionCreateView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionCreateSerializer
    permission_classes = (IsAdminUser,)
