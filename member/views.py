from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.response import Response

@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed", "username": username, "password": password})
    return Response(
        {"login_id": user.id})