# 系统功能
* 增加诗歌
* 修改诗歌
* 删除诗歌

# 初步的链接设计
* 首页（诗歌列表） /poem/
* 诗歌详情 /poem/detail/<id>
* 添加诗歌 /poem/add
* 删除诗歌 /poem/delete/<id>
* 修改诗歌 /poem/edit/<id>

## 操作步骤
### 1 创建项目及子应用，使用git进行管理
### 2 添加基本的 url和views
### 3 添加model以及数据库的支持
### 4 实现首页，诗歌列表页面
* template html模板
* views 渲染模板
* service 获得数据
### 5 诗歌详情页面
* html模板
* service 获取数据
* views渲染
### 6 添加诗歌
* views 添加诗歌 渲染添加诗歌的模板
* html 模板 form表单
* 接收form表单传递的数据并处理=》svc_add视图
### 步骤
1. add.html 模板
2. 修改views.add视图
3. 添加svc_add用于添加记录
### 修改诗歌
1. 进入修改页面，修改页面中包含要修改的诗歌数据
2. 点击提交按钮，修改完成
### 待修改代码
1. 修改页面html
2. 修改view edit
    1.获得要修改诗歌的service
3. 处理提交后数据的view，svc_edit，实际处理修改业务

### 9 完善
设置统一的格式模板