def check_status(user):
    group = user.groups.first()
    return group.name