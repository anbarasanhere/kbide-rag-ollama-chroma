from services.vector_service import VectorService

vs = VectorService()

db = vs.get_vector_db()

print(db._collection.count())
