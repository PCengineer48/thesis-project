# coding: utf-8

import urllib

fields = [ "Photo/video identifier",
"User NSID",
"User nickname", 
"Date taken", 
"Date uploaded", 
"Capture device", 
"Title", 
"Description", 
"User tags (comma-separated)", 
"Machine tags (comma-separated)", 
"Longitude", 
"Latitude", 
"Accuracy", 
"Photo/video page URL", 
"Photo/video download URL", 
"License name", 
"License URL", 
"Photo/video server identifier", 
"Photo/video farm identifier", 
"Photo/video secret", 
"Photo/video secret original", 
"Photo/video extension original", 
"Photos/video marker (0 = photo, 1 = video)" ]

cities = set(["istanbul", "ankara", "izmir", "bursa", "adana", "eskişehir", "antalya", "gaziantep", u"muğla", "denizli", "konya", "kocaeli","mersin","kayseri","sakarya","manisa","samsun","yalova","trabzon","edirne",u"karabük","karabuk",u"balıkesir","balikesir",u"ısparta","isparta","malatya",
u"çanakkale","canakkale","erzurum",u"kırıkkale","kirikkale",u"tekirdağ","tekirdag","bolu",u"uşak","usak",u"aydın","aydin","ordu","sivas",u"kütahya","kutahya","afyon",u"çorum","corum","giresun",u"diyarbakır","diyarbakir",u"elazığ","elazig"
u"kahramanmaraş","kahramanmaras","burdur","rize","bilecik","zonguldak",u"nevşehir","nevsehir","artvin","karaman","tunceli",u"düzce","duzce",u"kırşehir","kirsehir",u"kırklareli","kirklareli",u"çankırı","cankiri","sinop",
"kastamonu","hatay","osmaniye","tokat","erzincan","yozgat","batman",u"şanlıurfa","sanliurfa","van",u"niğde","nigde","amasya","aksaray",u"gümüşhane","gumushane",u"adıyaman","adiyaman","kilis",
"siirt","kars","mardin","bartin",u"bartın","hakkari",u"şırnak","sirnak",u"ığdır","igdir","bayburt","bitlis",u"bingöl","bingol","agri",u"ağrı","ardahan","mus",u"muş"])


# cities listesi 71 il
# her set elemanı için o isimle 

cities2 = set()
for city in cities:
  city2 = urllib.quote(city.encode("utf-8"))
  if city2 != city: cities2.add(city2)

print cities2

# cities = set(["cambodia", "365"])

found = dict()
for city in cities:
  found[city] = []

def readfile(part):
   filename = "yfcc100m_dataset-%d" % part
   f = open(filename, "r")
   for i,line in enumerate(f):
      arr = line.split("\t")
      if (arr[22] == 1): continue    # if video bypass loop      
      # for j,v in enumerate(arr):
         # print "%d %s : %s" % (j,fields[j], v)    
      tags = set(arr[8].split(","))
      if (len(tags) > 1):
        if any(city in tags for city in cities):          
           print i,(tags & cities),arr[13] 
           for t in (tags & cities):
              found[t].append(arr[13]) 
        if any(city in tags for city in cities2):
           print i,(tags & cities2),arr[13]
           for t in (tags & cities2):
              found[urllib.unquote(t).decode("utf8")].append(arr[13])         
      # if i==50: break
   print "LAST", i
   f.close()
   
readfile(2)
found
