from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .tasks import sending_mail
from .models import Todo
from decouple import config
from .serializers import TodoSerializer

permission = [IsAuthenticated]


## Если не получается авторизоваться через токен, то поменяйте permission
# permission = [AllowAny]


def home(request):
    return HttpResponse('sent')


class TodoView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = permission
    queryset = Todo.objects.all()


class DetailedView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = permission
    queryset = Todo.objects.all()


class Executed(APIView):
    permission_classes = permission

    def post(self, request, pk):
        obj = get_object_or_404(Todo, pk=pk)
        completed = obj.done
        obj.done = not completed
        obj.save()
        sending_mail.delay(request.user.email, completed)

        if completed:
            return HttpResponse('The task was marked as completed, please wait 10 seconds until message comes')
        return HttpResponse("You marked the task as uncompleted please wait 10 seconds until message comes")
