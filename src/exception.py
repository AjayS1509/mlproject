import sys
import logging

def error_message_detail(error, error_detail):  
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get file name

    error_msg = "Error occurred in Python script [{0}] at line [{1}]: {2}".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )

    return error_msg


class CustomException(Exception):
    def __init__(self, error_msg, error_detail):  # fixed typo
        super().__init__(error_msg)
        self.error_msg = error_message_detail(error_msg, error_detail=error_detail)

    def __str__(self):
        return self.error_msg

# if __name__ == '__main__':
#     try:
#         a = 1 / 0
        
#     except Exception as e:
#         logging.info("Exception occurred, raising CustomException...")
#         raise CustomException(e, sys)
    