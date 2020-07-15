"""Changed notest table

Revision ID: a597e592ae3d
Revises: d086bc8b0f30
Create Date: 2020-07-15 19:46:54.681387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a597e592ae3d'
down_revision = 'd086bc8b0f30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notes', sa.Column('test_field', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('notes', 'test_field')
    # ### end Alembic commands ###