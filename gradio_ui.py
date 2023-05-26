import gradio as gr
from agent import agent_init

from dotenv import load_dotenv
load_dotenv()


# Util for Gradio to use
def chat(uesr_query : str):
    '''
    Input:
        user_query : str
    Output:
        message : str
    '''
    message = uesr_query
    agent = agent_init()
    res = agent.run(message)
    return res

def respond(message, chat_history):
    bot_message = chat(message)
    chat_history.append((message, bot_message))
    return "", chat_history

def ui():
    blocks = gr.Blocks(
        title="🧙🏼 Earning Report Assistant",
    )

    with blocks:
        gr.Markdown('# 🧙🏼 Earning Report Assistant')
        gr.Markdown('''
            This is an earning report assistant built for investors are too lazy to listen over the whole  \
            earning report. Currently, only very few earning reports are provided. Feel free to reach out to \
            yuze.bob.ma@gmail.com for more advanced features.
        ''')
        chatbot = gr.Chatbot()
        with gr.Row():
            msg = gr.Textbox(
                value = 'What earning reports are available',
                info = """
                    Sample questions: What earning reports are available? | What was talked during Apple's earning report? | How much revenue is achieved on the iphone sector
                """,
                label = 'Questions you would like to ask'
                
            )
            
        with gr.Row():
            send = gr.Button("Send")
            clear = gr.Button("Clear")

        msg.submit(respond, [msg, chatbot], [msg, chatbot])
        send.click(respond, [msg, chatbot], [msg, chatbot])
        clear.click(lambda: None, None, chatbot, queue=False)
    return blocks


if __name__ == '__main__' : 
    gui = ui()
    gui.launch()