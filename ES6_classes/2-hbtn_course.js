export default class HolbertonCourse {
  constructor(name = '', length = 0, students = []) {
    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  set length(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = value;
  }

  set students(value) {
    if (typeof value === 'object') {
      for (const student in value) {
        if (typeof student !== 'string') {
          throw new TypeError('Students must be a string');
        }
      }
    } else {
      throw new TypeError('Students must be an array');
    }
    this._students = value;
  }
}
