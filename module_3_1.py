calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length_of_string = len(string)
    upper_string = string.upper()
    lower_string = string.lower()
    return (length_of_string, upper_string, lower_string)

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    list_to_search_lower = []
    for i in list_to_search:
        list_to_search_lower.append(i.lower())
    return string_lower in list_to_search_lower

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban',['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
