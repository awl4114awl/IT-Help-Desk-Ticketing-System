const express = require('express');
const router = express.Router();
const Ticket = require('../models/ticket');

router.get('/', (req, res) => {
  res.render('home');
});

router.post('/submit-ticket', async (req, res) => {
  const newTicket = new Ticket(req.body);
  await newTicket.save();
  res.redirect('/tickets');
});

router.get('/tickets', async (req, res) => {
  const tickets = await Ticket.find();
  res.render('tickets', { tickets });
});

router.get('/admin', async (req, res) => {
  const tickets = await Ticket.find();
  res.render('admin', { tickets });
});

router.post('/admin/edit-ticket/:id', async (req, res) => {
  await Ticket.findByIdAndUpdate(req.params.id, req.body);
  res.redirect('/admin');
});

router.post('/admin/delete-ticket/:id', async (req, res) => {
  await Ticket.findByIdAndDelete(req.params.id);
  res.redirect('/admin');
});

router.post('/admin/add-comment/:id', async (req, res) => {
  const ticket = await Ticket.findById(req.params.id);
  ticket.comments.push({ body: req.body.comment, date: new Date() });
  await ticket.save();
  res.redirect('/tickets');
});

module.exports = router;
