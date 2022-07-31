from rest_framework import serializers
from api.models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True,max_length=100,allow_blank=True)
    body= serializers.CharField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.body = validated_data.get('body',instance.body)
        instance.save()
        return instance


