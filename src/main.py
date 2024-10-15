import typer
import os

from snyk_project_importer import SnykProjectImporter

app = typer.Typer()

@app.command()
def run(file_path: str):
    snyk_token = os.environ.get('SNYK_TOKEN')
    org_id = os.environ.get('SNYK_ORG_ID')
    integration_id = os.environ.get('SNYK_INTEGRATION_ID')

    if file_path is None or file_path == "":
        typer.echo("Error: file_path is required")
        raise typer.Exit(code=1)

    snyk_project_importer = SnykProjectImporter(snyk_token, org_id, integration_id)
    print(f"Running with file path: {file_path}")

    snyk_project_importer.run(file_path)

    
if __name__ == "__main__":
    app()

