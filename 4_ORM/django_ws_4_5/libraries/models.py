from django.db import models
import requests

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()

    @classmethod
    def insert_data(cls):
        API_KEY = 'ttbwhdcks11291123002'
        API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
        
        params = {
            'ttbkey': API_KEY,
            'QueryType': 'ItemNewAll', 
            'SearchTarget': 'Book',
            'MaxResults': 13,        
            'output': 'js',
            'Version': '20131101'
        }

        response = requests.get(API_URL, params=params)
        data = response.json()
        
        print("API 전체 응답 데이터:", data) 
        
        books_array = data.get('item', []) 
        
        print(f"추출된 도서 개수: {len(books_array)}")

        for book in books_array:
            my_book = cls(
                isbn=book.get('isbn13', book.get('isbn', '')), 
                title=book.get('title', ''),
                author=book.get('author', ''),
                category_name=book.get('categoryName', ''),
                category_id=book.get('categoryId', 0),
                price=book.get('priceStandard', 0), 
                fixed_price=book.get('fixedPrice', True),
                pub_date=book.get('pubDate', '1900-01-01')
            )
            my_book.save()