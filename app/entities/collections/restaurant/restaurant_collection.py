from dataclasses import asdict

from motor.motor_asyncio import AsyncIOMotorCollection

from app.entities.category.category_codes import CategoryCode
from app.entities.collections.restaurant.restaurant_document import (
    RestaurantDeliveryAreaSubDocument,
    RestaurantDocument,
)
from app.utils.mongo import db


class RestaurantCollection:
    _collection = AsyncIOMotorCollection(db, "restaurants")

    @classmethod
    async def insert_one(
        cls, name: str, category_codes: list[CategoryCode], delivery_areas: list[RestaurantDeliveryAreaSubDocument]
    ) -> RestaurantDocument:
        result = await cls._collection.insert_one(
            {
                "name": name,
                "category_codes": category_codes,
                "delivery_areas": [asdict(delivery_area) for delivery_area in delivery_areas],
            }
        )
        return RestaurantDocument(
            _id=result.inserted_id,
            name=name,
            category_codes=category_codes,
            delivery_areas=delivery_areas,
        )
