"""Add uuid for products

Revision ID: a10c5e01e782
Revises: e7243df83002
Create Date: 2024-08-25 20:52:35.301563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a10c5e01e782'
down_revision = 'e7243df83002'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'id',
               existing_type=sa.INTEGER(),
               type_=sa.UUID(),
               existing_nullable=False)
    op.drop_index('ix_products_id', table_name='products')
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.create_index('ix_products_id', 'products', ['id'], unique=False)
    op.alter_column('products', 'id',
               existing_type=sa.UUID(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###