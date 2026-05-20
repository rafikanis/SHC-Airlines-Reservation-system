import calendar
###########
## database
###########
import sqlite3
from datetime import datetime, timedelta
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

class User:
    def __init__(self, name, national_id, username, phone_number=None, date_of_birth=None, nationalities=None, passport=None, gender=None, password=None):
        self.name = name
        self.national_id = national_id
        self.username = username
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.nationalities = nationalities
        self.passport = passport
        self.gender = gender
        self.password = password

    @staticmethod
    def add_user(name, national_id, username, phone_number=None, date_of_birth=None, nationalities=None, passport=None, gender=None, password=None):
        try:
            # Always create a new connection
            conn = sqlite3.connect('SHCdb.db')
            cursor = conn.cursor()
            
            cursor.execute(
                """
                INSERT INTO Users (name, national_id, username, phone_number, date_of_birth, nationalities, passport, gender, password)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (name, national_id, username, phone_number, date_of_birth, nationalities, passport, gender, password),
            )
            conn.commit()
            print(f"User {name} added successfully.")
            return True
        except sqlite3.Error as e:
            print(f"Error adding user: {e}")
            return False
        finally:
            # Ensure connection is always closed
            if conn:
                conn.close()

    # Rest of the methods remain the same...
    @staticmethod
    def validate_user(username, password):
        try:
            conn = sqlite3.connect('SHCdb.db')
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT * FROM Users
                WHERE username = ? AND password = ?
                """,
                (username, password),
            )
            user = cursor.fetchone()
            if user:
                print(f"Validation successful for user with Username: {username}")
                return True
            else:
                print("Invalid Username or password.")
                return False
        except sqlite3.Error as e:
            print(f"Error validating user: {e}")
            return False
        finally:
            conn.close()

    # Other methods remain the same...
    # Other methods remain the same...
    def get_user_data(username):
        try:
            conn = sqlite3.connect('SHCdb.db')
            cursor = conn.cursor() # ask about what is essential data
            cursor.execute(
                """
                SELECT username, name, national_id, phone_number, date_of_birth, nationalities, passport, gender
                FROM Users
                WHERE username = ?
                """,
                (username,)
            )
            user_data = cursor.fetchone()
            if user_data:
                if user_data:
                 return User(
                name=user_data[1],
                national_id=user_data[2],
                username=user_data[0],
                phone_number=user_data[3],
                date_of_birth=user_data[4],
                nationalities=user_data[5],
                passport=user_data[6],
                gender=user_data[7]) 
            else:
                print(f"User with username {username} not found.")
        except sqlite3.Error as e:
            print(f"Error fetching user data: {e}")
        finally:
            conn.close()
class Flight:
    def __init__(self, flight_id, departure_airport, arrival_airport, departure_time, arrival_time, price_economy, price_business, day_of_week):
        self.flight_id = flight_id
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price_economy = price_economy
        self.price_business = price_business
        self.day_of_week = day_of_week
    
def get_flights_by_date(departure_airport, arrival_airport, date):
    global dep_date
    dep_date = date

    def extract_3_letters_in_parentheses(input_string):
        start = input_string.find('(')
        end = input_string.find(')', start)
        return input_string[start + 1:end] if start != -1 and end != -1 and end - start - 1 == 3 else None

    def is_date_valid(date_str, date_format="%Y-%m-%d"):
        input_date = datetime.strptime(date_str, date_format)
        current_date = datetime.now()
        return input_date >= current_date

    def adjust_arrival_date(departure_time, arrival_time, departure_date):
        """
        Adjusts the arrival date if the flight arrives on the next day.
        """
        dep_time_obj = datetime.strptime(departure_time, "%H:%M")
        arr_time_obj = datetime.strptime(arrival_time, "%H:%M")
        dep_date_obj = datetime.strptime(departure_date, "%Y-%m-%d")

        if arr_time_obj < dep_time_obj:  # Arrival time is earlier than departure time, implying next day
            return (dep_date_obj + timedelta(days=1)).strftime("%Y-%m-%d")
        else:
            return departure_date

    try:
        conn = sqlite3.connect('SHCdb.db')
        cursor = conn.cursor()

        if not is_date_valid(date):
            return []

        dep_airport = extract_3_letters_in_parentheses(departure_airport)
        arr_airport = extract_3_letters_in_parentheses(arrival_airport)

        if not dep_airport or not arr_airport or dep_airport == arr_airport:
            return []

        flights = []
        base_date = datetime.strptime(date, "%Y-%m-%d")

        for day_offset in range(-3, 4):
            search_date = base_date + timedelta(days=day_offset)
            if search_date.date() < datetime.now().date():
                continue
            day_of_week = calendar.day_name[search_date.weekday()]

            # Fetch direct flights
            cursor.execute(
                """
                SELECT 
                    flight_id, ?, ?, departure_airport, NULL AS transit_airport, arrival_airport,
                    departure_time, arrival_time, NULL AS departure_time_2, NULL AS arrival_time_2, 
                    NULL AS departure_date_2, NULL AS arrival_date_2, 
                    price_economy, price_business
                FROM Flights
                WHERE departure_airport = ? AND arrival_airport = ? AND day_of_week = ?
                """,
                (search_date.strftime("%Y-%m-%d"), search_date.strftime("%Y-%m-%d"), dep_airport, arr_airport, day_of_week),
            )
            results = cursor.fetchall()
            for flight in results:
                # Adjust the arrival date for direct flights
                adjusted_arrival_date = adjust_arrival_date(flight[6], flight[7], flight[1])
                flights.append(flight[:2] + (adjusted_arrival_date,) + flight[3:])

            # Fetch connecting flights
            cursor.execute(
                """
                SELECT 
                    f1.flight_id || '-' || f2.flight_id AS combined_flight_id,
                    ?, ?, f1.departure_airport, f1.arrival_airport AS transit_airport, f2.arrival_airport,
                    f1.departure_time, f1.arrival_time,
                    f2.departure_time, f2.arrival_time,
                    ?, ?, 
                    f1.price_economy + f2.price_economy AS total_price_economy, 
                    f1.price_business + f2.price_business AS total_price_business
                FROM Flights f1
                JOIN Flights f2 ON f1.arrival_airport = f2.departure_airport
                WHERE f1.departure_airport = ? 
                  AND f2.arrival_airport = ?
                  AND f1.day_of_week = ?
                  AND (f1.arrival_time < f2.departure_time OR f1.arrival_time = f2.departure_time)
                  AND f1.arrival_time IS NOT NULL
                  AND f2.departure_time IS NOT NULL
                """,
                (
                    search_date.strftime("%Y-%m-%d"),
                    search_date.strftime("%Y-%m-%d"),
                    search_date.strftime("%Y-%m-%d"),  # Departure Date 2 (same as Arrival Date 1 logically)
                    search_date.strftime("%Y-%m-%d"),  # Arrival Date 2
                    dep_airport,
                    arr_airport,
                    day_of_week,
                ),
            )
            results = cursor.fetchall()
            for flight in results:
                # Adjust dates for connecting flights
                adjusted_arrival_date_1 = adjust_arrival_date(flight[6], flight[7], flight[1])
                adjusted_departure_date_2 = adjusted_arrival_date_1  # Second flight departs on the first flight's arrival date
                adjusted_arrival_date_2 = adjust_arrival_date(flight[8], flight[9], adjusted_departure_date_2)

                flights.append(
                    flight[:2]
                    + (adjusted_arrival_date_1,)
                    + flight[3:6]
                    + (flight[6], flight[7], flight[8], flight[9])
                    + (adjusted_departure_date_2, adjusted_arrival_date_2)
                    + flight[12:]
                )

        return flights
    except sqlite3.Error as e:
        print(f"Error fetching flights: {e}")
        return []
    finally:
        conn.close()

class Ticket:
    def __init__(self, ticket_id, username, flight_id, seat_class,date1,status="reserved"):
        self.ticket_id = ticket_id
        self.username = username
        self.flight_id = flight_id
        self.seat_class = seat_class
        self.status = status
        self.date1=dep_date
  

    @staticmethod
    def book_ticket(username, flight_id, seat_class):
        
        def show_error_message(self, message):
            """
            Displays an error pop-up with the specified message.
            """
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            msg_box.setText(message)
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()
        
        try:
            conn = sqlite3.connect('SHCdb.db')
            cursor = conn.cursor() # ask about what is essential data
            # Check availability
            seat_column = "available_economy_seats" if seat_class == "Economy" else "available_business_seats"
            cursor.execute(
                f"SELECT {seat_column} FROM Flights WHERE flight_id = ?",
                (flight_id,),
            )
            seats = cursor.fetchone()

            if seats and seats[0] > 0:
                current_date=datetime.now().date()
                current_time = datetime.now().time()  # Get the time part only
                current_time = current_time.strftime("%H:%M:%S")  # Format as 'HH:MM:SS'
                # Insert ticket
                cursor.execute(
                    """
                    INSERT INTO Tickets (username, flight_id, seat_class, status, departure_date, status_date, status_time)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (username, flight_id, seat_class, "reserved",dep_date, current_date, current_time),
                )

                # Update available seats
                cursor.execute(
                    f"UPDATE Flights SET {seat_column} = {seat_column} - 1 WHERE flight_id = ?",
                    (flight_id,),
                )

                conn.commit()
            else:
                print("Not Enough seats.")
        except sqlite3.Error as e:
            print(f"Error booking ticket: {e}")
        finally:
            conn.close()

    @staticmethod
    def cancel_ticket(ticket_id):
        # Function to validate if the date is today or in the future
        def is_date_valid(date_str, date_format="%Y-%m-%d"):
            input_date = datetime.strptime(date_str, date_format).date()
            current_date = datetime.now().date()
            return input_date >= current_date

        try:
            conn = sqlite3.connect('SHCdb.db')
            cursor = conn.cursor()

            # Get ticket details along with the flight departure date
            cursor.execute(
                """
                SELECT t.flight_id, t.seat_class, t.departure_date
                FROM Tickets t
                JOIN Flights f ON t.flight_id = f.flight_id
                WHERE t.ticket_id = ? AND t.status = 'reserved'
                """,
                (ticket_id,),
            )
            ticket = cursor.fetchone()

            if ticket:
                flight_id, seat_class, departure_date = ticket
                print(flight_id)
                
                current_date=datetime.now().date()
                current_time = datetime.now().time()  # Get the time part only
                current_time = current_time.strftime("%H:%M:%S")  # Format as 'HH:MM:SS'
                # Check if the departure date is valid
                if not is_date_valid(departure_date):
                    print("Cannot cancel a ticket for a flight that has already departed.")
                    return

                # Determine which seat column to update
                seat_column = "available_economy_seats" if seat_class == "Economy" else "available_business_seats"
                
                # Increment the available seat count
                cursor.execute(
                    f"UPDATE Flights SET {seat_column} = {seat_column} + 1 WHERE flight_id = ?",
                    (flight_id,),
                )
                conn.commit()
                cursor.execute(
                        """UPDATE Tickets
                        SET status = 'canceled',
                        status_date = ?,
                        status_time = ?
                        WHERE ticket_id = ?""",
                        (current_date, current_time, ticket_id)
                    )

                

                conn.commit()
                print("Ticket canceled successfully.")
            else:
                print("Ticket not found or already canceled.")

        except sqlite3.Error as e:
            print(f"Error canceling ticket: {e}")
        finally:
            if conn:
                conn.close()


    @staticmethod
    def user_history(username):
        try:
            conn = sqlite3.connect('SHCdb.db')
            cursor = conn.cursor() # ask about what is essential data
            cursor.execute(
                """
                SELECT t.ticket_id, f.flight_id, f.departure_airport, f.arrival_airport, t.seat_class, t.status, t.departure_date, t.status_date, t.status_time
                FROM Tickets t
                JOIN Flights f ON t.flight_id = f.flight_id
                WHERE t.username = ?
                ORDER BY t.status_date DESC, t.status_time DESC  -- Sort by date and time
                """,
                (username,),
            )
            history = cursor.fetchall()
            return history
            
        except sqlite3.Error as e:
            print(f"Error retrieving user history: {e}")
        finally:
            conn.close()
