class horse:
    """This class is a horse

    Class of animal. 

    :param name: horse name
    """
    kind = 'equidae'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

    def make_wild():
        """ horse becomes wild

        This function makes horse to be wild

        
        """
        print('wild')

