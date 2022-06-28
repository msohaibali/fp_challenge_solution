import sys
import warnings
import pandas as pd
from utils.ProcessingUtils import ProcessingUtils

if not sys.warnoptions:
    warnings.simplefilter("ignore")


# operations_dict = {
#     "Average": [200, 300],
#     "Standard_deviation": [100, 300],
#     "Exponential_average": [500, 700],
# }


class FeaturesReader:
    def __init__(self, target_path: str) -> pd.DataFrame:
        """
        Get the Target Path (Local File or URL) and load that in DataFrame
        :param target_path: Path of the csv file
        """
        self.data = pd.read_csv(target_path)


class MultiFeaturesGenerator:
    def __init__(self) -> None:
        self.df = pd.DataFrame()

    def RollingOperations(
        self,
        incoming_df: pd.DataFrame,
        rolling_window_size: int,
        operation_type: str,
    ):
        if operation_type == "Average":
            sub_df = incoming_df.rolling(rolling_window_size).mean()

        elif operation_type == "Standard_deviation":
            sub_df = incoming_df.rolling(rolling_window_size).std()

        elif operation_type == "Exponential_average":
            sub_df = incoming_df.ewm(span=rolling_window_size).mean()

        updated_col_names = ProcessingUtils.col_names_updator(
            column_names_list=sub_df.columns.to_list(),
            window_size=rolling_window_size,
            operation_type=operation_type,
        )

        sub_df.columns = updated_col_names
        self.df = pd.concat([self.df, sub_df], axis=1)
