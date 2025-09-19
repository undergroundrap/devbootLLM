const fs = require('fs');
const path = require('path');
const safelist = fs.readFileSync(path.join(__dirname, 'tailwind.classes.txt'), 'utf-8')
  .split(/\r?\n/)
  .map(x => x.trim())
  .filter(Boolean);
module.exports = {
  content: [],
  safelist,
  theme: {
    extend: {},
  },
  plugins: [],
};
