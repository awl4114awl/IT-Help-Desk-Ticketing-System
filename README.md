# IT Help Desk Ticketing System

A responsive and modern IT Help Desk Ticketing System built with Node.js, Express, EJS, and MongoDB. This web application allows users to submit, track, and manage IT support tickets efficiently. The interface is designed with Bootstrap for a sleek, user-friendly experience, featuring a collapsible menu for easy navigation and a live world clock in Pacific Standard Time (PST). The admin panel includes functionality for viewing, updating, and deleting tickets, as well as adding comments. The application is fully responsive and optimized for both desktop and mobile use.

## Features

- **User-Friendly Interface**: Simple and intuitive design using Bootstrap and custom CSS.
- **Ticket Management**: Users can submit tickets with details like department, priority, and description.
- **Admin Panel**: Admins can view, edit, and delete tickets, and add comments.
- **Real-Time Clock**: A running clock displaying the current time in PST.
- **Mobile Optimized**: Fully responsive design for use on any device.

## Technologies Used

- **Node.js**: Server-side JavaScript runtime.
- **Express**: Fast, unopinionated, minimalist web framework for Node.js.
- **EJS**: Embedded JavaScript templating.
- **MongoDB**: NoSQL database for storing tickets.
- **Bootstrap**: Front-end component library for styling.
- **Mongoose**: MongoDB object modeling for Node.js.

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/YOUR-USERNAME/IT-Help-Desk-Ticketing-System.git
    cd IT-Help-Desk-Ticketing-System
    ```

2. **Install Dependencies**:
    ```bash
    npm install
    ```

3. **Set Up Environment Variables**:
    - Create a `.env` file in the root directory.
    - Add your MongoDB connection string:
    ```env
    MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
    ```

4. **Run the Application**:
    ```bash
    npm start
    ```
    The application will run on `http://localhost:3000`.

5. **Access the Application**:
    - Visit `http://localhost:3000` in your browser.

## Deployment

To deploy this application on a platform like Heroku, follow these steps:

1. Create a new application on the deployment platform.
2. Set up environment variables as required by the platform.
3. Push the code to the platform's Git repository.
4. Start the application on the platform.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.