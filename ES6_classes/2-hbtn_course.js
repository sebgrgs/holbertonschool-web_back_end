export default class HolbertonCourse {
  constructor(name, length, students) {
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
    if (typeof value === 'string') {
      this._name = value;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  set length(value) {
    if (typeof value === 'number') {
      this._length = value;
    } else {
      throw new TypeError('Length must be a number');
    }
  }

  set students(value) {
    if (Array.isArray(value)) {
      for (const student of value) {
        if (typeof student !== 'string') {
          throw new TypeError('Each student must be a string');
        }
      }
      this._students = value;
    } else {
      throw new TypeError('Students must be an array');
    }
  }
}
