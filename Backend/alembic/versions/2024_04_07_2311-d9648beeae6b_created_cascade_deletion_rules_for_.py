"""Created cascade deletion rules for necessary tables

Revision ID: d9648beeae6b
Revises: 4a21baa68558
Create Date: 2024-04-07 23:11:41.508283

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d9648beeae6b"
down_revision: Union[str, None] = "4a21baa68558"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "cart_plant_association_plant_id_fkey",
        "cart_plant_association",
        type_="foreignkey",
    )
    op.drop_constraint(
        "cart_plant_association_cart_id_fkey",
        "cart_plant_association",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "cart_plant_association",
        "carts",
        ["cart_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        None,
        "cart_plant_association",
        "plants",
        ["plant_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "carts_user_id_fkey",
        "carts",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "carts",
        "users",
        ["user_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "categories_collection_id_fkey",
        "categories",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "categories",
        "collections",
        ["collection_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "order_plant_association_plant_id_fkey",
        "order_plant_association",
        type_="foreignkey",
    )
    op.drop_constraint(
        "order_plant_association_order_id_fkey",
        "order_plant_association",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "order_plant_association",
        "plants",
        ["plant_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        None,
        "order_plant_association",
        "orders",
        ["order_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "orders_user_id_fkey",
        "orders",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "orders",
        "users",
        ["user_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "plant_category_association_category_id_fkey",
        "plant_category_association",
        type_="foreignkey",
    )
    op.drop_constraint(
        "plant_category_association_plant_id_fkey",
        "plant_category_association",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "plant_category_association",
        "plants",
        ["plant_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        None,
        "plant_category_association",
        "categories",
        ["category_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "profiles_user_id_fkey",
        "profiles",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "profiles",
        "users",
        ["user_id"],
        ["id"],
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "profiles", type_="foreignkey")
    op.create_foreign_key(
        "profiles_user_id_fkey",
        "profiles",
        "users",
        ["user_id"],
        ["id"],
    )
    op.drop_constraint(
        None,
        "plant_category_association",
        type_="foreignkey",
    )
    op.drop_constraint(
        None,
        "plant_category_association",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "plant_category_association_plant_id_fkey",
        "plant_category_association",
        "plants",
        ["plant_id"],
        ["id"],
    )
    op.create_foreign_key(
        "plant_category_association_category_id_fkey",
        "plant_category_association",
        "categories",
        ["category_id"],
        ["id"],
    )
    op.drop_constraint(
        None,
        "orders",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "orders_user_id_fkey",
        "orders",
        "users",
        ["user_id"],
        ["id"],
    )
    op.drop_constraint(
        None,
        "order_plant_association",
        type_="foreignkey",
    )
    op.drop_constraint(
        None,
        "order_plant_association",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "order_plant_association_order_id_fkey",
        "order_plant_association",
        "orders",
        ["order_id"],
        ["id"],
    )
    op.create_foreign_key(
        "order_plant_association_plant_id_fkey",
        "order_plant_association",
        "plants",
        ["plant_id"],
        ["id"],
    )
    op.drop_constraint(
        None,
        "categories",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "categories_collection_id_fkey",
        "categories",
        "collections",
        ["collection_id"],
        ["id"],
    )
    op.drop_constraint(
        None,
        "carts",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "carts_user_id_fkey",
        "carts",
        "users",
        ["user_id"],
        ["id"],
    )
    op.drop_constraint(
        None,
        "cart_plant_association",
        type_="foreignkey",
    )
    op.drop_constraint(
        None,
        "cart_plant_association",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "cart_plant_association_cart_id_fkey",
        "cart_plant_association",
        "carts",
        ["cart_id"],
        ["id"],
    )
    op.create_foreign_key(
        "cart_plant_association_plant_id_fkey",
        "cart_plant_association",
        "plants",
        ["plant_id"],
        ["id"],
    )
    # ### end Alembic commands ###
