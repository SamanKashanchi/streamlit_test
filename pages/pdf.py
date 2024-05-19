import os
from llama_index import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers import PDFReader
os.environ["OPENAI_API_KEY"] = "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"

def get_index(data, index_name):
    index = None

    if not os.path.exists(index_name):
        print("Building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress = True)
        index.storage_context.persist(persist_dir = index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir = index_name)
        )
    return index


pdf_path = os.path.join("data", "Saman Kashanchi Resume 2024.pdf")
saman_pdf = PDFReader().load_data(file = pdf_path)
saman_index = get_index(saman_pdf, 'saman')
saman_engine = saman_index.as_query_engine()
