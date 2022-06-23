import hashlib
from pyspark.sql.functions import substring, udf, StringType

def generated(column):
    hashColumn = str(column).strip()[0:3]
    hashColumnSha256 = hashlib.sha256(str(hashColumn).encode()).hexdigest()
    hashColumnMd5 = hashlib.md5(str(hashColumn + hashColumnSha256 + hashColumn).encode('utf-16')).hexdigest()
    return hashColumnMd5

def generateColumn(column):
    hashFinal = udf_func(column)
    return hashFinal


udf_func = udf(lambda x: Hash.generated(x), returnType=StringType())