from rest_framework import routers
from .views import UserViewSet, TransactionViewSet, TransactionsByDate, TransactionsByType
from django.urls import path

#router = routers.DefaultRouter()
# router.register('user', UserViewSet, 'user')
#router.register('transaction', TransactionViewSet, 'transaction')

router = routers.SimpleRouter()
router.register('user', UserViewSet)
router.register('transaction', TransactionViewSet)

urlpatterns = [
    path("transactionsbydate/<int:pk>/", TransactionsByDate.as_view()),
    path("transaction/<str:type>/", TransactionsByType.as_view())
    #path("user/", UserViewSet.as_view())
]

urlpatterns += router.urls
