arn = ("arn:aws:iam::123456789012:user/john", 1, 2, "arn:aws:iam::123456789012:user/peter")
for user in arn:
    print(str(user).split("/")[-1])

    