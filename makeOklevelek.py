import gmail
import requests
from gmail import Authorize,sendMail
from write_on import makePDFCountry,makePDFRegion
from write_on import makeCategory

def mail(csapat):
    if csapat["kategoria"] in ["E+","K+","F"]:
        morsz(csapat)
    else:
        mreg(csapat)

def mreg(csapat):
    print("%s csapat, országos %s, regionális %s helyen végzett, %s kategóriában"%(csapat['csapatnev'],csapat['helyOrszag'],csapat['helyRegio'],csapat['kategoria']))
    for i in range(0,3): #TODO THREADING
        nev = csapat["csapat"][i][0]
        mail = csapat["csapat"][i][1]
        #actualMail = ["horvathhanga125@gmail.com","durerinfo@gmail.com"]
        actualMail = mail
        print("\tEmail küldése %s részére a %s címre (%s)"%(nev,mail,actualMail))
        makePDFRegion(nev,csapat['csapatnev'],csapat['kategoria'],csapat['regioNev'],csapat['helyRegio'],csapat['varos'])
        prettyString = """
Kedves %s!

    Ezúton is gratulálunk a XIII. Dürer versenyen a
    %s csapatban regionálisan elért %s helyezésedhez.

    Csatolva küldünk egy elektromos oklevelet, hogy közösen védjük a környezetet.

Minden jót:
Dürer Szervezők
        """%(nev,csapat['csapatnev'],csapat['helyRegio'])
        sendMail(service,"durerinfo@gmail.com",actualMail,prettyString,"document-output.pdf")

def morsz(csapat):
    print("%s csapat, országos %s, regionális %s helyen végzett, %s kategóriában"%(csapat['csapatnev'],csapat['helyOrszag'],csapat['helyRegio'],csapat['kategoria']))
    for i in range(0,3): #TODO THREADING
        nev = csapat["csapat"][i][0]
        mail = csapat["csapat"][i][1]
        #actualMail = ["horvathhanga125@gmail.com","durerinfo@gmail.com"]
        actualMail = mail
        print("\tEmail küldése %s részére a %s címre (%s)"%(nev,mail,actualMail))
        makePDFCountry(nev,csapat['csapatnev'],csapat['kategoria'],csapat['helyOrszag'],csapat['varos'])
        prettyString = """
Kedves %s!

    Ezúton is gratulálunk a XIII. Dürer versenyen a
    %s csapatban országosan elért %s helyezésedhez.

    Csatolva küldünk egy elektromos oklevelet, hogy közösen védjük a környezetet.

Minden jót:
Dürer Szervezők
        """%(nev,csapat["csapatnev"],csapat["helyOrszag"])
        sendMail(service,"durerinfo@gmail.com",actualMail,prettyString,"document-output.pdf")


service = Authorize()
print("Service authenticated, ready to send.")

URL = "https://script.google.com/macros/s/AKfycbygcaO_CP_Fgg2ddo-tCSYuabnBQNvt9LtUhzaB01CktRwCbdQ/exec"
params = {
    'secret' : "superSecr5781559630etString578155781559630596305781559630",
    'ID' : "1gEMdH_CJCkqr85S5KlrCOxQKbh1Fx5CMCAe_8w_raZE",
    'range' : "Math_raw_data!A1:AA209",
    'header':"true"
}
r = requests.post(url = URL,params = params)
matekData = r.json()
for csapat in matekData['raw']:
    team = {}
    team["csapatnev"] = csapat[3]
    team["helyOrszag"] = csapat[0]
    team["helyRegio"] = csapat[1]
    team["regioNev"] = csapat[5]
    team["varos"] = csapat[4]
    team["csapat"] = [[csapat[22],csapat[19]],[csapat[23],csapat[20]],[csapat[24],csapat[21]]]
#    for tag in team["csapat"]:
#        tag[1] = "tomi@csilling.com"
    team["kategoria"] = ""
    try:
        team["kategoria"]  = makeCategory(csapat[-1])
    except Exception as e:
        print(e)
        team["kategoria"]  = ""
    mail(team)


params = {
    'secret' : "superSecr5781559630etString578155781559630596305781559630",
    'ID' : "1gEMdH_CJCkqr85S5KlrCOxQKbh1Fx5CMCAe_8w_raZE",
    'range' : "NMath_raw_data!A3:AB100",
    'header':"true"
}
r = requests.post(url = URL,params = params)
NmatekData = r.json()
for csapat in NmatekData['raw']:
    team = {}
    team["csapatnev"] = csapat[2]
    team["helyOrszag"] = csapat[0]
    team["helyRegio"] = csapat[-1]
    team["regioNev"] = csapat[4]
    team["varos"] = csapat[3]
    team["csapat"] = [[csapat[21],csapat[18]],[csapat[22],csapat[19]],[csapat[23],csapat[20]]]
#    for tag in team["csapat"]:
#        tag[1] = "tomi@csilling.com"
    team["kategoria"] = ""
    try:
        team["kategoria"]  = makeCategory(csapat[-2])
    except Exception as e:
        print(e)
        team["kategoria"]  = ""
    #print("%s csapat, országos %s, regionális %s helyen végzett, %s-ban"%(csapat[2],csapat[0],csapat[-1],csapat[-2]))
    mail(team)
