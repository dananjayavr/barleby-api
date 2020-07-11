def generate_urls(canonical, ceil):
    # https://www.bartleby.com/77/
    # index1.html

    for i in range(1, ceil):
        print(f"\"{canonical}index{i}.html\",")
