# 企业贷款评分数据分析项目

这个项目使用Apache Spark对中国企业贷款评分数据进行分析。

## 环境要求

- Python 3.8+
- Apache Spark 3.5.0
- Anaconda环境（包含Spark）

## 安装步骤

1. 确保已安装Anaconda并创建了Spark环境
2. 安装项目依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 项目结构

- `spark_analysis.py`: 主程序文件
- `loan_evaluation.csv`: 企业贷款评分数据集
- `requirements.txt`: 项目依赖文件

## 运行方式

```bash
python spark_analysis.py
```

## 数据分析内容

当前版本包含以下分析：
1. 数据基本信息展示
2. 数据预览
3. 基本统计信息
4. 空值分析

## 注意事项

请确保在运行程序前已正确设置Python解释器路径，当前设置为：
```python
os.environ["PYSPARK_PYTHON"] = r"E:\Tool\Anaconda\envs\Spark\python.exe"
``` 