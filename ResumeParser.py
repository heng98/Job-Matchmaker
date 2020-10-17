import PyPDF2
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def read_pdf(filename):
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    count = 0
    resume = ""

    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        resume += pageObj.extractText()

    if resume != "":
        resume = resume

    else:
        resume = textract.process(filename, method='tesseract', language='eng')
        
    pdfFileObj.close()
    text = resume.replace('\n', ' ')

    return text

def read_txt(filename):
    resume = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data = line.replace('\n', '')
            resume.append(data)

    resume = " ".join(resume)
    
    return resume

def resume_parser(filename):
    if filename.endswith('.pdf'):
        return read_pdf(filename)

    elif filename.endswith('.txt'):
        return read_txt(filename)

    else:
        raise NotImplementedError('Currently only support txt file and pdf file')