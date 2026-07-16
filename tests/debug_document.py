from services.vector_service import VectorService

vs = VectorService()

vs.rebuild()

db = vs.get_vector_db()

print(db._collection.count())


