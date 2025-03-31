from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database connection URL
DATABASE_URL = 'postgresql://postgres:lenovo@localhost/portfolio_contact'

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the Contact model
class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    subject = Column(String)
    message = Column(String)
    timestamp = Column(DateTime)

    def __repr__(self):
        return f"Contact(name='{self.name}', email='{self.email}', message='{self.message}')"

# Create the tables in the database
Base.metadata.create_all(engine)