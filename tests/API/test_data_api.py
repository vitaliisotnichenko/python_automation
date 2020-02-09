class Payload:

    def create_issue_payload(self, key, summary, description, issue_type_id):
        payload = {
            "fields": {
                "project": {
                     "key": key
                },
                "summary": summary,
                "description": description,
                "issuetype": {
                    "id": issue_type_id
                }
            }
        }
        return payload