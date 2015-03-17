# coding: utf-8

import urllib
import math

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

cities = set(["adana" , u"adıyaman" , "afyonkarahisar" , u"ağrı" , "aksaray" , "amasya" , "ankara" ,"antalya" , "ardahan" ,
 "artvin" , u"aydın" , u"balıkesir" , u"bartın" , "batman" , "bayburt" , "bilecik" ,  u"bingöl" , "bitlis" , "bolu" , "burdur" , "bursa" ,
 u"çanakkale" ,u"çankırı" , u"çorum" , "denizli" , u"diyarbakır" , u"düzce" ,  "edirne" , u"elazığ" , "erzincan" , "erzurum" , u"eskişehir" , "gaziantep" , "giresun" ,u"gümüşhane" ,"hakkari" , "hatay" ,u"ığdır" , u"ısparta" ,"istanbul" , "izmir" , u"kahramanmaraş" ,
 u"karabük" , "karaman" , "kars" , "kastamonu" , "kayseri" , u"kırıkkale" , u"kırklareli" , u"kırşehir" , "kilis" , "kocaeli" , "konya" ,   u"kütahya" , "malatya" , "manisa" , "mardin" , "mersin" , u"muğla" , "mugla" , u"muş" , u"nevşehir" , u"niğde" , "ordu" , "osmaniye" , "rize" , "sakarya" , "samsun" , "siirt" , "sinop" , "sivas" u"şanlıUrfa" , u"şırnak" , u"tekirdağ" , "tokat" , "trabzon" , "tunceli" , u"uşak" , "van" , "yalova" , "yozgat" , "zonguldak"])

cities2 = set()
for city in cities:
  city2 = urllib.quote(city.encode("utf-8"))
  if city2 != city: cities2.add(city2)


benzeyen=dict()
for city in cities:
  benzeyen[city] = {}

tag_fr = {}

def add_tags(city, tags, user):
   global benzeyen
   city_data = benzeyen[city]
   for t in tags:
     if t == city: continue
     if not city_data.get(t): city_data[t] = { 'count': 0, 'users': set() }
     tag_data = city_data[t]
     if True or not user in tag_data['users']:
        tag_data['count'] += 1
        # tag_data['users'].add(user)
   

def readfile(part):
   filename ="data/yfcc100m_dataset-%d" % part
   f = open(filename, "r")
   for i,line in enumerate(f):
      arr = line.split("\t") 
      """ print arr:  ['6856867812', '22002814@N00', 'AHOME+PHOTO', '2012-03-16 15:48:23.0', '1332340107', 'Canon+EOS-1D+Mark+IV', 'IMG_6811_%E8%AA%BF%E6%95%B4%E5%A4%A7%E5%B0%8F', '', '', '', '', '', '', 'http://www.flickr.com/photos/22002814@N00/6856867812/', 'http://farm8.staticflickr.com/7096/6856867812_d1a645cdd0.jpg', 'Attribution-NonCommercial-ShareAlike License', 'http://creativecommons.org/licenses/by-nc-sa/2.0/', '7096', '8', 'd1a645cdd0', '3d7e9fe1f5', 'jpg', '0\n'] """

      if (arr[22] == 1): continue    # if video bypass loop 
      tags = set(arr[8].split(",")) #print tags set(['dcsf', 'drupalcon'])
      if (len(tags) >= 1):
       for t in tags:
          cnt = tag_fr.get(t, 0)
          tag_fr[t] = cnt + 1
       if any(city in tags for city in cities):          
           #print i,(tags & cities),arr[13] 
	   for t in (tags & cities):
              if (len(tags) >= 2): add_tags(t, tags, arr[1])
              """print found {u'mu\u011fla': [], 'karaman': [], 'istanbul': ['http://www.flickr.com/photos/23748404@N00/8203127516/'], 'urfa': [], 'ankara': [], 'adana': [], 'antalya': [], 'konya': [], 'izmir': []}
 """ 	      
 	      

               
      if any(city in tags for city in cities2):
           #print i,(tags & cities2),arr[13]
           for t in (tags & cities2):
              city = urllib.unquote(t).decode("utf8")
              if (len(tags) >= 2): add_tags(city, tags, arr[1])

      
 

      	   
		
               
      if i==10000000: break
         
   print "TOTAL" , i
   f.close()
   return i  # total lines
   
N = readfile(2)

results = {}
for city, data in benzeyen.items():
  # if data == {}: continue
  for tag, val in data.items():
     tfidf = val['count'] * math.log(N/tag_fr[tag]) 
     if val['count'] > 3:
        val['score'] = tfidf
        # print "%s  ->   %s:%d (tfidf=%f)" % (city, tag, val['count'], tfidf)  
     else:
        val['score'] = tfidf / 2

for city, data in benzeyen.items():
    results[city] = sorted(data.items(), key=lambda x: x[1]['score'], reverse=True)

for city, data in results.items():
  for (tag,val) in data: 
     print "%s  ->   %s:%d (tfidf=%f)" % (city, tag, val['count'], val['score']) 
	       
               
#print found























