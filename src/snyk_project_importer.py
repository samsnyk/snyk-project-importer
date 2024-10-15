import csv
import requests


class SnykProjectImporter:
    def __init__(self, snyk_token: str, org_id: str, integration_id: str):
        self.snyk_token = snyk_token
        self.org_id = org_id
        self.integration_id = integration_id

    def parse_unimported_projects_csv(self, file_path: str):
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            
            repos = []

            for row in csv_reader:
                if row['Type'] == 'Repository':
                    if row['Control Covered'] == '':
                        print(f"{row['Asset']},{row['Repository URL']}")
                        repo = {"Asset": row['Asset'], "Repo URL": row['Repository URL']}
                        repos.append(repo)

            return repos

    def import_snyk_project(self, integration_id: str, repo_url: str):
        api_url = f"https://snyk.io/api/v1/org/{self.org_id}/integrations/{integration_id}/import"
        
        headers = {
            "Authorization": f"token {self.snyk_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "target": {
                "owner": "owner_name",
                "name": "repo_name",
                "branch": "main"
            }
        }
        
        # Extract owner and repo name from the URL
        parts = repo_url.split('/')
        if len(parts) >= 2:
            payload["target"]["owner"] = parts[-2]
            payload["target"]["name"] = parts[-1].replace(".git", "")
        else:
            print(f"Invalid repository URL: {repo_url}")
            return
        
        response = requests.post(api_url, json=payload, headers=headers)
        
        if response.status_code == 201:
            print(f"Successfully imported {repo_url}")
        else:
            print(f"Failed to import {repo_url}. Status code: {response.status_code}")
            print(f"Response: {response.text}")

    def run(self, file_path: str):
        repos = self.parse_unimported_projects_csv(file_path)

        for repo in repos:
            self.import_snyk_project(integration_id=self.integration_id, repo_url=repo["Repo URL"])

if __name__ == "__main__":  
    file_path = 'test-assets/all_assets_2024_10_11_184130.csv'

    snyk_project_importer = SnykProjectImporter()

    snyk_project_importer.run(file_path)