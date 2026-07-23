from client import PharmaSpecializedDocumentRagClient

def main():
    client = PharmaSpecializedDocumentRagClient()
    res = client.query_compliance(query="FDA Phase III adverse event reporting criteria", clinical_docs=["doc_1"])
    print(f"Compliance Flag: {res['compliance_flag']}")
    for ev in res["retrieved_evidence"]:
        print(f"  [{ev['doc_id']}] {ev['snippet']} (Score: {ev['relevance_score']})")

if __name__ == "__main__":
    main()
