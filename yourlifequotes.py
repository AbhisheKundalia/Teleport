#!/usr/bin/python3.5
import facebook
import xlrd
import xlwt
from xlutils.copy import copy
from urllib.request import urlopen
import urllib
import requests
import json

def main():
  reqNum = get_var_value()
  print("This script has been run {} times.".format(reqNum))
  r = requests.get("https://www.googleapis.com/customsearch/v1?q=quotes&cx=011689125835766794874%3Awpruo5gry80&filter=1&imgSize=large&num=1&safe=medium&searchType=image&start="+str(reqNum)+"&fields=items%2Flink&key=AIzaSyAW-K-aVm6OXUInIF2DniLEOgXbu5DIv58")
  print(r.text)
  responseJson = json.loads(r.text)
  searchResultLink = responseJson["items"][0]["link"]
  # facebook posting works fine
  post_data = { 
     # all the data you want to send
    "url": searchResultLink,
    "caption": "--YourLife",
    'access_token':"EAAKOeOJaag8BAARap2sX4f6vyNeiAIB6lZA3FjQbiyuAg64MXJ6zXa6bW6RAeArEaLTJubONKDwjTeV1f9iZBWwYlm3zxjQhAEU2wpYUwhWxSpdg6YaQlZAn7GxcIP1kbu7bGM4WuwtS8mPzrg8gFL5VAWZCVpHoOyh64zEDFwZDZD" #longlived token
  }
  response = requests.post('https://graph.facebook.com/v2.10/740833762717018/photos', data=post_data)
  print(response.text)

def get_var_value(filename="varstore.dat"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val
'''
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : "740833762717018",  # Step 1
    "access_token" : "EAAKOeOJaag8BAP3WCUwXq78zTZCQp8hSZCKQHREDLNtZC0BkpPNyiEZAUvvl08mxeZBTqjs5yW2WLYWOsiq5LOF8X4P2MnoWezo0opZACKgca7r0qjqVGUUV2C9HAgUOA8sI1ef1UGbsxBDoxHR5M4v7KfJdsR3q4ZD"   # Step 3
    }
  graph = facebook.GraphAPI(access_token="EAAKOeOJaag8BAP3WCUwXq78zTZCQp8hSZCKQHREDLNtZC0BkpPNyiEZAUvvl08mxeZBTqjs5yW2WLYWOsiq5LOF8X4P2MnoWezo0opZACKgca7r0qjqVGUUV2C9HAgUOA8sI1ef1UGbsxBDoxHR5M4v7KfJdsR3q4ZD", version="2.1")
  access_token = "EAAKOeOJaag8BAP3WCUwXq78zTZCQp8hSZCKQHREDLNtZC0BkpPNyiEZAUvvl08mxeZBTqjs5yW2WLYWOsiq5LOF8X4P2MnoWezo0opZACKgca7r0qjqVGUUV2C9HAgUOA8sI1ef1UGbsxBDoxHR5M4v7KfJdsR3q4ZD"   # Step 3
    
  #api = get_api(cfg)
  #status = api.put_photo(image=open('https://s-media-cache-ak0.pinimg.com/736x/49/10/af/4910af8173a92cfe0edcc38c82a05447--biker-quotes-quotes-quotes.jpg', 'rb'),message='YourLife')
    

#  response = requests.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous",
 # headers={
  #  "X-Mashape-Key": "ZuCmAk3TLMmshPOZOKuKB9NPBZvwp1TrNYPjsnV75Q416PCuW1",
   # "Content-Type": "application/x-www-form-urlencoded",
    #"Accept": "application/json"
  #}
#)
  #if response.status_code == 200:
    #a = json.loads(response.text)
    #msg = a['quote'] + "    --Your life"
    #print(msg)
    #saveWorkSpace(a)
   #put_wall_post(msg)
   


def saveWorkSpace(fields):
    rb = xlrd.open_workbook('D:\Awiserk\Python\yourlifequotes\quotes.xls',formatting_info=True)
    r_sheet = rb.sheet_by_index(0) 
    r = r_sheet.nrows
    wb = copy(rb) 
    sheet = wb.get_sheet(0) 
    sheet.write(r,0,fields['quote'])
    sheet.write(r,1,fields['author'])
    sheet.write(r,2,fields['category'])
    wb.save('D:\Awiserk\Python\yourlifequotes\quotes.xls')
    print('Wrote quotes.xls')
  
def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip 
  # the following if you want to post as yourself. 
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph
  # You can also skip the above if you get a page token:
  # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
  # and make that long-lived token as in Step 3
  '''

if __name__ == "__main__":
  main()
