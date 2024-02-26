#Create a new list named shopping_list
shopping_list = []

def show_help():
    print("What should we pick up at the store?")
    print("""
  Enter 'DONE' to stop adding itmes.
  Enter 'HELP' to display help.
  Enter 'SHOW LIST' to display your list.""")
    
def add_to_list(item):
    shopping_list.append(item)
    print("An item was added! Your total number of items is: {}".format(len(shopping_list)))
    
def show_list():
    print("Your list: ")
    for item in shopping_list:
        print(item)
    
show_help()

while True:
    new_item = input("> ")
    
    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW LIST":
        show_list()
        continue
        
    # Call add_to_list with new_item as an argument
    add_to_list(new_item)
    
show_list()