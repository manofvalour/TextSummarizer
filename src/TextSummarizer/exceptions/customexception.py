import os, sys

class TextSummarizerException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)

        _,_,exc_tb = error_details.exc_info()
        file_name= exc_tb.tb_frame.f_code.co_filename
        line_no = exc_tb.tb_lineno

        self.error_message_info = f"Error exists in the {file_name} at line {line_no} with {error_message} error"

    def __str__(self):
        return self.error_message_info
    