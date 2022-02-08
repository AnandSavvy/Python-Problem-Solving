import urllib.request
import re 

url = "https://www.summet.com/dmsi/html/codesamples/addresses.html"
response = urllib.request.urlopen(url)
html = response.read()
html_str = html.decode()
phones = re.findall(r'\(\d{3}\)\s\d{3}-\d{4}',html_str)
print(len(phones))
names = re.findall(r'<li>([A-Z][A-Za-z]+\s[A-Z][a-z]+)',html_str)
print(names)
print(len(names))