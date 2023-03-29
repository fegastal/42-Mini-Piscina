#!/usr/bin/python3

class Intern:

    # eu defino essa string como "padrão" de nome do estagiário
    def __init__(self, name="My name? I'm nobody, an intern, I have no name."):
        self.name = name

    # retornando uma string
    def __str__(self):
        return self.name

    class Coffee:

        # representa o coffee
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def make_coffee(self):
        return self.Coffee()

    # lida com o erro
    def work(self):
        raise Exception("I'm just an intern, I can't do that...")

def tests():

    estagiario = Intern()
    estagiario1 = Intern("Mark")

    print(estagiario)
    print(estagiario1)
    print(estagiario.make_coffee())
    print(estagiario1.make_coffee())
    print(estagiario.Coffee())
    print(estagiario1.Coffee())

    # tente fazer o estagiário trabalhar (cai dentro)
    try:
            estagiario.work()
    except Exception as e:
            print(e)

if __name__ == '__main__':
    tests()