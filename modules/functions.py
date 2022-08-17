from builtins import staticmethod

class GeneralFunctions():
    @staticmethod
    def print_error(error_message, optional_variable=""):
        print("\n\n**********************************************")
        print("***   ", error_message, optional_variable)
        print("**********************************************\n\n")
        
