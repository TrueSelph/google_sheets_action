# Google Sheets Action

![GitHub release (latest by date)](https://img.shields.io/github/v/release/TrueSelph/google_sheets_action)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/TrueSelph/google_sheets_action/test-google_sheets_action.yaml)
![GitHub issues](https://img.shields.io/github/issues/TrueSelph/google_sheets_action)
![GitHub pull requests](https://img.shields.io/github/issues-pr/TrueSelph/google_sheets_action)
![GitHub](https://img.shields.io/github/license/TrueSelph/google_sheets_action)

This action provides seamless integration with Google Sheets using the gspread API for managing and automating spreadsheet tasks. It enables efficient spreadsheet operations such as creating, updating, sharing, and formatting Google Sheets. As a singleton in the action group, it ensures centralized management for Google Sheets integrations. This package requires the Jivas library version 2.0.0 and the gspread library version 6.1.3.

## Package Information

- **Name:** `jivas/google_sheets_action`
- **Author:** [V75 Inc.](https://v75inc.com/)
- **Architype:** `GoogleSheetsAction`
- **Version:** 0.0.1

## Meta Information

- **Title:** Google Sheets Action
- **Description:** Provides seamless integration with Google Sheets using the gspread API for managing and automating spreadsheet tasks.
- **Group:** core
- **Type:** action

## Configuration
- **Singleton:** true

## Dependencies
- **Jivas:** ^2.0.0
- **gspread:** 6.1.3

---

### Best Practices
- Always store your Google Service Account credentials securely.
- Regularly update and rotate access tokens to maintain security.
- Test configurations in a staging environment before going live.

---

## 🚀 Google Sheets API Setup Guide

### Step 1: Create a Service Account

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Navigate to **APIs & Services > Credentials**.
4. Click **Create Credentials > Service Account**.
5. Fill in the required details and click **Done**.

### Step 2: Enable Google Sheets API

1. In the **APIs & Services > Library**, search for **Google Sheets API**.
2. Click **Enable** to activate the API for your project.

### Step 3: Download Service Account Key

1. In the **Credentials** section, locate your service account and click it.
2. Click **keys > add key > Create new key**.
4. Select **JSON** and create.

### Step 4: Share Spreadsheet with Service Account email

1. Open your Google Spreadsheet.
2. Click **Share** and add the service account email (found in the JSON key file) with **Editor** permissions.

---

## 🔰 Contributing

- **🐛 [Report Issues](https://github.com/TrueSelph/google_sheets_action/issues)**: Found a bug or want to request a feature? Submit it here.
- **💡 [Submit Pull Requests](https://github.com/TrueSelph/google_sheets_action/blob/main/CONTRIBUTING.md)**: Check out open PRs or submit your own improvements.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/TrueSelph/google_sheets_action