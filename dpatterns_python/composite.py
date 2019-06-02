"""
composite pattern in python
"""


class Component:
    """Abstract class"""

    # pylint: disable=unused-argument
    def __init__(self, *args, **kwargs):
        print("initializing")


class Child(Component):  # Inherits from the abstract class, Component
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # This is where we store the name of your child item!
        self.name = args[0]

    def component_function(self):
        """
        # Print the name of your child item here!
        :return:
        """

        print("{}".format(self.name))


class Composite(Component):  # Inherits from the abstract class, Component
    """Concrete class and maintains the tree recursive structure"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # This is where we store the name of the composite object
        self.name = args[0]

        # This is where we keep our child items
        self.children = []

    def append_child(self, child):
        """Method to add a new child item"""
        self.children.append(child)

    def remove_child(self, child):
        """Method to remove a child item"""
        self.children.remove(child)

    def component_function(self):
        """
        # Print the name of the composite object
        :return:
        """

        print("{}".format(self.name))

        # Iterate through the child objects and invoke their component function printing their names
        for i in self.children:
            i.component_function()


# Build a composite submenu 1
SUB1 = Composite("submenu1")

# Create a new child sub_submenu 11
SUB11 = Child("sub_submenu 11")
# Create a new Child sub_submenu 12
SUB12 = Child("sub_submenu 12")

# Add the sub_submenu 11 to submenu 1
SUB1.append_child(SUB11)
# Add the sub_submenu 12 to submenu 1
SUB1.append_child(SUB12)

# Build a top-level composite menu
TOP = Composite("top_menu")

# Build a submenu 2 that is not a composite
SUB2 = Child("submenu2")

# Add the composite submenu 1 to the top-level composite menu
TOP.append_child(SUB1)

# Add the plain submenu 2 to the top-level composite menu
TOP.append_child(SUB2)

# Let's test if our Composite pattern works!
TOP.component_function()
