def main():

    p2 =input("Message:")
    final_mess = convert(p2)
    print(final_mess)


def convert(p2):

    p1 = p2.replace(':)', "🙂")
    frown = p1.replace(':(', "🙁")
    return frown

main()
