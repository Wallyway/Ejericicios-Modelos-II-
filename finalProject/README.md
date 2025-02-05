### Folders and Files

- **static/**: Contains all static assets like CSS, JavaScript, and images.
  - **styles.css**: Defines the styles for the HTML elements, including layout, colors, and typography.
  - **search.js**: Handles the client-side logic for searching and interacting with the server.
  - **index.html**: The main HTML template for the project. It includes the structure of the web page and references to CSS and JavaScript files.

- **server.pl**: The main server-side script written in Prolog. It handles incoming HTTP requests, processes them, and returns the appropriate responses.
  - Sets up the web server and routes.
  - Handles form submissions and interacts with the database.

- **database.pl**: Manages database values.
  - Contains a list of category 'Food' and 'Cleaning'

## Core Functionality

- **styles.css**: 
  - Provides styling for the results container and table.
  - Ensures the table is visually appealing with padding, borders, and background colors.
  - Includes responsive design elements to enhance readability on different screen sizes.

- **index.html**:
  - Defines the structure of the main web page.
  - Includes form elements for user input.
  - References `styles.css` for styling and `search.js` for client-side logic.

- **server.pl**:
  - Sets up the web server using Prolog.
  - Defines routes for handling different HTTP requests.
  - Processes form submissions and interacts with `database.pl` to fetch data.

- **database.pl**:
  - Storage the products and his characteristics
  - Retrieves and updates data as requested by `server.pl`.

- **search.js**:
  - Handles client-side logic for searching.
  - Sends AJAX requests to `server.pl` to fetch search results.
  - Updates the web page dynamically with the search results.

## Project Structure

<div align="center">

    finalProject/ │ 
        ├── static/ 
        │ ├── styles.css 
        │ └── search.js 
        │ └── index.html 
        ├── server.pl 
        └── database.pl
</div>