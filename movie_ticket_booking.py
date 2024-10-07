import random
import textwrap

class Movie:
    def __init__(self, movie_id, title, genre, duration, seats):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.duration = duration
        self.seats = seats

class Booking:
    def __init__(self, movie, seats_requested, customer_name):
        self.booking_id = random.randint(1000, 9999)
        self.movie = movie
        self.seats_requested = seats_requested
        self.customer_name = customer_name

    def format_ticket(self):
        # Ticket formatting
        ticket = f"""
        ========================================
                      MOVIE TICKET
        ========================================
        Booking ID  : {self.booking_id}
        Customer    : {self.customer_name}
        Movie       : {self.movie.title}
        Genre       : {self.movie.genre}
        Duration    : {self.movie.duration} minutes
        Seats Booked: {self.seats_requested}
        ========================================
        """
        return textwrap.indent(ticket, ' ' * 4)  # Indenting the ticket for margin

    def save_ticket_to_file(self):
        file_name = f"Ticket_{self.booking_id}.txt"
        with open(file_name, 'w') as file:
            ticket_content = self.format_ticket()
            file.write(ticket_content)
        print(f"\nTicket successfully saved to {file_name}.\n")


class MovieTicketBooking:
    def __init__(self):
        self.movies = [
            Movie(1, "Inception", "Sci-Fi", 148, 5),
            Movie(2, "Interstellar", "Sci-Fi", 169, 3),
            Movie(3, "The Matrix", "Action", 136, 2)
        ]
        self.bookings = []

    def display_movies(self):
        print("\nAvailable Movies:")
        for movie in self.movies:
            print(f"{movie.movie_id}. {movie.title} ({movie.genre}, {movie.duration} mins) - {movie.seats} seats available")

    def book_ticket(self):
        self.display_movies()
        try:
            movie_id = int(input("\nEnter the movie ID to book tickets: "))
            movie = next((m for m in self.movies if m.movie_id == movie_id), None)

            if not movie:
                print("\nInvalid movie selection.")
                return

            seats_requested = int(input(f"Enter number of seats to book (Available: {movie.seats}): "))

            if seats_requested <= movie.seats:
                customer_name = input("Enter customer name: ")
                booking = Booking(movie, seats_requested, customer_name)
                movie.seats -= seats_requested
                self.bookings.append(booking)
                print(f"\n{seats_requested} ticket(s) successfully booked for {movie.title}!")
                booking.save_ticket_to_file()  # Save the ticket to a file after booking
            else:
                print("\nSorry, not enough seats available.")
        except ValueError:
            print("\nInvalid input. Please try again.")

    def display_bookings(self):
        if not self.bookings:
            print("\nNo bookings made yet.")
        else:
            print("\nBookings:")
            for booking in self.bookings:
                print(f"Booking ID: {booking.booking_id}, Movie: {booking.movie.title}, Customer: {booking.customer_name}, Seats: {booking.seats_requested}")

    def run(self):
        while True:
            print("\n1. View Movies")
            print("2. Book Tickets")
            print("3. View Bookings")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.display_movies()
            elif choice == '2':
                self.book_ticket()
            elif choice == '3':
                self.display_bookings()
            elif choice == '4':
                print("Thank you for using the Movie Ticket Booking System!")
                break
            else:
                print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    booking_system = MovieTicketBooking()
    booking_system.run()
