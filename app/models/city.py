from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base
from app.models.mixins import IdIntPkMixin


class City(Base, IdIntPkMixin):
    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True,
        nullable=False,
    )

    temperatures = relationship("temperature", back_populates="city")
