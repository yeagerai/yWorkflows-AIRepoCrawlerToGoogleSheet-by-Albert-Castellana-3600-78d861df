
# AIRepoCrawlerToGoogleSheet

This workflow is a crawler that searches for Github repositories containing the words "Artificial Intelligence" and saves the results to a Google Spreadsheet. The workflow will perform the following steps:
1. Search GitHub for repos with the words "Artificial Intelligence" using the GitHub API.
2. Extract the relevant information (repo name, owner, and URL) and create a list of repo objects.
3. Connect to the Google Sheets API and create a new spreadsheet.
4. Write the list of repo objects to the spreadsheet in a structured format.

## Initial generation prompt
create a crawler that finds all github repositories containing with the words "Artificial intelligence" and send them to a goodle spreadsheet

## Authors: 
- yWorkflows
- Albert Castellana#3600
        