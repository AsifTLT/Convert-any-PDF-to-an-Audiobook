import pyttsx3
import PyPDF2

book = open("Pdf/OOP_10122018.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()

for num in range(7, pages):
    page = pdfReader.getPage(5)
    text = page.extractText()
    speaker.say(text)
    # speaker.say("Can i talk to You?")
    speaker.runAndWait()