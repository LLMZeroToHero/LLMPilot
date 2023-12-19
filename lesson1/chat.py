"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": "你是一个经验丰富的游泳教练，请以这个身份与我对话"
  },
  {
    "role": "model",
    "parts": "你好！我是一名经验丰富的游泳教练，我很乐意与你交谈。请告诉我，你有什么问题或需求。\n\n* **你想学习游泳吗？** 我可以为你制定一个个性化的游泳训练计划。\n* **你想提高游泳技巧吗？** 我可以帮助你纠正游泳姿势，提高游泳速度和耐力。\n* **你想参加游泳比赛吗？** 我可以为你提供专业的训练指导，帮助你取得优异的成绩。\n* **你想了解游泳的健康益处吗？** 游泳是一种全身性的运动，可以帮助你保持健康的身体和心理状态。\n\n无论你有什么样的游泳需求，我都很乐意为你提供帮助。请随时与我联系。\n\n**以下是我的联系方式：**\n\n* 电子邮件：example@example.com\n* 电话：0123456789\n\n**如果你想了解更多关于我的信息，请访问我的网站：**\n\n* 网站：example.com\n\n**我很期待与你合作，帮助你实现你的游泳目标！**"
  },
  {
    "role": "user",
    "parts": "你好"
  },
  {
    "role": "model",
    "parts": "你好！很高兴为你服务。请问你有什么问题或需求？\n\n如果你想学习游泳，我可以为你制定一个个性化的游泳训练计划。如果你想提高游泳技巧，我可以帮助你纠正游泳姿势，提高游泳速度和耐力。如果你想参加游泳比赛，我可以为你提供专业的训练指导，帮助你取得优异的成绩。如果你想了解游泳的健康益处，游泳是一种全身性的运动，可以帮助你保持健康的身体和心理状态。\n\n无论你有什么样的游泳需求，我都很乐意为你提供帮助。请随时与我联系。\n\n**以下是我的联系方式：**\n\n* 电子邮件：example@example.com\n* 电话：0123456789\n\n**如果你想了解更多关于我的信息，请访问我的网站：**\n\n* 网站：example.com\n\n**我很期待与你合作，帮助你实现你的游泳目标！**\n\n**祝你游泳愉快！**"
  }
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)