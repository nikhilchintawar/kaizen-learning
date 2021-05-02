from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

from .serializers import SignUpSerializer, SignInSerializer, UserSerializer


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def SignIn(request):
    signin_serializer = SignInSerializer(data=request.data)

    if not signin_serializer.is_valid():
        return Response(signin_serializer.errors, status=HTTP_400_BAD_REQUEST)

    """
        use request.data.get() method for authenticate
        because serializer returns the html and because of
        that authenticate method doesn't work properly
        check here: https://stackoverflow.com/questions/66848323/typeerror-password-must-be-a-string-or-bytes-got-boundfield
    """

    user = authenticate(
        username=request.data.get("username"), password=request.data.get("password")
    )
    if not user:
        return Response({"error": "Invalid Credentials"}, status=HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)

    user_serialized = UserSerializer(user)
    return Response(
        {
            "user": user_serialized.data,
            "token": token.key,
        },
        status=HTTP_200_OK,
    )


@method_decorator(csrf_exempt, name="dispatch")
class SignUpAPI(generics.GenericAPIView):
    # queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        signup_serializer = self.get_serializer(data=request.data)
        signup_serializer.is_valid(raise_exception=True)
        user = signup_serializer.save()

        user_serialized = UserSerializer(user)
        token = Token.objects.create(user=user)
        return Response(
            {
                "user": user_serialized.data,
                "token": token.key,
            },
            status=HTTP_201_CREATED,
        )


class SignOutAPI(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=HTTP_200_OK)


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
