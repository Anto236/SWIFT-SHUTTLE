from rest_framework.response import Response
from rest_framework import status

def create_response(data=None, message=None, status_code=status.HTTP_200_OK):
    return Response(
        {
            "message": message,
            "data": data,
        },
        status=status_code,
    )