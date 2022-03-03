# Google-PubSub-Stream-to-BigQuery
Stream messages from Google PubSub to Google BigQuery


This code was created to be a Google Cloud Function to stream messages from Google Cloud PubSub and insert as a row into a BigQuery table

Change the following for your use
  - dataset_id variable to "your-gcp-project.your-dataset"
  - Change the rows_to_insert variable to match your BigQuery table columns on the left and your Google Cloud PubSub messages on the right
  - table_id to your destination table in BigQuery
