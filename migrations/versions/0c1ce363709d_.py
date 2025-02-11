"""empty message

Revision ID: 0c1ce363709d
Revises: f65d14df2af3
Create Date: 2025-02-08 19:12:56.633689

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0c1ce363709d"
down_revision = "f65d14df2af3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "projects",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("start_date", sa.Date(), nullable=False),
        sa.Column("end_date", sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("projects")
    # ### end Alembic commands ###
