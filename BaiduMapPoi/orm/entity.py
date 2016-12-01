# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Float, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import func

Base = declarative_base()

class Community(Base):
    __tablename__ = "community"
    id = Column(String(36), primary_key=True)
    source = Column(String(10))
    title = Column(String(64))
    internal_id = Column(String(64))
    district = Column(String(10))
    address = Column(String(64))
    total_buildings = Column(String(64))
    total_houses = Column(String(64))
    build_type = Column(String(64))
    build_time = Column(String(64))
    developer = Column(String(64))
    property = Column(String(64))
    property_fee = Column(String(64))
    parking_num = Column(String(64))
    green_rate = Column(String(10))
    plot_rate = Column(String(10))
    lat = Column(Float(32))
    lng = Column(Float(32))
    update_time = Column(TIMESTAMP(), default=func.now())

class CommunityPriceHistory(Base):
    __tablename__ = "community_price_history"
    id = Column(String(36), primary_key=True)
    source = Column(String(10))
    community_id = Column(String(36))
    month = Column(String(10))
    price = Column(Integer)

class BusStation(Base):
    __tablename__ = "bus_station"
    id = Column(String(36), primary_key=True)
    name = Column(String(64))
    lat = Column(Float(32))
    lng = Column(Float(32))
    lines = Column(String(512))

class SubwayStation(Base):
    __tablename__ = "subway_station"
    id = Column(String(36), primary_key=True)
    name = Column(String(64))
    lat = Column(Float(32))
    lng = Column(Float(32))
    lines = Column(String(255))

class Hospital(Base):
    __tablename__ = "hospital"
    id = Column(String(36), primary_key=True)
    name = Column(String(64))
    address = Column(String(255))
    lat = Column(Float(32))
    lng = Column(Float(32))
    tag= Column(String(255))

class School(Base):
    __tablename__ = "school"
    id = Column(String(36), primary_key=True)
    name = Column(String(64))
    address = Column(String(255))
    lat = Column(Float(32))
    lng = Column(Float(32))
    tag = Column(String(255))

class CommercialArea(Base):
    __tablename__ = "commercial_area"
    id = Column(String(36), primary_key=True)
    name = Column(String(64))
    address = Column(String(255))
    lat = Column(Float(32))
    lng = Column(Float(32))
    tag = Column(String(255))

class MarketPlace(Base):
    __tablename__ = "market_place"
    id = Column(String(36), primary_key=True)
    name = Column(String(64))
    address = Column(String(255))
    lat = Column(Float(32))
    lng = Column(Float(32))
    tag = Column(String(255))

class CommunityBusRelation(Base):
    __tablename__ = "community_bus_relation"
    id = Column(String(36), primary_key=True)
    community_id = Column(String(36))
    bus_station_id = Column(String(36))
    distance = Column(Integer)

class CommunitySubwayRelation(Base):
    __tablename__ = "community_subway_relation"
    id = Column(String(36), primary_key=True)
    community_id = Column(String(36))
    subway_station_id = Column(String(36))
    distance = Column(Integer)

class CommunitySchoolRelation(Base):
    __tablename__ = "community_school_relation"
    id = Column(String(36), primary_key=True)
    community_id = Column(String(36))
    school_id = Column(String(36))
    distance = Column(Integer)

class CommunityHospitalRelation(Base):
    __tablename__ = "community_hospital_relation"
    id = Column(String(36), primary_key=True)
    community_id = Column(String(36))
    hospital_id = Column(String(36))
    distance = Column(Integer)

class CommunityCommercialRelation(Base):
    __tablename__ = "community_commercial_relation"
    id = Column(String(36), primary_key=True)
    community_id = Column(String(36))
    commercial_area_id = Column(String(36))
    distance = Column(Integer)

class CommunityMarketRelation(Base):
    __tablename__ = "community_market_relation"
    id = Column(String(36), primary_key=True)
    community_id = Column(String(36))
    market_place_id = Column(String(36))
    distance = Column(Integer)
