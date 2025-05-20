const http = require('http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.write('Hello Holberton School!');
    res.end();
  } else if (req.url === '/students') {
    res.write('This is the list of our students');
    countStudents(database)
      .then((output) => {
        res.write(output);
        res.end();
      });
  }
}).listen(1245);
module.exports = app;
