# Writing Google Sheets Data to MySQL
Google Sheets is a great tool for collaboration. When a sheet has too much data it will run very slowly, and in general it can be useful to store this data in a MySQL table. This script can be used to automate this process.

### Pull Data From Google Sheets
The script will connect to the Google sheet by using the `gspread` library where a json file is read in with credentials that are used by Python to be able to pull the data from the sheet. An email in the json file is added to the sheet as a collaborator. 

### Writing to MySQL
Once the data is pulled, it is written to a MySQL table. The table is created with the correct data types for each column, and the sheet data is written to the table.
