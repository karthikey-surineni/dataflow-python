variable "dataset_id" {
  type = string
}

variable "friendly_name" {
    type = string
}

variable "description" {
    type = string
}

variable "location" {
    type = string
    default = ""
}

variable "tables" {
    type = list
    default = []
}

variable "is_staging" {
    type = string
    default = ""
}