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
    id: int = 1
    name: str = "DSLR"
    icon: str = "dslr.svg"


class CategoryListSchema(BaseModel):
    """
    Define como uma listagem de categorias será retornada.
    """
    categories: List[CategorySchema]


def show_category(category: Category):
    """
    Retorna uma representação da categoria seguindo o schema definido em CameraViewSchema.
    """
    return {
        "id": category.id,
        "name": category.name,
        "icon": category.icon,
    }


def show_categories(categories: List[Category]):
    """
    Retorna uma representação da câmera seguindo o schema definido em CameraSchema.
    """
    result = []
    for category in categories:
        result.append({
            "id": category.id,
            "name": category.name,
            "icon": category.icon
        })
    return {"categories": result}
