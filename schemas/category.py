from typing import List
from pydantic import BaseModel
from model.category import Category

from schemas.camera import CameraSchema


class CategorySchema(BaseModel):
    """
    Define como uma categoria a ser inserida deve ser representada.
    """
    name: str = "DSLR"
    icon: str = "dslr.svg"


class CategoryViewSchema(BaseModel):
    name: str = "DSLR"
    icon: str = "dslr.svg"
    cameras: List[CameraSchema]


def show_category(category: Category):
    """
    Retorna uma representação da categoria seguindo o schema definido em CameraViewSchema.
    """
    return {
        "name": category.name,
        "icon": category.icon,
        "cameras": category.cameras
    }
