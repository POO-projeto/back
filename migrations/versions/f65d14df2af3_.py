"""empty message

Revision ID: f65d14df2af3
Revises: 8ad4e2504d70
Create Date: 2025-02-05 22:25:14.528453

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f65d14df2af3"
down_revision = "8ad4e2504d70"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("dailies", schema=None) as batch_op:
        batch_op.add_column(sa.Column("issue", sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("dailies", schema=None) as batch_op:
        batch_op.drop_column("issue")

    # ### end Alembic commands ###
