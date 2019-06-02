"""
proxy pattern in python
"""

import time


class Producer:
    """Define the 'resource-intensive' object to instantiate!"""

    @staticmethod
    def produce():
        """
        Producer is working hard
        :return:
        """
        print("Producer is working hard!")

    @staticmethod
    def meet():
        """
        meet the producer
        :return:
        """
        print("Producer has time to meet you now!")


class Proxy:
    """"Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""

    def __init__(self):
        self.occupied = "No"
        self.producer = None

    def produce(self):
        """Check if Producer is available"""
        print("Artist checking if Producer is available ...")

        if self.occupied == "No":
            # If the producer is available, create a producer object!
            self.producer = Producer()
            time.sleep(2)

            # Make the producer meet the guest!
            self.producer.meet()

        else:
            # Otherwise, don't instantiate a producer
            time.sleep(2)
            print("Producer is busy!")


def main():
    """
    Instantiate a Proxy
    Make the proxy: Artist produce until Producer is available
    Change the state to 'occupied'
    Make the Producer produce
    :return:
    """

    proxy1 = Proxy()
    proxy1.produce()
    proxy1.occupied = "Yes"
    proxy1.produce()


if __name__ == "__main__":
    main()
