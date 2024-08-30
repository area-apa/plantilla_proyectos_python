from pyspark.conf import SparkConf
class ConfiguracionSpark (SparkConf):
    
        def __init__(self,nombreApp, tipo="bajo"):
            super().__init__()
            
            super().setAppName(nombreApp+"_"+tipo)
            # super().master("local[*]")
            super().set("spark.kerberos.access.hadoopFileSystems", "abfs://data@datalakesii.dfs.core.windows.net")
            super().set("spark.sql.parquet.enableVectorizedReader","false")
            super().set("spark.sql.parquet.int96RebaseModeInRead", "CORRECTED")
            super().set("spark.sql.parquet.int96RebaseModeInWrite", "CORRECTED")
            super().set("spark.sql.parquet.datetimeRebaseModeInRead", "CORRECTED")
            super().set("spark.sql.parquet.datetimeRebaseModeInWrite", "CORRECTED")
            
            if tipo.lower() == 'alto':
                
                super().set("spark.driver.memory" , "8g")
                super().set("spark.executor.memory" , "6g")
                super().set("spark.executor.cores" , "3")
                super().set("spark.executor.instances" , "10")
                super().set("spark.dynamicAllocation.enabled" , "true")
                super().set("spark.dynamicAllocation.maxExecutors" , "10")
                super().set("spark.driver.maxResultSize" , "12g")
            

            elif tipo.lower() == 'medio':
                
                super().set("spark.driver.memory" , "6g")
                super().set("spark.executor.memory" , "4g")
                super().set("spark.executor.cores" , "3")
                super().set("spark.executor.instances" , "10")
                super().set("spark.dynamicAllocation.enabled" , "true")
                super().set("spark.dynamicAllocation.maxExecutors" , "10")
                super().set("spark.driver.maxResultSize" , "12g")
                
            
            elif tipo.lower() == 'bajo':
                
                super().set("spark.driver.memory" , "5g")
                super().set("spark.executor.memory" , "4g")
                super().set("spark.executor.cores" , "3")
                super().set("spark.executor.instances" , "5")
                super().set("spark.dynamicAllocation.enabled" , "true")
                super().set("spark.dynamicAllocation.maxExecutors" , "5")
                super().set("spark.driver.maxResultSize" , "10g")
            
            else:
                super().set("spark.driver.memory" ,"5g")
                super().set("spark.executor.memory", "4g")
                super().set("spark.executor.cores", "2")
                super().set("spark.executor.instances", "1")
                super().set("spark.dynamicAllocation.enabled", "false")
                super().set("spark.driver.maxResultSize", "10g")
