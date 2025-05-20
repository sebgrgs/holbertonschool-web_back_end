const http = require('http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.set('Content-Type', 'text/plain');
    res.write('Hello Holberton School!');
    res.end();
  } else if (req.url === '/students') {
    res.set('Content-Type', 'text/plain');
    res.write('This is the list of our students');
    countStudents(database)
      .then((output) => {
        res.write(output);
        res.end();
      })
      .catch((err) => {
        res.write(err.message);
        res.end();
      });
  } else {
    res.statusCode = 404;
    res.end('Not found');
  }
}).listen(1245);
module.exports = app;
