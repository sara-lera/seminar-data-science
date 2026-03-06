"""
Example statistical test for a research repository.

This script simulates two experimental groups and performs
an independent Student's t-test to evaluate whether their
means are statistically different.

Author: Your Name

"""

import numpy as np
from scipy import stats


def generate_data(seed=42):
    """
    Generate two synthetic datasets representing two groups.
    """
    np.random.seed(seed)

    # Simulated measurements
    group_a = np.random.normal(loc=50, scale=10, size=30)
    group_b = np.random.normal(loc=55, scale=10, size=30)

    return group_a, group_b


def run_t_test(group_a, group_b):
    """
    Perform an independent t-test between two groups.
    """
    t_stat, p_value = stats.ttest_ind(group_a, group_b)

    return t_stat, p_value


def main():
    group_a, group_b = generate_data()

    t_stat, p_value = run_t_test(group_a, group_b)

    print("Statistical comparison between Group A and Group B")
    print("-----------------------------------------------")
    print(f"T-statistic: {t_stat:.3f}")
    print(f"P-value: {p_value:.5f}")

    alpha = 0.05
    if p_value < alpha:
        print("Result: Significant difference (reject H0)")
    else:
        print("Result: No significant difference (fail to reject H0)")


if __name__ == "__main__":
    main()