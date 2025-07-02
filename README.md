# NutriSense

**Predicting the nutritional content of food items based on ingredients and quantities.**

This project aims to provide a comprehensive tool for analyzing the nutritional profile of recipes. By leveraging Natural Language Processing (NLP) to parse ingredient lists and integrating with robust nutritional databases, NutriSense will offer detailed breakdowns and valuable health insights.

## Key Features:
- Ingredient parsing from natural language input
- Accurate nutritional content prediction (calories, macros, micros)
- Unit conversion and standardization
- (Planned) Healthiness scoring and diet compatibility tagging (Keto, Vegan, Diabetic-friendly)
- (Planned) Ingredient similarity using embeddings

## Project Components:
1.  **Nutritional Data Management & Lookup:** (Current Focus)
    * Acquisition and cleaning of data from USDA FoodData Central and Nutritionix API.
    * Database storage for efficient lookup.
2.  **Recipe Parsing Module (NLP Core):**
    * Extracting ingredients, quantities, and units from text.
3.  **Nutritional Calculation Engine:**
    * Aggregating nutrient values based on ingredient quantities.
4.  **Bonus Features Module:**
    * Healthiness scoring and diet compatibility logic.
5.  **Presentation Layer:**
    * User interface for input and results.

## Getting Started:

### Prerequisites
- Python 3.12.10
- Git

### Installation

## Data Sources:
- USDA FoodData Central
- Nutritionix API

---
*Developed as a portfolio project.*