import os
import findspark
findspark.init()

# 指定python解释器路径
os.environ["PYSPARK_PYTHON"] = r"E:\Tool\Anaconda\envs\Spark\python.exe"

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# 创建SparkSession
spark = SparkSession.builder \
    .appName("企业贷款评分分析") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# 读取数据
df = spark.read.csv("loan_evaluation.csv", header=True, inferSchema=True)

# 显示数据基本信息
print("数据集基本信息：")
df.printSchema()
print("\n数据预览：")
df.show(5)

# 基本统计信息
print("\n基本统计信息：")
df.describe().show()

# 计算各列的空值数量
print("\n各列空值数量：")
null_counts = df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns])
null_counts.show()

# 停止SparkSession
spark.stop() 