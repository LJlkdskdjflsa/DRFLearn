from rest_framework.generics import CreateAPIView, ListAPIView
from categories.serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated
from .models import Category


class CreateCategoryAPIView(CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        user = self.request.user
        print('--------------------')
        print(self.request.user.id)
        result = serializer.save(owner=user)
        return result
        '''try:
            result = serializer.save(owner=owner.id)
            return result
        except Exception as e:
            print(e)'''

class ListCategoryAPIView(ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    #queryset = Category.objects.all()

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)
