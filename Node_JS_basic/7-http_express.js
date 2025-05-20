const express = require('express');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});
app.get('/students', (req, res) => {
  res.write('This is the list of our students');
  countStudents(database)
    .then((output) => {
      res.write(output);
      res.end();
    })
    .catch((err) => {
      res.status(500).send(err.message);
    });
});
app.listen(1245);
module.exports = app;
