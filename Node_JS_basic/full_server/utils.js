const fs = require('fs').promises;

async function readDatabase(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.trim().split('\n');

    const students = lines.slice(1).map((line) => {
      const [firstname, , , field] = line.split(',');
      return { firstname, field };
    });

    const studentsByField = {};

    for (const { firstname, field } of students) {
      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }
      studentsByField[field].push(firstname);
    }

    return studentsByField;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = readDatabase;
