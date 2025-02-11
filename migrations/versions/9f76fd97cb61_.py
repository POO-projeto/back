"""empty message

Revision ID: 9f76fd97cb61
Revises: 
Create Date: 2025-02-11 20:13:09.157581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f76fd97cb61'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('scholarships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('telephone', sa.String(length=13), nullable=True),
    sa.Column('github', sa.String(length=120), nullable=True),
    sa.Column('lattes', sa.String(length=120), nullable=True),
    sa.Column('scholarship_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['scholarship_id'], ['scholarships.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('github'),
    sa.UniqueConstraint('lattes')
    )
    op.create_table('dailies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('issue', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('daily_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['daily_id'], ['dailies.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    op.drop_table('dailies')
    op.drop_table('users')
    op.drop_table('user_tasks')
    op.drop_table('tasks')
    op.drop_table('scholarships')
    op.drop_table('projects')
    # ### end Alembic commands ###
