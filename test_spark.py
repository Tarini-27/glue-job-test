# from pyspark import SparkContext
from pyspark.sql import SQLContext
import importlib
import pandas as pd
my_mod = importlib.import_module('sunlife-aman-glue-test')

from pyspark.context import SparkContext

def test_filter_spark_data_frame_by_value():
    # Spark Context initialisation
    # spark_context = SparkContext()
    # sql_context = SQLContext(spark_context)
   
# from awsglue.job import Job

    # glueContext = GlueContext(SparkContext.getOrCreate())

    # datasource0 = glueContext.create_dynamic_frame.from_catalog(database = 'dbcrawler', table_name = 'sunlife-cyber-sec-testtestset_json')


    # Input and output dataframes
    input = my_mod.sql_context.createDataFrame(
        [('charly', 15),
         ('fabien', 18),
         ('sam', 21),
         ('sam', 25),
         ('nick', 19),
         ('nick', 40)],
        ['name', 'age'],
    )
    expected_output = my_mod.sql_context.createDataFrame(
        [('sam', 25),
         ('sam', 21),
         ('nick', 40)],
        ['name', 'age'],
    )
    real_output = my_mod.filter_spark_data_frame(input)
    real_output = get_sorted_data_frame(
        real_output.toPandas(),
        ['age', 'name'],
    )
    expected_output = get_sorted_data_frame(
        expected_output.toPandas(),
        ['age', 'name'],
    )

    # Equality assertion
    
    pd.testing.assert_frame_equal(expected_output,real_output,check_like=True)
    3return real_output.equals(expected_output)
    # Close the Spark Context
    my_mod.spark_context.stop()
    #return result

def get_sorted_data_frame(data_frame, columns_list):
    return data_frame.sort_values(columns_list).reset_index(drop=True)
