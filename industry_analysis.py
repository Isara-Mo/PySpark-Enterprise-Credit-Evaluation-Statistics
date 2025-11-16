import os
import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count, desc
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False 
#plt.rcParams.update({'font.size': 10}) # 设置字体大小
# 设置Python解释器路径
os.environ["PYSPARK_PYTHON"] = r"E:\Tool\Anaconda\envs\Spark\python.exe"

# 创建Spark会话
spark = SparkSession.builder \
    .appName("行业贷款评分分析") \
    .getOrCreate()

# 读取数据
df = spark.read.csv("loan_evaluation.csv", header=True, inferSchema=True)

# 显示数据集的列名
print("数据集列名：")
df.printSchema()

# 1. 各行业贷款数量分布
industry_counts = df.groupBy("行业名称") \
    .count() \
    .orderBy(desc("count")) \
    .limit(10) \
    .toPandas()

plt.figure(figsize=(12, 6))
sns.barplot(data=industry_counts, x="行业名称", y="count")
plt.title("前10大行业贷款数量分布")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("industry_counts.png")
plt.close()

# 2. 各行业平均评分
industry_avg_score = df.groupBy("行业名称") \
    .agg(avg("评分").alias("avg_score")) \
    .orderBy(desc("avg_score")) \
    .limit(10) \
    .toPandas()

plt.figure(figsize=(12, 6))
sns.barplot(data=industry_avg_score, x="行业名称", y="avg_score")
plt.title("前10大行业平均评分")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("industry_avg_score.png")
plt.close()

# 3. 行业评分与财务指标的关系
industry_stats = df.groupBy("行业名称") \
    .agg(
        avg("评分").alias("avg_score"),
        avg("资产报酬率").alias("avg_roa"),
        avg("净资产收益率ROE").alias("avg_roe"),
        avg("资产负债率").alias("avg_debt_ratio"),
        count("*").alias("count")
    ) \
    .filter(col("count") > 100) \
    .toPandas()

# 创建行业评分与ROE的散点图
plt.figure(figsize=(15, 10))

# 为每个行业分配不同的颜色
colors = plt.cm.tab20(np.linspace(0, 1, len(industry_stats)))
scatter = plt.scatter(
    industry_stats["avg_roe"],
    industry_stats["avg_score"],
    s=industry_stats["count"]/100,
    alpha=0.6,
    c=colors
)

plt.title("行业ROE与评分关系", fontsize=14)
plt.xlabel("平均ROE", fontsize=12)
plt.ylabel("平均评分", fontsize=12)

# 添加图例
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', 
                            markerfacecolor=color, label=industry, 
                            markersize=10, alpha=0.6)
                  for color, industry in zip(colors, industry_stats["行业名称"])]

# 将图例放在图表右侧
plt.legend(handles=legend_elements, 
          title="行业名称",
          bbox_to_anchor=(1.05, 1),
          loc='upper left',
          borderaxespad=0.)

# 调整布局以确保图例完全显示
plt.tight_layout()
plt.savefig("industry_roe_correlation.png", bbox_inches='tight', dpi=300)
plt.close()

# 4. 生成分析报告
report = f"""
行业贷款分析报告
================

1. 贷款数量最多的前5个行业：
{industry_counts.head().to_string()}

2. 平均评分最高的前5个行业：
{industry_avg_score.head().to_string()}

3. 行业特征统计：
- 总行业数量：{len(industry_stats)}
- 评分范围：{industry_stats['avg_score'].min():.2f} - {industry_stats['avg_score'].max():.2f}
- ROE范围：{industry_stats['avg_roe'].min():.2f}% - {industry_stats['avg_roe'].max():.2f}%
- 资产负债率范围：{industry_stats['avg_debt_ratio'].min():.2f}% - {industry_stats['avg_debt_ratio'].max():.2f}%
"""

# 保存报告
with open("industry_analysis_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

# 停止Spark会话
spark.stop()