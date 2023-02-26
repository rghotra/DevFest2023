import json
import os
import openai

data = json.load(open('tmp/output.json'))
# code = data['responses'][0]['fullTextAnnotation']['text']
code = data['fullTextAnnotation']['text']

"""lines = code.split('\n')
for i in range(len(lines)):
    if lines[i] and lines[i][-1] in ',.:':
        lines[i] = lines[i][:-1] + ';'
    elif lines[i] and lines[i][-1] != ';':
        lines[i] += ';'"""

openai.api_key = "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"
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"can you make this code compile, but don't fix runtime errors%n{code}%ndon't say anything before or after the fixed code",
  temperature=0,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
lines = str(response['choices'][0]['text'])
        
        
if os.path.isfile('tmp/Code.java'):
    os.remove('tmp/Code.java')
f = open('tmp/Code.java', 'a')

pre = """
package tmp;
class Code {
public static void main(String[] args) {
"""

post = """
}
}
"""

f.writelines(pre)
f.writelines(lines)
f.writelines(post)


f.close()