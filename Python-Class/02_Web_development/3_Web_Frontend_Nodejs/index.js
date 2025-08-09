// Basic Express.js server setup
const express = require('express');
const path = require('path');

// Initialize express application
const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Parse JSON body
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Simple route for the home page
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// API route example
app.get('/api/hello', (req, res) => {
  res.json({ message: 'Hello from the API!' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
