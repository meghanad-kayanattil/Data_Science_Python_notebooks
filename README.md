# Collection of Python scripts and Jupyter notebooks 
## Exploring techniques of data acquisition, cleaning and application of machine learning models
The repository is divided into sub modules where a unique problems are tackled, each module contains all the necessary ingreadents (data, data acquisition scripts and analysis notebooks) for completion of these relatively small projects. 

- ## [Rent prediction for Hamburg from the web-scraped data](https://github.com/meghanad-kayanattil/Data_Science_Python_notebooks/tree/main/Rent%20prediction%20wt%20linear%20regression-Hamburg-2022-July)

Implementad on web scrapped data using <code>Scikit-learn</code> (linear & polynomial) regression models and neural network built using <code>Tensorflow, keras </code> 

![summary_rent](https://github.com/meghanad-kayanattil/Data_Science_Python_notebooks/blob/main/Rent%20prediction%20wt%20linear%20regression-Hamburg-2022-July/Figures/Summary.jpg)
  **Data collection**: A web scraper for a prominent real estate website is implimented to generate a data set containing the apartment/house area, number of rooms and the     asking rent using <code>Beautifulsoup and requests</code>. 
  
  **Additional required libraries**  <code>Numpy, Matplotlib, Geopy, Seaborn</code> and <code>Pandas</code>.
  
  **Take aways**: More data and more features (like, specific location, age of the building, other amenities like balcony, furnishing etc.) are needed for a very accurate     prediction. But, for now this will serve as a simple introduction to regression. 
