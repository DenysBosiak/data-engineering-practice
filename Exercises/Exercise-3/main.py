import boto3
import configparser
import io


S3_BUCKET = 'commoncrawl'
KEY = 'crawl-data/CC-MAIN-2022-05/wet.paths.gz'
LOCAL_FILENAME = './wet_paths.gz'

parser = configparser.ConfigParser()
parser.read("aws_config.conf")
AWS_KEY = parser.get("aws_boto_credentials", "aws_access_key_id")
SECRET_KEY = parser.get("aws_boto_credentials", "aws_secret_access_key")


def main():

    def download_file_from_s3(bucket_name, key, filename):
        s3_client = boto3.client('s3',
                                 aws_access_key_id=AWS_KEY,
                                 aws_secret_access_key=SECRET_KEY)
        try:
            s3_client.download_file(Bucket=bucket_name,
                                    Key=key,
                                    Filename=filename)
            print(f"File downloaded successfully to {filename}")
        except Exception as e:
            print(f"Error encountered: {e}")

            
    download_file_from_s3(bucket_name=S3_BUCKET,
                          key=KEY,
                          filename=LOCAL_FILENAME)


if __name__ == "__main__":
    main()
