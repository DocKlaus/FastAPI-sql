from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession


from core.models import db_helper, Product

from . import crud


async def get_product_by_id(
		product_id: Annotated[int, Path],
		session: AsyncSession = Depends(db_helper.scoped_session_dependency),
		) -> Product:
	product = await crud.get_product(session = session, product_id = product_id)
	if product is not None:
		return product
	raise HTTPException(
		status_code = status.HTTP_400_BAD_REQUEST,
		detail = f"Product{product_id} not found",
		)
