import pickle

with open("test1.pkl", "wb") as f:
    my_list = list(range(1, 11))
    result = pickle.dump(my_list, f)
    print(result)
