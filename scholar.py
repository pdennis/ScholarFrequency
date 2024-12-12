import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

def fetch_scholar_frequency(search_term, start_year, end_year):
    """
    Fetches publication frequency data from Google Scholar for a given search term
    
    Args:
        search_term (str): Term to search for
        start_year (int): Starting year for analysis
        end_year (int): Ending year for analysis
    
    Returns:
        pandas DataFrame with years and publication counts
    """
    # Initialize data storage
    years = list(range(start_year, end_year + 1))
    counts = []
    
    print(f"Fetching data for '{search_term}'...")
    
    # Set up selenium (you'll need webdriver installed)
    driver = webdriver.Chrome()
    
    for year in years:
        print(f"Processing year {year}...")
        # Construct the search URL with year filter
        search_url = f"https://scholar.google.com/scholar?q={search_term}&as_ylo={year}&as_yhi={year}"
        
        # Fetch the page
        driver.get(search_url)
        time.sleep(2)  # Avoid getting blocked
        
        # Parse results
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results_text = soup.find('div', {'id': 'gs_ab_md'}).text
        
        # Extract count using regex
        count_match = re.search(r'About ([\d,]+) results', results_text)
        if count_match:
            count = int(count_match.group(1).replace(',', ''))
            counts.append(count)
        else:
            counts.append(0)
    
    driver.quit()
    
    # Create DataFrame
    df = pd.DataFrame({
        'Year': years,
        'Publications': counts
    })
    
    return df

def plot_frequency(df, search_term):
    """
    Creates a line plot of publication frequency over time
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['Year'], df['Publications'], marker='o')
    plt.title(f'Publication Frequency for "{search_term}" in Google Scholar')
    plt.xlabel('Year')
    plt.ylabel('Number of Publications')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    # Get user input
    search_term = input("Enter your search term: ")
    start_year = int(input("Enter start year (e.g., 2000): "))
    end_year = int(input("Enter end year (e.g., 2023): "))
    
    # Fetch and plot the data
    df = fetch_scholar_frequency(search_term, start_year, end_year)
    plot_frequency(df, search_term)

if __name__ == "__main__":
    main()