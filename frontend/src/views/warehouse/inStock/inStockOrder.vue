<template>
  <div>
    <!-- <a-card title="入库任务"> -->
      <a-row gutter="16">
        <a-col :span="24" :md="8" :xl="6" style="max-width: 256px; margin-bottom: 12px;">
          <a-input-search v-model="searchForm.search" placeholder="单号" allowClear @search="search" />
        </a-col>
        <!-- <a-col :span="24" :md="8" :xl="6" style="max-width: 256px; margin-bottom: 12px;">
          <a-range-picker @change="onChangePicker" />
        </a-col> -->
      </a-row>

      <a-row style="margin-top: 12px;">
        <a-table size="small" :columns="columns" :dataSource="items" rowKey="id" :loading="loading" :pagination="pagination"
          @change="tableChange">
          <div slot="action" slot-scope="value, item">
            <a-button-group size="small">
              <a-button size="small" @click="detail(item)">详情</a-button>
              <a-button type="primary" size="small" @click="toStockIn(item)">入库</a-button>
            </a-button-group>
          </div>
        </a-table>
      </a-row>
    <!-- </a-card> -->
  </div>
</template>

<script>
  import { stockInOrdersList, stockInOrdersVoid } from '@/api/warehouse'

  export default {
    name: 'SaleRecord',
    components: {
    },
    data() {
      return {
        columns: [
          {
            title: '序号',
            dataIndex: 'index',
            key: 'index',
            customRender: (value, item, index) => {
              return index + 1
            },
            width: 45
          },
          {
            title: '单号',
            dataIndex: 'number',
            sorter: true,
          },
          {
            title: '仓库',
            dataIndex: 'warehouse_name',
          },
          {
            title: '入库类型',
            dataIndex: 'type_display',
          },
          {
            title: '入库完成状态',
            dataIndex: 'is_completed',
            customRender: (value, item, index) => {
              return item.is_completed ? '完成' : '待入库'
            },
          },
          {
            title: '状态',
            dataIndex: 'is_void',
            customRender: (value, item, index) => {
              return item.is_void ? '已作废' : '正常'
            },
          },
          {
            title: '处理日期',
            dataIndex: 'create_time',
            width: 170
          },
          {
            title: '操作',
            dataIndex: 'action',
            scopedSlots: { customRender: 'action' },
            width: 147
          },
        ],
        searchForm: { page: 1, is_completed: false, page_size: 16 },
        pagination: { current: 1, total: 0, pageSize: 16 },
        loading: false,
        items: [],
        visible: false,
        targetItem: {},
        form: {},
      };
    },
    computed: {
    },
    methods: {
      initialize() {
        this.list();
      },
      list() {
        this.loading = true;
        stockInOrdersList(this.searchForm).then(data => {
          this.pagination.total = data.count;
          this.items = data.results;
        }).finally(() => {
          this.loading = false;
        });
      },
      tableChange(pagination, filters, sorter) {
        this.searchForm.page = pagination.current;
        this.pagination.current = pagination.current;
        this.searchForm.ordering = `${sorter.order == 'descend' ? '-' : ''}${sorter.field}`;
        this.list();
      },
      onChangePicker(date, dateString) {
        let startDate = date[0], endDate = date[1];
        this.searchForm.start_date = startDate ? startDate.format('YYYY-MM-DD') : undefined;
        this.searchForm.end_date = endDate ? endDate.add(1, 'days').format('YYYY-MM-DD') : undefined;
        this.search();
      },
      search() {
        this.searchForm.page = 1;
        this.pagination.current = 1;
        this.list();
      },
      toStockIn(item) {
        this.$router.push({ path: '/warehouse/inStock_create', query: { id: item.id } });
      },
      detail(item) {
        this.$router.push({ path: '/warehouse/inStock_detail', query: { id: item.id } });
      },
      voidItem(item) {
        stockInOrdersVoid({ id: item.id }).then(() => {
          this.$message.success('作废成功');
          this.list();
        });
      },
    },
    mounted() {
      this.initialize();
    },
  }
</script>