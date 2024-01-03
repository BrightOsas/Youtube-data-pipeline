provider "aws" {
  region = "eu-west-1"

}

resource "aws_s3_bucket" "youtubes3bucket" {
  bucket = "brightyoutubes3"

}