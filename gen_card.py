# Read xlsx file
import os
import pandas as pd
# Openai API request
import langchain_openai
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()  # 這會加載同目錄下的.env檔案中的變量


############ Set vocab_file here ############
vocab_file = 'card_vocab_11'
llm = langchain_openai.ChatOpenAI(model="gpt-3.5-turbo", max_tokens=3000)
df = pd.read_excel(f'{vocab_file}.xlsx')

# read prompt.txt
with open('card_prompt.txt', 'r') as f:
    prompt = f.read()
columns = df.columns
outputResponse = ""
for col in columns:
    Lst = df[col].tolist()
    wordLst = ",".join(Lst)
    with open('card_prompt.txt', 'r') as f:
        prompt = f.read()
        prompt = prompt + "\n" + wordLst
        print(prompt)
        messages = [
            SystemMessage(content="You are a english tutor."),
            HumanMessage(content=prompt)
        ]
        response = llm.invoke(messages)
        # add next line
        outputResponse = outputResponse + '\n' + response.content
        # write response to markdown file
        if not os.path.exists('card'):
            os.makedirs('card')
        with open(f'card/{vocab_file}_{col}.txt', 'w') as f:
            f.write(response.content)    
        print(f'{vocab_file}_{col} is done')

# Save response as markdown file
# make sure the output folder is exist
if not os.path.exists('card'):
    os.makedirs('card')
with open(f'card/{vocab_file}.txt', 'w') as f:
    f.write(outputResponse)
    print('All done')

    