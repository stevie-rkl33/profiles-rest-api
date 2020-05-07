from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of ApiView features"""
        an_apiview = {
            'Uses HTTP methos as fnction (get, post, patch, put, delete)',
            'Is similar t traditional Djago view',
            'Gives you the most control over your application logix',
            'is mapped manually to URLs',
        }

        return Response({'message':'Hello', 'an_apiview': an_apiview})
