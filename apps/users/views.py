from rest_framework.views import APIView, Request, Response

from .serializers import RegisterSerializer


class UserRegister(APIView):
    
    def post(self, request: Request) -> Response:
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "User registered successfully."}, status=201)
        return Response(serializer.errors, status=400)

