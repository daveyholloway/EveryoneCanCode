from flask import Flask, render_template, request, redirect

todo_list = []
app = Flask(__name__)

todo_list = []

try:
    with open("todo_list.txt", "r") as file:
        for line in file:
            todo_list.append(line.strip())
except FileNotFoundError:
    print("No saved items found")


@app.route("/")
def index():
    return render_template("index.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add_todo():
    todo = request.form.get("todo")
    todo_list.append(todo)
    return redirect("/")

@app.route("/remove", methods=["POST"])

def remove_todo():
    item_number = int(request.form.get("item_number"))
    if item_number > 0 and item_number <= len(todo_list):
        todo_list.pop(item_number - 1)
    return redirect("/")

@app.route("/save", methods=["POST"])
def save_todo_list():
    with open("todo_list.txt", "w") as file:
        for todo in todo_list:
            file.write(f"{todo}\n")
    return redirect("/")


if __name__ == "__main__":
    app.run()
        todo = input("Enter the to-do item: ") 
        todo_list.append(todo)
        continue  # tells the program to go back to the start of the loop

    # user selected 'r' or 'R' to remove an item from the list
    if choice == "R":
        item_number = int(input("Enter the number of the item to remove: "))
        if item_number > 0 and item_number <= len(todo_list):
            todo_list.pop(item_number - 1)
        else:
            print("Invalid item number")
        continue

    # user selected 'x' or 'X' to exit the program
    if choice == "X":
        # save the to-do list to a file
        #**********THIS CODE ****************
        with open("todo_list.txt", "w") as file:
            for todo in todo_list:
                file.write(f"{todo}\n")
        #************************************
        break

    # user selected something else
    print("Invalid choice")