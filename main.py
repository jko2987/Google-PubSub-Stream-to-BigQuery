"""Push Pub / Sub message to BigQuery."""

import base64
import datetime
import json
from google.cloud import bigquery
dataset_id = "your-gcp-project.your-dataset"


def record_event_to_bq(event, context):
  """Triggered from a message on a Cloud Pub/Sub topic."""

  # retrieve attributes

   # current time
  ts = datetime.datetime.now()
  ts_string = str(ts)

  # retrieve message id
  message_id = context.event_id

  # retrieve and decode data from message
  data = event["data"]
  json_string = base64.urlsafe_b64decode(data)
  print("The json_string is: ", str(json_string))

  msg_data = json.loads(json_string)
  print(str(msg_data))

  # populate test table
  rows_to_insert = [{
    "Column1-BigQuery": msg_data["Column1-PubSub-message"],
    "Column2-BigQuery": msg_data["Column2-PubSub-message"],
    "Column3-BigQuery": msg_data["Column3-PubSub-message"],
    "etc-BigQuery": msg_data["etc-PubSub-message"],
  }]

  table_id = "your-table-name"

  # attempt insert of data into BigQuery
  client = bigquery.Client()
  table = client.get_table(dataset_id + "." + table_id)
  errors = client.insert_rows(table, rows_to_insert)

  if errors == []:
    # no errors! success, do something
    print("success")
  else:
    # errors!
    print(errors)
