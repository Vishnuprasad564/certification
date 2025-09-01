marks = (30,35,40,25,46)
print(max(marks))
print(min(marks))
if marks:
    avg = sum(marks)/len(marks)
    print(f"Average: {avg}")

else:
    print("empty set")
