PRECISION = 0.01

def test_simple_compound():
    # given
    loan = 10_000
    interest = 0.04
    years = 5

    # when
    monthly = calculate_monthly_payment(loan, interest, years)

    # then
    expected_result = 184.1652
    assert(abs(monthly - expected_result) < PRECISION)
