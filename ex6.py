types_of_people = 10 #nint a
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I alse said: '{y}'")

hilarious = True
joke_evaluation = "Isn't that joke so fonny?! {} {}"

yes_string = "Yes"
no_string = "No"

yes_or_no_string = yes_string + "or" + no_string;

print(joke_evaluation.format(yes_or_no_string, yes_string))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
