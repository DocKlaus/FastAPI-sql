from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
# from sqlalchemy.testing.schema import mapped_column


class Base(DeclarativeBase):
	""" Абстрактная модель, на основе которой строится таблица продуктов Products"""
	__abstract__ = True

	@declared_attr.directive
	def __tablename__(cls) -> str:
		return cls.__name__.lower()

	id: Mapped[int] = mapped_column(primary_key=True)