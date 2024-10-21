from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
client.drop_database('facebookABC')
db = client['facebookABC']
users_collection = db['users']
posts_collection = db['videos']
comments_collection = db['comments']

users_data = [{'user_id': 1, 'name': 'user1', 'email': 'a@gmail.com', 'age': 25},
              {'user_id': 2, 'name': 'user2', 'email': 'b@gmail.com', 'age': 30},
              {'user_id': 3, 'name': 'user3', 'email': 'c@gmail.com', 'age': 22}
]
users_collection.insert_many(users_data)

posts_data = [{ 'post_id': 1, 'user_id': 1, 'content': 'Hôm nay thật đẹp trời!', 'created_at': datetime(2024,10,1)},
              { 'post_id': 2, 'user_id': 2, 'content': 'Mình vừa xem một bộ phim hay!', 'created_at':datetime(2024,10,2)},
              { 'post_id': 3, 'user_id': 1, 'content': 'Chúc mọi người một ngày tốt lành!', 'created_at': datetime(2024,10,3)}]
posts_collection.insert_many(posts_data)

comments_data = [{ 'comment_id': 1, 'post_id': 1, 'user_id': 2, 'content': "Thật tuyệt vời!", 'created_at': datetime(2024,10,1) },
                 { 'comment_id': 1, 'post_id': 1, 'user_id': 2, 'content': "Chúc anh em 83, 86!", 'created_at': datetime(2024,10,13) },
                 { 'comment_id': 2, 'post_id': 2, 'user_id': 3, 'content': "Mình cũng muốn xem bộ phim này!", 'created_at': datetime(2024,10,2) },
                 { 'comment_id': 3, 'post_id': 3, 'user_id': 1, 'content': "Cảm ơn bạn!", 'created_at': datetime(2024,10,3) }]
comments_collection.insert_many(comments_data)

print("Tất cả người dùng: ")
for user in users_collection.find():
    print(user)
    
#Xem tất cả bài đăng của người dùng user_id = 1
print("\nTất cả post của người dùng 'user1': ")
user_posts = posts_collection.find({'user_id':1})
for post in user_posts:
    print(post)
    
# Xem tất cả bình luận cho bài đăng với post_id = 1
print("Xem tất cả bình luận cho bài đăng với post_id = 1")
comment_post = comments_collection.find({'post_id': 1})
for comment in comment_post:
    print(comment)
    
print(" Truy vấn người dùng có độ tuổi trên 25")
ages = users_collection.find({'age': {'$gt':25}})
for age in ages:
    print(age) 
print("Truy vấn tất cả bài đăng được tạo trong tháng 10")
post_in_10th = posts_collection.find({'created_at': {'$gte': datetime(2024,10,1), '$lt': datetime(2024,11,1)} })
for post1 in post_in_10th:
    print(post1)
    
#Cập nhật nội dung bài đăng của người dùng với post_id = 1
update_post = posts_collection.update_one({'post_id':1}, {'$set': {'content': 'Anh Vũ mãi đỉnh, mãi đỉnh!'}})
for post in posts_collection.find():
    print(post)
    