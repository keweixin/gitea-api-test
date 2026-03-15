# Gitea 接口自动化测试项目

[![CI](https://github.com/keweixin/gitea-api-test/actions/workflows/ci.yml/badge.svg)](https://github.com/keweixin/gitea-api-test/actions/workflows/ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.11+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> 基于 Python + pytest 构建的 Gitea 接口自动化测试项目，覆盖用户、仓库、Issue 三个核心模块，包含数据驱动、数据库一致性校验、报告生成与 CI 持续验证能力。

## 项目概述

本项目以 Gitea 真实业务接口为测试对象，围绕用户信息、仓库管理、Issue 与标签管理等核心场景，搭建了一套可运行、可扩展、可展示的接口自动化测试框架。项目目标不是简单验证状态码，而是通过分层设计、数据驱动、数据库校验和持续集成，完整体现接口自动化测试项目的落地过程。

## 项目亮点

- 分层设计清晰：拆分为配置层、请求层、API 封装层、测试层和数据层，便于维护与扩展。
- 数据驱动测试：使用 YAML 维护测试数据，减少重复代码，便于新增场景。
- 数据库一致性校验：通过 PyMySQL 验证关键业务动作是否真正落库。
- 报告输出完整：支持 pytest HTML 报告与 Allure 报告。
- CI 持续验证：接入 GitHub Actions，提交后自动完成环境启动、测试执行与报告产物上传。

## 当前成果

- 34 条自动化测试用例
- 22 个真实接口操作覆盖
- 3 个核心业务模块覆盖
- 2 条数据库一致性校验
- 支持 `smoke`、`db`、`auth`、`repo`、`issue` 等 marker 分组执行

## 技术栈

- Python
- pytest
- requests
- PyYAML
- PyMySQL
- python-dotenv
- pytest-html
- allure-pytest
- Docker Compose
- GitHub Actions

## 项目结构

```text
gitea-api-test/
├─ api/                  # 业务接口封装层
├─ common/               # 配置、请求封装、数据库工具
├─ data/                 # YAML 测试数据
├─ docs/                 # 项目说明文档
├─ reports/              # pytest HTML 报告
├─ testcases/            # pytest 测试用例
├─ utils/                # 工具方法
├─ conftest.py           # 公共 fixture
├─ pytest.ini            # pytest 标记配置
├─ docker-compose.yml    # Gitea + MySQL 本地环境
├─ requirements.txt      # 项目依赖
├─ .env.example          # 环境变量模板
└─ README.md
```

## 快速开始

```bash
git clone https://github.com/keweixin/gitea-api-test.git
cd gitea-api-test
pip install -r requirements.txt
docker-compose up -d
cp .env.example .env
pytest -v
```

访问 `http://localhost:3000` 完成 Gitea 初始化。默认管理员账号为 `admin_user`，密码为 `Admin123456`。

## 测试执行

执行全部测试：

```bash
pytest -v
```

执行核心 smoke 场景：

```bash
pytest -m smoke -v
```

执行数据库校验场景：

```bash
pytest -m db -v
```

## 报告生成

生成 pytest HTML 报告与 Allure 原始结果：

```bash
pytest -v --html=reports/pytest-report.html --self-contained-html --alluredir=allure-results
```

生成 Allure HTML 报告：

```bash
allure generate allure-results -o allure-report --clean
```

## 文档索引

- [文档说明总览](docs/README.md)
- [自动化覆盖说明](docs/automation-coverage.md)
- [数据库校验说明](docs/db-validation.md)
- [项目亮点总结](docs/project-highlights.md)
- [Allure 报告说明](docs/allure-report-guide.md)
- [CI 工作流说明](docs/ci-workflow.md)

## 项目价值

本项目已经具备较完整的小型接口自动化测试项目形态，能够体现接口自动化测试在分层设计、数据驱动、数据库校验、结果展示和持续集成方面的综合能力，适合作为自动化测试/测试开发方向的项目实践案例。
