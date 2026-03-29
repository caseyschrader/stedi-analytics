import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node trainer_landing
trainer_landing_node1774728618186 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="step_trainer_landing", transformation_ctx="trainer_landing_node1774728618186")

# Script generated for node customer_curated
customer_curated_node1774728611013 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="customer_curated", transformation_ctx="customer_curated_node1774728611013")

# Script generated for node SQL Query
SqlQuery0 = '''
select t.* from trainer t
join customer c on c.serialNumber = t.serialNumber
'''
SQLQuery_node1774728630713 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"trainer":trainer_landing_node1774728618186, "customer":customer_curated_node1774728611013}, transformation_ctx = "SQLQuery_node1774728630713")

# Script generated for node step_trainer_trusted
EvaluateDataQuality().process_rows(frame=SQLQuery_node1774728630713, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1774728318934", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
step_trainer_trusted_node1774728633361 = glueContext.getSink(path="s3://casey-schrader2/step_trainer/trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="step_trainer_trusted_node1774728633361")
step_trainer_trusted_node1774728633361.setCatalogInfo(catalogDatabase="stedi",catalogTableName="step_trainer_trusted")
step_trainer_trusted_node1774728633361.setFormat("json")
step_trainer_trusted_node1774728633361.writeFrame(SQLQuery_node1774728630713)
job.commit()