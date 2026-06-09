# The Data Visualization Workshop

- **Source:** TheDataVisualizationWorkshop_eBook-200229-110313.pdf
- **Drive link:** https://drive.google.com/file/d/1I5ht79h9QG0op1mKa6Sow_jubUUBADm_/view?usp=drivesdk
- **Type:** book
- **Author/Year:** Mario Döbler, Tim Großmann / 2020 (Second Edition)
- **Coverage:** partial (large file, truncated extraction)

## Overview
A hands-on workshop-style textbook teaching data visualization in Python, published by Packt. The second edition covers foundational Python data libraries (NumPy and pandas), an extensive catalogue of plot types, interactive plotting with Bokeh, and geospatial visualization. Each concept is reinforced through exercises and activities on real datasets.

## Unique contribution
Provides a taxonomy of visualization types organized by purpose (comparison, relation, composition, distribution, geospatial) with explicit design guidelines for when to use each. Pairs statistical theory (correlation, central tendency, dispersion) directly with implementation in Python, bridging the gap between conceptual understanding and code.

## Key concepts
- Data wrangling
- NumPy array operations (indexing, slicing, filtering, reshaping)
- pandas DataFrame and Series
- Matplotlib line chart, bar chart, radar chart
- Scatter plot, bubble plot, correlogram, heatmap
- Pie chart, donut chart, stacked bar chart
- Distribution plots (histogram, density/KDE, box plot, violin plot)
- Bokeh interactive visualization
- Geospatial visualization
- Summary statistics, measures of central tendency, dispersion
- Exploratory data analysis (EDA)

## Methods / results / takeaways
- NumPy underpins fast array math but pandas is better suited for tabular, labeled data despite higher overhead.
- Design guidelines emphasize avoiding misleading scales in bar charts and using color sparingly.
- Radar charts suit multi-attribute comparison but become cluttered beyond ~8 dimensions.
- Correlation matrices and correlograms are recommended before modeling to spot multicollinearity.
- Bokeh adds hover interactivity useful for exploratory dashboards without requiring a web server.
- Geospatial chapter covers choropleth maps and marker overlays with folium/geopandas.
