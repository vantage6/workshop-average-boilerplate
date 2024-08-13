"""
This file contains all partial algorithm functions, that are normally executed
on all nodes for which the algorithm is executed.

The results in a return statement are sent to the vantage6 server (after
encryption if that is enabled). From there, they are sent to the partial task
or directly to the user (if they requested partial results).
"""

import pandas as pd
from typing import Any

from vantage6.algorithm.tools.util import info, warn, error
from vantage6.algorithm.tools.decorators import data


@data(1)
def partial_function(df: pd.DataFrame, column, group_by) -> Any:
    """Decentral part of the algorithm"""

    grouped = df.groupby(group_by)
    return {
        "sum": grouped[column].sum().to_dict(),
        "count": grouped[column].size().to_dict(),
    }

    # numbers = df[column]

    # # compute the sum, and count number of rows
    # info("Computing partials")
    # local_sum = float(numbers.sum())
    # local_count = len(numbers)

    # # return the values as a dict
    # return {"sum": local_sum, "count": local_count}
