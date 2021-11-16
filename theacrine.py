from utils.win_ide import Theacrine
from utils.win_error import TheacrineError


"""
Main Script to start Theacrine App
@Version: 1.2
"""


def main():
    """
    Main function
    @param :
    @return:
    """
    try:
        # Calls the Theacrine constructor
        theacrine = Theacrine

        raise Exception('Erro crítico')
        # Create Theacrine main panel
        theacrine.modal_theacrine()

    except Exception as e:
        theacrine = TheacrineError
        theacrine.modal_theacrine_error()

    return


if __name__ == '__main__':
    import sys
    sys.exit(main())
