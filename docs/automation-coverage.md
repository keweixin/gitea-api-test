# 自动化覆盖说明

## 一、文档定位

本文件用于说明项目当前已经完成的自动化覆盖范围、接口操作数量和测试组织方式，重点体现项目在接口自动化测试方面的实际完成度。

## 二、整体覆盖结果

当前项目共实现 **24 条自动化测试用例**，真实覆盖 **22 个接口操作**，覆盖以下三类核心业务模块：

- 用户模块
- 仓库模块
- Issue 模块

此外，项目还完成了以下能力落地：

- YAML 数据驱动测试
- MySQL 数据库一致性校验
- pytest marker 分组执行
- pytest HTML 报告与 Allure 报告生成

## 三、模块覆盖情况

### 1. 用户模块

对应文件：

- `testcases/test_user.py`

当前已覆盖场景：

1. 获取当前用户信息成功
2. 获取当前用户仓库列表成功
3. 获取公开用户信息成功
4. 获取公开用户仓库列表成功
5. 无 token 获取当前用户失败
6. 非法 token 获取当前用户失败
7. 当前用户查询 smoke 场景

### 2. 仓库模块

对应文件：

- `testcases/test_repo.py`

当前已覆盖场景：

1. 创建仓库成功
2. 仓库名为空创建失败
3. 仓库名重复创建失败
4. 查询仓库详情成功
5. 修改仓库描述成功
6. 删除仓库成功
7. 查询仓库语言统计成功
8. 查询仓库协作者列表成功
9. 创建仓库后数据库校验成功
10. 查询仓库详情 smoke 场景

### 3. Issue 模块

对应文件：

- `testcases/test_issue.py`

当前已覆盖场景：

1. 创建 Issue 成功
2. 标题为空创建 Issue 失败
3. 查询 Issue 列表成功
4. 查询 Issue 详情成功
5. 查询仓库标签列表成功
6. 关闭 Issue 成功
7. Issue 标签生命周期测试成功
8. 关闭 Issue 后数据库校验成功
9. 关闭 Issue smoke 场景

## 四、接口操作覆盖明细

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

## 五、测试组织方式

当前项目采用以下组织方式：

- 通过 YAML 文件管理测试数据
- 通过 fixture 管理测试前置与清理逻辑
- 通过 marker 实现 `smoke`、`db`、`repo`、`issue`、`auth` 分组执行
- 通过命令生成 pytest HTML 报告和 Allure 报告

## 六、结论

从实际覆盖结果来看，当前项目已经具备较完整的小型接口自动化测试项目形态，既能够体现接口覆盖能力，也能够体现测试结构设计、数据库校验和结果展示能力。
