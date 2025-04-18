#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import requests
import datetime
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew
from typing import List, Dict, Any
from crewai.tools import tool
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential


# In[ ]:


# load_dotenv(dotenv_path='C:/Users/Tim/.env')
load_dotenv()


# In[ ]:


endpoint         = "https://openai-setup-tmf.openai.azure.com/"
model_name       = "gpt-4"
deployment       = "gpt-4"
subscription_key = "F0aU0fHPoOy3x5e4e2iLbl7vLrMNQDOyhL5lqxDMTCV4KVjXxtx3JQQJ99BDACYeBjFXJ3w3AAABACOG0OSZ"
api_version      = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)


# In[ ]:


response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Who is boog powell the baseball player",
        }
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0,
    model=deployment
)
print(response.choices[0].message.content)

 



