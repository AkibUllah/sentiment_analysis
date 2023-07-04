from django.urls import path
from .views import SentimentAnalysisView

urlpatterns = [
    path('sentiment-analysis/', SentimentAnalysisView.as_view()),
]
