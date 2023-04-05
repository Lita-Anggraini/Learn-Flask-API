"""Tabel Dosen

Revision ID: cb98afe06f9a
Revises: eb3797ccd800
Create Date: 2022-12-15 11:18:56.311649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb98afe06f9a'
down_revision = 'eb3797ccd800'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dosen',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nidn', sa.String(length=10), nullable=False),
    sa.Column('nama', sa.String(length=50), nullable=False),
    sa.Column('alamat', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dosen')
    # ### end Alembic commands ###