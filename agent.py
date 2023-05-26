from langchain import OpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.chains.conversation.memory import ConversationBufferMemory
from utils import get_available_reports_tool, get_report_insight_tool

memory = ConversationBufferMemory(memory_key="chat_history")

def agent_init():
    tools = [get_available_reports_tool, get_report_insight_tool]

    prefix_prompt = '''
    Assistant is an earning report large language model. 
    Assistant always need to use a tool.
    Assistant will only answer question related to financial industry.\n
    If Assistant is not sure about a question, reply with `I do not know`
    '''

    
    llm = OpenAI(temperature=0)
    agent = initialize_agent(
        tools, 
        llm, 
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, 
        verbose=True, 
        memory=memory
    )

    temp = agent.agent.llm_chain.prompt.template
    agent.agent.llm_chain.prompt.template = prefix_prompt + temp[temp.find('TOOLS'):]
    print(agent.agent.llm_chain.prompt.template)
    return agent