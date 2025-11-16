# 🚀 Enterprise Loan Analysis System

[📖 中文文档](#-中文文档)

## 📋 Project Overview

This project leverages Apache Spark to perform comprehensive analysis on enterprise loan evaluation data. It provides insights into industry trends, credit assessments, and financial metrics through distributed data processing and visualization.

## ✨ Key Features

- **📊 Data Analysis**: Distributed processing of large-scale enterprise data using Apache Spark
- **📈 Industry Analysis**: Comprehensive analysis of loan distribution and credit scores by industry
- **💡 Financial Metrics**: ROE, ROA, debt-to-asset ratio, and other key financial indicators
- **📊 Visualization**: Beautiful charts and reports for data insights and decision making

## 📦 System Requirements

- **Python**: 3.8 or higher
- **Apache Spark**: 3.4.4 or higher
- **Anaconda**: With Spark environment configured
- **Operating System**: Windows, macOS, or Linux

## 📥 Installation Guide

### Step 1: Prerequisites
Ensure Anaconda is installed and you have a Spark-enabled environment configured.

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure Python Interpreter Path
Update the Python interpreter path in the script files:
```python
os.environ["PYSPARK_PYTHON"] = r"path/to/your/python.exe"
```

## 📂 Project Structure

| File | Description |
|------|-------------|
| `spark_analysis.py` | Main analysis script with basic data statistics and null value checks |
| `industry_analysis.py` | Advanced industry-level analysis with visualizations |
| `loan_evaluation.csv` | Enterprise loan evaluation dataset |
| `requirements.txt` | Project dependencies |
| `industry_analysis_report.txt` | Generated analysis report |

## 🚀 Usage

### Run Basic Analysis
```bash
python spark_analysis.py
```

This script performs:
- Data schema inspection
- Data preview (first 5 records)
- Basic statistical summaries
- Null value analysis

### Run Industry Analysis
```bash
python industry_analysis.py
```

This script generates:
- Loan distribution by industry
- Average credit scores by industry
- Correlation analysis between ROE and credit scores
- Detailed industry statistics report

## 📊 Output Files

- `industry_counts.png` - Bar chart of top 10 industries by loan volume
- `industry_avg_score.png` - Bar chart of top 10 industries by average score
- `industry_roe_correlation.png` - Scatter plot of ROE vs credit scores
- `industry_analysis_report.txt` - Text-based analysis report

## 📋 Data Analysis Workflow

1. Read enterprise loan evaluation data from CSV
2. Parse schema and validate data integrity
3. Perform industry-level aggregations
4. Calculate financial metrics (ROE, ROA, debt ratio)
5. Generate visualizations for key insights
6. Export analysis report

## ⚙️ Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| pyspark | 3.4.4 | Distributed data processing |
| pandas | 2.1.0 | Data manipulation and analysis |
| matplotlib | 3.7.1 | Data visualization |
| seaborn | 0.12.2 | Statistical data visualization |
| numpy | 1.24.3 | Numerical computing |
| findspark | 2.0.1 | Spark initialization |

## ⚠️ Important Notes

- Please ensure the Python interpreter path is correctly configured before running the scripts
- Update the path according to your Anaconda Spark environment location
- The CSV file should be in the same directory as the script files

## 🔧 Troubleshooting

### Issue: Spark not found
**Solution**: Verify findspark is installed and your Spark environment is properly configured.

### Issue: CSV file not found
**Solution**: Ensure `loan_evaluation.csv` is in the same directory as the script files.

### Issue: Out of memory error
**Solution**: Allocate more memory to Spark by configuring the SparkSession.

## 📝 License

This project is open-source and available for educational and commercial use.

## 👥 Contributing

We welcome contributions! Please feel free to submit issues and enhancement requests.

---

<a id="中文文档"></a>

# 🚀 企业贷款分析系统

[📖 English Documentation](#-enterprise-loan-analysis-system)

## 📋 项目概述

本项目利用 Apache Spark 对企业贷款评估数据进行全面分析。通过分布式数据处理和可视化，提供行业趋势、信用评估和财务指标的深入洞察。

## ✨ 主要功能

- **📊 数据分析**: 使用 Apache Spark 进行大规模企业数据的分布式处理
- **📈 行业分析**: 按行业分类的贷款分布和信用评分的全面分析
- **💡 财务指标**: ROE、ROA、资产负债率等关键财务指标分析
- **📊 数据可视化**: 美观的图表和报告，用于洞察数据和决策支持

## 📦 系统要求

- **Python**: 3.8 或更高版本
- **Apache Spark**: 3.4.4 或更高版本
- **Anaconda**: 配置有 Spark 环境
- **操作系统**: Windows、macOS 或 Linux

## 📥 安装指南

### 第一步：前置条件
确保已安装 Anaconda 并配置了 Spark 环境。

### 第二步：安装依赖
```bash
pip install -r requirements.txt
```

### 第三步：配置 Python 解释器路径
在脚本文件中更新 Python 解释器路径：
```python
os.environ["PYSPARK_PYTHON"] = r"path/to/your/python.exe"
```

## 📂 项目结构

| 文件 | 说明 |
|------|------|
| `spark_analysis.py` | 主要分析脚本，包含基本数据统计和空值检查 |
| `industry_analysis.py` | 高级行业级别分析与可视化 |
| `loan_evaluation.csv` | 企业贷款评分数据集 |
| `requirements.txt` | 项目依赖文件 |
| `industry_analysis_report.txt` | 生成的分析报告 |

## 🚀 使用方法

### 运行基础分析
```bash
python spark_analysis.py
```

此脚本执行：
- 数据模式检查
- 数据预览（前 5 条记录）
- 基本统计摘要
- 空值分析

### 运行行业分析
```bash
python industry_analysis.py
```

此脚本生成：
- 按行业的贷款分布
- 按行业的平均信用评分
- ROE 与信用评分的关联分析
- 详细的行业统计报告

## 📊 输出文件

- `industry_counts.png` - 贷款数量最多的前 10 个行业柱状图
- `industry_avg_score.png` - 平均评分最高的前 10 个行业柱状图
- `industry_roe_correlation.png` - ROE 与信用评分的散点图
- `industry_analysis_report.txt` - 文本格式的分析报告

## 📋 数据分析流程

1. 从 CSV 文件读取企业贷款评估数据
2. 解析数据模式并验证数据完整性
3. 执行行业级别的数据聚合
4. 计算财务指标（ROE、ROA、资产负债率）
5. 生成关键洞察的可视化图表
6. 导出分析报告

## ⚙️ 依赖包

| 包名 | 版本 | 用途 |
|------|------|------|
| pyspark | 3.4.4 | 分布式数据处理 |
| pandas | 2.1.0 | 数据操作和分析 |
| matplotlib | 3.7.1 | 数据可视化 |
| seaborn | 0.12.2 | 统计数据可视化 |
| numpy | 1.24.3 | 数值计算 |
| findspark | 2.0.1 | Spark 初始化 |

## ⚠️ 重要提示

- 运行脚本前，请确保 Python 解释器路径配置正确
- 请根据您的 Anaconda Spark 环境位置更新路径
- CSV 数据文件应与脚本文件位于同一目录

## 🔧 故障排除

### 问题：未找到 Spark
**解决方案**: 验证 findspark 已安装，并且 Spark 环境已正确配置。

### 问题：找不到 CSV 文件
**解决方案**: 确保 `loan_evaluation.csv` 与脚本文件在同一目录中。

### 问题：内存不足错误
**解决方案**: 通过配置 SparkSession 为 Spark 分配更多内存。

## 📝 许可证

本项目是开源的，可用于教育和商业用途。

## 👥 贡献

欢迎贡献！请随时提交问题和增强请求。

---

© 2025 Enterprise Loan Analysis System | All Rights Reserved 