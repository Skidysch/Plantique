"""Create plants table

Revision ID: aef88d8ed2f5
Revises: 
Create Date: 2024-04-04 20:13:36.639923

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "aef88d8ed2f5"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "plants",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("slug", sa.String(), nullable=False),
        sa.Column("link", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("soil_type", sa.String(), nullable=False),
        sa.Column("image_url", sa.String(), nullable=False),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column(
            "stock_available", sa.Boolean(), server_default="false", nullable=False
        ),
        sa.Column("stock_quantity", sa.Integer(), server_default="0", nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("plants")
    # ### end Alembic commands ###