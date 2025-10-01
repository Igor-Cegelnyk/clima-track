from sqlalchemy import Integer, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base
from app.models.mixins import IdIntPkMixin


class Temperature(Base, IdIntPkMixin):
    city_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("cities.id"),
        nullable=False,
    )
    temperature: Mapped[float] = mapped_column(Float, nullable=False)
    temperature_date: Mapped[int] = mapped_column(Integer, nullable=False)
    temperature_time: Mapped[int] = mapped_column(Integer, nullable=False)
    created_date: Mapped[int] = mapped_column(Integer, nullable=False)
    created_time: Mapped[int] = mapped_column(Integer, nullable=False)

    city = relationship("city", back_populates="temperatures")
