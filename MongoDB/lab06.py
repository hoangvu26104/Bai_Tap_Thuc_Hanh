from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
client.drop_database('driveABC')
db = client['driveABC']
files_collection = db['files']
posts_collection = db['videos']
comments_collection = db['comments']

files_data = [{ 'file_id': 1, 'name': 'Report.pdf', 'size': 2048, 'owner': 'Nguyen Van A', 'created_at': datetime(2024,1,10), 'shared': 'false' },
    { 'file_id': 2, 'name': 'Presentation.pptx', 'size': 5120, 'owner': 'Tran Thi B', 'created_at': datetime(2024,1,15), 'shared': 'true' },
    { 'file_id': 3, 'name': 'Image.png', 'size': 1024, 'owner': 'Le Van C', 'created_at': datetime(2024,1,20), 'shared': 'false' },
    { 'file_id': 4, 'name': 'Spreadsheet.xlsx', 'size': 3072, 'owner': 'Pham Van D', 'created_at': datetime(2024,1,25), 'shared': 'true' },
    { 'file_id': 5, 'name': 'Notes.txt', 'size': 512, 'owner': 'Nguyen Thi E', 'created_at': datetime(2024,1,30), 'shared': 'false' }
]
files_collection.insert_many(files_data)
for file in files_collection:
    print(file)

