from Analyser import Analyser

while True:
    print('Choose an option:\n1) Check your text\n2) Generate random matching string\n3) Quit')
    ans = input()
    if ans == '1':
        print('Enter text: ')
        text = input()
        analyser = Analyser(text)
        if analyser.base_check():
            print(analyser.base_check())
        else:
            print(analyser.analyse())
    elif ans == '2':
        analyser = Analyser('')
        print(analyser.get_random())
    else:
        break
