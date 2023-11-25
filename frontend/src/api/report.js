import request from '@/utils/request';

// 销售报表
export function salesReportStatistics(params) {
  return request({ url: `/sales_reports/statistics/`, method: 'get', params })
}
// 销售报表明细
export function salesReportdetailsList(params) {
  return request({ url: `/sales_reports/details/`, method: 'get', params })
}
// 销售报表按产品汇总
export function salesReportByGoodsList(params) {
  return request({ url: `/sales_reports/group_by_goods/`, method: 'get', params })
}

// 采购报表
export function purchaseReportStatistics(params) {
  return request({ url: `/purchase_reports/statistics/`, method: 'get', params })
}
// 采购报表明细
export function purchaseReportdetailsList(params) {
  return request({ url: `/purchase_reports/details/`, method: 'get', params })
}
// 采购报表按产品汇总
export function purchaseReportByGoodsList(params) {
  return request({ url: `/purchase_reports/group_by_goods/`, method: 'get', params })
}

// 库存报表
export function inventoryReportList(params) {
  return request({ url: `/inventories/`, method: 'get', params })
}

// 收支统计
export function financialStatistics(params) {
  return request({ url: `/finance_statistics/`, method: 'get', params })
}

// 订单收款明细
export function salesPaymentRecord(params) {
  return request({ url: `/sales_collection_details/`, method: 'get', params })
}

// 销售退款明细
export function salesReturnPaymentRecord(params) {
  return request({ url: `/sales_return_payment_details/`, method: 'get', params })
}

// 采购支出明细
export function purchasePaymentRecord(params) {
  return request({ url: `/purchase_payment_details/`, method: 'get', params })
}

// 采购退款明细
export function purchaseReturnPaymentRecord(params) {
  return request({ url: `/purchase_return_collection_details/`, method: 'get', params })
}

// 批次报表
export function batchsReportList(params) {
  return request({ url: `/batchs/`, method: 'get', params })
}
