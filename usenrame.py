from graphics import *

''' 
'''

def getUserPass(userEntry, passEntry):
    username = userEntry.getText()
    password = passEntry.getText()
    both = username + " " +password
    userpass = both.split(" ")
    return userpass

def guesser(password):

    guessedWord = ""
    letters= "abcdefghijklmnopqrstuvwxyxz"
    i = 0
    while guessedWord != password and i <=26:
        guessedWord = letters[i]
        i +=1
    if guessedWord != password:
        for i in range(26):
            for j in range(26):
                guessedWord = letters[i]+letters[j]
                if guessedWord == password:
                    break
            if guessedWord == password:
                break
    if guessedWord != password:
        for i in range(26):
            for j in range(26):
                for l in range(26):
                    guessedWord = letters[i]+letters[j]+letters[l]
                    if guessedWord ==password:
                        break
                if guessedWord ==password:
                    break
            if guessedWord ==password:
                break
    if guessedWord != password:
        for i in range(26):
            for j in range(26):
                for l in range(26):
                    for k in range(26):
                        guessedWord = letters[i]+letters[j]+letters[l]+letters[k]
                        if guessedWord ==password:
                            break
                    if guessedWord ==password:
                        break
                if guessedWord == password:
                    break
            if guessedWord ==password:
                break
    if guessedWord != password:
        for i in range(26):
            for j in range(26):
                for l in range(26):
                    for k in range(26):
                        for o in range(26):
                            guessedWord = letters[i]+letters[j]+letters[l]+letters[k]+letters[o]
                            if guessedWord ==password:
                                break
                        if guessedWord ==password:
                            break
                    if guessedWord ==password:
                        break
                if guessedWord ==password:
                    break
            if guessedWord ==password:
                break
            
    return guessedWord

def main():

    win  = GraphWin("password thing", 500,500)
    usernamePrompt = Text(Point(150,150), "username: ")
    usernamePrompt.draw(win)
    passwordsPrompt = Text(Point(150,200), "password: ")
    passwordsPrompt.draw(win)
    passwordsEntry = Entry(Point(275,200),15)
    passwordsEntry.draw(win)
    usernameEntry = Entry(Point(275,150),15)
    usernameEntry.draw(win)
    create = Text(Point(250,300), "create")
    rectangle = Rectangle(Point(300,325), Point(200,275))
    create.draw(win)
    rectangle.draw(win)
    win.getMouse()
    create.undraw()
    rectangle.undraw()
    userPass = getUserPass(usernameEntry,passwordsEntry)
    print(userPass)
    password = userPass[1]
    guessedPassword = guesser(password)
    print(guessedPassword)

main()
