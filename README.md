# Afro Productions — Box Office Analysis

**Authors:** Angela Masaki, Joy Nyuguto, David Theuri, Joel Muoki, Felista Mwangi  
**Date:** March 2026

---

## Overview

This project presents an exploratory data analysis (EDA) to guide the launch of Afro Productions, a new movie studio entering the film industry for the first time. Using box office, budget, and genre data from three industry sources, we identify what separates high-performing films from low-performing ones and translate those findings into clear, actionable recommendations for the studio's first production.

---

## Business Understanding

### Key Stakeholder
The Head of the New Movie Studio — Afro Productions

### Business Problem
Despite having no prior experience producing movies, Afro Productions wants to enter the original video content business. Without historical insight, every decision — including genre, budget, release date, target markets, and studio benchmarks — is an expensive bet. An underperforming first film could cost millions of dollars and seriously damage the business before it ever gets off the ground.

### Key Business Questions
1. What film genres give the best return on investment?
2. What production budget range maximizes profitability?
3. Which release month generates the highest box office gross?
4. Should our studio prioritize domestic or international markets?
5. Which studios should we model ourselves after?

---

## Data Understanding and Analysis

### Source of Data

The analysis uses three CSV datasets extracted from well-known film industry databases:

| Source | File | Size |
|--------|------|------|
| The Numbers | `tn_movie_budgets.csv` | 5,782 rows, 6 columns |
| The Movie DB (TMDB) | `tmdb_movies.csv` | 26,517 rows, 10 columns |
| Box Office Mojo | `bom_movie_gross.csv` | 3,387 rows, 5 columns |

### Description of Data

- **tn_movie_budgets.csv** contains production budgets and gross revenue figures (domestic and worldwide) for thousands of films. This dataset is the primary source for all financial calculations including ROI, profitability by budget tier, and market comparisons.

- **tmdb_movies.csv** contains genre metadata, popularity scores, and audience ratings from The Movie Database. It was merged with the tn dataset on movie title to enable genre-level financial analysis.

- **bom_movie_gross.csv** contains domestic and foreign gross earnings broken down by studio and year. This dataset was used to identify the top-performing studios by total box office earnings.

---

### Visualizations

#### Visualization 1 — Median ROI by Genre
![Median ROI by Genre]('../images/q1_genre_roi.png')
Horror (307%) and Mystery (217%) deliver the highest median ROI among theatrical genres, meaning these films consistently earn back more than double their production budget — largely because they are made on relatively small budgets. Animation (209%) and Family (199%) also rank highly, suggesting broad audience appeal is another reliable path to profitability.  
*Note: Although TV Movie ranks first at 345% ROI, it has been excluded from the recommendation because it refers to television productions rather than theatrical film releases.*

---

#### Visualization 2 — ROI Distribution by Production Budget Tier
![ROI by Budget Tier]('../images/q2_distribution_production_tier.png')

Films with very high budgets (over $100M) show the strongest and most consistent ROI, while low-budget films show a wide spread — meaning some do very well but many do not. Mid-range budgets ($10M–$50M) offer a reasonable middle ground for a studio just starting out.

---

#### Visualization 3 — Average Worldwide Gross by Release Month
![Average Gross by Release Month]('../images/q3_gross_release_month.png')

Films released in May ($172M), June ($152M), and July ($149M) earn significantly more on average than films released in any other month, with May standing out as the single best month to release a film. November ($145M) also performs well, while January ($51M), September ($50M), and October ($53M) are consistently the weakest months.

---

## Conclusions

Based on the analysis, Afro Productions should:

- **Start with Horror or Mystery** — these genres deliver strong returns on modest budgets, making them the lowest-risk entry point for a studio with no track record.
- **Target a large production budget (over $100M)** — bigger budgets are associated with stronger and more consistent returns once the studio is established.
- **Aim for a May or June release** — these months consistently generate the highest box office earnings. November is a reliable backup option.
- **Prioritize international distribution from day one** — the international market ($55M average) outperforms the domestic market ($46M average), so limiting reach to one region leaves significant revenue on the table.
- **Study Buena Vista (Disney), Fox, Warner Bros, and Universal** — these four studios have dominated the global box office and their strategies around genre, budget, and distribution offer the clearest benchmark for a new studio to follow.

