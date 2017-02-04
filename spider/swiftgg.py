# -*- coding: utf-8 -*-

import bs4
import datetime
from utility import attrs2dic


HOME_URL = "http://swift.gg"

class SwiftGGParser:
      def getMsg(self, html):
            soup = bs4.BeautifulSoup( html, "html.parser" )
            items = soup.find_all( attrs={ "class": "post-expand post" } )
            if len(items) > 0:
                  topItem = items[0]
                  time = topItem.header.p.time.string.encode('utf-8')
                  today = datetime.date.today()
                  
                  if time == today:
                        title = topItem.header.h1.a.get( 'title' ).encode('utf-8')
                        url = HOME_URL + topItem.a.get( 'href' ).encode('utf-8')
                        
                        summary = topItem.find('blockquote')
                        
                        source = "原文链接：%s" % (summary.findAll('a')[0].get( 'href' ).encode('utf-8'))
                        translator = "译者：@%s" % (summary.findAll('a')[1].text.encode('utf-8'))
                        proofreader = "校对：@%s" % (summary.findAll('a')[2].text.encode('utf-8'))
                        reviewer = "定稿：@%s" % (summary.findAll('a')[3].text.encode('utf-8'))
                        
                        text = "#SwiftGG# 今日新文：《%s》%s，%s，%s，%s，%s" % ( title, url, source, translator, proofreader, reviewer)
                        return text
            return None



if __name__ == '__main__':

      import zHTTP

      def getMessage():
            html = zHTTP.get(HOME_URL)
            listname = SwiftGGParser()
            return listname.getMsg(html)

      for i in range(3):
            text = getMessage()
            print (text)
