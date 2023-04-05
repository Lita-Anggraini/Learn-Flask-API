"""update tabel

Revision ID: 51534e499797
Revises: c490413da78a
Create Date: 2022-12-16 14:28:43.403301

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '51534e499797'
down_revision = 'c490413da78a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.alter_column('nim',
               existing_type=mysql.VARCHAR(length=10),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.alter_column('nim',
               existing_type=mysql.VARCHAR(length=10),
               nullable=True)

    # ### end Alembic commands ###
