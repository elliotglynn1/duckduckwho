from pyspark.sql.types import (
    IntegerType,
    StringType,
    FloatType,
    BooleanType,
    StructType,
    StructField
)
from pyspark.sql import SparkSession
from pyspark.sql.dataframe import DataFrame
from typing import List

class Birds:
    schema = StructType([
        StructField("species_code", StringType(), True),
        StructField("common_name", StringType(), True),
        StructField("scientific_name", StringType(), True),
        StructField("location_id", StringType(), True),
        StructField("location_name", StringType(), True),
        StructField("observation_date", StringType(), True),
        StructField("how_many", IntegerType(), True),
        StructField("latitude", FloatType(), True),
        StructField("longitude", FloatType(), True),
        StructField("observation_valid", BooleanType(), True),
        StructField("observation_reviewed", BooleanType(), True),
        StructField("location_private", BooleanType(), True),
        StructField("subspecies_id", StringType(), True),
    ])

    def __init__(self, dataframe: DataFrame):
        if dataframe.schema != self.schema:
            raise ValueError("Dataframe schema does not match bird schema")
        self.dataframe = dataframe

    @classmethod
    def from_ebird_response(cls, ebird_data: List[dict]):

        key_map = {
            'speciesCode': 'species_code',
            'comName': 'common_name',
            'sciName': 'scientific_name',
            'locId': 'location_id',
            'locName': 'location_name',
            'obsDt': 'observation_date',
            'howMany': 'how_many',
            'lat': 'latitude',
            'lng': 'longitude',
            'obsValid': 'observation_valid',
            'obsReviewed': 'observation_reviewed',
            'locationPrivate': 'location_private',
            'subId': 'subspecies_id',
        }

        # Transform data to use final column names directly, ensuring all fields exist
        normalized_data = [
            {key_map[orig_key]: bird.get(orig_key, None) for orig_key in key_map}
            for bird in ebird_data
        ]

        spark = (
            SparkSession.builder
            .appName("Bird")
            .config("spark.sql.execution.pyspark.udf.faulthandler.enabled", "true")
            .config("spark.python.worker.faulthandler.enabled", "true")
            .getOrCreate()
        )

        # Create DataFrame with final schema directly - no renaming or casting needed!
        df = spark.createDataFrame(normalized_data, schema=cls.schema)

        return cls(df)
