

def mood(M1):
    user = input('What is your name?')

    mood = input('what is your mood?')
    M1 =mood

    if (M1 == ' tired' or M1

            == 'sleepy'):
        print(f'Go home and get some rest{user}')
    elif M1 == 'Happy' or M1 == 'Excited':
        print(f'Nice! i am glad you are {mood} {user}!')
    else:
        print(f'Your mood is not a vibe i guess {user}!')
    quit()


print(mood('happy'))