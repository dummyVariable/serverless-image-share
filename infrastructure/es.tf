resource "aws_elasticsearch_domain" "es-domain" {

    domain_name = "es-domain"
    elasticsearch_version = "7.4"
    
    cluster_config {
      instance_type = "t3.small.elasticsearch"
      instance_count = 1
      dedicated_master_enabled = false
    }

    ebs_options {
        ebs_enabled = true
        volume_type = "gp2"
        volume_size = 10
    }

    advanced_security_options {
      enabled = true  
      master_user_options {
        master_user_arn = "ARN:USER"
      }
    }

    node_to_node_encryption {
      enabled = true
    }
    encrypt_at_rest {
      enabled = true

    }
    domain_endpoint_options {
      enforce_https = true
      tls_security_policy = "Policy-Min-TLS-1-0-2019-07"
    }
}

resource "aws_elasticsearch_domain_policy" "es-domain-policy" {
  domain_name = aws_elasticsearch_domain.es-domain.domain_name

  access_policies = <<POLICY
    {
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": {
            "AWS": [
            "*"
            ]
        },
        "Action": [
            "es:*"
        ],
        "Resource": "arn:aws:es:REGION:ACC-ID:domain/es-domain/*"
        }
    ]
    }
    POLICY
}


output "es_endpoint" {
  description = "ES endpoint"
  value = aws_elasticsearch_domain.es-domain.endpoint
}