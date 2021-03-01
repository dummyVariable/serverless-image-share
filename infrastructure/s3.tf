resource "aws_s3_bucket" "lolserverless" {
	bucket = "lolserverless"
}

resource "aws_s3_bucket_public_access_block" "lolserverless-access" {
	bucket = aws_s3_bucket.lolserverless.id

	block_public_acls = false
	block_public_policy = false
}

resource "aws_s3_bucket_notification" "lolserverless-notification" {
 	bucket = aws_s3_bucket.lolserverless.id
	
	lambda_function {
	  lambda_function_arn = var.lambda_arn
	  events = [ "s3:ObjectCreated:*" ]
	  filter_prefix = "full/"
	}
	
	depends_on = [aws_lambda_permission.allow_bucket]
}

resource "aws_lambda_permission" "allow_bucket" {
	
	statement_id  = "AllowExecutionFromS3Bucket"
	action        = "lambda:InvokeFunction"
	function_name = var.lambda_name
	principal     = "s3.amazonaws.com"
	source_arn    = aws_s3_bucket.lolserverless.arn

}

resource "aws_s3_bucket" "sam_bucket" {
	bucket = "sambucketimageshare"
}

resource "aws_s3_bucket_public_access_block" "sam_bucket_access" {
	bucket = aws_s3_bucket.sam_bucket

	block_public_acls = false
	block_public_policy = false
}

output "lolserverless_endpoint" {
  description = "S3 domain name"
  value = aws_s3_bucket.lolserverless.bucket_domain_name
}

output "sam_bucket_endpoint" {
  description = "SAM bucket domain name"
  value = aws_s3_bucket.sam_bucket.bucket_domain_name
}