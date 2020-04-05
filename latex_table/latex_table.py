'''
Simple tool to create latex tables to automatise the export of data to latex
reports.

Author : Lucas Gomes de Camargos Silveira
date : 05.04.2020
'''

#%%
import numpy as np

#%%

class LatexTable(object):
    '''
    The class incorporates the attributes and methods to create a latex tabular
    which can be imported in the main latex file, giving the possibility to
    automatically update the table values once the simulations values are
    changed.
    
    Attributes
    ----------
    file_name : str
                file name (with extension)
    M : numpy.ndarray[:, :], dtype = str
        2D array containing the table values
    H : numpy.ndarray[:], dtype = str
        1D array containing the top horizontal table description
    V : numpy.ndarray[:], dtype = str
        1D array containing the left vertical table description
    corner: str
            top left corner of the table
    alignment : str
                string containg the columns alignment. Includes the alignment
                of the V column.
                example: '{l|c|c|r}'

    Methods
    -------
    tabular
    '''
    
    def __init__(self):
        self.file_name = []
        self.M = []
        self.H = []
        self.V = []
        self.corner = []
        self.alignment = []
    
    def tabular(self, alignment=None):
        '''
        The method creates a latex tabular which can be imported in the main
        latex file, giving the possibility to automatically update the table
        values once the simulations values are changed.

        Parameters
        ----------
        alignment : str, optional, default = None
                    string containg the columns alignment. Includes the
                    alignment of the V column. If not specified, the alignment
                    is defined as centered for all columns.
                    example: 'l', 'r', '{l|c|c|r}'
        '''
        
        # Number of lines and columns respectively
        n_lin = self.M.shape[0]
        n_col = self.M.shape[1]
        
        # Create the self.alignment string
        if (alignment is None):
            self.alignment = '{'+(n_col)*'c|'+'c'+'}'
        elif (alignment == 'l'):
            self.alignment = '{'+(n_col)*'l|'+'l'+'}'
        elif (alignment == 'r'):
            self.alignment = '{'+(n_col)*'r|'+'r'+'}'
        else:
            self.alignment = alignment
        
        # Write the tabular file
        with open(self.file_name, 'wt') as f:
            print('\\begin{tabular}' + self.alignment, file=f)
            # Double lines initiating the table
            print('\\hline', file=f)
            print('\\hline', file=f)
            
            # Write the table header
            for i_c in range(n_col-1):
                print(self.H[i_c] + ' & ', end='', file=f)
            else:
                i_c += 1
                print(self.H[i_c] + ' \\\\ ', file=f)
            print('\\hline', file=f)
      
            # Write the rest of table
            for i_l in range(n_lin):
                print(self.V[i_l] + ' & ', end='', file=f)
                for i_c in range(n_col-1):
                    print(self.M[i_l, i_c] + ' & ', end='', file=f)
                else:
                    i_c += 1
                    print(self.M[i_l, i_c] + ' \\\\ ', file=f)
            
            # Double lines finishing the table
            print('\\hline', file=f)
            print('\\hline', file=f)
    
#%%

@np.vectorize
def num2str(num, fmt):
    '''
    Transforms the elements of a numerical numpy.ndarray into strings following
    the especified format fmt.

    Parameters
    ----------
    num : numpy.ndarray, dtype='float' or 'int'
          numerical array to be converted
    fmt : str
          format used to transform a numeric value into a string
          example: '%0.3e'

    Returns
    -------
    string : numpy.ndarray, dtype='str'
             converted array
    '''
    
    string = str(fmt %(num))
    return string