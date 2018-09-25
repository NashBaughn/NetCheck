import subprocess
import re
import os
import sys
import requests
import time
import json

iprgx   =  re.compile('(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,5})')
api_url = "https://www.abuseipdb.com/check/"
key     = os.environ["IPABUSE_API_KEY"]

def main():
  conns = get_conns()
  for conn in conns:
    lip = conn.split()[3]
    fip = conn.split()[4] 
    if re.match(iprgx, lip) is not None:
        ipabuse_test(fip)
        time.sleep(.3)
    

def ipabuse_test(ip):
  print(ip)
  resp = requests.get(api_url + ip + "/json?key="+ key + "&days=" + sys.argv[1])
  jresp = json.loads(resp.content)
  print(jresp[0])

def get_conns():
  netstat = subprocess.check_output(['netstat','-f','inet'])
  nets = netstat.split("\n")
  return nets[2:len(nets)-3]

if __name__ == "__main__":
  main()  
