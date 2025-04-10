from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from ampay.connections import Base


class Clients(Base):
    __tablename__ = "clients"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password_id: Mapped[UUID] = mapped_column(ForeignKey("passwords.id"), nullable=False)

    payin = relationship("PayIn", back_populates="client")
    refund = relationship("Refund", back_populates="client")
    password = relationship("Passwords", back_populates="client_password")


class Admins(Base):
    __tablename__ = "admins"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password_id: Mapped[UUID] = mapped_column(ForeignKey("passwords.id"), nullable=False)

    password = relationship("Passwords", back_populates="admin_password")
