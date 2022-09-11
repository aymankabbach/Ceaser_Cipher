alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def get_shift_value_from_the_user():
    wrong_input=True
    while wrong_input==True:
        try:
            user_input=int(input("type the shift number"))
        except ValueError:
            pass
        else:
            wrong_input=False
    return user_input
def get_the_text_from_the_user():
    wrong_input=True
    while wrong_input==True:
        user_input=input("enter the world\n")
        try:
            check_text=int(user_input)
        except ValueError:
            wrong_input=False
        else:
            print("invalid text, try something else")
    return user_input.lower()
def convert_input_To_List(user_word):
    letters_list=[]
    for letter in user_word:
        letters_list.append(letter)
    return letters_list
def coding_The_Word(letters_list,shift):
    global alphabet
    coded_list=[]
    for letter in letters_list:
        if letter in alphabet:
            if alphabet.index(letter)+shift>=len(alphabet):
                coded_list.append(alphabet[alphabet.index(letter)-len(alphabet)+shift])
            else:
                coded_list.append(alphabet[alphabet.index(letter)+shift])
        else:
            coded_list.append(letter)
    return coded_list
def convert_the_list_to_a_Word(coded_list):
    x=0
    coded_word=coded_list[x]
    for letter in range(len(coded_list)-1):
        coded_word+=coded_list[x+1]
        x+=1
    return coded_word
def print_the_word():
    user_word=get_the_text_from_the_user()
    shift=get_shift_value_from_the_user()
    letters_list=convert_input_To_List(user_word)
    coded_list=coding_The_Word(letters_list,shift)
    coded_word=convert_the_list_to_a_Word(coded_list)
    print(coded_word)
print_the_word()