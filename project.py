import requests
import xml.etree.ElementTree as ET
import csv

from requests_ntlm import HttpNtlmAuth

schema XML microsoft 
ns0 = "http://www.w3.org/2005/Atom"
ns1 = "http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"
ns2 = "http://schemas.microsoft.com/ado/2007/08/dataservices"

Create csv file 
csv_file = open('file_name_csv.csv', 'w', newline = '', encoding='ansi')
csvwriter = csv.writer(csv_file)

col_names = ['Col_1', 'Col_2', 'Col_3', 'Col_n']
csvwriter.writerow(col_names)

field_tag = ['dado_1', 'dado_2', 'dado_3', 'dado_n']


for member in root:
    if member.tag == '{' + ns0 + '}entry':
        for element in member:
            if element.tag == '{' + ns0 + '}content':
                data_line = []

                for field in element[0]:            
                    for count in range(0, len(field_tag)):
                        if field.tag == '{' + ns2 + '}' + field_tag[count]:
                            data_line.append(field.text)

response = requests.get("your_url", auth=HttpNtlmAuth('xxxx\\username','password'))
tree =  ET.ElementTree(ET.fromstring(response.content))
tree.write('file_name_xml.xml')
root = tree.getroot()


                csvwriter.writerow(data_line)

csv_file.close()
