import dataclasses

from app.entities.category.category_codes import CategoryCode
from app.entities.collections.base_document import BaseDocument
from app.entities.collections.geo_json import GeoJsonPolygon


@dataclasses.dataclass
class RestaurantDeliveryAreaSubDocument:
    polygon: GeoJsonPolygon


@dataclasses.dataclass
class RestaurantDocument(BaseDocument):
    name: str
    category_codes: list[CategoryCode]
    delivery_areas: list[RestaurantDeliveryAreaSubDocument]
