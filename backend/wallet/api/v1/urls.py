from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CustomerWalletViewSet,
    PaymentMethodViewSet,
    PaymentTransactionViewSet,
    TaskerPaymentAccountViewSet,
    TaskerWalletViewSet,
)

router = DefaultRouter()
router.register("taskerwallet", TaskerWalletViewSet)
router.register("paymenttransaction", PaymentTransactionViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("taskerpaymentaccount", TaskerPaymentAccountViewSet)
router.register("customerwallet", CustomerWalletViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
