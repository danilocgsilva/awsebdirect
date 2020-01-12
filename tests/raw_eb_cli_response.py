import datetime


raw_eb_cli_response =     {
    "Environments": [
        {
            "EnvironmentName": "ebtestesp-danilocgsilva",
            "EnvironmentId": "e-pcvgx6jgjy",
            "ApplicationName": "ebtestesp",
            "VersionLabel": "app-200112_105058",
            "SolutionStackName": "64bit Amazon Linux 2018.03 v2.9.1 running PHP 7.3",
            "PlatformArn": "arn:aws:elasticbeanstalk:sa-east-1::platform/PHP 7.3 running on 64bit Amazon Linux/2.9.1",
            "Description": "Environment created from the EB CLI using \"eb create\"",
            "EndpointURL": "awseb-e-p-AWSEBLoa-12OEZMYUMZXKZ-1976166717.sa-east-1.elb.amazonaws.com",
            "CNAME": "ebtestesp-danilocgsilva.5nwpruwrwk.sa-east-1.elasticbeanstalk.com",
            "DateCreated": datetime.datetime(2020, 1, 12, 13, 51, 2),
            "DateUpdated": datetime.datetime(2020, 1, 12, 13, 53, 15),
            "Status": "Ready",
            "AbortableOperationInProgress": False,
            "Health": "Green",
            "HealthStatus": "Ok",
            "Tier": {
                "Name": "WebServer",
                "Type": "Standard",
                "Version": "1.0"
            },
            "EnvironmentLinks": [],
            "EnvironmentArn": "arn:aws:elasticbeanstalk:sa-east-1:063695957269:environment/ebtestesp/ebtestesp-danilocgsilva"
        }
    ],
    "ResponseMetadata": {
        "RequestId": "0b1184fd-1404-4efc-bba0-459d0bf1bbb3",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "content-type": "text/xml",
            "date": "Sun, 12 Jan 2020 18:06:08 GMT",
            "x-amzn-requestid": "0b1184fd-1404-4efc-bba0-459d0bf1bbb3",
            "content-length": "1771",
            "connection": "keep-alive"
        },
        "RetryAttempts": 0
    }
}