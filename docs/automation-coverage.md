# 自动化覆盖说明

## 文档定位

本文档用于说明当前项目的接口覆盖范围、测试场景分布以及测试组织方式，重点展示项目在接口自动化测试方面的完成度。

## 整体覆盖结果

当前项目共包含 **34 条自动化测试用例**，真实覆盖 **22 个接口操作**，覆盖以下三类核心业务模块：

- 用户模块
- 仓库模块
- Issue/标签模块

此外，项目已经完成以下能力落地：

- YAML 数据驱动测试
- MySQL 数据库一致性校验
- pytest marker 分组执行
- pytest HTML 报告与 Allure 报告生成
- JMeter 基础接口性能测试实践

## 模块覆盖情况

### 用户模块

对应文件：
- `testcases/test_user.py`

当前已覆盖场景：

1. 获取当前用户信息成功
2. 获取当前用户仓库列表成功
3. 获取公开用户信息成功
4. 获取公开用户仓库列表成功
5. 当前用户鉴权数据驱动场景
6. 当前用户查询 smoke 场景

### 仓库模块

对应文件：
- `testcases/test_repo.py`

当前已覆盖场景：

1. 创建仓库数据驱动场景
2. 查询仓库详情成功
3. 修改仓库描述成功
4. 删除仓库成功
5. 查询仓库语言统计成功
6. 查询仓库协作者列表成功
7. 创建仓库后数据库校验成功
8. 仓库详情 smoke 场景

### Issue/标签模块

对应文件：
- `testcases/test_issue.py`

当前已覆盖场景：

1. 创建 Issue 数据驱动场景
2. 查询 Issue 列表成功
3. 查询 Issue 详情成功
4. 查询仓库标签列表成功
5. 关闭 Issue 成功
6. Issue 标签生命周期测试成功
7. 关闭 Issue 后数据库校验成功
8. 关闭 Issue smoke 场景

### 异常场景模块

对应文件：
- `testcases/test_negative.py`

当前已覆盖场景：

1. 关闭不存在仓库下的 Issue
2. 查询不存在的 Issue
3. 删除不存在的标签
4. 查询不存在的仓库
5. 删除不存在的仓库
6. 查询不存在的公开用户
7. 使用非法分页参数查询 Issue 列表
8. 更新不存在的仓库
9. 使用非法 `private` 类型创建仓库
10. 给不存在的 Issue 添加标签

## 接口覆盖明细

当前真实覆盖的 22 个接口操作如下：

1. `GET /user`
2. `GET /user/repos`
3. `GET /users/{username}`
4. `GET /users/{username}/repos`
5. `POST /user/repos`
6. `GET /repos/{owner}/{repo}`
7. `PATCH /repos/{owner}/{repo}`
8. `DELETE /repos/{owner}/{repo}`
9. `GET /repos/{owner}/{repo}/languages`
10. `GET /repos/{owner}/{repo}/collaborators`
11. `POST /repos/{owner}/{repo}/issues`
12. `GET /repos/{owner}/{repo}/issues`
13. `GET /repos/{owner}/{repo}/issues/{index}`
14. `PATCH /repos/{owner}/{repo}/issues/{index}`
15. `GET /repos/{owner}/{repo}/labels`
16. `POST /repos/{owner}/{repo}/labels`
17. `GET /repos/{owner}/{repo}/labels/{id}`
18. `DELETE /repos/{owner}/{repo}/labels/{id}`
19. `POST /repos/{owner}/{repo}/issues/{index}/labels`
20. `GET /repos/{owner}/{repo}/issues/{index}/labels`
21. `PUT /repos/{owner}/{repo}/issues/{index}/labels`
22. `DELETE /repos/{owner}/{repo}/issues/{index}/labels`

## 测试组织方式

项目当前采用以下组织方式：

- 使用 YAML 文件维护接口测试数据
- 使用 fixture 管理测试前置和清理逻辑
- 使用 marker 实现 `smoke`、`db`、`auth`、`repo`、`issue` 分组执行
- 使用 pytest HTML 与 Allure 进行测试结果展示

## 结论

从当前覆盖结果来看，项目已经具备较完整的小型接口自动化测试项目形态，既能体现基础接口覆盖能力，也能体现数据驱动、数据库校验和结果展示能力。
