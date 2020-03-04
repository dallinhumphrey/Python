string = 'the chubby rabid fox jumped over the playfull dog'
string_length = (len(string))
print(string_length)

string_1 = "The chubby "
string_2 = "rabid fox "
string_3 = "jumped over the "
string_4 = "playfull dog"

string_5 = (string_1 + string_2 + string_3 + string_4)

print(string_5)
string_1 = "The chubby "
string_2 = "rabid fox "
string_3 = "jumped over the "
string_4 = "playfull dog"
string_5 = f"{string_1}{string_2}{string_3}{string_4}"
print(string_5)

name = 'Alex'
print(name[-1] + name[1: -1] + name[0])

str = "the dog"


def new_str():
    print(str[-1:] + str[1: -1], str[:1])
    return f"{str[-1:]}, {str[1: -1]}, {str[:1]}"


print(new_str)

numbers = [1, 2, 3]
total = sum(numbers)
print(total)
string = "racecar"
string_replace = string.replace[0, ]
print(string_replace)


first_list = ["dallin", "kortney", "lincoln", "lily"]


def return_longest(li):
    longest_word = li[0]

    for word in li:
        if len(word) > len(longest_word):
            longest_word = word

    return f"""
Longest Word: {longest_word}
Length: {len(longest_word)}
  """.strip()


print(return_longest(first_list))
