# Story: There once was a very (adjective) (animal) who lived in (city). He loved to eat (type of candy).

#1) print welcome
#2) ask for input for each blank
#3) print story

print("Hello, and welcome to MadLibs! Please enter the following words to complete your story.")
adj = input("Enter an adjective: ")
animal = input("Enter a type of animal: ")
city = input( "Enter the name of a city: ")
candy = input("Enter a type of candy: ")
\n
print("Thank you! Your story is:")
\n
print("There once was a very " + adj + " " + animal + " who lived in " + city + ". He loved to eat " + candy + ".")
