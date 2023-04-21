from datetime import datetime
from typing import Union
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from model import Base


class Camera(Base):
    __tablename__ = 'camera'

    id = Column("pk_camera", Integer, primary_key=True)
    name = Column(String(140), unique=True)
    brand = Column(String(140))
    value = Column(Integer)
    description = Column(String(1000))
    created_at = Column(DateTime, default=datetime.now())

    category = relationship("Category")

    category_id = Column(Integer, ForeignKey(
        "category.pk_category"), nullable=False)

    def __init__(self, name: str, brand: str, value: float, description: str, category_id: int, created_at: Union[DateTime, None] = None):
        """
        Cria uma Camera

        Arguments:
            name: nome da câmera.
            brand: marca da câmera.
            value: valor (em reais) avaliador da câmera.
            description: descrição de detalhes da câmera.
            category_id: id da categoria.
            created_at: data de quando a câmera foi inserida à base.
        """
        self.name = name
        self.brand = brand
        self.value = value
        self.description = description
        self.category_id = category_id

        if created_at:
            self.created_at = created_at
