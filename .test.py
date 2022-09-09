import json

jsonData = '''
{
    "json":
    [
        {
            "pathtxt": "TXT/car.txt",
            "keyword": "car"
        },
        
        {
            "pathtxt": "TXT/mountains.txt",
            "keyword": "mountain"
        }
    ]
}
'''

data = json.loads(jsonData)

for i in data["json"]:
    print(i["keyword"])