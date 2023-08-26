#Can you change the self parameter inside a class to something else(say "harry").Try Changing "slf" or "harry" and see the effects.

class Change:
    def __init__(slf):
        print("It works")

    def harry(harry):
        print("This works too.")
c=Change()
c.harry()

#YES it WORKS EVEN IF WE PUT "slf" or "harry"