# Quantium Job Simulation
A brief course that gives hands-on data and building dashboards with Dash.  

![image](https://github.com/ezz55/quantium-dash-app/assets/98974918/57190f8b-5a5c-4276-b5d1-46725281794e)

1. **Data Pre-Processing and preparation**:
   - 3 CSV files were given in this task; they where merged into 1 CSV file and filter to suit the required items.
2. ** Creation of Dash Interface and Development**:
   - Based on the structure of the provided sales data, code was provided to create a Dash application. This application was designed to include a line chart for visualizing sales data over time, with dates on the X-axis and sales figures on the Y-axis. Features for aggregating sales data by date and a dropdown menu for selecting different regions to filter the displayed sales data in the graph were included.
   - Python code was requested to be used for generating a Dash interface where 'X' would represent the date and 'Y' would represent the sales. A CSV file containing sales data was loaded and inspected to understand its structure.

3. **Enhancements to Dash App**:
   - The graph title was modified to include dynamic content based on the selection from the dropdown.
   - An "All Regions" option was added to the dropdown menu.
   - A second Y-axis was included in the graph to display price data alongside sales data.
   - An additional chart was created to display quantity data in a similar manner.

4. **Styling of the Dash App**:
   - Styling for the Dash application was requested to make it visually appealing. Guidance was provided on applying inline CSS styles to various components of the app to adopt a dark-themed interface. This included styling for the header, dropdown menu, and graphs.

5. **Unit Testing with Dash[testing]**:
   - The setup of unit testing for the Dash application using the Dash testing framework, which is built on top of Selenium, was discussed. Examples of how to write unit tests to verify the presence of key elements in the app (the header, a visualization (graph), and the region picker (dropdown)) were provided.

6. **Troubleshooting of Test Execution Issues**:
   - Errors encountered while attempting to run the tests, specifically issues related to importing the Dash app module in the tests and warnings regarding the Selenium WebDriver setup, were addressed. Solutions to the module import error by ensuring the correct project structure and file naming, as well as updating the Selenium WebDriver instantiation to use the `Service` object and `webdriver_manager`, were offered.

7. **Simplified Testing Approach**:
   - After issues continued to be faced with running the tests, a simplification of both the Dash app and the test suite was suggested to isolate and identify the problem. This approach was aimed at verifying the basic setup and functionality of testing a minimal Dash application.

