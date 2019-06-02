"""
observer pattern in python
"""


class Subject:
    """
    # Represents what is being 'observed'
    """

    def __init__(self):
        self._observers = (
            []
        )  # This where references to all the observers are being kept
        # Note that this is a one-to-many relationship: there will be one subject to be observed by multiple _observers

    def attach(self, observer):
        """
        # If the observer is not already in the observers list
        # append the observer to the list
        :param observer:
        :return:
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """
        Simply remove the observer
        :param observer:
        :return:
        """
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        """
        notify
        For all the observers in the list
        Don't notify the observer who is actually updating the temperature
        :param modifier:
        :return:
        """
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)  # Alert the observers!


class Core(Subject):
    """
    # Inherits from the Subject class
    """

    def __init__(self, name=""):
        Subject.__init__(self)
        self.core_name = name  # Set the name of the core
        self.core_temp = 0  # Initialize the temperature of the core

    @property  # Getter that gets the core temperature
    def temp(self):
        """

        :return:
        """
        return self.core_temp

    @temp.setter  # Setter that sets the core temperature
    def temp(self, temp):
        self.core_temp = temp
        self.notify()  # Notify the observers whenever somebody changes the core temperature


class TempViewer:
    """
    TempViewer
    """

    @staticmethod
    def update(subject):
        """
        Alert method that is invoked when the notify() method in a concrete subject is invoked
        :param subject:
        :return:
        """

        print(
            "Temperature Viewer: {} has Temperature {}".format(
                subject.core_name, subject.core_temp
            )
        )


def main():
    """
    Let's create our subjects
    Let's create our observers
    Let's attach our observers to the first core
    Let's change the temperature of our first core

    :return:
    """

    core1 = Core("Core 1")
    core2 = Core("Core 2")

    viewer1 = TempViewer()
    viewer2 = TempViewer()

    core1.attach(viewer1)
    core1.attach(viewer2)

    core1.temp = 80
    core1.temp = 90
    core2.temp = 100


if __name__ == "__main__":
    main()
