from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Pap Batch processing").getOrCreate()

# Read batch data from a file
df = spark.read.csv("resources/stocke_invoice.data", header=True, inferSchema=True)
result = df.groupby("UnitPrice").count()
print(df.count())
# result.write.csv("output_batch.csv")


print(df.select('CustomerId').collect())