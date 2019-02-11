#PYTHON3 PROBLEMS TESTER

##DESCRIPTION:

  This project helps you to evaluate python specific programs. It consists
  of two main python programs, called *'tester.py'* and *'grader.py'*. The first of
  them is the one to be runned (contains the GUI code and general functioning),
  the other one contains a function implemented in *'tester.py'* which makes the
  evaluation part.

  As an exaple, we include a *.odt* file with some problems instructions whose
  expected output are in grader.py.

##HOW IT WORKS:

  When running he file *'tester.py'*, it first pops a terminal window in which you
  are asked whether you want to star a new exam or just continue with the previous
  one (in case you've accidentally closed the window so you don't lose what
  you've done). The option a (new test) will delete all exercise python files
  and apart from then will create as many as you tell.

  Once passed that, a TKinter window will prompt, there is where you'll control
  the tests made over the problems. There's a default path written in the text
  boxes which should be respected. The files to edit (where you write your
  solution) are located in the folder problems. When you want to test your code,
  you must save the file, go to the Tk window and hit the *Comprobar* button, the
  results will be sowed up in the text boxes at the top of the window.

##FOR CHANGING THE PROBLEMS TO BE EVALUATED:

  For you to change the problems to be solved, you just have to open *'grader.py'*
  and follow the examples included there for including your own inputs and
  outputs.

**IMPORTANT!!**

  For this to work, in the solutions code the one only thing that shall be
  respected is not getting any argument inside the `input()` functions, otherwise
  our program wont work.

##AUTHORS:

  Made by the https://www.github.com users @Korven48 and @RoDiHackProg.
