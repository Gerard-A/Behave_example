# Behave_example

This Behave example shows the following Gherkin features:

- Background
- Scenario and Scenario Outline + Examples
- Given, When, Then, And
- tags

"Behave" documentation is available on: https://behave.readthedocs.io/en/stable/

## Feature files

### CheckLocation.feature
This feature contains Gherkin Scenarios and Scenario Outlines and is compatible with other test frameworks that implement the Gherkin syntax.
For example Cucumber and SpecFlow. See https://github.com/Gerard-A/SpecFlow_Example for a SpecFlow C# project, that uses the same feature file.

### BackgroundExample.feature
This feature contains an example of a feature that uses a Background.
The Background contains common steps that will be executed before every Scenario

## Test execution

Prerequisites: 
- python 3 must be installed on your system. 
- All required python packages are installed on your system or in a "virtual environment".
  To install the required packages run `pip install -r requirements.txt`

To run the tests execute command:  
`runTest.bat`