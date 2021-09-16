const express = require('express');
const app = express();

app.use(express.json());

app.listen({ host: 'localhost', port: 8000 });

app.post('/port29775002217', (req, res) => {
  const { data } = req.body;
  console.log(data);
  res.send('ok');
})