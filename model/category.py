from datetime import datetime
from typing import Union
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from model import Base, Camera


class Category(Base):
    __tablename__ = 'category'

    id = Column("pk_category", Integer, primary_key=True)
    name = Column(String(140), unique=True)
    icon = Column(String(140))
    created_at = Column(DateTime, default=datetime.now())

    cameras = relationship("Camera")

    def __init__(self, name: str, icon: str, created_at: Union[DateTime, None] = None):
        """
        Cria uma Categoria

        Arguments:
        name: o nome da categoria.
        icon: o caminho para o ícone da categoria.
        created_at: data quando a categoria foi adicionada à base
        """
        self.name = name
        self.icon = icon

        if created_at:
            self.created_at = created_at

    def add_camera(self, camera: Camera):
        """
        Adiciona uma câmera a uma categoria
        """
        self.cameras.append(camera)
