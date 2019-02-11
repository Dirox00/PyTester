from tkinter import *
from grader import *
import os

solved = []

mode = input("Do you want to start a new test (enter 'a') or continue with the last one (enter 'b')? ")

if mode == 'a': #If 'a' is choosen, all files in Problems/ will be deleated, otherwise the content will be preserved.
    for filename in os.listdir('Problems/'):
        os.unlink('Problems/{}'.format(filename))

print('\n', '-'*100, '\n')
num_of_problems = int(input('Number of problems: '))+1

window = Tk()

def check(prog, prog_number=0): #This function is the one which is connected to the grader file and checks if the solutions are correct.
    global t
    if prog:
       	with open(prog) as f:
            exercise = f.read()
            out, inpt = soluciones[prog_number]
            result = test(exercise, out, inpt)
            number = prog[16]
            t.delete("1.0", END)
            t.insert(END, 'Problem {}: {}'.format(number, result))
        if result[0] == result[1]:
            if number not in solved:
                solved.append(number)
            solved.sort()
            solved_list = ['p' + str(i) for i in solved]
            t2.delete("1.0", END)
            t2.insert(END, 'Solved: {}'.format(', '.join(solved_list)))
        if len(solved) == num_of_problems:
            t2.delete("1.0", END)
            t2.insert(END, "You've solved all the problems, congratulations!")

def calc(n): #Used for calculating the row in which boxes should be placed.
    if n<3: return n**2 + 1
    return 3*n+n-3

def newProblem(number): #Creates stuff needed for every problem checker.
    global problem
    problem = number
    problem_name = 'problem{}.py'.format(number)
    try:
        file = open('Problems/{}'.format(problem_name))
    except FileNotFoundError:
        file = open('Problems/{}'.format(problem_name),'w')
    file.close()
    y = calc(number)
    l0 = Label(text='')
    l0.grid(row=y, column=0)

    l = Label(text='Problem {}'.format(number))
    l.grid(row=y+1, column=0)

    e = Entry(window, width=50)
    e.insert(END, problem_name)
    e.grid(row=y+2, column=0)
    e_value = str(e.get())

    b = Button(window, text='Check',
    command= lambda: check('Problems/{}'.format(e_value), number-1), height=1,
    width=20)
    b.grid(row=y+2, column=1)

t = Text(window, height=1, width=60)
t.grid(row=0, column=0, columnspan=2)
t.delete("1.0", END)
t.insert(END, 'Tests')

t2 = Text(window, height=1, width=60)
t2.grid(row=1, column=0, columnspan=2)
t2.delete("1.0", END)
t2.insert(END, 'No test resolved yet.')

for i in range(1, num_of_problems):
    newProblem(i)

window.mainloop()

#Made by @Korven48 and @RoDiHackProg.
