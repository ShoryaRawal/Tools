from textblob import TextBlob
import pyttsx3

engine = pyttsx3.init()

class textTranslator() :
    while True :
        while True :
            Input = input("Input: ")
            if len(Input) < 3 :
                print("\nCannot translate any word with less then 3 character.")
            elif Input == "exit()" :
                exit(0)
            else :
                break

        Input = TextBlob(u"" + Input)
        detect = Input.detect_language()

        translated = Input.translate(to = "en")
        print(translated)

        engine.say(translated)
        engine.runAndWait()


class FileTranslator() :
    Input = input("File: ")

    File = open(Input, "r")
    Lines = File.readlines()
    for line in Lines :
        translated = line.translate(to = "en")
        print(translated)

if __name__ == "__main__":
    FileTranslator()
