import csv,os,json

filename = 'C:\\Users\\deepa\\Downloads\\50_Startups.csv'
fileprac = 'C:\\Users\\deepa\\Downloads\\file_practice.csv'

with open(filename,'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    data_list = []
    field_name = csv_reader.fieldnames
    for row in csv_reader:
        data_list.append(row)

print(field_name)
for i in data_list[:5]:
    print(i['Administration'])

with open (filename,'r') as src_file, open(fileprac,'w') as dest_file:
    csv_reader = csv.reader(src_file)
    csv_writer = csv.writer(dest_file)

    for i in csv_reader:
        csv_writer.writerow(i)

with open(fileprac,'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    dis_lst = []
    for i in csv_reader:
        dis_lst.append(i)
print(dis_lst)

with open(fileprac,'r')as csv_file:
    reader = csv.DictReader(csv_file)
    filenames = reader.fieldnames + ['id'] if 'id' not in reader.fieldnames else reader.fieldnames
    rows = []
    for i,row in enumerate(reader):
        row['id'] = i
        rows.append(row)

with open(fileprac,'w') as csv_file:
    writer = csv.DictWriter(csv_file,fieldnames=filenames)
    writer.writeheader()
    writer.writerows(rows)

with open(fileprac,'r')as csv_file:
    reader = csv.DictReader(csv_file)
    for i in reader:
        print(i)

# Image File Handling
from PIL import Image
img = Image.open("C:\\Users\\deepa\\Pictures\\paper.png")

try:
    width,height = img.size
    mirror_img = img.transpose(Image.ROTATE_270)
    mirror_img.show()
    img = img.resize((width*2,height*2))
    img.save("C:\\Users\\deepa\\Pictures\\paper.png")
    img.show()
except Exception as e:
    print(e)

x = '{"Name":"deepak","details":{"School":"S.V.V.M","Grade":10}}'
y = json.loads(x)
print(y)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(type(x))
y = json.dumps(x,indent=4,separators=('.',','),sort_keys=True)
print(y)

with open('D:\\practice\\info.json','r') as json_file:
    reader = json.load(json_file)
    print(reader)
    
print(type(reader))
dic = {'grade': ['1',2,3,None]}
reader.update(dic)
print(reader)

with open(r'D:\\practice\\info.json','r+') as json_file:
    reader = json.load(json_file)
    json.dump(dic,json_file,indent=4,separators=(',',': '))
    print(reader)

with open('D:\\practice\\info.json','r') as json_file:
    reader = json.load(json_file)
with open('D:\\practice\\info1.json','w') as json1_file:
    json.dump(reader,json1_file,indent=4)
