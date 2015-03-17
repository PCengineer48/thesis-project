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

cities = set(["adana" , u"adıyaman" , "afyonkarahisar" , u"ağrı" , "aksaray" , "amasya" , "ankara" ,"antalya" , "ardahan" ,
 "artvin" , u"aydın" , u"balıkesir" , u"bartın" , "batman" , "bayburt" , "bilecik" ,  u"bingöl" , "bitlis" , "bolu" , "burdur" , "bursa" ,
 u"çanakkale" ,u"çankırı" , u"çorum" , "denizli" , u"diyarbakır" , u"düzce" ,  "edirne" , u"elazığ" , "erzincan" , "erzurum" , u"eskişehir" , "gaziantep" , "giresun" ,u"gümüşhane" ,"hakkari" , "hatay" ,u"ığdır" , u"ısparta" ,"istanbul" , "izmir" , u"kahramanmaraş" ,
 u"karabük" , "karaman" , "kars" , "kastamonu" , "kayseri" , u"kırıkkale" , u"kırklareli" , u"kırşehir" , "kilis" , "kocaeli" , "konya" ,   u"kütahya" , "malatya" , "manisa" , "mardin" , "mersin" , u"muğla" , "mugla" , u"muş" , u"nevşehir" , u"niğde" , "ordu" , "osmaniye" , "rize" , "sakarya" , "samsun" , "siirt" , "sinop" , "sivas" u"şanlıUrfa" , u"şırnak" , u"tekirdağ" , "tokat" , "trabzon" , "tunceli" , u"uşak" , "van" , "yalova" , "yozgat" , "zonguldak" ,"taksim" , "fenerbahce" , "galatasaray" , "kordon" , "galatasaray"])

cities2 = set()
for city in cities:
  city2 = urllib.quote(city.encode("utf-8"))
  if city2 != city: cities2.add(city2)


benzeyen=dict()
benzeyen= {"istanbul":["taksim" , "fenerbahce" ,"galatasaray"] , "izmir":["kordon"]  }

found = dict()
for city in cities:
  found[city] = [] #print found {u'mu\u011fla': [], 'karaman': [], 'istanbul': [], 'urfa': [], 'ankara': [], 'adana': [], 'antalya': [], 'konya': [], 'izmir': []}


def readfile(part):
   filename ="data/yfcc100m_dataset-%d" % part
   f = open(filename, "r")
   for i,line in enumerate(f):
      arr = line.split("\t") 
      """ print arr:  ['6856867812', '22002814@N00', 'AHOME+PHOTO', '2012-03-16 15:48:23.0', '1332340107', 'Canon+EOS-1D+Mark+IV', 'IMG_6811_%E8%AA%BF%E6%95%B4%E5%A4%A7%E5%B0%8F', '', '', '', '', '', '', 'http://www.flickr.com/photos/22002814@N00/6856867812/', 'http://farm8.staticflickr.com/7096/6856867812_d1a645cdd0.jpg', 'Attribution-NonCommercial-ShareAlike License', 'http://creativecommons.org/licenses/by-nc-sa/2.0/', '7096', '8', 'd1a645cdd0', '3d7e9fe1f5', 'jpg', '0\n'] """

      if (arr[22] == 1): continue    # if video bypass loop 
      tags = set(arr[8].split(",")) #print tags set(['dcsf', 'drupalcon'])
      if (len(tags) > 1):
       if any(city in tags for city in cities):          
           #print i,(tags & cities),arr[13] 
	   for t in (tags & cities):
              found[t].append(arr[13])
              """print found {u'mu\u011fla': [], 'karaman': [], 'istanbul': ['http://www.flickr.com/photos/23748404@N00/8203127516/'], 'urfa': [], 'ankara': [], 'adana': [], 'antalya': [], 'konya': [], 'izmir': []}
 """ 	      
 	      

               
      if any(city in tags for city in cities2):
           #print i,(tags & cities2),arr[13]
           for t in (tags & cities2):
              found[urllib.unquote(t).decode("utf8")].append(arr[13])

      
 
      if any(benz in tags for k ,v in benzeyen.items() for benz in v  ):
	   
           for benz1 in tags:
		for k ,v in benzeyen.items():
			for benz2 in v:
				if(benz1==benz2):
                                 
				    found[k].append(arr[13])
                                    #print found[k]
				    #print "\n"
				    #print len(found[k])
				    #print "\n"
				    #unique=set(found[k])
                                    #print unique
				    print benz1
				    print len(benz1)
      	   
		
               
      if i==100000: break
         
    
   f.close()
   
readfile(2)

for city in cities:
	       for i in range(len(found[city])):
			city_filenames = "data/iller/" + city + ".txt"
			f1 = open(city_filenames, "a") 
	       		print >>f1,found[city][i]       
	       
               

#print found























