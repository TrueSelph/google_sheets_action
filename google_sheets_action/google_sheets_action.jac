import:py logging;
import:py traceback;
import:py from logging { Logger }
import:py from .modules.google_sheet_api { GoogleSheetAPI }
import:jac from jivas.agent.action.action { Action }


node GoogleSheetsAction :Action: {

    has description:str = "Provides seamless integration with Google Sheets using the gspread API for managing and automating spreadsheet tasks.";
    has key_or_url:str = "";
    has worksheet_title:str = "Sheet1";

    has info_type:str = "service_account";
    has project_id:str = "";
    has private_key_id:str = "";
    has private_key:str = "";
    has client_email:str = "";
    has client_id:str = "";
    has auth_uri:str = "";
    has token_uri:str = "";
    has auth_provider_x509_cert_url:str = "";
    has client_x509_cert_url:str = "";
    has universe_domain:str = "googleapis.com";


    can get_credentials() -> dict {

        credentials = {
            "credentials": {
                "type": self.info_type,
                "project_id": self.project_id,
                "private_key_id": self.private_key_id,
                "private_key": self.private_key,
                "client_email": self.client_email,
                "client_id": self.client_id,
                "auth_uri": self.auth_uri,
                "token_uri": self.token_uri,
                "auth_provider_x509_cert_url": self.auth_provider_x509_cert_url,
                "client_x509_cert_url": self.client_x509_cert_url,
                "universe_domain": self.universe_domain
            },
            "key_or_url": self.key_or_url,
            "worksheet_title": self.worksheet_title
        };
        return credentials;
    }


    can open_spreadsheet() -> dict {
        credentials = self.get_credentials();
        spreadsheet = GoogleSheetAPI.open_spreadsheet(credentials);
        return spreadsheet;
    }


    can open_worksheet(worksheet_title:str) -> dict {
        if not worksheet_title {
            worksheet_title = self.worksheet_title;
        }

        credentials = self.get_credentials();
        worksheet = GoogleSheetAPI.open_worksheet(credentials, worksheet_title);
        return worksheet;
    }


    can create_spreadsheet(title:str) -> dict {
        credentials = self.get_credentials();
        spreadsheet = GoogleSheetAPI.create_spreadsheet(credentials, title);
        return spreadsheet;
    }


    can create_worksheet(worksheet_title:str) -> dict {
        credentials = self.get_credentials();
        worksheet = GoogleSheetAPI.create_worksheet(credentials, worksheet_title);
        return worksheet;
    }


    can delete_worksheet(worksheet_title:str) -> dict {
        credentials = self.get_credentials();
        worksheet = GoogleSheetAPI.delete_worksheet(credentials, worksheet_title);
        return worksheet;
    }


    can share_spreadsheet(emails:list, permissions:str, role:str) -> dict {
        credentials = self.get_credentials();
        spreadsheet = GoogleSheetAPI.share_spreadsheet(credentials, emails, permissions, role);
        return spreadsheet;
    }


    can update_cell(cell:str, value:str, worksheet_title:str="") -> dict {
        if not worksheet_title {
            worksheet_title = self.worksheet_title;
        }

        credentials = self.get_credentials();
        worksheet = GoogleSheetAPI.update_cell(credentials, worksheet_title, cell, value);
        return worksheet;
    }


    can update_cell_by_coordinates(row:str, col:str, value:str, worksheet_title:str="") -> dict {
        if not worksheet_title {
            worksheet_title = self.worksheet_title;
        }

        credentials = self.get_credentials();
        worksheet = GoogleSheetAPI.update_cell_by_coordinates(credentials, worksheet_title, row, col, value);
        return worksheet;
    }


    can format_cell(cell:str, format_options:str, worksheet_title:str="") -> dict {
        if not worksheet_title {
            worksheet_title = self.worksheet_title;
        }

        credentials = self.get_credentials();
        worksheet = GoogleSheetAPI.format_cell(credentials, worksheet_title, cell, format_options);
        return worksheet;
    }


    can merge_cells(cells:str, worksheet_title:str="") -> dict {
        if not worksheet_title {
            worksheet_title = self.worksheet_title;
        }

        credentials = self.get_credentials();
        worksheet = GoogleSheetAPI.merge_cells(credentials, worksheet_title, cells);
        return worksheet;
    }


    can insert_rows(values:list, row_index:str, value_input_option:str="RAW", inherit_from_before:bool=False, worksheet_title:str="") -> dict {
        if not worksheet_title {
            worksheet_title = self.worksheet_title;
        }

        credentials = self.get_credentials();
        worksheet = GoogleSheetAPI.insert_rows(credentials, worksheet_title, values, row_index, value_input_option, inherit_from_before);
        return worksheet;
    }


    can batch_clear(range: list, worksheet_title:str="") -> dict {
        if not worksheet_title {
            worksheet_title = self.worksheet_title;
        }

        credentials = self.get_credentials();
        worksheet = GoogleSheetAPI.batch_clear(credentials, worksheet_title, range);
        return worksheet;
    }


    can find_cell(value: str, worksheet_title:str="") -> dict {
        if not worksheet_title {
            worksheet_title = self.worksheet_title;
        }

        credentials = self.get_credentials();
        worksheet = GoogleSheetAPI.find_cell(credentials, worksheet_title, value);
        return worksheet;
    }


    can healthcheck() -> Union[bool, dict] {
        try {
            # Validate required credentials
            if not self.project_id or not self.private_key or not self.client_email or not self.token_uri {
                return {
                    "status": False,
                    "message": "Missing required Google Service Account credentials.",
                    "severity": "error"
                };
            }

            # Validate key_or_url
            if not self.key_or_url {
                return {
                    "status": False,
                    "message": "Missing key_or_url for the spreadsheet.",
                    "severity": "error"
                };
            }

            # Attempt to connect to Google Sheets API
            credentials = self.get_credentials();
            try {
                spreadsheet = GoogleSheetAPI.open_spreadsheet(credentials);
                if not spreadsheet {
                    return {
                        "status": False,
                        "message": "Unable to access the spreadsheet. Please check the key_or_url and permissions.",
                        "severity": "error"
                    };
                }
            } except Exception as e {
                return {
                    "status": False,
                    "message": f"Failed to open the spreadsheet: {e}",
                    "severity": "error"
                };
            }
            
            return True;

        } except Exception as e {
            return {
                "status": False,
                "message": f"Failed to connect to Google Sheets API: {e}",
                "severity": "error"
            };
        }
    } 


}


