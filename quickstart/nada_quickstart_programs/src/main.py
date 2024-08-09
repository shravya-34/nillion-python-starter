# from nada_dsl import *

# def nada_main():
#     party1 = Party(name="Party1")
#     party2 = Party(name="Party2")
#     party3 = Party(name="Party3")
#     a = SecretInteger(Input(name="A", party=party1))
#     b = SecretInteger(Input(name="B", party=party2))

#     result = a + b

#     return [Output(result, "my_output", party3)]


from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    height = SecretInteger(Input(name="my_int1", party=party1))
    weight = SecretInteger(Input(name="my_int2", party=party1))

    return [Output(height, weight, party1)]