arn = ("arn:aws:iam::123456789012:user/john", 1, 2, "arn:aws:iam::123456789012:user/peter")
for user in arn:
    if isinstance(user, str):
        print(user.split("/")[1])

    