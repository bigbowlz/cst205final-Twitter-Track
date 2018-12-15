searchTerm = "server"
search_change = input(f'Current keyword on track is {searchTerm}, wanna change the keyword? (Y/N)')
while search_change != "N":
    if search_change == "Y":
        searchTerm = input("Enter Keyword/Tag to search about: ")
        search_change = "N"
    else:
        search_change = input(f'Please enter Y or N. \nCurrent keyword on track is {searchTerm}, wanna change the keyword? (Y/N)')

print (searchTerm)
