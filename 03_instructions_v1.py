# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "Yes"
            return response

            # If they say no, output 'display instructions'

        elif response == "no" or response == "n":
            response = "No"
            return response

        else:
            print("Please answer yes / no")


# Main routine goes here...
show_instructions = yes_no("Have you played this game before? ")

if show_instructions == "yes":
    print("Display instructions")
else:
    print("Program Continues")
