def emojireP(text):
    emoji = {
        "happy":"😊",
        "sad":"🥺",
        "angry":"🤬",
         "monica":"💃"}
    for key,value in emoji.items():
        text = text.replace(key,value)
    return text
msg = input("Enter your messsage: ").lower()
output = emojireP(msg)
print(output)