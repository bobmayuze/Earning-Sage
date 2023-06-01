# 🧙 Earning-Sage
This is an earning call assistant built for investors are too lazy to listen over the whole earning report. Currently, only very few earning reports are provided.

Currently Supported Earning Calls:

| Company | Report |
|---------|--------|
| Apple   | Q2 Fiscal Year 2023 Earnings Conference Call |
| Electronic Arts  | Fourth Quarter and Fiscal Year-End 2023 Conference Call |
| Under Armour | Q4 '23 Earnings Conference Call |

Feel free to reach out to yuze.bob.ma@gmail.com for more advanced features or expand earning calls.

# Getting Started

## 1. Create .env file and provide your openAPI key
```shell
echo OPENAI_API_KEY={YOUR OPENAI_API_KEY} > .env
```

## 2. Start
```shell
pip install -r requirements.txt
python gradio_ui.py
```

## 3. Try it out
Visit http://127.0.0.1:7860/ 

Sample questions you could be asking :

- What earning reports are available?
- What was talked during Apple's earning report?
- How much revenue is achieved on the iphone sector
