"""CSC104 — Week 9: from a narrative to a coordinated loan program.

Run with Python 3. This file includes its own helpers and needs no other files.
Prepared reference implementation; prompt examples are not Copilot transcripts.

1. SPECIFY — THE ASK
Create a function that calculates a monthly loan payment given a loan amount
in dollars, an annual interest rate as a percentage, and a term in whole years.
Convert the years into monthly periods and the annual percentage into a monthly
decimal rate using two support functions. Return the monthly payment. A caller
will request the input values and display the payment in dollars and cents.

STRUCTURED ENGLISH / PARSING
Nouns (data): loan amount, annual percentage, years, periods, monthly rate,
             monthly payment.
Verbs (actions): request, convert, calculate, return, display.
Helpers: convert years and convert rate.
Coordinating function: call the helpers, calculate payment, return payment.
Calling code: request input, cast strings to numbers, call, display.

Mathematical model: payment = P * r / (1 - (1 + r) ** (-n))
P = loan amount; r = monthly decimal rate; n = number of monthly payments.
Assume a fixed positive nominal annual rate, monthly compounding, month-end
payments, no fees, a positive loan amount, and positive whole years.
These assumptions are not validated. A zero rate needs a separate rule later.

2. DOCUMENT AND PROMPT
Write each header and docstring first. Then ask Copilot to implement that
contract. Read and explain its suggestion before accepting it.

3. VERIFY
Predict, run, compare, explain, and repair. See sample runs below.

4. SUBMIT
For the assigned homework, submit the Python file and a screenshot of its
results, following the instructor's GitHub/LMS directions.
"""


# MONDAY: Each helper performs one small, reusable task.
def payment_periods(years):
    """Return monthly periods for positive whole years: years times 12.

    Return a number without printing or requesting input.
    """
    return years * 12


def monthly_interest_rate(annual_rate_percent):
    """Return monthly decimal rate from a positive annual percentage.

    Use 6 for 6 percent. Divide by 100, then by 12.
    Return a number without rounding, printing, or requesting input.
    """
    return annual_rate_percent / 100 / 12


# WEDNESDAY: Coordinate helpers to solve the larger problem.
def monthly_loan_payment(loan_amount, annual_rate_percent, years):
    """Return the monthly loan payment in dollars.

    Inputs: positive loan amount, positive annual percentage (6 means 6%),
    and positive whole years. Use payment_periods and monthly_interest_rate.
    Assume a fixed rate, monthly compounding, month-end payments, and no fees.
    Use P * r / (1 - (1 + r) ** (-n)). Return the unrounded payment.
    Do not request input or print. Inputs are not validated.
    """
    # Example Copilot prompt after writing this header and docstring:
    # Implement monthly_loan_payment using the two existing helpers.
    # Store their results as n and r, then apply the documented formula.
    # Use only calls, assignment, arithmetic, and return. Do not add loops,
    # validation, rounding, input, or print. Explain the order of the calls.

    n = payment_periods(years)  # Pause here; helper returns; resume here.
    r = monthly_interest_rate(annual_rate_percent)
    payment = loan_amount * r / (1 - (1 + r) ** (-n))
    # ** means exponentiation; parentheses preserve the formula's grouping.
    return payment


# CALLING CODE: Function definitions above do not execute their bodies yet.
# input returns text. float converts decimal input; int converts whole years.
# Enter 5 for years, not 5.0. The helpers perform unit conversion, not casting.
print("MONTHLY LOAN PAYMENT — Week 9")
print("Use positive values; enter 6 for 6% and whole years such as 5.")
loan_amount = float(input("Loan amount in dollars: "))
annual_rate_percent = float(input("Annual interest rate (%): "))
years = int(input("Loan term in whole years: "))

# Arguments supply the function's parameters. The returned number is saved.
payment = monthly_loan_payment(loan_amount, annual_rate_percent, years)
# Format only the displayed result; the calculation retains its precision.
print(f"Monthly payment: ${payment:.2f}")

# VERIFY by running this program separately for each case:
# Loan amount | Annual % | Years | Expected display
# 12000       | 6        | 5     | $231.99
# 24000       | 6        | 5     | $463.99
# 10000       | 12       | 1     | $888.49
# Trace the first case: years=5 -> n=60; annual_rate_percent=6 -> r=0.005.
# Doubling the principal with the same rate and term doubles the unrounded
# payment. Explain why displayed cents may not appear to double exactly.

# WEEKEND TRANSFER: Reuse these helpers for monthly savings contributions.
# Write a new narrative, header, docstring, prompt, implementation, and tests
# for monthly_savings_payment(savings_goal, annual_rate_percent, years).
# Assume zero starting savings and month-end deposits with monthly compounding.
# The savings implementation belongs to the weekend assignment.
