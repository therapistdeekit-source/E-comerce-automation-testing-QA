# E-Commerce Website Automation Testing with Playwright and Python

## Project Overview

This project focuses on automating functional test cases for an e-commerce website using **Python, Playwright, and Pytest**.

The purpose of this project is to validate important e-commerce functionalities, identify potential defects, and ensure that the website performs as expected from a user's perspective.

The tests are performed on [Automation Exercise](https://automationexercise.com/), an online platform designed for practicing software testing.

## Tools and Technologies

- **Programming Language:** Python
- **Automation Framework:** Playwright
- **Testing Framework:** Pytest
- **Code Editor:** Visual Studio Code (VS Code)
- **Browser:** Chromium
- **Version Control:** Git and GitHub
- **Website Under Test:** Automation Exercise

## Project Objectives

- Automate important e-commerce user journeys.
- Verify website navigation and functionality.
- Test product listings and search functionality.
- Validate shopping cart operations.
- Test login and registration functionality.
- Identify and report application defects.
- Practise writing and executing automated test scripts.

## Test Scenarios

The project covers the following test areas:

| Test Scenario | Description |
|---|---|
| Homepage | Verify that the homepage loads successfully. |
| Product Listing | Verify that products are displayed correctly. |
| Product Search | Verify that users can search for products. |
| Product Details | Verify product information and availability. |
| Add to Cart | Verify that products can be added to the cart. |
| Shopping Cart | Verify product quantity, price and removal functionality. |
| Login | Verify user login functionality. |
| Registration | Verify account registration and validation. |
| Checkout | Verify the checkout process. |

## Project Structure

```text
E-commerce-Automation-Testing/
│
├── test_ecommerce.py
├── README.md
├── requirements.txt
│
└── .venv/
```

## Installation and Setup

### 1. Clone the Repository

```bash
[git clone YOUR_GITHUB_REPOSITORY_URL](https://github.com/therapistdeekit-source/E_commerce-automation.git)
```

### 2. Navigate to the Project Folder

```bash
cd E-commerce-Automation-Testing
```

### 3. Create a Virtual Environment

```bash
python3 -m venv .venv
```

### 4. Activate the Virtual Environment

For macOS:

```bash
source .venv/bin/activate
```

For Windows:

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 6. Install Playwright Chromium

```bash
python3 -m playwright install chromium
```

## Running the Tests

To execute all tests:

```bash
python3 -m pytest -v
```

To execute a specific test file:

```bash
python3 -m pytest -v test_ecommerce.py
```

To execute an individual test:

```bash
python3 -m pytest -v test_ecommerce.py::test_ecommerce
```

## Test Results

Test execution is performed using Pytest.

The test results indicate whether each automated test has passed or failed.

Screenshots and additional test evidence can be added as the project develops.

## Learning Outcomes

Through this project, I am developing practical skills in:

- Python programming for test automation.
- Playwright browser automation.
- Pytest test execution and reporting.
- Writing and maintaining automated test scripts.
- Identifying and debugging test failures.
- Using Git and GitHub for version control.
- Understanding real-world e-commerce testing workflows.

## Future Improvements

- Expand automated test coverage.
- Implement reusable functions and fixtures.
- Add positive and negative test scenarios.
- Introduce assertions and validation checks.
- Generate HTML test reports.
- Integrate automated tests into a CI/CD pipeline.

## Author

**Deborah Oladipupo**

QA Engineer | Manual Testing | Python | Playwright | Pytest

This project is part of my continuous learning journey in Software Quality Assurance and Test Automation.

