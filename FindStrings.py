from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    """
    This class allow as to
    count duplicates.
    """
    pass


def clear_dos():
    """
    A fuction to clear
    the screen.
    We can import os
     and write os.system('cls')
    :return: Does not return nothing.
    """
    print("\n" * 15)


def find_duplicate(word):
    """
    A function to find all
    duplicate letters only.
    :param word: It takes sentence in function
    :return: Returns the result of letters and the times appears.
    """
    return [(ch, cnt) for ch, cnt in OrderedCounter(word).items() if cnt > 1]


def find_letter(sentence, l_search):
    """
    A function to find only
    letters.
    :param sentence:
    In this sentence we search for letter.
    :param l_search:
    l_search is the letter we searching.
    :return: return nothing.
    """
    m = 0
    for i in sentence:
        if i == l_search:
            m += 1

    print(f"\nΤο {l_search} υπάρχει {m} φορές ")


def find_word(sentence, w_search):
    """
    A function to find words.
    :param sentence: In this sentence we search for word.
    :param w_search: w_search is the word we searching.
    :return: return nothing.
    """
    count = 0
    sl = sentence.split(" ")
    for i in range(0, len(sl)):
        if w_search == sl[i]:
            count = count + 1

    print(f"\nΤο {w_search} υπάρχει {count} φορές")


def del_word(sentence, s):
    """
    A function to delete words.
    :param sentence: In this sentence we search for word.
    :param s: s is the word we deleting.
    :return: return nothing.
    """
    new = ""
    for i in range(len(s)):
        if s in sentence:
            # Στην Μέθοδο replace() μπορούμε να δώσουμε μία τιμή για να διαγράψει όσες λέξεις θέλουμε.
            new = sentence.replace(s, "*")
    for j in range(len(new)):
        print(new[j], end="")
    print(" ")


def del_vowels(s):
    """
    A function to delete words.
    :param s: s is the vowel we deleting.
    :return: return nothing.
    """
    vowels = ["α", "ε", "η", "ι", "υ", "ο", "ω", "a", "e", "i", "o", "u", "y"]
    new = list(s)

    for i in range(len(s)):
        if new[i] in vowels:
            new.pop(i)
            new.insert(i, "*")
    for i in range(len(new)):
        print(new[i], end="")


def user_choice(choices):
    """
    Select user choice
    from basic Menu.
    :param choices:
    Input user choice to
    function from Menu.
    """
    flag = 1
    choice = choices

    while flag:
        if choice == 1:
            find_words()
            print("Θέλετε να συνεχίσετε?? (Y/N)")
            ans = input(">>>").upper()
            check_user(ans)
            flag = 0
        elif choice == 2:
            find_letters()
            print("Θέλετε να συνεχίσετε?? (Y/N)")
            ans = input(">>>").upper()
            check_user(ans)
            flag = 0
        elif choice == 3:
            print("Πρόγραμμα μετατροπής φράσεων\n ή κειμένων χωρίς φωνήεντα!!")
            phrase = input("Δώσε μια φράση :").lower()
            print(f"Η φράση που έδωσες είναι :\n{phrase}")
            print("Η φράση τώρα έγινε.....")
            del_vowels(phrase)
            print(" ")
            print("Θέλετε να συνεχίσετε?? (Y/N)")
            ans = input(">>>").upper()
            check_user(ans)
            flag = 0
        elif choice == 4:
            print("Πρόγραμμα διαγραφής φράσεων ή κειμένων!!")
            phrase = input("Δώσε μια φράση :").lower()
            print(f"Η φράση που έδωσες είναι :\n{phrase}")
            print("Τι θέλεις να διαγράψεις ??")
            phrase_to_dell = input(">>>")
            print("Η φράση τώρα έγινε.....")
            del_word(phrase, phrase_to_dell)
            print("Θέλετε να συνεχίσετε?? (Y/N)")
            ans = input(">>>").upper()
            check_user(ans)
            flag = 0
        else:
            if choice <= 0 or choice > 4:
                print("Error in Users choice!!")
                flag = 0


def check_user(user_input):
    """
    A function to check Users input.
    :param user_input: user_input is the User choice.
    :return:
    """
    while user_input != 'Y' or user_input != 'N':
        if user_input == 'Y':
            clear_dos()
            print("Μενού :")
            print("********************")
            print("1.Βρές λέξεις\n2.Βρές γράμματα\n3.Διέγραψε τα φωνήεντα\n4.Διέγραψε λέξεις")
            print("********************")
            print("Επέλεξε μία από τις επιλογές Μενού\n")
            print("ΣΗΜΕΙΩΣΗ : ΑΝ ΔΩΣΕΤΕ ΟΤΙΔΗΠΟΤΕ ΕΚΤΟΣ\nΑΠΟ ΑΡΙΘΜΟ ΤΟ ΠΡΟΓΡΑΜΜΑ ΘΑ ΤΕΡΜΑΤΙΣΕΙ!!\n")
            choice = int(input(">>>"))
            if choice == 1:
                user_choice(choice)
                return
            elif choice == 2:
                user_choice(choice)
                return
            elif choice == 3:
                user_choice(choice)
                return
            elif choice == 4:
                user_choice(choice)
                return
        elif user_input == 'N':
            print("Finish Program!")
            exit(0)
        else:
            clear_dos()
            print("Error! in User choice!!")
            print(" ")
            main()


def find_letters():
    """
    A function to make menu to find letters.
    :return: return nothing.
    """
    print("Θέλετε να ψάξετε σε μια έτοιμη πρόταση (Y/N)?")
    print("Πατήστε A για αυτόματη εύρεση διπλότυπων!!")
    answer = input("\n>>>").upper()

    while (answer == 'Y') or (answer == 'N') or (answer == 'A') or (answer == 'Υ') or (answer == 'Ν') or (
            answer == 'Α'):

        if answer == "Y":
            local_sentence = "the rain in Spain stays mainly in the plain ain"
            print(f"Η πρόταση είναι : \n{local_sentence}")
            local_str_search = input("Ποιό γράμμα αναζητάτε?? \n>>>")
            find_letter(local_sentence, local_str_search)
            break
        elif answer == "N":
            print("Παρακαλώ γράψτε μια πρόταση της αρεσκείας σας... ")
            input_sentence = input("\n>>>")
            print(f"Η πρόταση είναι : \n{input_sentence}")
            input_str_search = input("Ποιό γράμμα αναζητάτε?? \n>>>")
            find_letter(input_sentence, input_str_search)
            break
        elif answer == "A":
            local_sentence = "the rain in Spain stays mainly in the plain ain"
            print(f"Η πρόταση είναι : \n{local_sentence}")
            print(find_duplicate(local_sentence))
            break
        else:
            print("Error!! In users choice!!")
            exit(-1)


def find_words():
    """
    A function to make menu to find words.
    :return: return nothing.
    """
    print("Θέλετε να ψάξετε σε μια έτοιμη πρόταση (Y/N)?")
    print("Πατήστε A για αυτόματη εύρεση διπλότυπων!!")
    answer = input("\n>>>").upper()

    while (answer == 'Y') or (answer == 'N') or (answer == 'A') or (answer == 'Υ') or (answer == 'Ν') or (
            answer == 'Α'):

        if answer == "Y":
            local_sentence = "the rain in Spain stays mainly in the plain ain"
            print(f"Η πρόταση είναι : \n{local_sentence}")
            local_str_search = input("Ποιά λέξη αναζητάτε?? \n>>>")
            find_word(local_sentence, local_str_search)
            break
        elif answer == "N":
            print("Παρακαλώ γράψτε μια πρόταση της αρεσκείας σας... ")
            input_sentence = input("\n>>>")
            print(f"Η πρόταση είναι : \n{input_sentence}")
            input_str_search = input("Ποιά λέξη αναζητάτε?? \n>>>")
            find_word(input_sentence, input_str_search)
            break
        elif answer == "A":
            local_sentence = "the rain in Spain stays mainly in the plain ain"
            print(f"Η πρόταση είναι : \n{local_sentence}")
            print(find_duplicate(local_sentence))
            break
        else:
            print("Error!! In users choice!!")
            exit(-1)


def main():
    """
    main function of program
    """
    print("Μενού :")
    print("********************")
    print("1.Βρές λέξεις\n2.Βρές γράμματα\n3.Διέγραψε τα φωνήεντα\n4.Διέγραψε λέξεις")
    print("********************")
    print("Επέλεξε μία από τις επιλογές Μενού\n")
    print("ΣΗΜΕΙΩΣΗ : ΑΝ ΔΩΣΕΤΕ ΟΤΙΔΗΠΟΤΕ ΕΚΤΟΣ\nΑΠΟ ΑΡΙΘΜΟ ΤΟ ΠΡΟΓΡΑΜΜΑ ΘΑ ΤΕΡΜΑΤΙΣΕΙ!!\n")
    choice = int(input(">>>"))
    user_choice(choice)


main()
