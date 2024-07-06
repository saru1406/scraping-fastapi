"""{create_job_table}

Revision ID: e56d72b48ad7
Revises: 163f1a007790
Create Date: 2024-06-08 17:07:30.192093

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "e56d72b48ad7"
down_revision: Union[str, None] = "163f1a007790"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "jobs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("link", sa.String(255), nullable=False),
        sa.Column("tags", sa.String(255), nullable=True),
        sa.Column("show", sa.Text(), nullable=True),
        sa.Column("price", sa.String(255), nullable=True),
        sa.Column("limit", sa.String(255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("jobs")
