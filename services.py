from database import Base, Engine

def create_database():
    return Base.metadata.create_all(bind=Engine)

# Call the function to create the database
create_database()

