from src.models.video import Video


class DocumentService:
    @staticmethod
    def add_document(document_name):
        Video.create_document(document_name)
