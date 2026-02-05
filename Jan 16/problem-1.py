login_counts = {"admin": 5, "dev_user": 12, "guest_1": 1}

def record_login(user_dict, username):
    if username in user_dict:
        user_dict[username] += 1
    else:
        user_dict[username] = 1


record_login(login_counts, "admin")
record_login(login_counts, "guest_1")
print("After recording logins:", login_counts)

new_login_counts = {"salam": 1, "barkat": 1, "rafiq": 1}
login_counts.update(new_login_counts)
print("After batch update:", login_counts)