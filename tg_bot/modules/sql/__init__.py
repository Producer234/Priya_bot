import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from tg_bot import DB_URI


def start() -> scoped_session:
    # Use environment variable or fallback to SQLite
    db_uri = DB_URI or os.getenv("DATABASE_URL", "sqlite:///data.db")

    try:
        # SQLite doesn't support client_encoding
        if db_uri.startswith("sqlite"):
            engine = create_engine(db_uri, echo=False)
        else:
            engine = create_engine(db_uri, client_encoding="utf8")

        BASE.metadata.bind = engine
        BASE.metadata.create_all(engine)
        return scoped_session(sessionmaker(bind=engine, autoflush=False))
    except Exception as e:
        print(f"[WARN] Database initialization failed: {e}")
        print("[INFO] Running without database (some modules may be disabled).")
        return None


BASE = declarative_base()
SESSION = start()
