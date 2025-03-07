<template>
  <div>
    <a-card title="生产计划">
      <a-row :gutter="[12, 8]">
        <a-col :span="24" style="width: 256px;">
          <a-range-picker @change="onChangePicker" />
        </a-col>
        <a-col :span="24" style="width: 200px;">
          <a-input v-model="searchForm.search" placeholder="生产单号, 销售单号" allowClear @pressEnter="search" />
        </a-col>
        <a-col :span="24" style="width: 84px;">
          <a-button type="primary" icon="search" @click="search">查询</a-button>
        </a-col>

        <div style="margin-bottom: 12px; float: right">
          <a-button type="primary" icon="plus" style="margin: 0 8px" @click="openCreateModal({})">
            新增生产计划
          </a-button>
        </div>
      </a-row>

      <a-row style="margin-top: 12px">
        <a-table
          rowKey="id"
          :columns="columns"
          :data-source="items"
          :pagination="pagination"
          :loading="loading"
          :scroll="{ x: 1600 }"
        >
          <div slot="action" slot-scope="value, item, index">
            <a-button-group size="small">
              <a-button v-if="item.status == 'in_plan'" @click="openCreateModal(item)">编辑</a-button>
              <a-button @click="detail(item)">详情</a-button>
              <a-popconfirm v-if="item.status == 'in_plan'" title="确定发布吗?" @confirm="issue(item)">
                <a-button type="primary">发布工单</a-button>
              </a-popconfirm>
              <a-popconfirm v-if="item.status == 'in_progress'" title="确定关闭吗?" @confirm="close(item)">
                <a-button type="primary">关闭工单</a-button>
              </a-popconfirm>
              <a-popconfirm v-if="item.status == 'in_plan'" title="确定删除吗?" @confirm="destroy(item)">
                <a-button type="danger">删除</a-button>
              </a-popconfirm>
            </a-button-group>
          </div>
        </a-table>
      </a-row>
    </a-card>

    <form-modal v-model="visible" :form="targetItem" @create="create" @update="update" />
  </div>
</template>

<script>
import {
  productionOrderList,
  productionOrderDelete,
  productionOrderIssue,
  productionOrderClose,
} from "@/api/production";

export default {
  components: {
    FormModal: () => import("./FormModal.vue"),
  },
  data() {
    return {
      searchForm: { search: "", page: 1, ordering: undefined },
      pagination: { current: 1, total: 0, pageSize: 16 },
      loading: false,
      items: [],
      columns: [
        {
          title: "序号",
          dataIndex: "index",
          width: 60,
          fixed: "left",
          customRender: (value, item, index) => {
            return index + 1;
          },
        },
        {
          title: "生产计划单号",
          dataIndex: "number",
          fixed: "left",
        },
        {
          title: "销售单号",
          dataIndex: "sales_order_number",
        },
        {
          title: "状态",
          dataIndex: "status_display",
          width: 100,
        },
        {
          title: "产品编号",
          dataIndex: "goods_number",
        },
        {
          title: "产品名称",
          dataIndex: "goods_name",
        },
        {
          title: "计划数量",
          dataIndex: "total_quantity",
          width: 100,
        },
        {
          title: "完成数量",
          dataIndex: "quantity_produced",
          width: 100,
        },
        {
          title: "计划开始时间",
          dataIndex: "start_time",
          width: 180,
        },
        {
          title: "计划结束时间",
          dataIndex: "end_time",
          width: 180,
        },
        {
          title: "操作",
          dataIndex: "action",
          fixed: "right",
          width: 256,
          scopedSlots: { customRender: "action" },
        },
      ],
      visible: false,
      targetItem: {},
    };
  },
  methods: {
    initialize() {
      this.list();
    },
    list() {
      this.loading = true;
      productionOrderList(this.searchForm)
        .then((data) => {
          this.pagination.total = data.count;
          this.items = data.results;
        })
        .finally(() => {
          this.loading = false;
        });
    },
    create(item) {
      this.items = this.$functions.insertItem(this.items, item);
    },
    update(item) {
      this.items = this.$functions.replaceItem(this.items, item);
    },
    destroy(item) {
      productionOrderDelete({ id: item.id }).then(() => {
        this.$message.success("删除成功");
        this.items = this.$functions.removeItem(this.items, item);
      });
    },
    issue(item) {
      productionOrderIssue({ id: item.id }).then((data) => {
        this.$message.success("发布成功");
        this.items = this.$functions.replaceItem(this.items, data);
      });
    },
    close(item) {
      productionOrderClose({ id: item.id }).then((data) => {
        this.$message.success("关闭成功");
        this.items = this.$functions.replaceItem(this.items, data);
      });
    },
    detail(item) {
      this.$router.push({ path: "/production/detail", query: { id: item.id } });
    },
    search() {
      this.searchForm.page = 1;
      this.pagination.current = 1;
      this.list();
    },
    tableChange(pagination, filters, sorter) {
      this.searchForm.page = pagination.current;
      this.pagination.current = pagination.current;
      this.searchForm.ordering = `${sorter.order == "descend" ? "-" : ""}${sorter.field}`;
      this.list();
    },
    onChangePicker(date, dateString) {
      let startDate = date[0];
      let endDate = date[1];
      this.searchForm.start_date = startDate ? startDate.format("YYYY-MM-DD") : undefined;
      this.searchForm.end_date = endDate ? endDate.add(1, "days").format("YYYY-MM-DD") : undefined;
      this.search();
    },
    openCreateModal(item) {
      this.targetItem = { ...item };
      this.visible = true;
    },
  },
  mounted() {
    this.initialize();
  },
};
</script>

<style scoped></style>
