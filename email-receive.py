#!/usr/bin/env python
# coding: utf-8

# In[1]:


import imaplib
import email
mail = imaplib.IMAP4_SSL('imap.gmail.com')
   
mail.login('username', 'password')
   
   
mail.list() 
mail.select('inbox') 
result, data = mail.uid('search', None, "ALL")
   
i = len(data[0].split()) 
for x in range(i):
    latest_email_uid = data[0].split()[x] 
    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
   
    raw_email = email_data[0][1]
   
    raw_email_string = raw_email.decode('utf-8')
   
    email_message = email.message_from_string(raw_email_string)
   
    for part in email_message.walk():
        if part.get_content_type() == "text/plain": 
            body = part.get_payload(decode=True)
            messajbody = body.decode('utf-8')
            messajbody = messajbody.split("<div dir=\"auto\">")
            messajbody = messajbody[0].replace("\n","")
            print(messajbody)


# In[ ]:





# In[ ]:



