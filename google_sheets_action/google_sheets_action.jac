import:py logging;
import:py traceback;
import:py from logging { Logger }
import:py from .modules.google_sheet_api { GoogleSheetsAPI }
import:jac from jivas.agent.action.action { Action }


node GoogleSheetsAction :Action: {
    # Provides seamless integration with Google Sheets using the gspread API for managing and automating spreadsheet tasks.

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

    can on_enable() {
        self.on_register();
    }

    can api() -> GoogleSheetsAPI {
        return GoogleSheetsAPI(
            key_or_url=self.key_or_url,
            worksheet_title=self.worksheet_title,
            info_type=self.info_type,
            project_id=self.project_id,
            private_key_id=self.private_key_id,
            private_key=self.private_key,
            client_email=self.client_email,
            client_id=self.client_id,
            auth_uri=self.auth_uri,
            token_uri=self.token_uri,
            auth_provider_x509_cert_url=self.auth_provider_x509_cert_url,
            client_x509_cert_url=self.client_x509_cert_url,
            universe_domain=self.universe_domain
        );
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
            try {
                spreadsheet = self.api().open_spreadsheet();

                if "error" in spreadsheet {
                    return {
                        "status": False,
                        "message": f"{spreadsheet['error']}",
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


