# Snyk Project Importer

This script helps manage Snyk projects by importing unimported repositories from a CSV file exported from Snyk's AppRisk Inventory.

## Prerequisites

- Python 3.6 or higher
- Snyk account with API access

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/snyk-project-manager.git
   cd snyk-project-manager
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the following environment variables:
   - `SNYK_TOKEN`: Your Snyk API token.
   - `SNYK_ORG_ID`: Your Snyk organization ID where the projects will be imported.
   - `SNYK_INTEGRATION_ID`: The integration ID for your version control system (e.g., GitHub, GitLab).

   You can set these variables in your shell or create a `.env` file in the project root.

4. Set up the virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

## Usage

1. Generate a CSV file from Snyk's AppRisk Inventory.
    In the Snyk UI, go to the AppRisk Inventory page.
    Click on the "Export" button, and then confirm by clicking the Export button in the pop-up.
    Save the file to your local machine.

2. Run the script with the following command:
```
python main.py <csv_file_path>
```

The script will read the CSV file, extract unimported repositories, and attempt to import them into the specified Snyk organization.