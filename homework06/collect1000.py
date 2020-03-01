from scraputils import *
from db import News, session, Base, engine

Base.metadata.create_all(bind=engine)
f = session()
news1000 = get_news('https://news.ycombinator.com/newest', 34)
for new in news1000:
    tmp = News(title=new['title'], 
                author=new['author'],
                url=new['url'],
                comments=new['comments'],
                points=new['points'])
    f.add(tmp)
    f.commit()
        
    