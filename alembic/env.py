import sys
from sqlalchemy import create_engine
from alembic import context
from logging.config import fileConfig
import os
from dotenv import load_dotenv

load_dotenv()
# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.session import Base  
from app.models import user, product, search_pattern

# Other configuration for Alembic
config = context.config
fileConfig(config.config_file_name)

def get_url():
    return os.getenv("DATABASE_URL")

def run_migrations_online():
    connectable = create_engine(get_url()) # type: ignore

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=Base.metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()