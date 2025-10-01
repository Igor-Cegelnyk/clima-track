from typing import TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey, Float, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base
from app.models.mixins import IdIntPkMixin
from app.utils.convert_date import current_date_int, current_time_int

if TYPE_CHECKING:
    from app.models import City


class Temperature(Base, IdIntPkMixin):
    city_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("cities.id"),
        nullable=False,
    )
    temperature: Mapped[float] = mapped_column(Float, nullable=False)
    temperature_date: Mapped[int] = mapped_column(Integer, nullable=False)
    temperature_time: Mapped[int] = mapped_column(Integer, nullable=False)
    created_date: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=current_date_int,
        server_default=text("CAST(to_char(now(),'YYYYMMDD') AS INTEGER)"),
    )
    created_time: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=current_time_int,
        server_default=text("CAST(to_char(now(),'HH24MISS') AS INTEGER)"),
    )

    city: Mapped["City"] = relationship(
        back_populates="temperatures",
        lazy="selectin",
    )
