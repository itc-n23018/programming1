class dog:
    cry = "ワン"
    legs = 4
    is_animal = True


tama = dog()
result = "鳴き声: {}, 足の数:{}, 動物: {}".format(tama.cry, tama.legs, tama.is_animal)
print(result)
