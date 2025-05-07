"""This module contains the GoogleSheetAPI class for interacting with the Google Sheets API."""

import logging
import traceback
from typing import Optional, Union

import gspread


class GoogleSheetsAPI:
    """Class for interacting with the Google Sheets API."""

    logger = logging.getLogger(__name__)

    def __init__(
        self,
        info_type: str,
        project_id: str,
        private_key_id: str,
        private_key: str,
        client_email: str,
        client_id: str,
        auth_uri: str,
        token_uri: str,
        auth_provider_x509_cert_url: str,
        client_x509_cert_url: str,
        universe_domain: str,
        key_or_url: str,
        worksheet_title: str,
    ) -> None:
        """
        Initializes the GoogleSheetAPI object with credentials.

        :param credentials: Dictionary containing Google API credentials.
        """
        self.credentials = {
            "type": info_type,
            "project_id": project_id,
            "private_key_id": private_key_id,
            "private_key": private_key,
            "client_email": client_email,
            "client_id": client_id,
            "auth_uri": auth_uri,
            "token_uri": token_uri,
            "auth_provider_x509_cert_url": auth_provider_x509_cert_url,
            "client_x509_cert_url": client_x509_cert_url,
            "universe_domain": universe_domain,
        }
        self.key_or_url = key_or_url
        self.worksheet_title = worksheet_title
        self.gc = gspread.service_account_from_dict(self.credentials)

    def open_spreadsheet(self, key_or_url: str = "") -> gspread.Spreadsheet:
        """
        Opens a Google Spreadsheet by key or URL.

        :param key_or_url: Spreadsheet key or URL.
        :return: gspread.Spreadsheet object.
        """
        try:
            if not key_or_url:
                key_or_url = self.key_or_url

            if "http" in key_or_url:
                return self.gc.open_by_url(key_or_url)

            return self.gc.open_by_key(self.key_or_url)
        except Exception as e:
            self.logger.error(f"Error opening spreadsheet: {traceback.format_exc()}")
            raise e

    def open_worksheet(
        self, key_or_url: str = "", worksheet_title: str = ""
    ) -> Union[list, dict]:
        """
        Opens a worksheet and returns all records.

        :param key_or_url: Spreadsheet key or URL.
        :param worksheet_title: Title of the worksheet to open.
        :return: List of records or error details.
        """
        try:
            if not worksheet_title:
                worksheet_title = self.worksheet_title

            response = self.open_spreadsheet(key_or_url)
            worksheet = response.worksheet(worksheet_title)
            return worksheet.get_all_records()
        except Exception as e:
            self.logger.error(f"Error opening worksheet: {traceback.format_exc()}")
            return {"error": str(e)}

    def create_spreadsheet(self, title: str) -> Union[str, dict]:
        """
        Creates a new Google Spreadsheet.

        :param title: Title of the new spreadsheet.
        :return: Spreadsheet ID.
        """
        try:
            spreadsheet = self.gc.create(title)
            return spreadsheet.id
        except Exception as e:
            self.logger.error(f"Error creating spreadsheet: {traceback.format_exc()}")
            return {"error": str(e)}

    def create_worksheet(
        self, title: str, key_or_url: str = "", rows: int = 100, cols: int = 20
    ) -> Union[str, dict]:
        """
        Creates a new worksheet in an existing Google Spreadsheet.

        :param key_or_url: Spreadsheet key or URL.
        :param title: Title of the new worksheet.
        :param rows: Number of rows in the worksheet.
        :param cols: Number of columns in the worksheet.
        :return: Worksheet ID.
        """
        try:
            spreadsheet = self.open_spreadsheet(key_or_url)
            worksheet = spreadsheet.add_worksheet(title=title, rows=rows, cols=cols)
            return worksheet.id
        except Exception as e:
            self.logger.error(f"Error creating worksheet: {traceback.format_exc()}")
            return {"error": str(e)}

    def delete_worksheet(
        self, key_or_url: str = "", worksheet_title: str = ""
    ) -> Union[bool, dict]:
        """
        Deletes a worksheet from an existing Google Spreadsheet.

        :param key_or_url: Spreadsheet key or URL.
        :param worksheet_title: Title of the worksheet to delete.
        :return: True if successful, False otherwise.
        """
        try:
            if not worksheet_title:
                worksheet_title = self.worksheet_title

            spreadsheet = self.open_spreadsheet(key_or_url)
            worksheet = spreadsheet.worksheet(worksheet_title)
            spreadsheet.del_worksheet(worksheet)
            return True
        except Exception as e:
            self.logger.error(f"Error deleting worksheet: {traceback.format_exc()}")
            return {"error": str(e)}

    def share_spreadsheet(
        self,
        emails: Union[str, list],
        key_or_url: str = "",
        permissions: str = "",
        role: str = "writer",
    ) -> Union[list, dict]:
        """
        Shares a spreadsheet with one or more users.

        :param key_or_url: Spreadsheet key or URL.
        :param emails: Email(s) to share the spreadsheet with.
        :param role: Role to assign (e.g., "reader", "writer").
        :return: List of share results.
        """
        try:
            spreadsheet = self.open_spreadsheet(key_or_url)
            shs = []
            if isinstance(emails, list):
                for email in emails:
                    result = spreadsheet.share(email, perm_type=permissions, role=role)
                    shs.append(result)
            else:
                result = spreadsheet.share(emails, perm_type=permissions, role=role)
                shs.append(result)

            return shs
        except Exception as e:
            self.logger.error(f"Error sharing spreadsheet: {traceback.format_exc()}")
            return {"error": str(e)}

    def update_cell(
        self, cell: str, value: str, key_or_url: str = "", worksheet_title: str = ""
    ) -> dict:
        """
        Updates a cell or a range of cells in the specified worksheet.

        :param key_or_url: Spreadsheet key or URL.
        :param worksheet_title: Title of the worksheet.
        :param cell: Cell or range to update (e.g., "A1" or "A1:B2").
        :param value: Value to set in the cell(s).
        :return: Update result.
        """
        try:
            if not worksheet_title:
                worksheet_title = self.worksheet_title

            spreadsheet = self.open_spreadsheet(key_or_url)
            worksheet = spreadsheet.worksheet(worksheet_title)
            result = worksheet.update(cell, value)
            return result
        except Exception as e:
            self.logger.error(f"Error updating cell: {traceback.format_exc()}")
            return {"error": str(e)}

    def update_cell_by_coordinates(
        self,
        row: int = 0,
        col: int = 0,
        key_or_url: str = "",
        worksheet_title: str = "",
        value: str = "",
    ) -> Union[dict, dict]:
        """
        Updates a cell by coordinates in the specified worksheet.

        Examples:
        - update_cell_by_coordinates(data, "Sheet4", 1, 4, "Bingo!!")
        """
        try:
            if not worksheet_title:
                worksheet_title = self.worksheet_title

            spreadsheet = self.open_spreadsheet(key_or_url)
            worksheet = spreadsheet.worksheet(worksheet_title)
            row = int(row)
            col = int(col)
            result = worksheet.update_cell(row, col, value)
            return result
        except Exception as e:
            self.logger.error(
                f"Error updating cell by coordinates cell: {traceback.format_exc()}"
            )
            return {"error": str(e)}

    def format_cell(
        self,
        key_or_url: str = "",
        worksheet_title: str = "",
        cell: str = "",
        format_options: Optional[dict] = None,
    ) -> Union[dict, dict]:
        """
        Formats a cell or a range of cells in the specified worksheet.

        Examples:
        - format_cell(data, "Sheet4", "A8", {'textFormat': {'bold': True}})
        """
        try:
            if not worksheet_title:
                worksheet_title = self.worksheet_title

            sh = self.open_spreadsheet(key_or_url)
            worksheet = sh.worksheet(worksheet_title)
            result = worksheet.format(cell, format_options)
            return result
        except Exception as e:
            self.logger.error(f"unable to format cell: {traceback.format_exc()}")
            return {"error": str(e)}

    def merge_cells(
        self, key_or_url: str = "", worksheet_title: str = "", cells: str = ""
    ) -> Union[dict, dict]:
        """Merges cells in the specified worksheet."""
        try:
            if not worksheet_title:
                worksheet_title = self.worksheet_title

            sh = self.open_spreadsheet(key_or_url)
            worksheet = sh.worksheet(worksheet_title)
            result = worksheet.merge_cells(cells)
            return result
        except Exception as e:
            self.logger.error(f"unable to merge cells: {traceback.format_exc()}")
            return {"error": str(e)}

    def insert_rows(
        self,
        values: list[list],
        key_or_url: str = "",
        worksheet_title: str = "",
        row_index: str = "",
        value_input_option: str = "RAW",
        inherit_from_before: bool = False,
    ) -> Union[dict, dict]:
        """Inserts rows into the specified worksheet."""
        try:
            if not worksheet_title:
                worksheet_title = self.worksheet_title

            sh = self.open_spreadsheet(key_or_url)
            worksheet = sh.worksheet(worksheet_title)
            result = worksheet.insert_rows(
                values, row_index, value_input_option, inherit_from_before
            )
            return result
        except Exception as e:
            self.logger.error(f"unable to insert rows: {traceback.format_exc()}")
            return {"error": str(e)}

    def batch_clear(
        self, range: list, key_or_url: str = "", worksheet_title: str = ""
    ) -> Union[dict, dict]:
        """Clears a range of cells in the specified worksheet."""
        try:
            if not worksheet_title:
                worksheet_title = self.worksheet_title

            sh = self.open_spreadsheet(key_or_url)
            worksheet = sh.worksheet(worksheet_title)
            result = worksheet.batch_clear(range)
            return result
        except Exception as e:
            self.logger.error(f"unable to batch clear: {traceback.format_exc()}")
            return {"error": str(e)}

    def find_cell(
        self, value: str, key_or_url: str = "", worksheet_title: str = ""
    ) -> Union[dict, dict]:
        """Finds a cell in the specified worksheet."""
        try:
            if not worksheet_title:
                worksheet_title = self.worksheet_title

            sh = self.open_spreadsheet(key_or_url)
            worksheet = sh.worksheet(worksheet_title)
            res = worksheet.find(value)

            return {"status": 200, "row": res.row, "column": res.col}

        except Exception as e:
            self.logger.error(f"unable to find cell: {traceback.format_exc()}")
            return {"error": str(e)}
