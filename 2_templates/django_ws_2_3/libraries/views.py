from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def book(request):
    API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
    API_KEY = 'ttbwhdcks11291123001'
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'SearchTarget': 'Book',
        'MaxResults': 50,
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params)
    books = response.json()
    sorted_books = []

    for book in books['item']:
        book_dict = {}
        book_dict['국제 표준 도서 번호'] = book['isbn']
        book_dict['저자'] = book['author']
        book_dict['제목'] = book['title']
        book_dict['출간일'] = book['pubDate']
        sorted_books.append(book_dict)

    context = {
        'book_list' : sorted_books,
    }
    
    return render(request, 'book.html', context)