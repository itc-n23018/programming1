my_list = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama", "gunma"]

result = []
for i in my_list:
    if len(i) >= 6:
        result.append(i)

print(result)
