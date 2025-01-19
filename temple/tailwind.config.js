/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [ './mandir/templates/**/*.html'],
  theme: {
  extend: {
    keyframes:{
      "slide-up":{
        form:{
          scale: 0.8
        },
        to:{
          scale: 1
        }
      }
    }
    ,animation:{
      "slide-up": "side-up 1s infinate"
    }
  },
  },
  plugins: [
    
    require("tailwindcss-animate"),
  ],
  };


