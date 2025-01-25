# NBA Game Logs Scraper

This project is a Python script designed to scrape NBA game logs from Basketball Reference for every NBA team from 2013 to 2024. The data is processed into a structured format and saved as a CSV file for further analysis.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)

---

## Features

- Scrapes game logs for NBA teams from the [Basketball Reference](https://www.basketball-reference.com/) website.
- Processes data into a pandas DataFrame.
- Adds contextual information such as season and team identifiers.
- Saves the final dataset as a CSV file for easy integration with other tools and workflows.

---

## Requirements

This script uses the following Python libraries:

- `numpy`
- `pandas`
- `lxml`
- `html5lib`
- `beautifulsoup4`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/a369kuma/nba-game-logs-scraper.git
   cd nba-game-logs-scraper
