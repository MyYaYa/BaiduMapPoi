# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from .entity import *
from ..baidu_api import BaiduApi
import uuid
from ..log import logger

class Operate():

    '''
        Initalization
    '''
    def __init__(self, dbconfig):
        self.dbconfig = dbconfig
        engine = create_engine('mysql+pymysql://%s:%s@localhost:3306/%s?charset=utf8' %
            (self.dbconfig["user"], self.dbconfig["passwd"], self.dbconfig["db"]))
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()
        logger.debug("******** Database Connected! ********\n")
        logger.debug("******** Database Session Created! ********\n")

    def query_community(self, limitation):
        return self.session.query(Community).filter(Community.lat == None).limit(limitation).all()

    '''
        The main insert operate
        com: community object, poi_type: POI type from(ie. bus, subway...)
    '''
    def insert(self, com):
        logger.debug("******** Start Community process: %s ********" % com.title)
        if not com.address:
            return
        bd = BaiduApi(com.address)
        com.lat = bd.lat
        com.lng = bd.lng
        self.session.add(com)
        bus_items = bd.getInfo("公交", 2000)
        for x in bus_items:
            bus = self.session.query(BusStation).filter(and_(BusStation.name == x.get("name"),
                                                            BusStation.lat == x.get("location").get("lat"),
                                                            BusStation.lng == x.get("location").get("lng"))).first()
            if not bus:
                bus = BusStation(id = str(uuid.uuid1()),
                                name = x.get("name"),
                                lat = x.get("location").get("lat"),
                                lng = x.get("location").get("lng"),
                                lines = x.get("address"),)
                self.session.add(bus)
            relation = CommunityBusRelation(id = str(uuid.uuid1()),
                                            community_id = com.id,
                                            bus_station_id = bus.id,
                                            distance = x.get("detail_info").get("distance"),)
            self.session.add(relation)
        logger.debug("          Add into session: 公交")
        subway_item = bd.getInfo("地铁", 2000)
        for x in subway_item:
            subway = self.session.query(SubwayStation).filter(and_(SubwayStation.name == x.get("name"),
                                                                SubwayStation.lat == x.get("location").get("lat"),
                                                                SubwayStation.lng == x.get("location").get("lng"))).first()
            if not subway:
                subway = SubwayStation(id = str(uuid.uuid1()),
                                        name = x.get("name"),
                                        lat = x.get("location").get("lat"),
                                        lng = x.get("location").get("lng"),
                                        lines = x.get("address"),)
                self.session.add(subway)
            relation = CommunitySubwayRelation(id = str(uuid.uuid1()),
                                                community_id = com.id,
                                                subway_station_id = subway.id,
                                                distance = x.get("detail_info").get("distance"),)
            self.session.add(relation)
        logger.debug("          Add into session: 地铁")
        school_items = bd.getInfo("学校", 2000)
        for x in school_items:
            school = self.session.query(School).filter(and_(School.name == x.get("name"),
                                                            School.lat == x.get("location").get("lat"),
                                                            School.lng == x.get("location").get("lng"))).first()
            if not school:
                school = School(id = str(uuid.uuid1()),
                                name = x.get("name"),
                                address = x.get("address"),
                                lat = x.get("location").get("lat"),
                                lng = x.get("location").get("lng"),
                                tag = x.get("detail_info").get("tag"),)
                self.session.add(school)
            relation = CommunitySchoolRelation(id = str(uuid.uuid1()),
                                                community_id = com.id,
                                                school_id = school.id,
                                                distance = x.get("detail_info").get("distance"),)
            self.session.add(relation)
        logger.debug("          Add into session: 学校")
        hospital_items = bd.getInfo("医院", 2000)
        for x in hospital_items:
            hospital = self.session.query(Hospital).filter(and_(Hospital.name == x.get("name"),
                                                                Hospital.lat == x.get("location").get("lat"),
                                                                Hospital.lng == x.get("location").get("lng"))).first()
            if not hospital:
                hospital = Hospital(id = str(uuid.uuid1()),
                                    name = x.get("name"),
                                    address = x.get("address"),
                                    lat = x.get("location").get("lat"),
                                    lng = x.get("location").get("lng"),
                                    tag = x.get("detail_info").get("tag"),)
                self.session.add(hospital)
            relation = CommunityHospitalRelation(id = str(uuid.uuid1()),
                                                    community_id = com.id,
                                                    hospital_id = hospital.id,
                                                    distance = x.get("detail_info").get("distance"),)
            self.session.add(relation)
        logger.debug("          Add into session: 医院")
        commercial_items = bd.getInfo("商圈", 2000)
        for x in commercial_items:
            commercial = self.session.query(CommercialArea).filter(and_(CommercialArea.name == x.get("name"),
                                                                        CommercialArea.lat == x.get("location").get("lat"),
                                                                        CommercialArea.lng == x.get("location").get("lng"))).first()
            if not commercial:
                commercial = CommercialArea(id = str(uuid.uuid1()),
                                            name = x.get("name"),
                                            address = x.get("address"),
                                            lat = x.get("location").get("lat"),
                                            lng = x.get("location").get("lng"),
                                            tag = x.get("detail_info").get("tag"),)
                self.session.add(commercial)
            relation = CommunityCommercialRelation(id = str(uuid.uuid1()),
                                                    community_id = com.id,
                                                    commercial_area_id = commercial.id,
                                                    distance = x.get("detail_info").get("distance"),)
            self.session.add(relation)
        logger.debug("          Add into session: 商圈")
        market_items = bd.getInfo("商场", 2000)
        for x in market_items:
            market = self.session.query(MarketPlace).filter(and_(MarketPlace.name == x.get("name"),
                                                                MarketPlace.lat == x.get("location").get("lat"),
                                                                MarketPlace.lng == x.get("location").get("lng"))).first()
            if not market:
                market = MarketPlace(id = str(uuid.uuid1()),
                                        name = x.get("name"),
                                        address = x.get("address"),
                                        lat = x.get("location").get("lat"),
                                        lng = x.get("location").get("lng"),
                                        tag = x.get("detail_info").get("tag"),)
                self.session.add(market)
            relation = CommunityMarketRelation(id = str(uuid.uuid1()),
                                                community_id = com.id,
                                                market_place_id = market.id,
                                                distance = x.get("detail_info").get("distance"),)
            self.session.add(relation)
        logger.debug("          Add into session: 商场")
        self.session.commit()
        logger.debug("******** Community %s Processed! ********\n" % com.title)

    def commit(self):
        self.session.commit()
        logger.debug("******** Session Commited! ********\n")

    def finish(self):
        self.session.close()
        logger.debug("******** Session finished! ********\n")
