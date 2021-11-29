### Goals
- Identify Drivers of Churn
- Build a Model that accurately predicts churn better than the baseline (of predicting no churn)

### Initial Hypotheses
- Contract status, Internet subscription status, partner status, payment type are all drivers of change.

### Data Dictionary\n,
| Feature                    | Datatype               | Description                                                           |
|:---------------------------|:-----------------------|:----------------------------------------------------------------------|
| customer_id                | 7043 non-null: object  | Identification number for customer                 |
| gender                     | 7043 non-null: object  | Customer gender, male or female                    |
| senior_citizen             | 7043 non-null: int64   | Yes or No, is the customer a senior citizen        |
| partner                    | 7043 non-null: object  | Yes or No, does the customer customer has a parter |
| dependents                 | 7043 non-null: object  | Number of dependents a customer has                |
| tenure                     | 7043 non-null: int64   | Months a customer has been with the company        |
| phone_service              | 7043 non-null: object  | Phone Service plan, Yes or No                      |
| multiple_lines             | 7043 non-null: object  | Multiple lines, Yes or No                          |
| internet_service_type_id   | 7043 non-null: int64   | 1, 2, 3                                            |
| online_security            | 7043 non-null: object  | Yes, no, or no internet service                    |
| online_backup              | 7043 non-null: object  | Yes, no, or no internet service                    |
| device_protection          | 7043 non-null: object  | Yes, no, or no internet service                    |
| tech_support               | 7043 non-null: object  | Yes, no, or no internet service                    |
| streaming_tv               | 7043 non-null: object  | Yes, no, or no internet service                    |
| streaming_movies           | 7043 non-null: object  | Yes, no, or no internet service                    |
| contract_type_id           | 7043 non-null: int64   | 1, 2, 3                                            |
| paperless_billing          | 7043 non-null: object  | Yes or no, customer uses paperless billing         |
| payment_type_id            | 7043 non-null: int64   | 1, 2, 3, 4                                         |
| monthly_charges            | 7043 non-null: float64 | Monthly charges the customer pays                  |
| total_charges              | 7043 non-null: object  | Total charges the customer has paid                |
| churn                      | 7043 non-null: object  | Yes or no, whether or not the customer has churned |
| contract_type_id.1         | 7043 non-null: int64   | 1, 2, 3                                            |
| contract_type              | 7043 non-null: object  | Month-to-month, One year, Two year                 |
| internet_service_type_id.1 | 7043 non-null: int64   | 1, 2, 3                                            |
| internet_service_type      | 7043 non-null: object  | DSL, Fiber Optic, or None                          |
| payment_type_id.1          | 7043 non-null: int64   | 1, 2, 3, 4                                         |
| payment_type               | 7043 non-null: object  | E-check, mailed check, bank transfer, credit card  |

### Project Planning\n",

- Wrangle (Acquire, Prepare, Tidy Data)
- Confirm/Deny independence of contracts, partner status, payment type, internet subscription status via statistical and graphical representations
- Explore categorization models (Decision Tree, Random Tree, KNN, Logistic Regression)

### Instructions
- Data pulled from Codeup DB
- Standard Python Libs for Pandas, Sklearn, Seaborn, Matplotlib.
- Random Seed used is always: 123

### Hypotheses Answer
- None of the items are independent, however internet subscription status is far less notable compared to contract, payment method, and partner status.

### Key Findings
- Payment type is a significant driver of churn

### Recommendations
- Automatic payments should be incentivized to reduce churn

### Takeaways
- Further explore extent to which automatic payment can be used to reduce churn
- Explore extent to which we can further incentivize contracts
