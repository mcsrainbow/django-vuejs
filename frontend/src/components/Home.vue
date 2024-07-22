<template>
  <div class="home">
    <el-row :gutter="20" style="margin-top:10px">
      <el-col :span="6">
        <el-input v-model="input" placeholder="请输入书名"></el-input>
      </el-col>
      <el-col :span="2">
        <el-button type="primary" @click="addBook">新增</el-button>
      </el-col>
    </el-row>
    <el-row style="margin-top:20px">
      <el-table :data="bookList" style="width: 100%" border>
        <el-table-column prop="id" label="编号" min-width="100">
          <template slot-scope="scope">{{ scope.row.pk }}</template>
        </el-table-column>
        <el-table-column prop="book_name" label="书名" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.book_name }}</template>
        </el-table-column>
        <el-table-column prop="add_time" label="添加时间" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.add_time }}</template>
        </el-table-column>
        <el-table-column label="操作" min-width="100">
          <template slot-scope="scope">
            <el-button type="danger" size="small" @click="deleteBook(scope.row.pk)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      input: '',
      bookList: []
    }
  },
  mounted () {
    this.showBooks()
  },
  methods: {
    addBook () {
      this.$http.post('http://127.0.0.1:9080/api/add_book/', { book_name: this.input })
        .then(response => {
          const res = response.data
          if (res.error_num === 0) {
            this.showBooks()
          } else {
            this.$message.error('新增书籍失败，请重试')
            console.error(res.msg)
          }
        }).catch(error => {
          this.$message.error('新增书籍时发生错误')
          console.error(error)
        })
    },
    deleteBook (bookId) {
      this.$http.delete(`http://127.0.0.1:9080/api/delete_book/${bookId}`)
        .then(response => {
          const res = response.data
          if (res.error_num === 0) {
            this.showBooks()
          } else {
            this.$message.error('删除书籍失败，请重试')
            console.error(res.msg)
          }
        }).catch(error => {
          this.$message.error('删除书籍时发生错误')
          console.error(error)
        })
    },
    showBooks () {
      this.$http.get('http://127.0.0.1:9080/api/show_books')
        .then(response => {
          const res = response.data
          if (res.error_num === 0) {
            this.bookList = res.list
          } else {
            this.$message.error('查询书籍失败')
            console.error(res.msg)
          }
        }).catch(error => {
          this.$message.error('查询书籍时发生错误')
          console.error(error)
        })
    }
  }
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
