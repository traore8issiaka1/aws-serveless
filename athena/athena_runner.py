import boto3, time, os

REGION      = "eu-west-1"
DATABASE    = "telecom_db"
S3_BUCKET   = "your-bucket-name"
S3_OUTPUT   = f"s3://{S3_BUCKET}/athena-results/"
QUERIES_DIR = os.path.join(os.path.dirname(__file__), "queries")

athena = boto3.client("athena", region_name=REGION)

def run_query(sql, name="query"):
    print(f"\n Execution : {name}")
    resp = athena.start_query_execution(
        QueryString=sql,
        QueryExecutionContext={"Database": DATABASE},
        ResultConfiguration={"OutputLocation": S3_OUTPUT}
    )
    eid = resp["QueryExecutionId"]
    while True:
        state = athena.get_query_execution(QueryExecutionId=eid)["QueryExecution"]["Status"]["State"]
        if state in ("SUCCEEDED","FAILED","CANCELLED"): break
        time.sleep(1)
    print(f"   Statut : {state}")

if __name__ == "__main__":
    for f in sorted(os.listdir(QUERIES_DIR)):
        if f.endswith(".sql"):
            run_query(open(os.path.join(QUERIES_DIR, f)).read(), f)
