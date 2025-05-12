# Google Sheets Action

![GitHub release (latest by date)](https://img.shields.io/github/v/release/TrueSelph/google_sheets_action)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/TrueSelph/google_sheets_action/test-google_sheets_action.yaml)
![GitHub issues](https://img.shields.io/github/issues/TrueSelph/google_sheets_action)
![GitHub pull requests](https://img.shields.io/github/issues-pr/TrueSelph/google_sheets_action)
![GitHub](https://img.shields.io/github/license/TrueSelph/google_sheets_action)

JIVAS action wrapper for Google Sheets automation using the [gspread API](https://docs.gspread.org/en/v6.1.3/). This action provides robust spreadsheet management capabilities for creating, updating, and formatting Google Sheets programmatically. The package is a singleton and requires the Jivas library version ^2.0.0.


## Package Information
- **Name:** `jivas/google_sheets_action`
- **Author:** [V75 Inc.](https://v75inc.com/)
- **Architype:** `GoogleSheetsAction`

## Meta Information
- **Title:** Google Sheets Action
- **Group:** core
- **Type:** action

## Configuration
- **Singleton:** true

## Dependencies
- **Jivas:** `~2.0.0-aplha.40`
- **gspread:** 6.1.3

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

### Best Practices
- Validate your API keys before deployment.
- Test webhook registration in a staging environment before production use.

---

## 🔰 Contributing

- **🐛 [Report Issues](https://github.com/TrueSelph/google_sheets_action/issues)**: Submit bugs found or log feature requests for the `google_sheets_action` project.
- **💡 [Submit Pull Requests](https://github.com/TrueSelph/google_sheets_action/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/TrueSelph/google_sheets_action
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details open>
<summary>Contributor Graph</summary>
<br>
<p align="left">
    <a href="https://github.com/TrueSelph/google_sheets_action/graphs/contributors">
        <img src="https://contrib.rocks/image?repo=TrueSelph/google_sheets_action" />
   </a>
</p>
</details>

## 🎗 License

This project is protected under the Apache License 2.0. See [LICENSE](../LICENSE) for more information.