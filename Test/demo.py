# Databricks notebook source

print("hello")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "select * from"

# COMMAND ----------

# MAGIC %run ./Includes/Setup

# COMMAND ----------

print(var1)

# COMMAND ----------

# MAGIC %fs ls 

# COMMAND ----------

# MAGIC %fs ls 'databricks-datasets'

# COMMAND ----------

dbutils.fs.ls("databricks-datasets")


# COMMAND ----------

files = dbutils.fs.ls("databricks-datasets")
print(files)

# COMMAND ----------

display(files)
