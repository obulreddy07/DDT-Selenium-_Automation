🚀 Project: Data-Driven Test Automation Using Selenium With Python & Excel.
I developed a data-driven test automation framework using Python and Selenium, integrated with Excel for input and reporting. The framework reads test data (Principal, Rate of Interest, Period, Expected Interest) from an Excel sheet, executes automated tests on a Money Deposit Calculator webpage, and validates the calculated interest against expected values.

✅ Pass cases are logged back into Excel with a green highlight using OpenPyXL PatternFill.
❌ Fail cases are logged with a red highlight for clear visibility.

The solution demonstrates end-to-end automation: data handling, browser interaction, validation, and reporting.

Technologies Used: Python, Selenium WebDriver, OpenPyXL, PatternFill, Excel
This project highlights my ability to design robust automation workflows, integrate external data sources, and produce professional test reports — making it ideal for real-world QA.

## 📂 Project Structure:
## Data-Driven Test Automation Using Selenium With Python & Excel

## 📌 Project Overview
This project automates the testing of a **Money Deposit Calculator** using data-driven testing. 
Test data (Principal, Rate of Interest, Period, Expected Interest) is stored in an Excel file. 
The script reads the data, enters it into the calculator webpage, and verifies the calculated interest against the expected value.

- ✅ If the result matches → "Passed" is written in Excel with **green fill**.
- ❌ If the result does not match → "Failed" is written in Excel with **red fill**.

## 🛠️ Technologies Used
- **Python** – Core programming language
- **Selenium WebDriver** – Browser automation
- **OpenPyXL** – Excel file handling
- **PatternFill (OpenPyXL)** – Cell formatting for Pass/Fail results
- **Excel** – Data source for test cases

## ⚙️ Workflow
1. Prepare test data in Excel:
 - Principal Amount
 - Rate of Interest
 - Period
 - Expected Interest
2. Run the Python script:
 - Script launches browser and navigates to Money Deposit Calculator.
 - Inputs values from Excel.
 - Captures calculated interest.
 - Compares with expected interest.
3. Write results back to Excel:
 - "Passed" → Green cell
 - "Failed" → Red cell.
### Instructions ####
1. The DDT file is the Main code of the python
2. The xlutils is the supportive functions file which is mandatory to execute the Workflow
3. The screenshots and Recordings will help you to understand the code execution.
