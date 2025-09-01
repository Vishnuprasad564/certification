sa = {"Gym","Music","football","tennis"}
sb = {"tennis","kungfu","travelling"}
hobbies = sa.intersection(sb)
print("common hobbies",hobbies)
c_hobbies = sa.union(sb)
print("All hobbies",hobbies)
only_a = sa-sb
print("hobbies unique for A: ", only_a)