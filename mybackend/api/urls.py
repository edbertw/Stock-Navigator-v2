# api/urls.py
from django.urls import path
from .views import submit_stock
from .views2 import predict_stock
from .rag_main import ask_chatbot

urlpatterns = [
    path('submit-stock/', submit_stock),
    path('predict-stock/', predict_stock),
    path('ask-chatbot/', ask_chatbot)
]
