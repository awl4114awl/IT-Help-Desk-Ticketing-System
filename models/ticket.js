const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const TicketSchema = new Schema({
  name: String,
  department: String,
  subject: String,
  description: String,
  priority: String,
  status: { type: String, default: 'Open' },
  createdAt: { type: Date, default: Date.now },
  updatedAt: { type: Date, default: Date.now },
  comments: [{ body: String, date: Date }]
});

module.exports = mongoose.model('Ticket', TicketSchema);
