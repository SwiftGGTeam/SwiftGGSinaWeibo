# -*- coding: utf-8 -*-

from spider.spider import Spider
import spider.swiftgg as swiftgg


spiders = [
      Spider(swiftgg.HOME_URL, swiftgg.SwiftGGParser()),
]

currentIndex = 0
count = len(spiders)

def getText():
      spider = nextSpider()
      text = spider.getAMessage()
      return text

def nextSpider():
      global currentIndex
      spider = spiders[currentIndex]
      currentIndex = (currentIndex + 1) % count
      return spider


if __name__ == '__main__':
      for i in range(2 * count):
            print ("%d: %s" % (i, getText()))
