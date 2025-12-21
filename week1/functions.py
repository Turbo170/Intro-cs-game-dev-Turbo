#created the functions vv
def greet_player(name):
    print(f"Hello, {name}, welcome.")
def calculate_damage(base_damage):
    return base_damage + 2

# calling the functions vv
greet_player("Alex")
damage = calculate_damage(5)
print(damage)