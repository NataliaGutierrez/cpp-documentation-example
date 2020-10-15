"""Docstrings documenting module.

It may extend multiple lines and any reStructuredText formatting is supported.
Use lines of 80 characters.
"""

def count_dogs(animallist):
    """Summary line: count the number of dogs in a list.
    
    Functiond description in detail.

    Args:
        animallist (list(str)): The input list to find dogs.
        arg2 (int): Description of `arg2`.

    Returns:
        The number of dogs.
    """
    # Code of implementation code

class dog:
    """Summary line: This class is a dog.

    Class of animal. 

    Attributes:
        name (str): Dog name.
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.
    """
    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        """Initialization method.

        Args:
            name (str): Dog name.
            param1 (list(str)): Description of `param1`.
        """

        self.name = name    # instance variable unique to each instance

    def _sleep():
        """Put dog into sleep.

        Example of private method. This method will be included in documentation
        because the configuration says so, as the special members like __init__
        """

    def make_ugly():
        """ Summary line: dog becomes ugly

        Full method description as regular functions. This function makes dog 
        to be ugly.

        Note:
            Example of note.

        """
        print('woof woof')

