from os import system

system('clang++ -std=c++20 -fcolor-diagnostics -fansi-escape-codes -g -Wall -Wextra -Wpedantic -fsanitize=undefined,address ./generator.cpp -o ./generator')
system('clang++ -std=c++20 -fcolor-diagnostics -fansi-escape-codes -g -Wall -Wextra -Wpedantic -fsanitize=undefined,address ./solution.cpp -o ./solution')
system('clang++ -std=c++20 -fcolor-diagnostics -fansi-escape-codes -g -Wall -Wextra -Wpedantic -fsanitize=undefined,address ./ok.cpp -o ./ok')

for i in range(1000):
  print(i)
  system("./generator > in.txt")
  system('./solution < in.txt > solution.txt')
  system('./ok < in.txt > ok.txt')

  with open('D.txt') as my:
    my_text = my.readlines()
 
  with open('ok.txt') as other:
    other_text = other.readlines()

  with open('in.txt') as inp:
    inp_text = inp.readlines()

  print(my_text, other_text)
  if my_text != other_text:
    for i in range(len(inp_text)):
      print(inp_text[i], end='')
    print("WRONG ANSWER")
    break
  else:
    print("PASSED TEST")
