import os

from dotenv import load_dotenv
load_dotenv()

from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain import OpenAI
from langchain.indexes import VectorstoreIndexCreator
from langchain.tools import Tool

def vdb_upsert(db_connection, embedding):
    '''

    '''
    pass 

def vdb_connection():
    '''
    Input:
    
        host,username,password,port,auth mode
    
    Return:
        
        db connection


    '''

# Tools for agent to use
def get_available_reports():
    stocks = ['AAPL','EA','UA']
    res = 'We have got '
    for i in stocks:
        res += i + ','
    
    res += ' Stocks available'
    return res

get_available_reports_tool = Tool(
    name = 'Reports available',
    func= lambda some : get_available_reports(),
    description='''
        Use when the Assistant is asked about available earning reports. 
    ''',
    return_direct = True    
)

def get_report_insight(user_query : str):
    embeddings = OpenAIEmbeddings()
    chroma_directory = './chroma_index'
    db = Chroma(persist_directory=chroma_directory, embedding_function=embeddings)
    query = user_query
    docs = db.similarity_search(query)
    target_file = docs[0].dict()['metadata']['source']
    target_file = './earning_reports/' + target_file.split('/')[-1]
    
    llm = OpenAI(temperature=0)
    loader = CSVLoader(target_file, csv_args={ 'delimiter': '\t' })
    index = VectorstoreIndexCreator().from_loaders([loader])
    query = user_query
    trend = index.query(query, llm=llm)    
    return trend

get_report_insight_tool = Tool(
    name = 'Get Report Feedback',
    func = lambda query : get_report_insight(query),
    description = '''
        Use when you are asked about a stock or company. The input to this tool should be kept as the way human asked.
        For example `What was talked during Apple's earning report?` should be kept as `What was talked during Apple's earning report?`
        Do not extract entity or modify the input.
    ''',
    return_direct = True 
)