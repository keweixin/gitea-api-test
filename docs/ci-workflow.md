# CI 工作流说明

## 目标

本项目通过 GitHub Actions 在每次 `push` 和 `pull_request` 时自动完成接口自动化回归，确保代码提交后能够被持续验证。

## 关键文件

- 工作流文件：`.github/workflows/ci.yml`
- 服务编排文件：`docker-compose.yml`

## 执行流程

1. 拉取仓库代码。
2. 安装 Python 依赖与 Allure CLI。
3. 使用 Docker Compose 启动 MySQL 与 Gitea。
4. 等待 Gitea 服务可用。
5. 自动初始化测试用户与基础仓库。
6. 执行 pytest 自动化测试。
7. 生成并上传 pytest HTML 报告与 Allure 报告。
8. 失败时输出容器日志，最后统一清理容器。

## 输出结果

- `pytest-report`：包含 `reports/pytest-report.html`
- `allure-report`：Allure HTML 报告目录

## 价值

CI 让项目具备持续验证能力，不依赖本地手工执行。面试场景下可直接通过 Actions 运行历史和报告产物展示自动化测试成果。
