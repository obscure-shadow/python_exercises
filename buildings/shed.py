from building import Building

class Shed(Building):
    """
    Author :

    Inherits from : Building

    Purpose:
    To represent any kind of shed for users to build in the UI

    """

    def __init__(self, windows):
        """ Initialization method for shed

        """
        super().__init__(self, windows) # this inherits the init from the previous building class
        self.windows = windows
        self.workbench = True
        self.tools = []