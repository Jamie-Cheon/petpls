import boto3
from botocore.exceptions import ClientError
from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

User = get_user_model()


def send_email_as_html(receiver, title, html, params):
    CHARSET = "UTF-8"
    from_email = 'PETPLS <info@petpls.ca>'
    boto3.setup_default_session(
        aws_access_key_id=settings.SES_KEY_ID,
        aws_secret_access_key=settings.SES_SECRET_KEY,
        region_name=settings.SES_REGION
    )
    client = boto3.client('ses')
    body = render_to_string(html, params)

    try:
        if type(receiver) == list:
            response = client.send_email(
                Destination={
                    'ToAddresses': receiver,
                },
                Message={
                    'Subject': {'Charset': CHARSET, 'Data': title},
                    'Body': {
                        'Html': {'Charset': CHARSET, 'Data': body}
                    },
                },
                Source=from_email,
            )
        else:
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        receiver,
                    ],
                },
                Message={
                    'Subject': {'Charset': CHARSET, 'Data': title},
                    'Body': {
                        'Html': {'Charset': CHARSET, 'Data': body}
                    },
                },
                Source=from_email,
            )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['ResponseMetadata']['RequestId'])

