from __future__ import with_statement
import sys
from os.path import abspath, dirname

# ensure project root is in sys.path so `import app` works
sys.path.append(abspath(dirname(dirname(__file__))))

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# import your app settings and Base metadata
try:
    from app.core.config import settings
    from app.db.base import Base
    # import models so they are registered on the metadata
    import app.models.user  # add other model imports here if you have them
except Exception as e:
    # if imports fail, provide a clearer error
    raise RuntimeError("Failed to import app modules in alembic/env.py: " + str(e))

config = context.config

# override sqlalchemy.url with settings value (if present)
if hasattr(settings, "DATABASE_URL") and settings.DATABASE_URL:
    config.set_main_option("sqlalchemy.url", str(settings.DATABASE_URL))

# set up logging from config file
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
