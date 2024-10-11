import pytest

from app.entities.category.category_codes import CategoryCode
from app.entities.collections.geo_json import GeoJsonPolygon
from app.entities.collections.restaurant.restaurant_collection import (
    RestaurantCollection,
)
from app.entities.collections.restaurant.restaurant_document import (
    RestaurantDeliveryAreaSubDocument,
)


async def test_shop_insert_one() -> None:
    # Given
    name = "Sample Restaurant"
    category_codes = [CategoryCode.CHICKEN]
    delivery_areas = [
        RestaurantDeliveryAreaSubDocument(
            polygon=GeoJsonPolygon(coordinates=[[[0, 0], [0, 10], [10, 10], [10, 0], [0, 0]]]),
        )
    ]

    # When
    restaurant = await RestaurantCollection.insert_one(name, category_codes, delivery_areas)
    results = await RestaurantCollection._collection.find({}).to_list(None)

    # Then
    assert len(results) == 1
    result = results[0]
    assert result["_id"] == restaurant.id
    assert result["name"] == restaurant.name
    assert result["category_codes"] == ["chicken"]
    assert result["delivery_areas"] == [
        {"polygon": {"type": "Polygon", "coordinates": [[[0, 0], [0, 10], [10, 10], [10, 0], [0, 0]]]}}
    ]
