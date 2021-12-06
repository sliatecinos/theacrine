# -*- coding: utf-8 -*-
import utils
import sys
import traceback


def main():
    """
    Main function
    @param :
    @return:
    """

    # instances Theacrine app
    theacrine = utils.Theacrine()
    try:
        # Create Theacrine main panel
        theacrine.modal_theacrine()
        # Error test
        # raise TypeError('Erro crítico')

    except Exception as err:
        _, _, tb = sys.exc_info()
        tb = traceback.extract_tb(tb)
        msg_error = str(tb)
        
        theacrine.modal_theacrine_error(msg_error)

    pass


if __name__ == '__main__':
    import sys
    sys.exit(main())
