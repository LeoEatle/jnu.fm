
#coding:utf-8
import smtplib  
from email.Message import Message  
from time import sleep  
def sendemail(title,content):
  smtpserver = 'smtp.gmail.com'  
  username = 'beordle@gmail.com'  
  password = '9461135698'  
  from_addr = 'beordle@gmail.com'  
  to_addr = '373866172@qq.com'  
  cc_addr = ''#'huzhenwei@csdn.net'  
        
        
  message = Message()  
  message['Subject'] = title
  message['From'] = from_addr   
  message['To'] = to_addr   
  message['Cc'] = cc_addr   
  message.set_payload(content)    #�ʼ�����   
  msg = message.as_string()  
        
        
  sm = smtplib.SMTP(smtpserver, port=587, timeout=20)  
  sm.set_debuglevel(1)                   #����debugģʽ   
  sm.ehlo()  
  sm.starttls()                          #ʹ�ð�ȫ����   
  sm.ehlo()  
  sm.login(username, password)  
  sm.sendmail(from_addr, to_addr, msg)  
  #sleep(5)                               #�����ʼ�û�з�����ɾ͵�����quit()   
  sm.quit()  

#sendemail("ff","gfgf")