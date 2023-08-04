import requests
import json

def send_message_vanilla(message):
    return 'vanilla ' + message

def send_message_ft(message):
    return 'finetune ' + message    

import gradio as gr
import random
import time

from leptonai.photon import Photon 

class EarningSage(Photon):

    def init(self):
        print('Initializing')

    @Photon.handler(mount=True)
    def ui(self):
        blocks = gr.Blocks( title="🧙🏼 Earning Report Assistant")
    
        with blocks:
            gr.Markdown('# 🧙🏼 Earning Report Assistant')
            gr.Markdown('''
                This is an earning report assistant built for investors are too lazy to listen over the whole  \
                earning report. Currently, only very few earning reports are provided. Feel free to reach out to \
                yuze.bob.ma@gmail.com for more advanced features.
            ''')
            with gr.Row():    
                chatbot = gr.Chatbot(label='Model 1')
                chatbot2 = gr.Chatbot(label='Model 2')        
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
            

            def respond_vanilla(message, chat_history):
                bot_message = send_message_vanilla(message)
                chat_history.append((message, bot_message))
                time.sleep(1)
                return "", chat_history

            def respond_ft(message, chat_history):
                bot_message = send_message_ft(message)
                chat_history.append((message, bot_message))
                time.sleep(1)
                return "", chat_history

            msg.submit(respond_vanilla, [msg, chatbot], [msg, chatbot])
            msg.submit(respond_ft, [msg, chatbot2], [msg, chatbot2])
            send.click(respond_vanilla, [msg, chatbot], [msg, chatbot])
            send.click(respond_ft, [msg, chatbot2], [msg, chatbot2])    

            clear.click(lambda: None, None, chatbot, queue=False)
            clear.click(lambda: None, None, chatbot2, queue=False)

        return blocks