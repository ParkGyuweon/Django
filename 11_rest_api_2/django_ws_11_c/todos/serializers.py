from rest_framework import serializers
from .models import Todo, Recommend

class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        fields = '__all__'
        read_only_fields = ('todo',)
        
class TodoSerializer(serializers.ModelSerializer):
    recommend_set = RecommendSerializer(many=True, read_only=True)
    class Meta:
        model = Todo
        fields = '__all__'

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('work', 'is_completed', )