# Thai dates

Project for [Dharma Voices for Animals](https://www.dharmavoicesforanimals.org) to normalize Thai-style dates to US-style dates.

## Background

In Thailand, dates are usually represented `mm/dd/yr`, where the year is 543 years later than the US year. For example, the Thai date `21/4/2563` would be `4/21/2020`.

The Thai uses Thai dates in their field notes, and we don't want to ask them to change. So, this project is to add a custom Google Sheets function that will normalize the date into US-style for the US team to view in their sheet. (The US team has a dedicated Google sheet that translates the Thai team's sheet by using IMPORTRANGE + GOOGLETRANSLATE functions.)

## Implementation

Google Sheets expects JavaScript for custom functions. But, I (Eric) am more familiar with Python and also want to use test-driven development. So, I'm writing the logic and tests in Python.

Then, I'm using ChatGPT to convert to JavaScript and saving the output in `chatgpt_google_sheet_function.js`. I'm using this prompt:

```
Convert this Python function to JavaScript

--------------------------

<Copy all the code from lib.py
```

### Pantsbuild

This uses [Pantsbuild](https://www.pantsbuild.org) to simplify setting up linters and Pytest.

* Run tests: `pants test :`
* Run formatters: `pants fmt :`
* Run linters: `pants lint :`
