from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import User, Transaction
from .serializers import UserSerializer, TransactionSerializer
from django.db.models import Sum
from django.db.models.functions import TruncDay
import json
from django.core.serializers.json import DjangoJSONEncoder
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['first_name', 'last_name', 'email']
    # permission_classes = [
    #     permissions.AllowAny
    # ]
    # filter_backends = [SearchFilter]
    # search_fields = ['first_name', 'last_name', 'email']
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     first_name, last_name = self.request.query_params.get('first_name'), self.request.query_params.get('last_name')
    #     search_params = {'first_name__iexact': first_name, 'last_name__iexact': last_name}
    #     return qs.filter(**search_params)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    # permission_classes = [
    #     permissions.AllowAny
    # ]
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['user_id', 'date', 'amount']
    search_fields = ['user_id', 'date', 'amount']
    ordering_fields = ['user_id', 'date', 'amount']

class TransactionsByDate(APIView):
    def get(self, request, pk):
        queryset = Transaction.objects.filter(user_id = pk).values(tr_date = TruncDay('date')).annotate(Sum('amount'))
        serializer = json.dumps(list(queryset), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
        return Response(json.loads(serializer))

class TransactionsByType(APIView):
    def get(self, request, type):
        if type == 'outcome':
            queryset = Transaction.objects.filter(amount__lt = 0)
        elif type == 'income':
            queryset = Transaction.objects.filter(amount__gt = 0)
        else:
            queryset = Transaction.objects.all()

        serializer = TransactionSerializer(queryset, many = True)
        return Response(serializer.data)
