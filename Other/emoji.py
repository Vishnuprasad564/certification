def emojiReplace():
    emo = input("Enter your message:  ").lower()

    if "sad" in emo:
        emo = emo.replace("sad", "🥲") 
        print(f"Converted message: {emo}")

    elif "happy" in emo:
        emo = emo.replace("happy", "😊") 
        print(f"Converted message: {emo}")

    else:
        print("bye")

emojiReplace()
