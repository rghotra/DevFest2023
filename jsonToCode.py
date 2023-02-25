import json
import os

data = json.load(open('tmp/output.json'))
code = data['responses'][0]['fullTextAnnotation']['text']


lines = code.split('\n')
for i in range(len(lines)):
    if lines[i] and lines[i][-1] in ',.:':
        lines[i] = lines[i][:-1] + ';'
    elif lines[i] and lines[i][-1] != ';':
        lines[i] += ';'
        
        
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
f.writelines('\n'.join(lines))
f.writelines(post)


f.close()