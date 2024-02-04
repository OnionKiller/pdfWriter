from reportlab.pdfgen import canvas
from PyPDF4 import PdfFileWriter,PdfFileReader

#retruns ["line0","line1"]
def makeName(s):
    namePieces = s.split(" ",1)
    if len(s)<=22:
        return ["",s]
    else:
        return[namePieces[0],namePieces[1]]
#returns ["line0","line1","line2"]
def makeTeamName(s):
    #print(len(s))
    if len(s)<=25:
        return ["",s,""]
    elif 25<len(s)<=50:
        return [s[0:25],s[25:50],""]
    #elif 50<len(s)<=75:
    #    return [s[0:25],s[25:50],s[50:75]]
    else:
        last = s[25:50]+"..."
        return [s[0:25],last,""]

def makePDFDefault(name, teamname,cat,place):
    c = canvas.Canvas("szoveg.pdf")
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    pdfmetrics.registerFont(TTFont('Comic Sans MS', 'comic.ttf'))
    c.setFont('Comic Sans MS',15)
    lines = makeName(name)
    c.drawCentredString(432,426,lines[0])
    c.drawCentredString(432,406,lines[1])
    #teamname
    offset = 0
    if len(teamname)<=15:     
        c.setFont('Comic Sans MS',20)
        offset = -10
    lines = makeTeamName(teamname)
    c.drawCentredString(432,359,lines[0])
    c.drawCentredString(432,341 + offset,lines[1])
    c.drawCentredString(432,323,lines[2])
    #category
    c.setFont('Comic Sans MS',17)
    c.drawCentredString(432,292,cat)
    #place
    c.setFont('Comic Sans MS',20)
    c.drawCentredString(432,250,str(place)+'.')
    c.showPage()
    c.save()
    w = PdfFileReader(open("szoveg.pdf","rb"))
    o = PdfFileWriter()
    i = PdfFileReader(open("helyif_okl_nagyok.pdf","rb"))
    ip = i.getPage(0)
    ip.mergePage(w.getPage(0))
    o.addPage(ip)
    with open("document-output.pdf", "wb") as outputStream:
        o.write(outputStream)

def makePDFCountry(name, teamname,cat,place,placeName = ""):
    c = canvas.Canvas("szoveg.pdf")
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    pdfmetrics.registerFont(TTFont('Comic Sans MS', 'comic.ttf'))
    pdfmetrics.registerFont(TTFont('Freestyle Script', 'FREESCPT.TTF'))
    c.setFont('Comic Sans MS',15)
    lines = makeName(name)
    c.drawCentredString(432,426,lines[0])
    c.drawCentredString(432,406,lines[1])
    #teamname
    offset = 0
    if len(teamname)<=15:     
        c.setFont('Comic Sans MS',20)
    lines = makeTeamName(teamname)
    c.drawCentredString(432,359,lines[0])
    c.drawCentredString(432,341 + offset,lines[1])
    #c.drawCentredString(432,323,lines[2])
    #category
    c.setFont('Comic Sans MS',17)
    c.drawCentredString(432,310,cat)
    #place
    c.setFont('Comic Sans MS',20)
    if str(place)[-1] == '.':
        place = place[0:-1]
    c.drawCentredString(432,250,str(place)+'.')
    #ort
    c.setFont('Freestyle Script',18)
    c.setFillColorRGB(54/255,93/255,173/255,0.9)
    c.setStrokeColorRGB(54/255,93/255,173/255,0.5)
    c.rotate(8)
    c.drawString(289,118,placeName)
    c.showPage()
    c.save()
    w = PdfFileReader(open("szoveg.pdf","rb"))
    o = PdfFileWriter()
    i = PdfFileReader(open("helyif_okl_nagyok_orszagos_jpg.pdf","rb"))
    ip = i.getPage(0)
    ip.mergePage(w.getPage(0))
    o.addPage(ip)
    with open("document-output.pdf", "wb") as outputStream:
        o.write(outputStream)

def makePDFRegion(name, teamname,cat,region,place,placeName = ""):
    c = canvas.Canvas("szoveg.pdf")
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    pdfmetrics.registerFont(TTFont('Comic Sans MS', 'comic.ttf'))
    pdfmetrics.registerFont(TTFont('Freestyle Script', 'FREESCPT.TTF'))
    c.setFont('Comic Sans MS',15)
    lines = makeName(name)
    c.drawCentredString(432,426,lines[0])
    c.drawCentredString(432,406,lines[1])
    #teamname
    offset = 0
    if len(teamname)<=15:     
        c.setFont('Comic Sans MS',20)
    lines = makeTeamName(teamname)
    c.drawCentredString(432,359,lines[0])
    c.drawCentredString(432,341 + offset,lines[1])
    #c.drawCentredString(432,323,lines[2])
    #category
    c.setFont('Comic Sans MS',17)
    c.drawCentredString(435,307,cat)
    #region
    c.setFont('Comic Sans MS',15)
    c.drawCentredString(435,276,region)
    #place
    c.setFont('Comic Sans MS',19)
    if str(place)[-1] == '.':
        place = place[0:-1]
    c.drawCentredString(432,242,str(place)+'.')
    #ort
    c.setFont('Freestyle Script',18)
    c.setFillColorRGB(54/255,93/255,173/255,0.9)
    c.setStrokeColorRGB(54/255,93/255,173/255,0.5)
    c.rotate(8)
    c.drawString(289,118,placeName)
    c.showPage()
    c.save()
    w = PdfFileReader(open("szoveg.pdf","rb"))
    o = PdfFileWriter()
    i = PdfFileReader(open("helyif_okl_nagyok_regios_jpg.pdf","rb"))
    ip = i.getPage(0)
    ip.mergePage(w.getPage(0))
    o.addPage(ip)
    with open("document-output.pdf", "wb") as outputStream:
        o.write(outputStream)

def makeCategory(categoryStr):
    if(categoryStr == "F kategória"):
        return "F"
    if(categoryStr == "K+ kategória"):
        return "K+"
    if(categoryStr == "K kategória"):
        return "K"
    if(categoryStr == "C kategória"):
        return "C"
    if(categoryStr == "D kategória"):
        return "D"
    if(categoryStr == "E kategória"):
        return "E"
    if(categoryStr == "E+ kategória"):
        return "E+"
    raise ValueError('Ne létező kategória:'+categoryStr)
    #return ""

#debug
if __name__ == "__main__":
   makePDFRegion("Csilling Tamás","Paralelepipedonok","D+","Budapest",1,"Budapest")
   makePDFCountry("Csilling Tamás","Paralelepipedonok","D+",1,"BácsKisés")