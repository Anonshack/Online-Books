from rest_framework.serializers import ModelSerializer
from .models import Books, AboutPage, QrCode
from django.contrib.auth import get_user_model


class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        # fields = ('id', 'name', 'last_name')
        fields = "__all__"


class AboutSerializer(ModelSerializer):
    class Meta:
        model = AboutPage
        # fields = ('id', 'name', 'last_name')
        fields = "__all__"


class QR_code(ModelSerializer):
      class Meta:
            model = QrCode
            fields = ['title', 'image', 'info', 'url']


class UserSerializers(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        extra_kwargs = {
            'username': {'read_only': True}
        }
