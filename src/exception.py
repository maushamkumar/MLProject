import sys 
from logger import logging

def error_message_detail(error, error_detail:sys):
    # The return type of sys it provides you
     
    _, _,exc_tb = error_detail.exc_info()
    # This will give you three important information first two 
    # information I am not at all interested but the last information 
    # Basically give me about exc_tb
    # This exc_tb probably give you all the information like on which 
    # file the exception has occured on which line number the exception 
    # has occur all those information will be probably given.
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occured in python script name [{0}] line number [{1}], error message[{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
    
    

# if __name__ == '__main__':
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info('Divide by Zero')
#         raise CustomException(e, sys)
        
        
    