from BaiduMapPoi.orm.operate import Operate
from BaiduMapPoi import setting

# engine = create_engine('mysql+pymysql://root:byd123@localhost:3306/house_spider?charset=utf8')
# DBSession = sessionmaker(bind=engine)
# session = DBSession()
#
# all = session.query(Community).filter(Community.lat == None).limit(10).all()
# i = 0
# for x in all:
#     bd = BaiduApi(x.address)
#     x.lat = bd.lat
#     x.lng = bd.lng
#     i = i + 1
#
# session.commit()
#
# print(i)
op = Operate(setting.DB_CONFIG)
communities = op.query_community(100)
for com in communities:
    op.insert(com)
op.commit()
op.finish()
