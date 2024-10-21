from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
client.drop_database('tiktokABC')
db = client['tiktokABC']
users_collection = db['users']
videos_collection = db['videos']


users_data = [{'user_id': 1, 'username': 'user1', 'full_name': 'Nguyen Van A', 'followers': 1500, 'following': 200},
              {'user_id': 2, 'username': "user2", 'full_name': "Tran Thi B", 'followers': 2000, 'following': 300 },
              { 'user_id': 3, 'username': "user3", 'full_name': "Le Van C", 'followers': 500, 'following': 100 }
]
users_collection.insert_many(users_data)

videos_data = [{ 'video_id': 1, 'user_id': 1, 'title': 'Video 1', 'views': 10000, 'likes': 500, 'created_at': '2024-01-01' },
               { 'video_id': 2, 'user_id': 2, 'title': 'Video 2', 'views': 20000, 'likes': 1500, 'created_at': '2024-01-05' },
               { 'video_id': 3, 'user_id': 3, 'title': 'Video 3', 'views': 5000, 'likes': 200, 'created_at': '2024-01-10' }]
videos_collection.insert_many(videos_data)

# print("Tất cả người dùng: ")
# for user in users_collection.find():
#     print(user)
    
# print("Video có nhiều lượt xem nhất: ")
# mosted_viewed_video = videos_collection.find().sort('views', -1).limit(1)
# for video in mosted_viewed_video:
#     print(user)


print("\nTất cả video của người dùng 'user1': ")
user_video = videos_collection.find({'user_id':1})
for video in user_video:
    print(video)

# print("Follower của user1 trước khi update: ")
# for user in users_collection.find():
#     print(user)
# print("Follower của user1 sau khi update: ")
users_collection.update_one({'user_id': 1}, {'$set': {'followers': 2000}})
# for user in users_collection.find():
#     print(user)


