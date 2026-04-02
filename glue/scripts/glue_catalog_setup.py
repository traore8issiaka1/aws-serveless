import boto3

REGION        = "eu-west-1"
DATABASE_NAME = "telecom_db"
TABLE_NAME    = "telecom"
S3_BUCKET     = "your-bucket-name"
S3_PREFIX     = "telecom-data/"

glue = boto3.client("glue", region_name=REGION)

def create_database():
    try:
        glue.create_database(DatabaseInput={"Name": DATABASE_NAME,
            "Description": "Base de donnees transactions telecom"})
        print(f"[OK] Base '{DATABASE_NAME}' creee.")
    except glue.exceptions.AlreadyExistsException:
        print(f"[INFO] Base '{DATABASE_NAME}' existe deja.")

def create_table():
    columns = [
        {"Name": "transaction_id", "Type": "string"},
        {"Name": "msisdn",         "Type": "string"},
        {"Name": "antenne_id",     "Type": "string"},
        {"Name": "pays",           "Type": "string"},
        {"Name": "operateur",      "Type": "string"},
        {"Name": "type_evenement", "Type": "string"},
        {"Name": "statut",         "Type": "string"},
        {"Name": "date_heure",     "Type": "timestamp"},
        {"Name": "duree_secondes", "Type": "int"},
        {"Name": "volume_mb",      "Type": "double"},
        {"Name": "montant_xof",    "Type": "double"},
    ]
    try:
        glue.create_table(
            DatabaseName=DATABASE_NAME,
            TableInput={
                "Name": TABLE_NAME,
                "StorageDescriptor": {
                    "Columns": columns,
                    "Location": f"s3://{S3_BUCKET}/{S3_PREFIX}",
                    "InputFormat":  "org.apache.hadoop.mapred.TextInputFormat",
                    "OutputFormat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat",
                    "SerdeInfo": {
                        "SerializationLibrary": "org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe",
                        "Parameters": {"field.delim": ",", "skip.header.line.count": "1"}
                    },
                },
                "TableType": "EXTERNAL_TABLE",
                "Parameters": {"classification": "csv", "skip.header.line.count": "1"}
            }
        )
        print(f"[OK] Table '{TABLE_NAME}' creee.")
    except glue.exceptions.AlreadyExistsException:
        print(f"[INFO] Table '{TABLE_NAME}' existe deja.")

if __name__ == "__main__":
    create_database()
    create_table()
    print("Setup Glue termine !")
