# Sprint-4-Project

## Description

The application allows users to visualize and analyze vehicle datasets using interactive charts and controls. It demonstrates the use of random event simulation, data visualization, and dashboard creation for exploratory data analysis.

## Methods and Libraries Used

- **Python 3**
- **Streamlit** – For building the interactive web application
- **Pandas** – For data manipulation and analysis
- **Plotly Express** – For interactive data visualizations
- **os** - For checking the current working directory (with os.getcwd()).
- **Statsmodels** - Used by Plotly Express to add a trendline (OLS) to the scatterplot.

## Directory & File Structure

- **Data File**: The app reads data from a CSV file (`.csv`), which should be located in the project directory. (vehicles_us.csv)
- **.gitignore**: Present to exclude unnecessary files and folders (e.g., virtual environments, OS-specific files, Python artifacts) from version control.
- **requirements.txt**: Lists all Python dependencies needed to run the app.

## Key Features

- **Histogram Plot**: Uses `px.histogram()` from Plotly Express to display the distribution of Paint Colors on vehicles.
- **Scatter Plot with Trendline**: Uses `px.scatter()` with the `trendline="ols"` argument to show the relationship between two variables (e.g., Mileage(Odometer) vs. Model Year) and fit a linear regression.
- **Streamlit Widgets**:
  - `st.header()` for section headers/titles.
  - `st.plotly_chart()` to display interactive charts.
  - `st.checkbox()` for toggling features or options.

## How to Run This Project Locally

1. **Clone the repository** (or download the source files):

   ```bash
   git clone https://github.com/amorgan13/Sprint-4-Project.git
   cd Sprint-4-Project
   ```

2. **Install the required libraries** (preferably in a virtual environment):

   For Windows: (Optional)
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
   ```bash
   pip install streamlit pandas plotly statsmodels
   ```

3. **Launch the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

4. **A browser window should open** showing the dashboard. If not, open the URL shown in your terminal (usually `http://localhost:8501`).