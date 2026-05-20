# SHC Airlines Reservation System ✈️

A comprehensive desktop application for airline flight reservations, built with **Python**, **PySide6** (Qt), and **SQLite**. 

This system provides a full graphical user interface (GUI) for users to register, log in, search for flights, book tickets, and manage their reservations. It handles complex flight routing, including direct and connecting flights, and automatically manages seat availability.

## 🌟 Key Features

* **User Authentication & Management:**
    * Secure login and registration system.
    * Collects and displays detailed user profiles (National ID, Passport Number, Nationality, Date of Birth).
* **Advanced Flight Search:**
    * Search for flights between 20+ international airports.
    * Automatically searches a 7-day window (±3 days from the selected date).
    * Handles both **Direct Flights** and **Connecting Flights** automatically.
    * Dynamic date adjustment for flights crossing midnight.
* **Ticket Booking System:**
    * Choose between Economy and Business Class.
    * Real-time seat availability tracking (prevents overbooking).
    * Calculates combined pricing for connecting flights.
* **Reservation Management:**
    * View complete booking history.
    * Cancel active tickets (with validation to prevent canceling past flights).
    * Automatically refunds seats to the database upon cancellation.
* **Modern GUI:**
    * Built with PySide6 featuring a clean, responsive layout using QStackedWidget for seamless page transitions.

## 🛠️ Technology Stack

* **Language:** Python 3.x
* **GUI Framework:** PySide6 (Qt for Python)
* **Database:** SQLite (`sqlite3`)

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/SHC-Airlines-Reservation-System.git](https://github.com/yourusername/SHC-Airlines-Reservation-System.git)
   cd SHC-Airlines-Reservation-System
