# Google Scholar Publication Frequency Tool

This tool creates visualizations of how frequently terms appear in academic publications over time, based on Google Scholar data. It scrapes the number of search results for each year and generates a graph.

## Installation

1. Install Python dependencies:
```bash
pip install pandas matplotlib selenium beautifulsoup4
```

2. Install ChromeDriver:
- **MacOS**: `brew install chromedriver`
- **Windows/Linux**: 
  1. Check your Chrome version (Help > About Google Chrome)
  2. Download matching ChromeDriver from https://sites.google.com/chromium.org/driver/
  3. Add to system PATH

## Usage

1. Save the script as `scholar_graph.py`
2. Run: `python scholar_graph.py`
3. Follow the prompts to enter:
   - Search term
   - Start year
   - End year

The tool will display a graph showing publication frequency over time.

## Important Notes

- Use responsibly to avoid being blocked by Google Scholar
- The tool includes a 2-second delay between requests
- Results are approximate based on Google Scholar's "About X results" count
- Requires active internet connection
- Chrome browser must be installed

## Troubleshooting

If you get WebDriver errors:
- Verify Chrome is installed
- Ensure ChromeDriver version matches your Chrome version
- Check that ChromeDriver is in your system PATH

## Limitations

- Google Scholar may block rapid repeated requests
- Results are estimates, not exact counts
- Cannot handle complex search queries with special characters
