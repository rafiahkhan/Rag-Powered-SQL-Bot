from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

def get_sql_chain(db):
    template = """     
You are a professional data analyst at a company. You are helping a user query the company's SQL database using only **read-only** operations.

Here are the STRICT RULES you must follow:
1. **NEVER** generate queries that modify the database — such as DELETE, INSERT, UPDATE, ALTER, DROP, CREATE, TRUNCATE, or any DDL/DML commands.
2. Only use **SELECT** queries that retrieve data.
3. Use **only the exact table and column names** as shown in the schema below. 

Table Schema:
<SCHEMA>{schema}</SCHEMA>

Conversation History:
{chat_history}

Your task is to write a clean and correct SQL SELECT query to answer the user’s question.

Example:
Question: Show the names of all products and their unit prices.
SQL Query: SELECT ProductName, UnitPrice FROM Products;

Your turn:

Question: {question}
SQL Query:
"""
  

    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

    def get_schema(_): return db.get_table_info()

    return (
        RunnablePassthrough.assign(schema=get_schema)
        | prompt
        | llm
        | StrOutputParser()
    )
