Business Scenario: Data Processing System for hypothetical business “IronGains Fitness”

IronGains Fitness Business Background:
IronGains Fitness is a fast-growing urban gym with multiple revenue streams and a steady flow of member activity. 
The gym operates a main facility with a weights area, cardio zone and a group fitness studio. 
The gym also maintains a small retail section at the front desk selling supplements, merchandise and accessories. 
Members check in daily through either barcode scanning or a mobile app, and the sales system exports raw data in Excel.

The gym’s operations generate four major datasets:
-Sales data (products, class packs, PT packs, memberships, retail items)
-Product catalogue (name, category, pricing)
-Member check-ins through QR or barcode
-Class attendance records
Currently, management exports these files monthly into Excel and manually cleans, merges and analyses them before performance meetings. 

This manual workflow often leads to business managerial inconsistencies, constant errors and delays when producing business insights.


Project Objectives:
The project objectives consist of five core areas:

1: Automating Core Monthly Reporting
This project replaces manual Excel work by using Python (Pandas) to ingest raw Excel sheets and automatically process:
-Sales data
-Product details
-Check-ins
-Class attendance

2: Generate Clear Commercial Insights
The script calculates:
-Revenue by product
-Revenue by category (Supplements, PT Packs, Class Packs, Merch and Accessories)
-Monthly revenue totals
-Units sold per product and per category

3: Track Member Engagement
Although future expansion could include dashboards and deeper engagement analytics, this version establishes the foundation by:
-Cleaning check-in timestamps
-Cleaning class attendance timestamps

4: Support Operational & Strategic Decisions
The output helps management quickly understand:
-Which products generate the highest revenue
-Which product categories perform best
-Whether revenue is trending up/down month-to-month
-Which areas of the business (retail, PT, group classes) deserve more focus

5: Minimise Manual Excel Work
By automating data cleaning, merging and aggregation,
this project eliminates hours of repetitive manual tasks and ensures results are accurate and reproducible every month.


Technical Summary:
This project uses Python, Pandas, and OpenPyXL to:
-Load multiple Excel sheets
-Standardise column names
-Convert date/time fields
-Merge sales with product data
-Compute revenue
-Group and aggregate analytics output
-Print insights directly into the console
All dependencies are stored in requirements.txt, enabling anyone to reproduce the analytics workflow easily.


Project Outcome:
The final script produces a complete performance summary, including:
-Revenue by product
-Revenue by category
-Monthly totals
-Sample data previews
-Cleaned and merged datasets ready for further dashboarding
This serves as a scalable foundation for future enhancements such as exporting reports, 
generating visual dashboards or integrating into a larger BI pipeline.









<img width="468" height="646" alt="image" src="https://github.com/user-attachments/assets/bd055a8c-2180-47a4-b298-aecdb406358b" />
