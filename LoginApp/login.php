<?php
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

// Tell the browser this response is JSON format
// JSON is just text structured as key-value pairs
// Example: {"status": "success", "message": "Welcome!"}
header('Content-Type: application/json');

// Allow requests from any origin
// This is needed because your HTML page and PHP script
// are technically on the same server, but this keeps things clean
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

// Only run this code if the request method is POST
// POST means data is being sent to this script (like a form submission)
// GET means someone is just visiting the URL directly
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode([
        'status'  => 'error',
        'message' => 'Invalid request method.'
    ]);
    exit;
}

// Read the raw JSON body sent from the browser
// When JavaScript uses fetch() to send data, it sends JSON
// php://input is how PHP reads that raw incoming data
$body = file_get_contents('php://input');

// Convert the JSON string into a PHP object we can work with
$data = json_decode($body);

// Check that the data was decoded successfully
// and that both username and password fields exist
if (!$data || !isset($data->username) || !isset($data->password)) {
    echo json_encode([
        'status'  => 'error',
        'message' => 'Missing username or password.'
    ]);
    exit;
}

// Pull the values out and trim extra whitespace
$username = trim($data->username);
$password = trim($data->password);

// Basic server-side validation
// Never trust the browser alone — always check on the server too
if (empty($username) || empty($password)) {
    echo json_encode([
        'status'  => 'error',
        'message' => 'Username and password cannot be empty.'
    ]);
    exit;
}

if (strlen($password) < 6) {
    echo json_encode([
        'status'  => 'error',
        'message' => 'Password must be at least 6 characters.'
    ]);
    exit;
}

// Multiple users stored as an array
// Each username maps to its password
$users = [
    'admin'    => 'password123',
    'priest'   => 'holywater1999',
    'Dr. Ajayi' => 'takeover2024',
];

// Check if username exists and password matches
if (isset($users[$username]) && $users[$username] === $password) {
    echo json_encode([
        'status'  => 'success',
        'message' => 'Login successful. Welcome, ' . htmlspecialchars($username) . '!'
    ]);
} else {
    echo json_encode([
        'status'  => 'error',
        'message' => 'Incorrect username or password. Please try again.'
    ]);
}

?>