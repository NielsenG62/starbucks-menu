# Starbucks Nutrition Analysis

This repo contains a web scraper and CSV of Starbucks drink nutrition data.

Nutrition facts are cloned from [yhejazy's repo](https://github.com/yhejazi/starbucks-nutrition), and updated for 06 Feb 2024.

## About the Nutition Data

This program scrapes the JSON data from Starbucks' online menu and saves it as a CSV with the following variables:

- drink_name: Name of the drink
- type: Type of drink, categories defined by Starbucks
- size: Size of the drink
- calories: Number of calories
- fat: Total fat (g)
- cholesterol: Cholesterol (mg)
- sodium: Sodium (mg)
- carb: Total carbohydrates (g)
- sugar: Sugars (g)
- protein: Protein (g)
- caffeine: Caffeine (g)

## About the Price Data

The Starbucks site does not run the price before the cart is loaded, in which it only gets the price of the items in the cart. To my knowledge, this makes it impossible to scrape. The prices listed are from Uber Eats in Wilsonville, OR. Only the Grande size was taken. The prices also didn't match what the Starbucks site has exactly, there seems to be a general upcharge baked into the Uber Eats price. The price is the same as other delivery services. My guess is this is a price set by Starbucks.
