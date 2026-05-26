// Price per ticket
const ticketPrice = 400;

// Read seat string from HTML (e.g., "A1, A2, A3")
const seatString = document.getElementById('seats').textContent;
const seatList = seatString.split(',').map(s => s.trim());

// Calculate total amount
const totalAmount = seatList.length * ticketPrice;

// Display result in the bill
document.getElementById('total').textContent = totalAmount;
