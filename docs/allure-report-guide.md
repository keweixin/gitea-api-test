# Allure 报告说明

## 一、文档定位

本文件用于说明项目的测试报告生成方式与展示结果，重点体现项目在测试结果可视化方面的能力。

## 二、当前已实现的报告能力

当前项目已实现两类报告输出：

1. pytest HTML 报告
2. Allure 测试报告

对应生成结果包括：

- `reports/pytest-report.html`
- `allure-results/`
- `allure-report/`

## 三、生成方式

### 1. 生成 pytest HTML 报告和 Allure 原始结果

```bash
pytest -v --html=reports/pytest-report.html --self-contained-html --alluredir=allure-results
```

### 2. 生成 Allure HTML 报告

```bash
allure generate allure-results -o allure-report --clean
```

### 3. 打开 Allure 报告

```bash
allure open allure-report
```

## 四、报告展示内容

当前报告输出能够展示以下信息：

- 测试总数
- 通过结果
- 用例明细
- 测试执行结果的可视化页面

## 五、结论

通过 HTML 报告和 Allure 报告输出，项目已经具备完整的测试结果展示能力。这部分内容能够直接用于 GitHub 展示、项目答辩和面试说明。
