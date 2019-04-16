# s3-unique-bucket
Utility to create a unique bucket for each S3 account, useful for deployment scenarios.

Did you ever need a bucket to upload your deployment templates into? Are you always annoyed by having to create them manually, not really making your deployment pipeline truly automatic? Well, worry no more!

This script is an **easy** and **idempotent** way to just create an S3 bucket that will have a very high chance to avoid name conflicts.
If run a second time, the script recognizes the bucket already exists and will only emit the bucket's name for reuse.

## Installation
`pip install s3_unique_bucket`

## Example
````bash
bucket=$(s3_unique_bucket)
aws s3 cp foo.txt s3://$bucket/foo.txt
````

## How it works
The bucket name is generated from a user-settable prefix, the sha1 hash of the account ID with base32 encoding, and the region the bucket is created in.
Then the script checks if a bucket with this name exists on the provided account. If not, it is created. Then finally the name of the bucket is emitted via `stdout`.

## Documentation
Set the AWS credentials and region with environment variables.
* `AWS_ACCESS_KEY_ID`
* `AWS_SECRET_ACCESS_KEY`
* `AWS_DEFAULT_REGION`

The rest is configured with command line arguments.

#### `-p`/`--prefix`: User-settable prefix (OPTIONAL)
**Default**: `account-bucket`

The bucket name starts with this settable prefix. It can also be empty. Note that a dash ('-') is automatically added between the prefix and the hash if prefix is not empty.

#### `-p`/`--prefix`: AWS Account Region (CONDITIONAL)
**Condition**: Must be provided if environment variable `AWS_DEFAULT_REGION` isn't set.

Which region the bucket shall be created in.

