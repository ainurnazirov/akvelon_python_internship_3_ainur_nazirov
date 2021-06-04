from rest_framework import routers
from .views import UserViewSet, TransactionViewSet, TransactionsByDate, TransactionsByType, TransactionsOfUserByType
from django.urls import path


router = routers.SimpleRouter()
router.register('users', UserViewSet)
router.register('transactions', TransactionViewSet)

urlpatterns = [
    path("transactionsbydate/<int:pk>/", TransactionsByDate.as_view()),
    path("transactionsbytype/<str:type>/", TransactionsByType.as_view()),
    path("transactionsbytype/<str:type>/<int:pk>/", TransactionsOfUserByType.as_view())
]

urlpatterns += router.urls
