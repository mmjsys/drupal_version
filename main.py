import requests
import sys
import re
def SendRequest(url):
    try:
       req = requests.get(url)
    except:
        sys.exit(1)
    if req.status_code != 200:
       sys.exit(1)
    return req

def GetXGeneratorFromHeader(url):
    req = SendRequest(url)
    try:
       text = req.headers['x-generator']
       return text
    except:
      print("can't get x-generator from header ... ")

def GetVertionFromText(text):
    m = re.search('(?<= )\w+' , text)
    print("wow ... \n[+] version : " , m.group(0))

if __name__ == "__main__":
  GetVertionFromText(GetXGeneratorFromHeader(sys.argv[1]))
