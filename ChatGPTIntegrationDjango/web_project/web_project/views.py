from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('OPENAI_KEY', None)

def chatbot(request):
    chatbot_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input

        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.5,
            max_tokens=256,
            # top_p=1,
            # frequency_penalty=0.0,
            # presence_penalty=0.6,
            # stop="."
        )
        print(response)
        chatbot_response = response.choices[0].text
    return render(request, 'main.html', {"response": chatbot_response})