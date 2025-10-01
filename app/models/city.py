from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base
from app.models.mixins import IdIntPkMixin


if TYPE_CHECKING:
    from app.models import Temperature


class City(Base, IdIntPkMixin):
    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True,
        nullable=False,
    )

    temperatures: Mapped["Temperature"] = relationship(
        back_populates="city",
    )
