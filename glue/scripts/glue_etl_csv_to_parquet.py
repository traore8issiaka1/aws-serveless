import sys
from awsglue.transforms  import *
from awsglue.utils       import getResolvedOptions
from pyspark.context      import SparkContext
from awsglue.context      import GlueContext
from awsglue.job          import Job
from awsglue.dynamicframe import DynamicFrame

args        = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc          = SparkContext()
glueContext = GlueContext(sc)
spark       = glueContext.spark_session
job         = Job(glueContext)
job.init(args["JOB_NAME"], args)

S3_BUCKET      = "your-bucket-name"
DATABASE_NAME  = "telecom_db"
TABLE_CSV      = "telecom"
S3_PARQUET_OUT = f"s3://{S3_BUCKET}/telecom-parquet/"

datasource = glueContext.create_dynamic_frame.from_catalog(
    database=DATABASE_NAME, table_name=TABLE_CSV)

glueContext.write_dynamic_frame.from_options(
    frame=datasource,
    connection_type="s3",
    connection_options={"path": S3_PARQUET_OUT, "partitionKeys": ["pays"]},
    format="parquet",
    format_options={"compression": "snappy"}
)
print(f"Conversion terminee : {S3_PARQUET_OUT}")
job.commit()
