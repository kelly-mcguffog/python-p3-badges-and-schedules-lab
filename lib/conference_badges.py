def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(badge_maker(name))
    return badges

def assign_rooms(names):
    new_list = []
    for index, name in enumerate(names):
        room_assignments = f"Hello, {name}! You'll be assigned to room {index + 1}!"
        new_list.append(room_assignments)
    return new_list

def printer(names):
    for name in names:
        print(badge_maker(name))

    room_messages = assign_rooms(names)
    for message in room_messages:
        print(message)