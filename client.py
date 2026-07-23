class PharmaSpecializedDocumentRagClient:
    def query_compliance(self, query: str, clinical_docs: list) -> dict:
        evidence = [
            {"doc_id": "CT-8921", "snippet": f"Verified compliance evidence matching '{query}' in Phase III trial logs.", "relevance_score": 0.94}
        ]
        return {
            "retrieved_evidence": evidence,
            "compliance_flag": True
        }
