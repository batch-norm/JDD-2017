import pandas as pd
import numpy as np
import pickle


# methods
def get_sales_amount_increase_rate(months):
    increase_rate_monthly = []
    if np.sum(months) == 50:
        # dataset1
        if np.sum(temp_df[temp_df.month == 8].sale_amt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 9].sale_amt) - np.sum(temp_df[temp_df.month == 8].sale_amt)) / np.sum(
                    temp_df[temp_df.month == 8].sale_amt))
        else: increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 9].sale_amt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 10].sale_amt) - np.sum(temp_df[temp_df.month == 9].sale_amt)) / np.sum(
                    temp_df[temp_df.month == 9].sale_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 10].sale_amt) != 0:
            increase_rate_monthly.append(
                float(
                np.sum(temp_df[temp_df.month == 11].sale_amt) - np.sum(temp_df[temp_df.month == 10].sale_amt)) / np.sum(
                    temp_df[temp_df.month == 10].sale_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 11].sale_amt) != 0:
            increase_rate_monthly.append(
                float(
                np.sum(temp_df[temp_df.month == 12].sale_amt) - np.sum(temp_df[temp_df.month == 11].sale_amt)) / np.sum(
                    temp_df[temp_df.month == 11].sale_amt))
        else:
            increase_rate_monthly.append(0)
        return increase_rate_monthly[0] * 0.1 + increase_rate_monthly[1] * 0.2 + increase_rate_monthly[2] * 0.3 + increase_rate_monthly[3] * 0.4
    if np.sum(months) == 43:
        # dataset2
        if np.sum(temp_df[temp_df.month == 9].sale_amt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 10].sale_amt) - np.sum(temp_df[temp_df.month == 9].sale_amt)) / np.sum(
                    temp_df[temp_df.month == 9].sale_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 10].sale_amt) != 0:
            increase_rate_monthly.append(
                float(
                np.sum(temp_df[temp_df.month == 11].sale_amt) - np.sum(temp_df[temp_df.month == 10].sale_amt)) / np.sum(
                    temp_df[temp_df.month == 10].sale_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 11].sale_amt) != 0:
            increase_rate_monthly.append(
                float(
                np.sum(temp_df[temp_df.month == 12].sale_amt) - np.sum(temp_df[temp_df.month == 11].sale_amt)) / np.sum(
                    temp_df[temp_df.month == 11].sale_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 12].sale_amt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 1].sale_amt) - np.sum(temp_df[temp_df.month == 12].sale_amt)) / np.sum(
                    temp_df[temp_df.month == 12].sale_amt))
        else:
            increase_rate_monthly.append(0)
        return increase_rate_monthly[0] * 0.1 + increase_rate_monthly[1] * 0.2 + increase_rate_monthly[2] * 0.3 + increase_rate_monthly[3] * 0.4
    if np.sum(months) == 22:
        # dataset3
        if np.sum(temp_df[temp_df.month == 12].sale_amt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 1].sale_amt) - np.sum(temp_df[temp_df.month == 12].sale_amt)) / np.sum(
                    temp_df[temp_df.month == 12].sale_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 1].sale_amt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 2].sale_amt) - np.sum(temp_df[temp_df.month == 1].sale_amt)) / np.sum(
                    temp_df[temp_df.month == 1].sale_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 2].sale_amt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 3].sale_amt) - np.sum(temp_df[temp_df.month == 2].sale_amt)) / np.sum(
                    temp_df[temp_df.month == 2].sale_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 3].sale_amt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 4].sale_amt) - np.sum(temp_df[temp_df.month == 3].sale_amt)) / np.sum(
                    temp_df[temp_df.month == 3].sale_amt))
        else:
            increase_rate_monthly.append(0)
        return increase_rate_monthly[0] * 0.1 + increase_rate_monthly[1] * 0.2 + increase_rate_monthly[2] * 0.3 + increase_rate_monthly[3] * 0.4
    else:
        return -999

def get_order_amount_increase_rate(months):
    increase_rate_monthly = []
    if np.sum(months) == 50:
        # dataset1
        if np.sum(temp_df[temp_df.month == 8].ord_cnt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 9].ord_cnt) - np.sum(
                    temp_df[temp_df.month == 8].ord_cnt)) / np.sum(
                    temp_df[temp_df.month == 8].ord_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 9].ord_cnt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 10].ord_cnt) - np.sum(
                    temp_df[temp_df.month == 9].ord_cnt)) / np.sum(
                    temp_df[temp_df.month == 9].ord_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 10].ord_cnt) != 0:
            increase_rate_monthly.append(
                float(
                    np.sum(temp_df[temp_df.month == 11].ord_cnt) - np.sum(
                        temp_df[temp_df.month == 10].ord_cnt)) / np.sum(
                    temp_df[temp_df.month == 10].ord_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 11].ord_cnt) != 0:
            increase_rate_monthly.append(
                float(
                    np.sum(temp_df[temp_df.month == 12].ord_cnt) - np.sum(
                        temp_df[temp_df.month == 11].ord_cnt)) / np.sum(
                    temp_df[temp_df.month == 11].ord_cnt))
        else:
            increase_rate_monthly.append(0)
        return increase_rate_monthly[0] * 0.1 + increase_rate_monthly[1] * 0.2 + increase_rate_monthly[2] * 0.3 + \
               increase_rate_monthly[3] * 0.4
    if np.sum(months) == 43:
        # dataset2
        if np.sum(temp_df[temp_df.month == 9].ord_cnt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 10].ord_cnt) - np.sum(
                    temp_df[temp_df.month == 9].ord_cnt)) / np.sum(
                    temp_df[temp_df.month == 9].ord_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 10].ord_cnt) != 0:
            increase_rate_monthly.append(
                float(
                    np.sum(temp_df[temp_df.month == 11].ord_cnt) - np.sum(
                        temp_df[temp_df.month == 10].ord_cnt)) / np.sum(
                    temp_df[temp_df.month == 10].ord_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 11].ord_cnt) != 0:
            increase_rate_monthly.append(
                float(
                    np.sum(temp_df[temp_df.month == 12].ord_cnt) - np.sum(
                        temp_df[temp_df.month == 11].ord_cnt)) / np.sum(
                    temp_df[temp_df.month == 11].ord_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 12].ord_cnt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 1].ord_cnt) - np.sum(
                    temp_df[temp_df.month == 12].ord_cnt)) / np.sum(
                    temp_df[temp_df.month == 12].ord_cnt))
        else:
            increase_rate_monthly.append(0)
        return increase_rate_monthly[0] * 0.1 + increase_rate_monthly[1] * 0.2 + increase_rate_monthly[2] * 0.3 + \
               increase_rate_monthly[3] * 0.4
    if np.sum(months) == 22:
        # dataset3
        if np.sum(temp_df[temp_df.month == 12].ord_cnt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 1].ord_cnt) - np.sum(
                    temp_df[temp_df.month == 12].ord_cnt)) / np.sum(
                    temp_df[temp_df.month == 12].ord_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 1].ord_cnt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 2].ord_cnt) - np.sum(
                    temp_df[temp_df.month == 1].ord_cnt)) / np.sum(
                    temp_df[temp_df.month == 1].ord_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 2].ord_cnt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 3].ord_cnt) - np.sum(
                    temp_df[temp_df.month == 2].ord_cnt)) / np.sum(
                    temp_df[temp_df.month == 2].ord_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 3].ord_cnt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 4].ord_cnt) - np.sum(
                    temp_df[temp_df.month == 3].ord_cnt)) / np.sum(
                    temp_df[temp_df.month == 3].ord_cnt))
        else:
            increase_rate_monthly.append(0)
        return increase_rate_monthly[0] * 0.1 + increase_rate_monthly[1] * 0.2 + increase_rate_monthly[2] * 0.3 + \
               increase_rate_monthly[3] * 0.4
    else:
        return -999
def get_back_order_increase_rate(months):
    increase_rate_monthly = []
    if np.sum(months) == 50:
        # dataset1
        if np.sum(temp_df[temp_df.month == 8].rtn_amt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 9].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 8].rtn_amt)) / np.sum(
                    temp_df[temp_df.month == 8].rtn_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 9].rtn_amt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 10].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 9].rtn_amt)) / np.sum(
                    temp_df[temp_df.month == 9].rtn_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 10].rtn_amt) != 0:
            increase_rate_monthly.append(
                float(
                    np.sum(temp_df[temp_df.month == 11].rtn_amt) - np.sum(
                        temp_df[temp_df.month == 10].rtn_amt)) / np.sum(
                    temp_df[temp_df.month == 10].rtn_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 11].rtn_amt) != 0:
            increase_rate_monthly.append(
                float(
                    np.sum(temp_df[temp_df.month == 12].rtn_amt) - np.sum(
                        temp_df[temp_df.month == 11].rtn_amt)) / np.sum(
                    temp_df[temp_df.month == 11].rtn_amt))
        else:
            increase_rate_monthly.append(0)
        return increase_rate_monthly[0] * 0.1 + increase_rate_monthly[1] * 0.2 + increase_rate_monthly[2] * 0.3 + \
               increase_rate_monthly[3] * 0.4
    if np.sum(months) == 43:
        # dataset2
        if np.sum(temp_df[temp_df.month == 9].rtn_amt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 10].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 9].rtn_amt)) / np.sum(
                    temp_df[temp_df.month == 9].rtn_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 10].rtn_amt) != 0:
            increase_rate_monthly.append(
                float(
                    np.sum(temp_df[temp_df.month == 11].rtn_amt) - np.sum(
                        temp_df[temp_df.month == 10].rtn_amt)) / np.sum(
                    temp_df[temp_df.month == 10].rtn_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 11].rtn_amt) != 0:
            increase_rate_monthly.append(
                float(
                    np.sum(temp_df[temp_df.month == 12].rtn_amt) - np.sum(
                        temp_df[temp_df.month == 11].rtn_amt)) / np.sum(
                    temp_df[temp_df.month == 11].rtn_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 12].rtn_amt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 1].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 12].rtn_amt)) / np.sum(
                    temp_df[temp_df.month == 12].rtn_amt))
        else:
            increase_rate_monthly.append(0)
        return increase_rate_monthly[0] * 0.1 + increase_rate_monthly[1] * 0.2 + increase_rate_monthly[2] * 0.3 + \
               increase_rate_monthly[3] * 0.4
    if np.sum(months) == 22:
        # dataset3
        if np.sum(temp_df[temp_df.month == 12].rtn_amt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 1].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 12].rtn_amt)) / np.sum(
                    temp_df[temp_df.month == 12].rtn_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 1].rtn_amt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 2].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 1].rtn_amt)) / np.sum(
                    temp_df[temp_df.month == 1].rtn_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 2].rtn_amt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 3].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 2].rtn_amt)) / np.sum(
                    temp_df[temp_df.month == 2].rtn_amt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 3].rtn_amt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 4].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 3].rtn_amt)) / np.sum(
                    temp_df[temp_df.month == 3].rtn_amt))
        else:
            increase_rate_monthly.append(0)
        return increase_rate_monthly[0] * 0.1 + increase_rate_monthly[1] * 0.2 + increase_rate_monthly[2] * 0.3 + \
               increase_rate_monthly[3] * 0.4
    else:
        return -999
def get_back_amount_increase_rate(months):
    increase_rate_monthly = []
    if np.sum(months) == 50:
        # dataset1
        if np.sum(temp_df[temp_df.month == 8].rtn_cnt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 9].rtn_cnt) - np.sum(
                    temp_df[temp_df.month == 8].rtn_cnt)) / np.sum(
                    temp_df[temp_df.month == 8].rtn_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 9].rtn_cnt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 10].rtn_cnt) - np.sum(
                    temp_df[temp_df.month == 9].rtn_cnt)) / np.sum(
                    temp_df[temp_df.month == 9].rtn_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 10].rtn_cnt) != 0:
            increase_rate_monthly.append(
                float(
                    np.sum(temp_df[temp_df.month == 11].rtn_cnt) - np.sum(
                        temp_df[temp_df.month == 10].rtn_cnt)) / np.sum(
                    temp_df[temp_df.month == 10].rtn_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 11].rtn_cnt) != 0:
            increase_rate_monthly.append(
                float(
                    np.sum(temp_df[temp_df.month == 12].rtn_cnt) - np.sum(
                        temp_df[temp_df.month == 11].rtn_cnt)) / np.sum(
                    temp_df[temp_df.month == 11].rtn_cnt))
        else:
            increase_rate_monthly.append(0)
        return increase_rate_monthly[0] * 0.1 + increase_rate_monthly[1] * 0.2 + increase_rate_monthly[2] * 0.3 + \
               increase_rate_monthly[3] * 0.4
    if np.sum(months) == 43:
        # dataset2
        if np.sum(temp_df[temp_df.month == 9].rtn_cnt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 10].rtn_cnt) - np.sum(
                    temp_df[temp_df.month == 9].rtn_cnt)) / np.sum(
                    temp_df[temp_df.month == 9].rtn_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 10].rtn_cnt) != 0:
            increase_rate_monthly.append(
                float(
                    np.sum(temp_df[temp_df.month == 11].rtn_cnt) - np.sum(
                        temp_df[temp_df.month == 10].rtn_cnt)) / np.sum(
                    temp_df[temp_df.month == 10].rtn_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 11].rtn_cnt) != 0:
            increase_rate_monthly.append(
                float(
                    np.sum(temp_df[temp_df.month == 12].rtn_cnt) - np.sum(
                        temp_df[temp_df.month == 11].rtn_cnt)) / np.sum(
                    temp_df[temp_df.month == 11].rtn_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 12].rtn_cnt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 1].rtn_cnt) - np.sum(
                    temp_df[temp_df.month == 12].rtn_cnt)) / np.sum(
                    temp_df[temp_df.month == 12].rtn_cnt))
        else:
            increase_rate_monthly.append(0)
        return increase_rate_monthly[0] * 0.1 + increase_rate_monthly[1] * 0.2 + increase_rate_monthly[2] * 0.3 + \
               increase_rate_monthly[3] * 0.4
    if np.sum(months) == 22:
        # dataset3
        if np.sum(temp_df[temp_df.month == 12].rtn_cnt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 1].rtn_cnt) - np.sum(
                    temp_df[temp_df.month == 12].rtn_cnt)) / np.sum(
                    temp_df[temp_df.month == 12].rtn_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 1].rtn_cnt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 2].rtn_cnt) - np.sum(
                    temp_df[temp_df.month == 1].rtn_cnt)) / np.sum(
                    temp_df[temp_df.month == 1].rtn_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 2].rtn_cnt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 3].rtn_cnt) - np.sum(
                    temp_df[temp_df.month == 2].rtn_cnt)) / np.sum(
                    temp_df[temp_df.month == 2].rtn_cnt))
        else:
            increase_rate_monthly.append(0)
        if np.sum(temp_df[temp_df.month == 3].rtn_cnt) != 0:
            increase_rate_monthly.append(
                float(np.sum(temp_df[temp_df.month == 4].rtn_cnt) - np.sum(
                    temp_df[temp_df.month == 3].rtn_cnt)) / np.sum(
                    temp_df[temp_df.month == 3].rtn_cnt))
        else:
            increase_rate_monthly.append(0)
        return increase_rate_monthly[0] * 0.1 + increase_rate_monthly[1] * 0.2 + increase_rate_monthly[2] * 0.3 + \
               increase_rate_monthly[3] * 0.4
    else:
        return -999
def get_real_sales_amount_increase_rate(months):
    if np.sum(months) == 50:
        # dataset1
        return np.average(
            (np.sum(temp_df[temp_df.month == 9].sale_amt - temp_df[temp_df.month == 9].rtn_amt) - np.sum(
                temp_df[temp_df.month == 8].sale_amt - temp_df[temp_df.month == 8].rtn_amt)) / np.sum(
                temp_df[temp_df.month == 8].sale_amt - temp_df[temp_df.month == 8].rtn_amt) + (
                np.sum(temp_df[temp_df.month == 10].sale_amt - temp_df[temp_df.month == 10].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 9].sale_amt - temp_df[temp_df.month == 9].rtn_amt)) / np.sum(
                temp_df[temp_df.month == 9].sale_amt - temp_df[temp_df.month == 9].rtn_amt) + (
                np.sum(temp_df[temp_df.month == 11].sale_amt - temp_df[temp_df.month == 11].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 10].sale_amt - temp_df[temp_df.month == 10].rtn_amt)) / np.sum(
                temp_df[temp_df.month == 10].sale_amt - temp_df[temp_df.month == 10].rtn_amt) + (
                np.sum(temp_df[temp_df.month == 12].sale_amt - temp_df[temp_df.month == 12].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 11].sale_amt - temp_df[temp_df.month == 11].rtn_amt)) / np.sum(
                temp_df[temp_df.month == 11].sale_amt - temp_df[temp_df.month == 11].rtn_amt))
    if np.sum(months) == 43:
        # dataset2
        return np.average(
            (np.sum(temp_df[temp_df.month == 10].sale_amt - temp_df[temp_df.month == 10].rtn_amt) - np.sum(
                temp_df[temp_df.month == 9].sale_amt - temp_df[temp_df.month == 9].rtn_amt)) / np.sum(
                temp_df[temp_df.month == 9].sale_amt - temp_df[temp_df.month == 9].rtn_amt) + (
                np.sum(temp_df[temp_df.month == 11].sale_amt - temp_df[temp_df.month == 11].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 10].sale_amt - temp_df[temp_df.month == 10].rtn_amt)) / np.sum(
                temp_df[temp_df.month == 10].sale_amt - temp_df[temp_df.month == 10].rtn_amt) + (
                np.sum(temp_df[temp_df.month == 12].sale_amt - temp_df[temp_df.month == 12].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 11].sale_amt - temp_df[temp_df.month == 11].rtn_amt)) / np.sum(
                temp_df[temp_df.month == 11].sale_amt - temp_df[temp_df.month == 11].rtn_amt) + (
                np.sum(temp_df[temp_df.month == 1].sale_amt - temp_df[temp_df.month == 1].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 12].sale_amt - temp_df[temp_df.month == 12].rtn_amt)) / np.sum(
                temp_df[temp_df.month == 12].sale_amt - temp_df[temp_df.month == 12].rtn_amt))
    if np.sum(months) == 22:
        # dataset3
        return np.average(
            (np.sum(temp_df[temp_df.month == 1].sale_amt - temp_df[temp_df.month == 1].rtn_amt) - np.sum(
                temp_df[temp_df.month == 12].sale_amt - temp_df[temp_df.month == 12].rtn_amt)) / np.sum(
                temp_df[temp_df.month == 12].sale_amt - temp_df[temp_df.month == 12].rtn_amt) + (
                np.sum(temp_df[temp_df.month == 2].sale_amt - temp_df[temp_df.month == 2].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 1].sale_amt - temp_df[temp_df.month == 1].rtn_amt)) / np.sum(
                temp_df[temp_df.month == 1].sale_amt - temp_df[temp_df.month == 1].rtn_amt) + (
                np.sum(temp_df[temp_df.month == 3].sale_amt - temp_df[temp_df.month == 3].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 2].sale_amt - temp_df[temp_df.month == 2].rtn_amt)) / np.sum(
                temp_df[temp_df.month == 2].sale_amt - temp_df[temp_df.month == 2].rtn_amt) + (
                np.sum(temp_df[temp_df.month == 4].sale_amt - temp_df[temp_df.month == 4].rtn_amt) - np.sum(
                    temp_df[temp_df.month == 3].sale_amt - temp_df[temp_df.month == 3].rtn_amt)) / np.sum(
                temp_df[temp_df.month == 3].sale_amt - temp_df[temp_df.month == 3].rtn_amt))
    else:
        return -999


with open('../../Data/order_month.pkl', 'rb') as f:
    All_train = pickle.load(f)
with open('../../Data/ads_month.pkl', 'rb') as f:
    All_train_ads = pickle.load(f)
with open('../../Data/comment_month.pkl', 'rb') as f:
    All_train_comment = pickle.load(f)
i = 1
for dataset in All_train:
    train = pd.DataFrame({
        'shop_id': np.unique(dataset.shop_id).astype(int)
    })
    # variables
    Times = 0
    months = np.unique(dataset.month).astype(int).tolist()
    # list for feature #
    # merchant features
    total_merchant_onSale = []
    average_every_merchant_order_amount = []
    average_every_merchant_back_order_amount = []
    average_every_merchant_real_order_amount = []
    # order features
    total_sales_amount = []
    total_offer_amount = []
    total_offer_amount_of_total_sales_amount = []
    total_order_amount = []
    total_back_order_amount = []
    total_real_order_amount = []
    average_every_order_sales = []
    average_every_order_offer = []
    total_back_amount = []
    total_back_amount_of_total_sales_amount = []
    total_real_sales_amount = []
    average_every_order_real_sales_amount = []
    total_customers_amount = []
    average_every_customer_order_amount = []
    average_every_customer_buy_amount = []
    average_every_customer_back_order_amount = []
    average_every_customer_back_amount = []
    total_offer_count = []
    total_offer_amount_of_total_back_amount = []
    average_every_order_offer_amount_of_back_amount = []
    average_every_order_offer_amount = []
    average_sales_amount_increase_rate = []
    average_real_sales_amount_increase_rate = []
    average_order_amount_increase_rate = []
    average_back_order_increase_rate = []
    average_back_amount_increase_rate = []

    # comment
    total_good_comment = []
    total_normal_comment = []
    total_bad_comment = []
    total_comment_amount = []
    good_comment_rate = []
    bad_comment_rate = []
    # ads
    total_charge_amount = []
    total_charge_using_amount = []
    total_using_of_charge_rate = []
    # others
    shop_cat = []
    for shop in train.shop_id:
        print('Calculating %d.....' % shop)
        # get feature from temp_df of every shop
        temp_df = dataset[dataset.shop_id == shop]
        temp_df_ads = All_train_ads[i-1][All_train_ads[i-1].shop_id == shop]
        temp_df_comment = All_train_comment[i - 1][All_train_comment[i - 1].shop_id == shop]
        # merchant features
        total_merchant_onSale.append(len(np.unique(temp_df.pid)))
        average_every_merchant_order_amount.append(float(np.sum(temp_df.ord_cnt)) / len(np.unique(temp_df.pid)))
        average_every_merchant_back_order_amount.append(float(np.sum(temp_df.rtn_cnt)) / len(np.unique(temp_df.pid)))
        average_every_merchant_real_order_amount.append(
            float(np.sum(temp_df.ord_cnt) - np.sum(temp_df.rtn_cnt)) / len(np.unique(temp_df.pid)))
        # order features
        total_sales_amount.append(np.sum(temp_df.sale_amt))
        total_offer_amount.append(np.sum(temp_df.offer_amt))
        total_offer_amount_of_total_sales_amount.append(float(np.sum(temp_df.offer_amt)) / np.sum(temp_df.sale_amt))
        total_order_amount.append(np.sum(temp_df.ord_cnt))
        total_back_order_amount.append(np.sum(temp_df.rtn_cnt))
        total_real_order_amount.append(np.sum(temp_df.ord_cnt) - np.sum(temp_df.rtn_cnt))
        average_every_order_sales.append(float(np.sum(temp_df.sale_amt)) / np.sum(temp_df.ord_cnt))
        average_every_order_offer.append(float(np.sum(temp_df.offer_amt)) / np.sum(temp_df.ord_cnt))
        total_back_amount.append(np.sum(temp_df.rtn_amt))
        total_back_amount_of_total_sales_amount.append(float(np.sum(temp_df.rtn_amt)) / np.sum(temp_df.sale_amt))
        total_real_sales_amount.append(np.sum(temp_df.sale_amt) - np.sum(temp_df.rtn_amt))
        average_every_order_real_sales_amount.append(
            float(np.sum(temp_df.sale_amt) - np.sum(temp_df.rtn_amt)) / np.sum(temp_df.ord_cnt))
        total_customers_amount.append(np.sum(temp_df.user_cnt))
        average_every_customer_order_amount.append(float(np.sum(temp_df.ord_cnt)) / np.sum(temp_df.user_cnt))
        average_every_customer_buy_amount.append(float(np.sum(temp_df.sale_amt)) / np.sum(temp_df.user_cnt))
        average_every_customer_back_order_amount.append(float(np.sum(temp_df.rtn_cnt)) / np.sum(temp_df.user_cnt))
        average_every_customer_back_amount.append(float(np.sum(temp_df.rtn_amt)) / np.sum(temp_df.user_cnt))
        total_offer_count.append(np.sum(temp_df.offer_cnt))
        if np.sum(temp_df.rtn_amt)==0:total_offer_amount_of_total_back_amount.append(0)
        else:total_offer_amount_of_total_back_amount.append(float(np.sum(temp_df.offer_amt)) / np.sum(temp_df.rtn_amt))
        if np.sum(temp_df.ord_cnt)==0 or np.sum(temp_df.rtn_amt)==0:
            average_every_order_offer_amount_of_back_amount.append(0)
        else:average_every_order_offer_amount_of_back_amount.append(
            float(float(np.sum(temp_df.offer_amt)) / np.sum(temp_df.rtn_amt)) / np.sum(temp_df.ord_cnt))
        average_every_order_offer_amount.append(float(np.sum(temp_df.offer_amt)) / np.sum(temp_df.ord_cnt))
        average_sales_amount_increase_rate.append(get_sales_amount_increase_rate(months))
        average_order_amount_increase_rate.append(get_order_amount_increase_rate(months))
        average_back_order_increase_rate.append(get_back_order_increase_rate(months))
        average_back_amount_increase_rate.append(get_back_amount_increase_rate(months))
        # comment features
        total_good_comment.append(np.sum(temp_df_comment.good_num))
        total_bad_comment.append(np.sum(temp_df_comment.bad_num))
        total_normal_comment.append(np.sum(temp_df_comment.mid_num))
        total_comment_amount.append(np.sum(temp_df_comment.cmmt_num))
        good_comment_rate.append(np.sum(temp_df_comment.good_num)/np.sum(temp_df_comment.cmmt_num))
        bad_comment_rate.append(np.sum(temp_df_comment.bad_num)/np.sum(temp_df_comment.cmmt_num))
        # ads features
        total_charge_amount.append(np.sum(temp_df_ads.charge))
        total_charge_using_amount.append(np.sum(temp_df_ads.consume))
        if np.sum(temp_df_ads.charge)==0:
            total_using_of_charge_rate.append(0)
        else:
            total_using_of_charge_rate.append(np.sum(temp_df_ads.consume)/np.sum(temp_df_ads.charge))
        # others
        if len(temp_df['brand'].mode()) == 1:
            shop_cat.append(int(temp_df['brand'].mode()))
        else:
            shop_cat.append(0)

        # average_real_sales_amount_increase_rate.append(get_real_sales_amount_increase_rate(months))
    # add features
    # merchant features
    train['total_merchant_onSale'] = total_merchant_onSale
    train['average_every_merchant_order_amount'] = average_every_merchant_order_amount
    train['average_every_merchant_back_order_amount'] = average_every_merchant_back_order_amount
    train['average_every_merchant_real_order_amount'] = average_every_merchant_real_order_amount
    # order features
    train['total_sales_amount'] = total_sales_amount
    train['total_offer_amount'] = total_offer_amount
    train['total_offer_amount_of_total_sales_amount'] = total_offer_amount_of_total_sales_amount
    train['total_order_amount'] = total_order_amount
    train['total_back_order_amount'] = total_back_order_amount
    train['total_real_order_amount'] = total_real_order_amount
    train['average_every_order_sales'] = average_every_order_sales
    train['average_every_order_offer'] = average_every_order_offer
    train['total_back_amount'] = total_back_amount
    train['total_back_amount_of_total_sales_amount'] = total_back_amount_of_total_sales_amount
    train['total_real_sales_amount'] = total_real_sales_amount
    train['average_every_order_real_sales_amount'] = average_every_order_real_sales_amount
    train['total_customers_amount'] = total_customers_amount
    train['average_every_customer_order_amount'] = average_every_customer_order_amount
    train['average_every_customer_buy_amount'] = average_every_customer_buy_amount
    train['average_every_customer_back_order_amount'] = average_every_customer_back_order_amount
    train['average_every_customer_back_amount'] = average_every_customer_back_amount
    train['total_offer_count'] = total_offer_count
    train['total_offer_amount_of_total_back_amount'] = total_offer_amount_of_total_back_amount
    train['average_every_order_offer_amount_of_back_amount'] = average_every_order_offer_amount_of_back_amount
    train['average_every_order_offer_amount'] = average_every_order_offer_amount
    train['average_sales_amount_increase_rate'] = average_sales_amount_increase_rate
    train['average_order_amount_increase_rate'] = average_order_amount_increase_rate
    train['average_back_order_increase_rate'] = average_back_order_increase_rate
    train['average_back_amount_increase_rate'] = average_back_amount_increase_rate
    train['total_good_comment'] = total_good_comment
    train['total_bad_comment'] = total_bad_comment
    train['total_normal_comment'] = total_normal_comment
    train['total_comment_amount'] = total_comment_amount
    train['good_comment_rate'] = good_comment_rate
    train['bad_comment_rate'] = bad_comment_rate
    train['total_charge_amount'] = total_charge_amount
    train['total_charge_using_amount'] = total_charge_using_amount
    train['total_using_of_charge_rate'] = total_using_of_charge_rate
    train['shop_cat'] = shop_cat

    # train['average_real_sales_amount_increase_rate'] = average_real_sales_amount_increase_rate
    # save (some data is 'inf')
    train.to_csv('../../Data/valid_dataset%d.csv' % i, index=False)
    i += 1
