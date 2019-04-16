"""Create a repeatably-unique S3 bucket on your AWS account.

Create a unique bucket for your S3 account without much effort. The bucket name is constructed from an user-settable
prefix, the sha256 hash of the account ID and the region the bucket is created in. That way a bucket name with very
low probability of collision is chosen.
"""

import boto3
import hashlib
import base64
import argparse
import sys
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--prefix", default="account-bucket", help="Prefix of bucket name", type=str,
                        required=False)
    if os.getenv("AWS_DEFAULT_REGION") is not None:
        parser.add_argument("-r", "--region", default=os.environ["AWS_DEFAULT_REGION"], help="Prefix of bucket name",
                            type=str, required=False)
    else:
        parser.add_argument("-r", "--region", help="Prefix of bucket name", type=str, required=True)

    args = parser.parse_args()

    # Collect required information
    account_id: str = boto3.client("sts").get_caller_identity().get("Account")
    account_hash: str = base64.b32encode(hashlib.sha1(account_id.encode()).digest()).decode()  # Generate sh256 hash
    account_hash = account_hash.lower().replace("=", "")  # Remove padding symbols             # and encode as base32

    region: str = args.region

    bucket_name: str = f"{args.prefix}{'-' if args.prefix else ''}{account_hash}-{region}"

    # Check if bucket already exists
    s3_resource = boto3.resource("s3", region_name=region)
    s3_bucket = s3_resource.Bucket(bucket_name)
    if not s3_bucket.creation_date:  # If creation date is set, bucket exists
        print(f"Bucket '{bucket_name}' does not exist. Creating...", file=sys.stderr)
        s3_bucket.create(CreateBucketConfiguration={
            "LocationConstraint": region
        })

    print(bucket_name)  # Finally print bucket name so it can be used in other places


if __name__ == "__main__":
    main()
