#coding:utf-8
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 批量执行用例并发送邮件附件
def send_mail():

    smtpserver = "smtp.qq.com"
    user = "2194375518@qq.com"
    password = "afaemruaciyweafe"
    sender = "2194375518@qq.com"
    receive = "2194375518@qq.com"
    # receive=["2194375518@qq.com","hhhh"]
    subject = "供应链商家端测试报告"
    content = "<html><h1>附件为本次供应链商家端测试报告结果，请下载查看</h1></html>"

    report_dir = '../reports'
    lists = os.listdir(report_dir)
    # 按照文件名排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    filename = os.path.join(report_dir, lists[-1])

    send_file = open(filename,"rb").read()
    att = MIMEText(send_file, "base64", "utf-8")
    att['Content-Type'] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename="result.html"'
    msgRoot = MIMEMultipart()
    msgRoot.attach(MIMEText(content, 'html', 'utf-8'))
    msgRoot['Subject'] = subject
    msgRoot['From'] = sender
    msgRoot['To'] = "2194375518@qq.com"
    msgRoot.attach(att)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receive, msgRoot.as_string())
    smtp.quit()


if __name__ == "__main__":
    send_mail()




