import requests
response = requests.get('http://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:
    json_data = response.json()
    print(f"Tổng số bài post: {len(json_data)}")
    for post in json_data:
        print("UserID:", post['userId'])
        print("ID bài đăng:", post['id'])
        print("Tiêu đề:", post['title'])
        print("Nội dung:", post['body'])
        print("==================================")
else:
    print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)