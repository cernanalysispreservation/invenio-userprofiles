# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Adds extra_data column to userprofiles."""

import sqlalchemy as sa
from alembic import op

from sqlalchemy.dialects import postgresql
from sqlalchemy_utils.types import JSONType

json_type = JSONType().with_variant(
    postgresql.JSONB(none_as_null=True),
    'postgresql',
).with_variant(
    JSONType(),
    'sqlite',
)

# revision identifiers, used by Alembic.
revision = 'a25efff50ffa'
down_revision = 'c25ef2c50ffa'
branch_labels = ()
depends_on = None


def upgrade():
    """Upgrade database."""
    op.add_column('userprofiles_userprofile',
                  sa.Column('extra_data', json_type, nullable=True))



def downgrade():
    """Downgrade database."""
    op.drop_column('userprofiles_userprofile', 'extra_data')
