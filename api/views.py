from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

from .models import Book

@csrf_exempt
@require_http_methods(["POST"])
def add_book(request):
    response = {}
    try:
        data = json.loads(request.body)
        book = Book(book_name=data.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_book(request, book_id):
    response = {}
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Book.DoesNotExist:
        response['msg'] = 'Book not found'
        response['error_num'] = 1
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
