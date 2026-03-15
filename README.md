# Gitea 接口自动化测试项目

## 项目概述

本项目基于 Gitea 真实业务接口构建，定位为一套可运行、可扩展、可展示的接口自动化测试项目。项目围绕用户、仓库、Issue 三个核心业务模块展开，覆盖接口调用、数据驱动、数据库校验、分组执行以及测试报告生成等关键能力。

## 项目目标

项目重点验证以下内容：

- 用户相关接口的鉴权与信息获取能力
- 仓库相关接口的增删改查与扩展查询能力
- Issue 相关接口的创建、查询、状态流转与标签能力
- 接口返回结果与数据库落库结果的一致性
- 自动化测试结果的可视化输出能力

## 技术栈

- Python
- pytest
- requests
- PyYAML
- PyMySQL
- python-dotenv
- allure-pytest
- pytest-html

## 项目结构

```text
gitea-api-test/
├─ api/                  # 接口封装层
├─ common/               # 配置、请求封装、数据库工具
├─ data/                 # YAML 测试数据
├─ docs/                 # 项目说明文档
├─ reports/              # pytest HTML 报告
├─ testcases/            # pytest 测试用例
├─ utils/                # 工具方法
├─ conftest.py           # 公共 fixture
├─ pytest.ini            # pytest 标记配置
├─ requirements.txt      # 项目依赖
├─ .env.example          # 环境变量模板
└─ README.md
```

## 当前成果

当前项目已完成以下结果：

- 24 条自动化测试用例
- 22 个真实接口操作覆盖
- 3 个核心业务模块覆盖
- 2 条数据库一致性校验
- YAML 数据驱动测试
- pytest marker 分组执行
- pytest HTML 报告与 Allure 报告生成

## 接口覆盖范围

当前真实覆盖的接口操作包括：

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

## 测试执行方式

执行全部自动化测试：

```bash
pytest -v
```

执行数据库校验：

```bash
pytest -m db -v
```

执行核心 smoke 场景：

```bash
pytest -m smoke -v
```

## 报告生成方式

生成 pytest HTML 报告与 Allure 原始结果：

```bash
pytest -v --html=reports/pytest-report.html --self-contained-html --alluredir=allure-results
```

生成 Allure HTML 报告：

```bash
allure generate allure-results -o allure-report --clean
```

打开 Allure 报告：

```bash
allure open allure-report
```

## 文档索引

- [文档说明总览](docs/README.md)
- [自动化覆盖说明](docs/automation-coverage.md)
- [数据库校验说明](docs/db-validation.md)
- [项目亮点总结](docs/project-highlights.md)
- [Allure 报告说明](docs/allure-report-guide.md)
- [Git 提交规范说明](docs/git-commit-guide.md)

## 项目价值

本项目已经具备较完整的自动化测试项目形态：既包含接口分层封装、数据驱动和数据库校验，也包含测试分组执行与报告输出，能够较完整地体现初级自动化测试 / 测试开发岗位所需的项目能力。
