import re
from transformers import pipeline
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SentimentAnalysisView(APIView):
    @classmethod
    def post(cls, request):

        if 'text' not in request.data:
            data = {
                'messages': "Text Field Is Missing"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        if request.data['text'] == '':
            data = {
                'messages': "Text Can't Be Empty"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        try:
            text = request.data['text']
            string_validation = bool(re.match(r"[a-zA-Z]+", text))
            print(string_validation)
            if not string_validation:
                data = {
                    'messages': "Only Sentence Are Allowed"
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            if type(text) != str:
                data = {
                    'messages': "Text Can't Be Integer"
                }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            else:
                model_classifier = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")
                analysis = model_classifier(text)
                sentiment = analysis[0]['label']
                data = {
                    'sentiment': sentiment.lower()
                }
                return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
