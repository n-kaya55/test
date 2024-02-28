# bellekte yer işgal etmeyen iterator uretir

# def cube():
#     for i in range(5):
#         yield i ** 3

# for i in cube():
#     print(i)

#eger koseli parantez olsaydı list te tutacaktı ama () normal paranteze koyup generator yaptı.
generator = (i**3 for i in range(5))
print(generator)

for i in generator:
    print(i)
# print(next(generator))
# print(next(generator))
# print(next(generator)) 