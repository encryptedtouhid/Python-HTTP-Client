import http.client
import json
import pprint

class apiClient:

  @classmethod
  def getData(self):
    connection = http.client.HTTPSConnection("www.journaldev.com")
    connection.request("GET", "/")
    response = connection.getresponse()
    headers = response.getheaders()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint("Headers: {}".format(headers))

  @classmethod
  def postData(self):
    conn = http.client.HTTPSConnection('www.httpbin.org')
    headers = {'Content-type': 'application/json'}
    foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
    json_data = json.dumps(foo)
    conn.request('POST', '/post', json_data, headers)
    response = conn.getresponse()
    print(response.read().decode())


  @classmethod
  def putData(self):
    conn = http.client.HTTPSConnection('www.httpbin.org')
    headers = {'Content-type': 'application/json'} 
    foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
    json_data = json.dumps(foo)
    conn.request("PUT", "/put", json_data)
    response = conn.getresponse()
    print(response.status, response.reason)





