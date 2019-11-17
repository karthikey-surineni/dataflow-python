resource "google_bigquery_dataset" "datasets" {
  dataset_id                  = var.dataset_id
  friendly_name               = var.friendly_name
  description                 = var.description
  location                    = var.location

  labels = {
    env = "default"
  }

}

resource "google_bigquery_table" "tables" {
  dataset_id = "${google_bigquery_dataset.datasets.dataset_id}"
  table_id   = var.tables[count.index]
  labels = {
    env = "default"
  }
  schema    = "${file("${path.module}/schema/${var.dataset_id}-${var.tables[count.index]}.json")}"
  count = length(var.tables)
#   count     = var.is_staging ? length(var.tables) : 0

}

# resource "google_bigquery_table" "store_tables" {
#   dataset_id = "${google_bigquery_dataset.datasets.dataset_id}"
#   table_id   = var.tables[count.index]
#   labels = {
#     env = "default"
#   }
#   schema    = "${file("${path.module}/schema/${var.dataset_id}_Store-${var.tables[count.index]}.json")}"
#   count     = var.is_staging ? 0 : length(var.tables)
# }