# Functions go here...
def yes_no(question):

    valid = False
    while not valid:
        response = input(question).lower()
        response = response.replace(" ", "")

        if response == "yes" or response == "y":
            response = "yes"
            return response

            # If they say no, output 'display instructions'

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


# Main routine goes here...
print()
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()

print("Program continues")
