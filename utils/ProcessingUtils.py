class ProcessingUtils:
    @staticmethod
    def col_names_updator(
        column_names_list: list,
        window_size: int,
        operation_type: str,
    ):
        updated_names = [
            "_".join([single_field, operation_type, str(window_size)])
            for single_field in column_names_list
        ]
        return updated_names
