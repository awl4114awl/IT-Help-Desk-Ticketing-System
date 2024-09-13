# IT Help Desk Ticketing System

This is a desktop-based IT Help Desk Ticketing System built using Python and PyQt5 for the frontend, and MongoDB for the backend database. The system allows users to create, view, and manage tickets. There are two modes: `Admin` and `User`, with Admin having additional privileges like deleting tickets.

## Features

- **Admin Mode**:
  - Requires a password to log in (default: `admin1`).
  - Admins can create, view, and delete tickets.
- **User Mode**:
  - Users can create and view tickets without needing a password.
- **Dark Mode**: The entire application, including the login prompt, operates in a dark mode theme for easier readability.
- **Ticket Management**: Create, view, and delete tickets with simple, user-friendly forms.
- **MongoDB Integration**: Tickets are stored and retrieved using MongoDB.

## Prerequisites

- **Python**: Make sure you have Python 3.x installed on your system.
- **MongoDB**: Set up a MongoDB Atlas account and configure your connection string.
- **PyQt5**: Install PyQt5 for the GUI framework.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/awl4114awl/IT-Help-Desk-Ticketing-System.git
    ```

2. Navigate to the project directory:
    ```bash
    cd IT-Help-Desk-Ticketing-System
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Update the MongoDB connection URI in `database.py` if necessary:
    ```python
    uri="your-mongodb-connection-uri"
    ```

## How to Run

1. Run the `main.py` file:
    ```bash
    python main.py
    ```

2. Upon startup, you'll be prompted to choose between **Admin** and **User** modes:
   - **Admin Mode**: Requires a password (`admin1` by default). Admins have the ability to delete tickets.
   - **User Mode**: Allows the creation and viewing of tickets without requiring a password.

3. Create and manage your tickets through the simple, easy-to-use interface.

## Screenshots

![Admin Mode Screenshot](path-to-screenshot-admin.png)
![User Mode Screenshot](path-to-screenshot-user.png)

## Project Structure

```
IT-Help-Desk-Ticketing-System/
│
├── main.py              # Main application file
├── database.py          # MongoDB operations
├── requirements.txt     # List of dependencies
├── README.md            # Project documentation
└── .gitignore           # Files to ignore in Git
```

## Requirements

- `PyQt5`
- `pymongo`
- `bson`

To install these dependencies, run:
```bash
pip install -r requirements.txt
```

## Future Enhancements

- **Search & Filter**: Add search and filtering capabilities for better ticket management.
- **User Roles**: Expand roles beyond Admin and User for more granular control.
- **Email Notifications**: Send email alerts for new tickets and updates.
- **Attachment Support**: Add the ability to upload and view file attachments for tickets.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
