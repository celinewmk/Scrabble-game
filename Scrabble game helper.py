def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name

def clean_word(word):
    '''(str)->str
    Returns a new string which is lowercase version of the given word
    with special characters and digits removed

    The returned word should not have any of the following characters:
    ! . ? : , ' " - _ \ ( ) [ ] { } % 0 1 2 3 4 5 6 7 8 9 tab character and new-line character

    >>> clean_word("co-operate.")
    'cooperate'
    >>> clean_word("Anti-viral drug remdesivir has little to no effect on Covid patients' chances of survival, a study from the World Health Organization (WHO) has found.")
    'antiviral drug remdesivir has little to no effect on covid patients chances of survival a study from the world health organization who has found'
    >>> clean_word("1982")
    ''
    >>> clean_word("born_y1982_m08\n")
    'bornym'

    '''
    word = word.lower()
    string=''
    for x in word:
        if x in "!.?:,'\"-_\()[]{}%0123456789\t\n":
            string = string
        else:
            string = string + x
    return string


def test_letters(w1, w2):
    '''(str,str)->bool
    Given two strings w1 and w2 representing two words,
    the function returns True if w1 and w2 have exactlly the same letters,
    and False otherwise

    >>> test_letters("listen", "enlist")
    True
    >>> test_letters("eekn", "knee")
    True
    >>> test_letters("teen", "need")
    False
    '''
    w1 = list(w1)
    w2 = list(w2)
    w1.sort()
    w2.sort()
    if w1==w2:
        return True
    else:
        return False
    
def create_clean_sorted_nodupicates_list(s):
    '''(str)->list of str
    Given a string s representing a text, the function returns the list of words with the following properties:
    - each word in the list is cleaned-up (no special characters nor numbers)
    - there are no duplicated words in the list, and
    - the list is sorted lexicographicaly (you can use python's .sort() list method or sorted() function.)

    This function must call clean_word function.

    You may find it helpful to first call s.split() to get a list version of s split on white space.
    
    >>> create_clean_sorted_nodupicates_list('able "acre bale beyond" binary boat brainy care cat cater crate lawn\nlist race react cat sheet silt slit trace boat cat crate.\n')
    ['able', 'acre', 'bale', 'beyond', 'binary', 'boat', 'brainy', 'care', 'cat', 'cater', 'crate', 'lawn', 'list', 'race', 'react', 'sheet', 'silt', 'slit', 'trace']

    >>> create_clean_sorted_nodupicates_list('Across Europe, infection rates are rising, with Russia reporting a record 14,321 daily cases on Wednesday and a further 239 deaths.')
    ['', 'a', 'across', 'and', 'are', 'cases', 'daily', 'deaths', 'europe', 'further', 'infection', 'on', 'rates', 'record', 'reporting', 'rising', 'russia', 'wednesday', 'with']
    '''
    s = s.split()
    new_list = []
    for i in range(len(s)):
        new_list.append(clean_word(s[i]))
    new_list.sort()
    i=0
    while i<(len(new_list))-1:
        if new_list[i]==new_list[i+1]:
            new_list.pop(i+1)
        else:
            i = i +1
    return new_list
            
            

def word_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - a string (representing a word)
    - wordbook is a list of words (with no words duplicated)

    This function should call test_letters function.

    The function returs a (lexicographicaly sorted) list of anagrams of the given word in wordbook

    >>> word_anagrams("listen", wordbook)
    ['enlist', 'silent', 'tinsel']
    >>> word_anagrams("race", wordbook)
    ['acre', 'care']
    >>> word_anagrams("care", wordbook)
    ['acre', 'race']
    >>> word_anagrams("year", wordbook)
    []
    >>> word_anagrams("ear", wordbook)
    ['are', 'era']
    '''
    new_list = []
    for i in range(len(wordbook)):  
        if test_letters(word,wordbook[i])==True and word!=wordbook[i]:
            new_list.append(wordbook[i])
    new_list.sort()
    return new_list
        


    
##############################
# main
##############################
wordbook=open("english_wordbook.txt").read().lower().split()
list(set(wordbook)).sort()

print("***** WELCOME TO YOUR SCRABBLE GAME HELPER *****")

flag=True
while flag:
    letters = input("Enter the letters that you have, one after another with no space: ")
    if ' ' in letters:
        print("Error: You entered space(s).")
    else:
        while flag:
            x = input("Would you like help forming a word with\n1. all these letters\n2. all but one of these letters?\n").strip()
            if x!='1' and x!='2':
                print("You must choose 1 or 2. Please try again.")
            elif x=='1':
                if word_anagrams(letters,wordbook)==[] and letters not in wordbook:
                    print("There is no word comprised of exactly these letters")
                else:
                    print("Here are the words that are comprised of exactly these letters:")
                    anagram = word_anagrams(letters,wordbook)
                    if letters in wordbook:
                        anagram.append(letters)
                    anagram.sort()
                    print(anagram)
                flag=False
            elif x=='2':
                print("The letters you gave are:",letters)
                print("Let's see what we can get if we ommit one of these letters.")
                new_letters = list(letters)
                for i in range(len(new_letters)):
                    new_letters.pop(i)
                    new_word = ''
                    for x in range(len(new_letters)):
                        new_word = new_word + new_letters[x]
                    print("Without the letter in position " + str(i+1) + " we have the letters " + new_word)
                    if word_anagrams(new_word, wordbook)==[] and new_word not in wordbook:
                        print("There is no word comprised of letters:",new_word)
                    else:
                        print("Here are the words that are comprised of letters:",new_word)
                        anagram = word_anagrams(new_word,wordbook)
                        if new_word in wordbook:
                            anagram.append(new_word)
                        anagram.sort()
                        print(anagram)       
                    new_letters = list(letters)
                flag=False
                    
                                        
                
print("Good bye")


