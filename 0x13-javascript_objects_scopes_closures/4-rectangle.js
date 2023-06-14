#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (!(w > 0 && h > 0)) { return; }
    this.width = w;
    this.height = h;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  print () {
    const row = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) { console.log(row); }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
};
