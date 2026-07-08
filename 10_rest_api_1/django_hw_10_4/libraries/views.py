from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Book
from .serializers import BookListSerializer, BookSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def book_detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        isbn = book.isbn
        title = book.title
        book.delete()
        data = {
            'message': f'{"delete": 도서 고유번호 {isbn}번의 {title}을 삭제하였습니다.}'
        }
        return Response(status=status.HTTP_200_OK)