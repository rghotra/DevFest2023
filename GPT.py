%env OPENAI_API_KEY=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

import os
import openai
import queue

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write a summary of the code to explain what the code is doing to a beginner\n" + '\n'.join(open('tmp/Code.java').readlines()),
  temperature=0,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

if os.path.isfile('tmp/summary.txt'):
    os.remove('tmp/summary.txt')
f = open('tmp/summary.txt', 'a')

f.writeLines(str(response['choices'][0]['text']));
f.close();
