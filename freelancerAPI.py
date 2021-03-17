import requests
import re
result=[]
query="translation"
url="https://www.freelancer.com/jobs/"+query+"/1/?cl=l-en-tr"
for i in range(100):
    response=requests.api.get(url=url)
    a=response.text
    dumb=re.findall('%s(.*)%s' % ("/projects/"+query, "class"), a)
    if dumb==[]:
        break
    for i in range(len(dumb)):
        result.append("https://www.freelancer.com/projects/"+query+dumb[i])
for i in range(len(result)):
    print(result[i])
