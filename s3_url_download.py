import boto3
s = input()
name_bucket = s.split("/")[-2]
file = s.split("/")[-1]
print(name_bucket, file)
session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    aws_access_key_id="YCAJETm0Cj5ftlR3IOAv9hhAq",
    aws_secret_access_key="YCMAtuRj6TthPwI7u5THqgnmMPeNFFmSB4kVxPYJ",
    endpoint_url='https://storage.yandexcloud.net'
)


s3.download_file(Bucket='24hours', Key='test_offer_clients.csv', Filename='test_offer_clients.csv')
get_object_response = s3.get_object(Bucket=name_bucket,Key=file)
print(get_object_response)
