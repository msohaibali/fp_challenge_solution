import sys
import warnings
import pandas as pd
from utils.ProcessingUtils import ProcessingUtils

if not sys.warnoptions:
    warnings.simplefilter("ignore")


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
        """
        Get the Main DataFrame and Generate the Sub-DataFrame with
        required operation applied
        :param incoming_df: main dataframe for applying the operation
        :param rolling_window_size: size of Rolling Window
        :param operation_type: type of operation to perform
        """

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
