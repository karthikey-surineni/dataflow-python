locals {
    table_staging   = ["ATest","BTest"]
    table_store     = ["ATest","BTest"]
    reject          = ["Reject"]
}

provider "google" {
#   credentials = "${file("${var.credentials}")}"
  project     = "${var.project}"
  region      = "${var.region}"
}

module "ADataset-staging" {
    source              = "./BigQuery"
    dataset_id          = "ADataset_Staging"
    friendly_name       = "ADataset Staging"
    description         = "ADataset Staging dataset"
    location            = "${var.region}"
    tables              = local.table_staging
    # is_staging          = true
}

module "BDataset-staging" {
    source              = "./BigQuery"
    dataset_id          = "BDataset_Staging"
    friendly_name       = "BDataset Staging"
    description         = "BDataset Staging dataset"
    location            = "${var.region}"
    tables              = local.table_staging
    # is_staging          = true
}

module "ADataset-store" {
    source              = "./BigQuery"
    dataset_id          = "ADataset_Store"
    friendly_name       = "ADataset Store"
    description         = "ADataset Store dataset"
    location            = "${var.region}"
    tables              = local.table_store
    # is_staging          = false
}

module "Reject" {
    source              = "./BigQuery"
    dataset_id          = "Common"
    friendly_name       = "Common dataset"
    description         = "Common dataset"
    location            = "${var.region}"
    tables              = local.reject
    # is_staging          = false
}

# module "cb-dataflow-store" {

# }