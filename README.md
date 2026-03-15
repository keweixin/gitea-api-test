# Gitea 开源 Git 服务接口自动化测试框架（Python + pytest）

> 覆盖用户/仓库/Issue 核心模块，支持数据驱动、数据库一致性校验、Allure 可视化报告

## 快速开始

```bash
# 1. 克隆项目
git clone https://github.com/keweixin/gitea-api-test.git
cd gitea-api-test

# 2. 安装依赖
pip install -r requirements.txt

# 3. 启动 Gitea 服务
docker-compose -f .github/ci/docker-compose.yml up -d

# 4. 配置环境变量
cp .env.example .env
# 编辑 .env 填入你的 Gitea 地址和 Token

# 5. 运行测试
pytest -v
```

访问 http://localhost:3000 完成 Gitea 初始化，默认管理员账号：`admin_user` / `Admin123456`

## 项目亮点

- **分层架构设计**：API 层、测试层、数据层、工具层分离，代码结构清晰易维护
- **数据驱动测试**：使用 YAML 文件管理测试数据，测试用例与数据解耦
- **数据库一致性校验**：PyMySQL 直连数据库，验证接口返回与落库数据一致
- **可视化报告**：集成 Allure + pytest-html，支持测试趋势分析和详细错误追踪
- **CI/CD 集成**：GitHub Actions 自动触发测试，一键生成测试报告
- **Docker 一键启动**：docker-compose 快速搭建 Gitea + MySQL 测试环境
- **灵活的测试分组**：支持 smoke、db、user、repo、issue 等 marker 精确控制测试范围
- **完整的测试覆盖**：22 个真实接口覆盖，包含正向和异常场景

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

## 接口覆盖矩阵

| 序号 | 模块 | 接口路径 | 方法 | 正向用例 | 负向用例 |
|:---:|:---:|:---|:---:|:---:|:---:|
| 1 | 用户 | /user | GET | ✅ | - |
| 2 | 用户 | /user/repos | GET | ✅ | - |
| 3 | 用户 | /users/{username} | GET | ✅ | ✅ |
| 4 | 用户 | /users/{username}/repos | GET | ✅ | - |
| 5 | 仓库 | /user/repos | POST | ✅ | ✅ |
| 6 | 仓库 | /repos/{owner}/{repo} | GET | ✅ | ✅ |
| 7 | 仓库 | /repos/{owner}/{repo} | PATCH | ✅ | ✅ |
| 8 | 仓库 | /repos/{owner}/{repo} | DELETE | ✅ | ✅ |
| 9 | 仓库 | /repos/{owner}/{repo}/languages | GET | ✅ | - |
| 10 | 仓库 | /repos/{owner}/{repo}/collaborators | GET | ✅ | - |
| 11 | Issue | /repos/{owner}/{repo}/issues | POST | ✅ | ✅ |
| 12 | Issue | /repos/{owner}/{repo}/issues | GET | ✅ | - |
| 13 | Issue | /repos/{owner}/{repo}/issues/{index} | GET | ✅ | ✅ |
| 14 | Issue | /repos/{owner}/{repo}/issues/{index} | PATCH | ✅ | ✅ |
| 15 | Issue | /repos/{owner}/{repo}/labels | GET | ✅ | - |
| 16 | Issue | /repos/{owner}/{repo}/labels | POST | ✅ | ✅ |
| 17 | Issue | /repos/{owner}/{repo}/labels/{id} | GET | ✅ | - |
| 18 | Issue | /repos/{owner}/{repo}/labels/{id} | DELETE | ✅ | ✅ |
| 19 | Issue | /repos/{owner}/{repo}/issues/{index}/labels | POST | ✅ | - |
| 20 | Issue | /repos/{owner}/{repo}/issues/{index}/labels | GET | ✅ | - |
| 21 | Issue | /repos/{owner}/{repo}/issues/{index}/labels | PUT | ✅ | - |
| 22 | Issue | /repos/{owner}/{repo}/issues/{index}/labels | DELETE | ✅ | - |

**总计**：22 个接口 | 24 个正向用例 | 12+ 个负向用例

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
