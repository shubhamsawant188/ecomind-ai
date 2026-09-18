# Import all models so SQLAlchemy's metadata registry is populated
# before Base.metadata.create_all() is called in main.py.
from app.models.environmental import (  # noqa: F401
    EnvironmentalObservation,
    LocationModel,
    SoilModel,
    ClimateModel,
    LandModel,
    BiodiversityModel,
    HumanImpactModel,
)
