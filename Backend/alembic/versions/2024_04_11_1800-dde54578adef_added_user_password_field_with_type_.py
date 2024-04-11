"""Added user password field with type bytes

Revision ID: dde54578adef
Revises: fc7824a246ec
Create Date: 2024-04-11 18:00:39.947223

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "dde54578adef"
down_revision: Union[str, None] = "fc7824a246ec"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("hashed_password", sa.LargeBinary(), nullable=False)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "hashed_password")
    # ### end Alembic commands ###
