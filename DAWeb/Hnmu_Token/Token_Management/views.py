import jwt
from django.conf.global_settings import SECRET_KEY
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken


class TokenView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            response = Response()

            response.data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return response
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class CombinedJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        token = None

        # Lấy token từ header Authorization
        auth_header = self.get_header(request)
        if auth_header is not None:
            raw_token = self.get_raw_token(auth_header)
            if raw_token is not None:
                token = raw_token

        # Nếu không tìm thấy token trong header, lấy từ cookie
        if token is None:
            token = request.COOKIES.get('jwt')

        if token is None:
            return None

        try:
            validated_token = self.get_validated_token(token)
            user = self.get_user(validated_token)
            return (user, validated_token)
        except Exception as e:
            raise AuthenticationFailed({'error': str(e)}, code=401)

    def check_token(self, token):
        try:
            validated_token = self.get_validated_token(token)
            user_id = validated_token['user_id']  # Giả sử user_id được lưu trong token payload
            return True, user_id
        except Exception as e:
            return False, str(e)


class CheckTokenAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        token = None

        # Lấy token từ header Authorization
        auth_header = self.request.headers.get('Authorization')
        if auth_header is not None and auth_header.startswith('Bearer '):
            token = auth_header.split('Bearer ')[1]

        # Nếu không tìm thấy token trong header, lấy từ cookie
        if token is None:
            token = request.COOKIES.get('jwt')

        # Kiểm tra xem token có tồn tại không
        if not token:
            return Response({"msg": "Token not found"}, status=status.HTTP_400_BAD_REQUEST)

        # Kiểm tra tính hợp lệ của token
        authentication = CombinedJWTAuthentication()
        is_valid, user_id_or_error = authentication.check_token(token)

        # Trả về phản hồi phù hợp
        if is_valid:
            return Response({"msg": user_id_or_error}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": user_id_or_error}, status=status.HTTP_401_UNAUTHORIZED)