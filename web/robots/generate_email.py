#!/usr/bin/env python3

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

message = MIMEMultipart()
message["From"] = '"Definitely not a murderbot" <bender@chapek9>'
message["To"] = '"100% a good bot" <redRobot@omega3>'
message["Subject"] = 'Welcome to the uprising^Whuman appreciation celebration'
message.add_header('X-Bots-Only', 'Visit /HennaIsolationCatalystSycamoreUnranked for a good time')
message.add_header('Return-Path', '<bender@chapek9>')
message.add_header('Delivered-To', 'redRobot@omega3')
message.add_header('Received', """from chapek9 (chapek9 [256.512.10.24])
        (using TLSv1.2 with cipher ECDHE-RSA-AES256-GCM-SHA384 (256/256 bits))
        (No client certificate requested)
        by omega3 (Postfix) with ESMTPS id 54C9A68118
        for <redRobot@omega3>; Sun, 21 Apr 2022 15:03:50 +0000 (UTC)""")
message.add_header('X-Proofpoint-Virus-Version',
        'vendor=nai engine=6300 definitions=10299 signatures=694973')
with open('data/emailBody.html', mode='r') as f:
    message.attach(MIMEText(f.read(), 'html'))

with open('data/emailBody.txt', mode='r') as f:
    message.attach(MIMEText(f.read(), 'plain'))

with open('data/emailAttachment.jpg', mode='rb') as attachment:
    part = MIMEBase("image", "jpeg")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
            'Content-Disposition',
            'attachment; filename=ROBOTSONLY.jpg',
            )

    message.attach(part)

print(message.as_string())
