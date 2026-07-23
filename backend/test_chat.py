from app.retrieval.retrieval_service import RetrievalService

rag = RetrievalService()

question = input("Ask a question: ")

response = rag.ask(question)

print("\nAnswer\n")
print(response["answer"])

print("\nSources\n")

for source in response["sources"]:

    print("--------------------------------")

    print(source["metadata"]["document"])

    print(source["metadata"]["chunk_id"])

    print(source["score"])