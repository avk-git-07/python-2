arn = ("arn:aws:iam::123456789012:user/john", "arn:aws:iam::123456789012:user/peter")
for user in arn:
    print(user.split("/")[1])