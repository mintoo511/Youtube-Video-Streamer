if __name__=='__main__':

  import bs4,requests
  import sys
  import gtk,webkit
  import os

  searchterm='+'.join(sys.argv[1:])
  text=requests.get('https://www.youtube.com/results?search_query='+searchterm).text
  soup=bs4.BeautifulSoup(text)
  div=[d for d in soup.find_all('div') if d.has_attr('class') and 'yt-lockup-dismissable' in d['class']]
  i=0
  urllist=[]
  title=[]
  time=[]
  for d in div:
    i=i+1
    img0=d.find_all('img')[0]
    a0=d.find_all('a')[0]
    imgl=img0['src'] if not img0.has_attr('data-thumb') else img0['data-thumb']
    a0=[x for x in d.find_all('a') if x.has_attr('title')][0]
    t=d.find_all('span')[1]
    urllist.append('http://www.youtube.com'+a0['href'])
    title.append(a0['title'])
    #time.append(str(t))
    s=str(t)
    time=""
    a,b=0,0
    for c in s:
      if c=='<':
        a=a+1
      if a==2:
        break
      if b==1:
        time+=c  
      if c=='>':
        b=1
    #print(imgl,'http://www.youtube.com'+a0['href'],a0['title'])
    print "\n--------------------------------------------------------------\n"
    print i,a0['title']
    print "  time:",time
  maxn=i  
  print "\nenter choice"
  x=int(input())
  print "you entered"
  print x
  if x>maxn:
    print "invalid choice"
 # print(urllist[x-1])  
  #s='https://www.youtube.com/v/'+urllist[x-1][-11:]
  s=urllist[x-1]
  print s
  # print "for vlc enter 1 else press 2"
  # x=int(input())
  # if x!=1 and x!=2 :
  #   print 'invalid choice'
  # else:
  #   if x==1:
  #     os.system('vlc '+s)
    
  win=gtk.Window()
  win.connect('destroy',lambda w: gtk.main_quit())
  win.set_icon_from_file("youtube.png")
  win.set_title(title[x-1])
  win.set_default_size(960,640)
  win.set_position(gtk.WIN_POS_CENTER)
  box1=gtk.VBox()
  win.add(box1)

  box2=gtk.HBox()
  box1.pack_start(box2,False)

  scroller=gtk.ScrolledWindow()
  box1.pack_start(scroller)

  web=webkit.WebView()
  web.open(s)
  scroller.add(web)

  # print "press any key to quit\n"
  # if(input()):
  #   sys.exit()
  win.show_all()
  gtk.main()



