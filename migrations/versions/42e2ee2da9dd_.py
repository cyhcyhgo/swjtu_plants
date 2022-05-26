"""empty message

Revision ID: 42e2ee2da9dd
Revises: e994bfc623b9
Create Date: 2022-05-26 14:48:48.409361

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '42e2ee2da9dd'
down_revision = 'e994bfc623b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('plants_ibfk_1', 'plants', type_='foreignkey')
    op.drop_column('plants', 'uid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plants', sa.Column('uid', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('plants_ibfk_1', 'plants', 'users', ['uid'], ['id'])
    # ### end Alembic commands ###