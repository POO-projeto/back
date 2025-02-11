"""empty message

Revision ID: 9442d981c500
Revises: 5ed66fc6634b
Create Date: 2025-02-04 21:41:01.067386

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9442d981c500"
down_revision = "5ed66fc6634b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.add_column(sa.Column("lattes", sa.String(length=120), nullable=True))
        batch_op.create_unique_constraint(None, ["lattes"])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="unique")
        batch_op.drop_column("lattes")

    # ### end Alembic commands ###
