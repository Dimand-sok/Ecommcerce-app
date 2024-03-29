"""add category model

Revision ID: 30752f7ffd3f
Revises: 8aad2c0ce80b
Create Date: 2022-07-26 07:32:47.563924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30752f7ffd3f'
down_revision = '8aad2c0ce80b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.Column('category_name', sa.String(length=128), nullable=True),
    sa.Column('category_desc', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category')
    # ### end Alembic commands ###
