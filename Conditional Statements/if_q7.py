#WAP to find out whether a given post is talking about "harry"or not

post=input("Enter the post")
post=post.lower()
print(post)
if("harry" in post):
    print("this post is about harry")
else:
    print("this post is not about harry")
