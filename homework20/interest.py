
from abc import ABC, abstractmethod


class Interest(ABC):

    @abstractmethod
    def calculate_interest(self):
        pass

    @abstractmethod
    def calculate_future_value(self):
        pass


class SimpleInterest(Interest):

    def __init__(self, principal, interest_rate, time):
        self.principal = principal
        self.interest_rate = interest_rate
        self.time = time

    def calculate_interest(self):
        interest = self.principal * self.interest_rate * self.time
        return interest

    def calculate_future_value(self):
        future_value = self.principal * (1 + self.interest_rate * self.time)
        return future_value


class CompoundInterest(Interest):

    def __init__(self, principal, interest_rate, number_of_times, time):
        self.principal = principal
        self.interest_rate = interest_rate
        self.number_of_time = number_of_times
        self.time = time

    def calculate_interest(self):
        interest = self.principal * (self.interest_rate / self.number_of_time) ** (self.time * self.number_of_time)
        return interest

    def calculate_future_value(self):
        future_value = self.principal * (1 + (self.interest_rate / self.number_of_time) ** (self.time *
                                                                                            self.number_of_time))
        return future_value

