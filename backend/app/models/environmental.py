from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.base import Base

class LocationModel(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    region = Column(String, nullable=True)
    observation_id = Column(Integer, ForeignKey("environmental_observation.id"))
    observation = relationship("EnvironmentalObservation", back_populates="location")

class SoilModel(Base):
    __tablename__ = "soil"
    id = Column(Integer, primary_key=True, index=True)
    soil_ph = Column(Float, nullable=True)
    organic_carbon = Column(Float, nullable=True)
    moisture = Column(Float, nullable=True)
    observation_id = Column(Integer, ForeignKey("environmental_observation.id"))
    observation = relationship("EnvironmentalObservation", back_populates="soil")

class ClimateModel(Base):
    __tablename__ = "climate"
    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float, nullable=True)
    rainfall = Column(Float, nullable=True)
    observation_id = Column(Integer, ForeignKey("environmental_observation.id"))
    observation = relationship("EnvironmentalObservation", back_populates="climate")

class LandModel(Base):
    __tablename__ = "land"
    id = Column(Integer, primary_key=True, index=True)
    land_use = Column(String, nullable=True)
    crop = Column(String, nullable=True)
    cropping_system = Column(String, nullable=True)
    observation_id = Column(Integer, ForeignKey("environmental_observation.id"))
    observation = relationship("EnvironmentalObservation", back_populates="land")

class BiodiversityModel(Base):
    __tablename__ = "biodiversity"
    id = Column(Integer, primary_key=True, index=True)
    species_richness = Column(Integer, nullable=True)
    habitat_diversity = Column(String, nullable=True)
    observation_id = Column(Integer, ForeignKey("environmental_observation.id"))
    observation = relationship("EnvironmentalObservation", back_populates="biodiversity")

class HumanImpactModel(Base):
    __tablename__ = "human_impact"
    id = Column(Integer, primary_key=True, index=True)
    pollution = Column(String, nullable=True)
    deforestation = Column(String, nullable=True)
    observation_id = Column(Integer, ForeignKey("environmental_observation.id"))
    observation = relationship("EnvironmentalObservation", back_populates="human_impact")

class EnvironmentalObservation(Base):
    __tablename__ = "environmental_observation"
    id = Column(Integer, primary_key=True, index=True)
    observed_at = Column(DateTime, default=datetime.utcnow)
    source_name = Column(String, nullable=True)
    source_type = Column(String, nullable=True)
    source_reference = Column(String, nullable=True)
    data_quality = Column(String, nullable=True)
    confidence = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    location = relationship("LocationModel", back_populates="observation", uselist=False, cascade="all, delete-orphan")
    soil = relationship("SoilModel", back_populates="observation", uselist=False, cascade="all, delete-orphan")
    climate = relationship("ClimateModel", back_populates="observation", uselist=False, cascade="all, delete-orphan")
    land = relationship("LandModel", back_populates="observation", uselist=False, cascade="all, delete-orphan")
    biodiversity = relationship("BiodiversityModel", back_populates="observation", uselist=False, cascade="all, delete-orphan")
    human_impact = relationship("HumanImpactModel", back_populates="observation", uselist=False, cascade="all, delete-orphan")
