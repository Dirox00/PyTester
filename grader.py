def test(exercise:str, expected_outputs:list, inputs:list=False):
  ''' Esta función comprueba si metiendo un determinado input a un programa
      devuelve el output esperado.  '''
  #if not inputs:
  #  inputs = [[None] for out in expected_outputs] #If ther's no inputs a None's list would be created.

  r_exercise = 'import sys\nold_stdout, sys.stdout = sys.stdout, open(r"log.txt", "w")\n' + exercise + '\nsys.stdout = old_stdout' #Redirects the output to a folder that can be later readed.
  passed = 0 #Successfully passed tests
  for inpt, output in zip(inputs, expected_outputs):
    #In order to give information every time an input is given, a list with all the inputs is created, and the elements of that are being picked progressively.
    exercise = 'inputs = {}\n'.format(inpt) + r_exercise.replace('input()', 'inputs.pop(0)')
    exec(exercise, globals()) #Ejecuta el ejercicio
    with open('log.txt') as f:
      a = f.read()
      if a == output: #Checks whether the output is the expected one or not.
        passed += 1
  return passed, len(expected_outputs)

#Inputs and expected outputs for all the problems: 
input1 = [['Pepe'], ['Lucas'], ['Paco']]
output1 = ['Hello world, my name is Pepe\n',
            'Hello world, my name is Lucas\n',
            'Hello world, my name is Paco\n']

input2 = [['3', 'Rex'], ['14', 'Paco'], ['2', 'Manolo']]
output2 = ['Rex is 24 human years old\n',
          'Paco is 68 human years old\n',
          'Manolo is 20 human years old\n']

input3 = [['7', '133', '256', '1389', '127', '0']]
output3 = ['7 is prime\n133 is not prime\n256 is not prime\n1389 is not prime\n127 is prime\n']

input4 = [['As I pee, sir, I see Pisa',
          'I am writing a palindrome program',
          'Anula la Luna', 'Palindrome!']]
output4 = ['"As I pee, sir, I see Pisa" is a palindrome\n"I am writing a palindrome program" is not a palindrome\n"Anula la Luna" is a palindrome\n']

input5 = [['GCGCTTA', 'AAAACCCGGT', 'GCTA', '.']]
output5 = ['TAAGCGC\nACCGGGTTTT\nTAGC\n']

input6 = [['5', 'born in the usa', 'destiny', 'roxanne', 'message in a bottle', 'born in the usa'],
          ['6', 'yesterday', 'hey jude', 'like a rolling stone', 'yesterday', 'yesterday', 'hey jude']]
output6 = ['2 born in the usa\n1 destiny\n1 roxanne\n1 message in a bottle\n',
            '3 yesterday\n2 hey jude\n1 like a rolling stone\n']

input7 = [['4', '1.13 USD', '0.74 GBP', '1.05 CHF', '7.08 CY',
          '5.00 USD in CHF', '2.50 GBP in CY', '2.00 USD in EUR', '.']]
output7 = ['5.00 USD = 4.65 CHF\n2.50 GBP = 23.92 CY\n2.00 USD = 1.77 EUR\n']

soluciones =  [[output1,input1],
              [output2,input2],
              [output3,input3],
              [output4,input4],
              [output5,input5],
              [output6,input6],
              [output7,input7]]
