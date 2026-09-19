from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import psycopg2  

# load .env so os.getenv() can read it
load_dotenv()

# connection string from .env — never hardcode secrets
raw_database_url = os.getenv("DATABASE_URL", "").strip()
if raw_database_url:
    # Strip accidental quotes from a .env value like:
    # postgresql://user:"pass word"@host/db
    raw_database_url = raw_database_url.strip('"').strip("'")
    DATABASE_URL = raw_database_url.replace(" ", "%20")
else:
    DATABASE_URL = "sqlite:///./candrasa.db"

# PostgreSQL must be configured intentionally; do not silently fall back to SQLite.
if DATABASE_URL.startswith("postgresql"):
    try:
        import psycopg2  # noqa: F401
    except ImportError as exc:
        raise RuntimeError(
            "psycopg2 is not installed for the configured PostgreSQL database. "
            "Run: pip install psycopg2-binary"
        ) from exc

engine_kwargs = {}
if DATABASE_URL.startswith("sqlite"):
    engine_kwargs["connect_args"] = {"check_same_thread": False}

# engine = the connection pool
engine = create_engine(DATABASE_URL, **engine_kwargs)
# SessionLocal = a factory for DB sessions
SessionLocal = sessionmaker(bind=engine, autoflush=False)

# Base = all ORM models inherit from this
Base = declarative_base()

# create all tables
def init_db() -> None:
  """Create all SQLAlchemy tables for the configured database."""
  Base.metadata.create_all(bind=engine)
