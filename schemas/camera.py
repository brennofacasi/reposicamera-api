from typing import List, Optional
from pydantic import BaseModel

from model.camera import Camera


class CameraSchema(BaseModel):
    """
    Define como uma nova câmera a ser inserida deve ser representada
    """
    name: str = "Instax Mini"
    brand: str = "Fujifilm"
    value: float = 450
    category_id: int = 1


class CameraSearchSchema(BaseModel):
    """
    Define como a busca deve ser estruturada, que será feita apenas com base no nome da câmera.
    """
    id: int = 1


def show_cameras(cameras: List[Camera]):
    """
    Retorna uma representação da câmera seguindo o schema definido em CameraSchema.
    """
    result = []
    for camera in cameras:
        result.append({
            "id": camera.id,
            "name": camera.name,
            "brand": camera.brand,
            "value": camera.value,
            "category_id": camera.category.id
        })
    return {"cameras": result}


class CameraViewSchema(BaseModel):
    """
    Define como uma scâmera será retornada.
    """
    id: int = 1
    name: str = "Instax Mini"
    brand: str = "Fujifilm"
    value: float = 450
    category_id: int = 1
    category_name = "Instant"
    category_icon = "instant.svg"


class CameraListSchema(BaseModel):
    """
    Define como uma listagem de câmeras será retornada.
    """
    cameras: List[CameraViewSchema]


class CameraDelSchema(BaseModel):
    """
    Define como deve ser a estrutura do dado retornado após uma requisição de remoção.
    """
    message: str
    name: str


def show_camera(camera: Camera):
    """
    Retorna uma representação da câmera seguindo o schema definido em CameraViewSchema.
    """
    return {
        "id": camera.id,
        "name": camera.name,
        "brand": camera.brand,
        "value": camera.value,
        "category_id": camera.category_id
    }
