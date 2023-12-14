from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializers


# Create your views here.

# GET methods - get data from the db, serializes it and returns it
# so we can print it

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializers(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializers(users, many=False)
    return Response(serializer.data)


# POST methods - gets the input from the json body and saves it if it's valid
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# PUT - gets already created instance and updates it
@api_view(['PUT'])
def update_user(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializers(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# DELETE
@api_view(['DELETE'])
def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user.delete()

    return Response('Deleted successfully!')
