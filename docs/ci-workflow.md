# CI 工作流说明

## 文档定位

本文档用于说明项目如何通过 GitHub Actions 自动执行接口自动化测试，并输出测试报告，体现项目的持续验证能力。

## 关键文件

- 工作流文件：`.github/workflows/ci.yml`
- 服务编排文件：`docker-compose.yml`

## 执行流程

当前 CI 工作流会自动完成以下步骤：

1. 拉取仓库代码
2. 安装 Python 依赖与 Allure CLI
3. 使用 Docker Compose 启动 MySQL 与 Gitea
4. 等待 Gitea 服务可用
5. 初始化测试用户和基础仓库
6. 执行 pytest 自动化测试
7. 生成并上传 pytest HTML 报告与 Allure 报告
8. 失败时输出容器日志并在结束后清理环境

## 输出结果

当前 CI 会上传两类产物：

- `pytest-report`：包含 `reports/pytest-report.html`
- `allure-report`：Allure HTML 报告目录

## 项目价值

CI 让项目具备了持续验证能力。每次代码提交后，都可以自动完成环境准备、测试执行和报告输出，不依赖本地手工运行。这部分能力能够更直接地体现项目的工程化程度。
