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
    description: Optional[str] = "Câmera amarela, usada, com filme mini, flash e filtros."


class CameraSearchSchema(BaseModel):
    """
    Define como a busca deve ser estruturada, que será feita apenas com base no nome da câmera.
    """
    name: str = "Instax"


class CameraListSchema(BaseModel):
    """
    Define como uma listagem de câmeras será retornada.
    """
    cameras: List[CameraSchema]


def show_cameras(cameras: List[Camera]):
    """
    Retorna uma representação da câmera seguindo o schema definido em CameraSchema.
    """
    result = []
    for camera in cameras:
        print(camera.categories.name)
        # result.append({
        #     "name": camera.name,
        #     "brand": camera.brand,
        #     "value": camera.value,
        #     "description": camera.description,
        #     "category_id": camera.category_id,
        # })
    return result


class CameraViewSchema(BaseModel):
    """
    Define como uma scâmera será retornada.
    """
    name: str = "Instax Mini"
    brand: str = "Fujifilm"
    value: float = 450
    category_id: int = 1
    description: Optional[str] = "Câmera amarela, usada, com filme mini, flash e filtros."


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
        "name": camera.name,
        "brand": camera.brand,
        "value": camera.value,
        "category_id": camera.category_id,
        "description": camera.description,
    }
