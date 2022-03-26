from django.db import models
# from product.models import Product_item
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class Collection (models.Model):
    title = models.CharField('Название', max_length=50)
    img = models.ImageField('Изображение', upload_to='images')

    def __str__(self):
        return self.title

class PaginationCollection(PageNumberPagination):
    page_size = 1
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })



