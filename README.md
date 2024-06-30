# Indian Election Results Scraper

This repository contains a Python script to scrape and compile election results from the Election Commission of India's website into an Excel file. The results include party-wise data for states and union territories.

 **Features**:

- Scrapes party-wise election results from the official ECI website.
- Compiles data into an Excel file with separate sheets for each state and union territory.
- The first sheet contains an overview of party-wise results.
- State and Union Territory sheet names are cleaned and shortened for better readability.

 **Prerequisites**

- Python 3.x
- Required Python libraries:
  - requests
  - beautifulsoup4
  - pandas
  - openpyxl

1. You can install the required libraries using:
  pip install requests beautifulsoup4 pandas openpyxl

2.Clone the repository:
  git clone https://github.com/your-username/indian-election-results-scraper.git
  cd indian-election-results-scraper
  
3. Run the script:
  python election_results_scraper.py

The script will generate an Excel file named election_results_final.xlsx with the scraped data.

**Customization**
If you need to customize the script, you can modify the following sections:
  -->URL format for states and union territories: The script uses formatted URLs to fetch data for each state and union territory. You can adjust the format if needed.
  -->Sheet naming: The script cleans and shortens sheet names to ensure they fit within Excel's 31-character limit. You can adjust the cleaning logic if necessary

**Contributing**
  Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please create a pull request or open an issue.
