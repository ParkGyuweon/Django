from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class ReviewListSerializer(serializers.ModelSerializer):
    isbn = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('content', 'score',)

    def get_isbn(self, obj):
        return obj.book.isbn

class BookSerializer(serializers.ModelSerializer):
    review_set = ReviewListSerializer(many=True, read_only=True)
    num_of_comments = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_num_of_comments(self, obj):
        return obj.review_set.count()
    
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)