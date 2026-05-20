import os
import sys
# Add 'ui' directory to system path so that compiled UI files can import res_rc
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'ui')))

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from ui.login import Ui_MainWindow as LoginWindow
from ui.signup import Ui_MainWindow as SignupWindow
from ui.ApplicationWindow import Ui_MainWindow as MainAppWindow
from code_1 import User, Flight, Ticket , get_flights_by_date  # Updated reference
from datetime import datetime
from PySide6 import QtWidgets
import calendar
import sqlite3
# Database initialization
#from SHCdbms import insert_more_flights_for_airports
baklaweez = ""

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = LoginWindow()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.LoginButton.clicked.connect(self.login)
        self.ui.SignUpButton.clicked.connect(self.open_signup)
    
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
    
    def login(self):
        username = self.ui.UsernameEntry.text()
        password = self.ui.PasswordEntry.text()
        global baklaweez
        #Validate user
        check = User.validate_user(username, password)
        if check:
            baklaweez = username
            self.open_main_app()
        else:
            self.show_error_message("Wrong username or password.")

    def open_signup(self):
        self.signup_window = Signup()
        self.signup_window.show()
        self.close()

    def open_main_app(self):
        self.main_app = MainApp()
        self.main_app.show()
        self.close()

class Signup(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = SignupWindow()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.LoginNow.clicked.connect(self.open_login)
        self.ui.CreateAccount.clicked.connect(self.register_user)

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

    def open_login(self):
        self.login_window = Login()
        self.login_window.show()
        self.close()

    def register_user(self):
        name = self.ui.FullName.text()
        national_id = self.ui.NationalID.text()
        username = self.ui.Username.text()
        phone_number = self.ui.PhoneNumber.text()
        date_of_birth = self.ui.BirthDate.text()
        nationalities = self.ui.Nationality.currentText()  # Updated for ComboBox
        passport = self.ui.PassportNumber.text()
        gender = self.ui.Gender.currentText()  # Updated for ComboBox
        password = self.ui.Password.text()

        if not all([name, national_id, username, date_of_birth, nationalities, passport, gender, password]):
            self.show_error_message("Complete specific data.")
            return

    # Create a User object
        try:
            new_user = User.add_user(name, national_id, username, phone_number, date_of_birth, nationalities, passport, gender, password)
            self.open_login()
        except ValueError as e:
            self.show_error_message(f"Error: {e}")

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainAppWindow()
        self.ui.setupUi(self)
        user = User.get_user_data(baklaweez)
        self.ui.HelloMessage.setText(f"Hello, {user.name}")

        # Connect buttons to features
        self.ui.BookingPage.clicked.connect(self.book_flight)
        self.ui.SearchButton.clicked.connect(self.check_inputs)
        self.ui.CancelTicket.clicked.connect(self.cancel_selected)
        self.ui.ReserveSelected.clicked.connect(self.reserve_selected)
        self.ui.History.clicked.connect(self.show_history)
        self.ui.Profile.clicked.connect(self.show_profile)
        self.ui.LogOut.clicked.connect(self.logout)        
    
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

    def reserve_selected(self):
        selected_items = self.ui.Resulttree.selectedItems()

        if selected_items:  # Check if an item is selected
            selected_item = selected_items[0]  # Get the selected item
            flight_id = selected_item.text(0)  # Access the first column value
            Ticket.book_ticket(baklaweez,flight_id,self.ui.ClassSelect.currentText())
            self.show_history()
        else:
            self.show_error_message("No flights selected.")

    def cancel_selected(self):
        
        def is_date_valid(date_str, date_format="%Y-%m-%d"):
            input_date = datetime.strptime(date_str, date_format)
            current_date = datetime.now()
            return input_date >= current_date

        selected_items = self.ui.Historytree.selectedItems()
        

        selected_item = selected_items[0]
        selected_item = selected_item.text(5)
        if selected_item == "canceled":
            self.show_error_message("Can't cancel a ticket that already been canceled.")
        selected_item = selected_items[0]
        selected_item = selected_item.text(6)
        if not is_date_valid(selected_item):
            self.show_error_message("Can't cancel a flight ticket that already been departured.")

        if selected_items:  # Check if an item is selected
            selected_item = selected_items[0]  # Get the selected item
            ticket_id = selected_item.text(0)  # Access the first column value (Ticket ID)
        
            if ticket_id.isdigit():  # Validate that the ticket ID is a number
                Ticket.cancel_ticket(int(ticket_id))  # Pass the ticket ID to cancel_ticket
                print(f"Ticket {ticket_id} cancellation attempted.")
                self.show_history()  # Refresh the history view
            else:
                print("Invalid ticket ID selected.")
        else:
            print("No item selected.")

    def book_flight(self):
        
        self.ui.DisplayStack.setCurrentIndex(0)
        print("Booking a flight...")

    def check_inputs(self):
        dep = self.ui.DepartureAirport.currentText()
        arr = self.ui.ArrivalAirport.currentText()
        seat_class = self.ui.ClassSelect.currentText()
        selected_date = self.ui.DepartureDate.date().toString("yyyy-MM-dd")
        
        def is_date_valid(date_str, date_format="%Y-%m-%d"):
            input_date = datetime.strptime(date_str, date_format)
            current_date = datetime.now()
            return input_date >= current_date
        
        # Validate input fields
        if not dep or not arr or not selected_date or not seat_class:
            self.show_error_message("Enter data correctly.")
            return

        if dep == arr:
            self.show_error_message("Can't travel from an airport to the same airport.")
            return
        
        if not is_date_valid(selected_date):
            self.show_error_message("Invalid date.")
            return
        
        self.search_results()

    def search_results(self):
    # Switch to the search results page
        self.ui.DisplayStack.setCurrentIndex(1)
    
    # Get departure and arrival airports
        dep = self.ui.DepartureAirport.currentText()
        arr = self.ui.ArrivalAirport.currentText()
        
    # Get the selected date and convert it to a string in the format YYYY-MM-DD
        selected_date = self.ui.DepartureDate.date().toString("yyyy-MM-dd")
        

    # Fetch flights and update UI
        flights = get_flights_by_date(dep, arr, selected_date)
    
    # Clear the tree widget before populating
        self.ui.Resulttree.clear()
    # Set the column count and headers
        self.ui.Resulttree.setColumnCount(14)  # Adjust the number of columns based on flight details
        self.ui.Resulttree.setHeaderLabels([
            "Flight ID","Departure Date 1","Arrival Date 1","Departure Date 2","Arrival Date 2","Departure Airport","Transit Airport", "Arrival Airport", "Departure Time 1", 
            "Arrival Time 1","Departure Time 2","Arrival Time 2", "Economy Price", "Business Price"
            ])
        if flights:
        # Populate the tree widget with flight data
            for flight in flights:
            # Create a tree widget item for each flight
                flight_item = QtWidgets.QTreeWidgetItem([
                str(flight[0]),  # Flight ID
                flight[1],       # Departure Date 1
                flight[2],       # Arrival Date 1
                flight[10] or "", # Departure Date 2 (empty if direct flight)
                flight[11] or "", # Arrival Date 2 (empty if direct flight)
                flight[3],       # Departure Airport
                flight[4] or "", # Transit Airport (empty if direct flight)
                flight[5],       # Arrival Airport
                flight[6],       # Departure Time 1
                flight[7],       # Arrival Time 1
                flight[8] or "", # Departure Time 2 (empty if direct flight)
                flight[9] or "", # Arrival Time 2 (empty if direct flight)
                f"${flight[12]:.2f}",  # Economy Price
                f"${flight[13]:.2f}"   # Business Price
            ])
                self.ui.Resulttree.addTopLevelItem(flight_item)
        else:
        # Display a message if no flights are found
            no_flights_item = QtWidgets.QTreeWidgetItem(["No flights available for the selected date."])
            self.ui.Resulttree.addTopLevelItem(no_flights_item)

    

    
    def show_history(self):
        self.ui.DisplayStack.setCurrentIndex(2)
        print("Showing ticket history...")
        history = Ticket.user_history(baklaweez)
    # Clear the tree widget before populating
        self.ui.Historytree.clear()
    
        # Set the column count and headers
        self.ui.Historytree.setColumnCount(8) # Adjust the number of columns based on flight details
        self.ui.Historytree.setHeaderLabels([
            "Ticket ID","Flight ID","Departure Airport", "Arrival Airport", "Seat Class", 
            "Ticket Status", "Departure Date", "Status Date","Status Time"
            ])
        
        if history:
            for ticket in history:
 #SELECT t.ticket_id, f.flight_id, f.departure_airport, f.arrival_airport, t.seat_class, t.status, t.booking_date
            # Create a tree widget item for each flight
                ticket_item = QtWidgets.QTreeWidgetItem([
                str(ticket[0]),
                str(ticket[1]),  # Flight ID
                ticket[2],       # Departure Airport
                ticket[3],       # Arrival Airport
                ticket[4],       # Departure Time
                ticket[5],       # Arrival Time
                ticket[6],       # Arrival Airport
                ticket[7],       # Arrival Airport
                ticket[8],       # Arrival Airport
            ])
                self.ui.Historytree.addTopLevelItem(ticket_item)
        else:
        # Display a message if no flights are found
            no_tickets_item = QtWidgets.QTreeWidgetItem(["No flights available for the selected date."])
            self.ui.Historytree.addTopLevelItem(no_tickets_item)
        

    def show_profile(self):
        self.ui.DisplayStack.setCurrentIndex(3)

        print("Displaying profile information...")
        global baklaweez
        user = User.get_user_data(baklaweez)
        self.ui.FullName.setText(user.name)
        self.ui.Username.setText(user.username)
        self.ui.NationalID.setText(user.national_id)
        self.ui.PhoneNumber.setText(user.phone_number)
        self.ui.PassportNumber.setText(user.passport)
        self.ui.BirthDate.setText(user.date_of_birth)
        self.ui.Gender.setText(user.gender)
        self.ui.MainNationality.setText(user.nationalities)


    def logout(self):
        self.login_window = Login()
        self.login_window.show()
        self.close()

if __name__ == "__main__":
    # Ensure database is initialized
    #try:
       # con = sqlite3.connect('SHCdb.db')
      #  insert_more_flights_for_airports(con)
   # except sqlite3.Error as e:
     #   print(f"Database initialization error: {e}")

    # Run the application
    import sys
    app = QApplication(sys.argv)
    login_window = Login()
    login_window.show()
    sys.exit(app.exec())
