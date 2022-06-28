class ProcessingUtils:
    @staticmethod
    def col_names_updator(
        column_names_list: list,
        window_size: int,
        operation_type: str,
    ):
        """
        Return a list of updated column names having the operation type
        and rolling window size of each operation
        """
        updated_names = [
            "_".join([single_field, operation_type, str(window_size)])
            for single_field in column_names_list
        ]
        return updated_names
