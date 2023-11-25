from apps.statistic.views import HomeOverviewViewSet
from extensions.routers import *
from apps.statistic.views import *


router = BaseRouter()
router.register('purchase_reports', PurchaseReportViewSet, 'purchase_report')
router.register('sales_reports', SalesReportViewSet, 'sales_report')
router.register('sales_hot_goods', SalesHotGoodsViewSet, 'sales_hot_goods')
router.register('sales_trends', SalesTrendViewSet, 'sales_trend')
router.register('finance_statistics', FinanceStatisticViewSet, 'finance_statistic')
router.register('payment_order_details', PaymentOrderdetailViewSet, 'payment_order_detail')
router.register('collection_order_details', CollectionOrderdetailViewSet, 'collection_order_detail')
router.register('income_charge_order_details', IncomeChargeOrderdetailViewSet, 'income_charge_order_detail')
router.register('expenditure_charge_order_details', ExpenditureChargeOrderdetailViewSet, 'expenditure_charge_order_detail')
router.register('purchase_payment_details', PurchasePaymentdetailViewSet, 'purchase_payment_detail')
router.register('purchase_return_collection_details', PurchaseReturnCollectiondetailViewSet, 'purchase_return_collection_detail')
router.register('sales_collection_details', SalesCollectiondetailViewSet, 'sales_collection_detail')
router.register('sales_return_payment_details', SalesReturnPaymentdetailViewSet, 'sales_return_payment_detail')
router.register('home_overview', HomeOverviewViewSet, 'home_overview')
urlpatterns = router.urls
