def disp():
    print('hi')
#disp()
def fav(title):
    print('my fav book is '+ title.title())
#fav(title='python')    
def t_shirt(size,text):
    print('The size of the shirt is '+str(size))
    print('The text you need is '+text)
#t_shirt(26,'Jai')
#t_shirt(size=27,text='Forever JAI')
def shirt(size,text='I LOVE PYTHON'):
    print('The size of the shirt is '+size)
    print('The text you need is '+text)
#shirt('medium size')
#shirt('large size')
def describe_city(city,country='India'):
    #print(city.title() +' is in '+country)
     c=city +' is in '+ country
     return c
#a=describe_city(' chennai')
#print(a)
#describe_city(city=' delhi')
#describe_city(city=' kingston',country=' England')
def city_country(city,country):
    print('"',city.title(),',',country.title(),'"' )
#city_country('chennai','india')    
def make_album(album,artist_name,track=''):
    if track:
       a={'album':album,'artist_name':artist_name,'track':track}
    else:
        a={'album':album,'artist_name':artist_name}
    return a
#c=make_album('aaa','bbb')
#d=make_album('cab','tab','bat')
#print(c)
#print(d)
while True:
    print('Enter the album and Title if you want else enter q in both album and/or Title')
    s=input('Album: ')
    d=input('Title: ')
    if s=='q' or d == 'q':
       break
    else:
       f= make_album(s,d)
