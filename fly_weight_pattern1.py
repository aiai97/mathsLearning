# class MovieTicket:
#     def __init__(self, movie_name, show_time, theater_location, seat_number):
#         self.movie_name = movie_name
#         self.show_time = show_time
#         self.theater_location = theater_location
#         self.seat_number = seat_number
#
#     def show_details(self):
#         print(f"Movie: {self.movie_name}")
#         print(f"Show Time: {self.show_time}")
#         print(f"Theater Location: {self.theater_location}")
#         print(f"Seat Number: {self.seat_number}")
#         print("")
#
# # 创建多个电影票对象
# ticket1 = MovieTicket("Avengers: Endgame", "19:00", "Cinema A", "A1")
# ticket2 = MovieTicket("Avengers: Endgame", "19:00", "Cinema A", "A2")
# ticket3 = MovieTicket("Spider-Man: Homecoming", "20:30", "Cinema B", "B1")
# ticket4 = MovieTicket("Avengers: Endgame", "19:00", "Cinema A", "A1")
#
# # 打印电影票对象的内存地址
# print(f"Ticket 1: {id(ticket1)}")
# print(f"Ticket 2: {id(ticket2)}")
# print(f"Ticket 3: {id(ticket3)}")
# print(f"Ticket 4: {id(ticket4)}")
from abc import ABC, abstractmethod

class MovieTicket(ABC):
    @abstractmethod
    def show_details(self, seat_number):
        pass

class MovieTicketFlyweight(MovieTicket):
    def __init__(self, movie_name, show_time, theater_location):
        self.movie_name = movie_name
        self.show_time = show_time
        self.theater_location = theater_location

    def show_details(self, seat_number):
        print(f"Movie: {self.movie_name}")
        print(f"Show Time: {self.show_time}")
        print(f"Theater Location: {self.theater_location}")
        print(f"Seat Number: {seat_number}")
        print("")

class MovieTicketFactory:
    def __init__(self):
        self.movie_tickets = {}

    def get_movie_ticket(self, movie_name, show_time, theater_location):
        if (movie_name, show_time, theater_location) not in self.movie_tickets:
            self.movie_tickets[(movie_name, show_time, theater_location)] = MovieTicketFlyweight(movie_name, show_time, theater_location)
        return self.movie_tickets[(movie_name, show_time, theater_location)]

# 客户端代码
ticket_factory = MovieTicketFactory()

ticket1 = ticket_factory.get_movie_ticket("Avengers: Endgame", "19:00", "Cinema A")
ticket1.show_details("A1")

ticket2 = ticket_factory.get_movie_ticket("Avengers: Endgame", "19:00", "Cinema A")
ticket2.show_details("A2")

ticket3 = ticket_factory.get_movie_ticket("Spider-Man: Homecoming", "20:30", "Cinema B")
ticket3.show_details("B1")

ticket4 = ticket_factory.get_movie_ticket("Spider-Man: Homecoming", "20:30", "Cinema B")
ticket4.show_details("B1")
# Ticket 1: 1941050997536
# Ticket 2: 1941050997536
# Ticket 3: 1941050997440
# Ticket 4: 1941050997440
# # 打印电影票对象的内存地址
print(f"Ticket 1: {id(ticket1)}")
print(f"Ticket 2: {id(ticket2)}")
print(f"Ticket 3: {id(ticket3)}")
print(f"Ticket 4: {id(ticket4)}")
