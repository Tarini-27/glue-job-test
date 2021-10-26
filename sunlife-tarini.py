import sys,os
# from awsglue.transforms import Join
# from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SQLContext
# from awsglue.job import Job
# sys.path.append("/root/aws-glue-libs/")
# print(sys.path)
# print(os.environ)
# sc=SparkContext() 
# sc.getConf().getAll()
# print(sc.getConf().getAll())
# glueContext = GlueContext(SparkContext.getOrCreate())
# datasource0 = glueContext.create_dynamic_frame.from_catalog(database = 'dbcrawler', table_name = 'sunlife-cyber-sec-testtestset_json')
# datasource0.printSchema()
## @type: ApplyMapping
## @args: [mapping = [("date", "string", "date", "string"), ("serverid", "string", "serverid", "string"), ("guard_sender", "string", "guard_sender", "string"), ("ruleid", "string", "ruleid", "string"), ("ruledesc", "string", "ruledesc", "string"), ("severity", "string", "severity", "string"), ("devtime", "string", "devtime", "string"), ("servertype", "string", "servertype", "string"), ("classification", "string", "classification", "string"), ("category", "string", "category", "string"), ("dbprotocolversion", "string", "dbprotocolversion", "string"), ("usrname", "string", "usrname", "string"), ("sourceprogram", "string", "sourceprogram", "string"), ("start", "string", "start", "string"), ("dbuser", "string", "dbuser", "string"), ("dst", "string", "dst", "string"), ("dstport", "string", "dstport", "string"), ("src", "string", "src", "string"), ("srcport", "string", "srcport", "string"), ("protocol", "string", "protocol", "string"), ("type", "string", "type", "string"), ("violationid", "string", "violationid", "string"), ("sql", "string", "sql", "string"), ("error", "string", "error", "string"), ("other", "string", "other", "string")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
# applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("date", "string", "date", "string"), ("serverid", "string", "serverid", "string"), ("guard_sender", "string", "guard_sender", "string"), ("ruleid", "string", "ruleid", "string"), ("ruledesc", "string", "ruledesc", "string"), ("severity", "string", "severity", "string"), ("devtime", "string", "devtime", "string"), ("servertype", "string", "servertype", "string"), ("classification", "string", "classification", "string"), ("category", "string", "category", "string"), ("dbprotocolversion", "string", "dbprotocolversion", "string"), ("usrname", "string", "usrname", "string"), ("sourceprogram", "string", "sourceprogram", "string"), ("start", "string", "start", "string"), ("dbuser", "string", "dbuser", "string"), ("dst", "string", "dst", "string"), ("dstport", "string", "dstport", "string"), ("src", "string", "src", "string"), ("srcport", "string", "srcport", "string"), ("protocol", "string", "protocol", "string"), ("type", "string", "type", "string"), ("violationid", "string", "violationid", "string"), ("sql", "string", "sql", "string"), ("error", "string", "error", "string"), ("other", "string", "other", "string")], transformation_ctx = "applymapping1")
# ## @type: DataSink
# ## @args: [connection_type = "s3", connection_options = {"path": "s3://sunlife-cdap-sample/Glue/GlueScript/output"}, format = "json", transformation_ctx = "datasink2"]
# ## @return: datasink2
# ## @inputs: [frame = applymapping1]
# datasink2 = glueContext.write_dynamic_frame.from_options(frame = applymapping1, connection_type = "s3", connection_options = {"path": args['outpath']}, format = "json", transformation_ctx = "datasink2")
# glueContext.write_dynamic_frame.from_options(frame = datasource0,
#           connection_type = "s3",
#           connection_options = {"path": "s3://sunlife-cybersec-test/output-dir/legislator_history"},
#           format = "json")
# # from pyspark import SparkContext
# # from pyspark.sql import HiveContext
# sc = SparkContext()
# SQLContext = HiveContext(sc)
# SQLContext.setConf("spark.sql.hive.convertMetastoreOrc", "false")
# txt = SQLContext.sql( "SELECT 1")
# txt.show(2000000, False)
spark_context = SparkContext()
sql_context = SQLContext(spark_context)
from pyspark.sql.functions import col
def filter_spark_data_frame(
    dataframe,
    column_name='age',
    value=10,
):
    
    return dataframe.where(col(column_name) > value)
