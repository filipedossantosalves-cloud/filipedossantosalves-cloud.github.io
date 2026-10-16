module.exports = {
  content: ['./index.html', './*/index.html', './assets/js/site.js'],
  theme: {
    extend: {
      colors: { imperial:'#0D231E', profundo:'#13312A', ouro:'#C5A059', luz:'#DFBD7C', marfim:'#F7F5F0', salvia:'#A3B1AC' },
      fontFamily: { display:['Cinzel','Georgia','serif'], label:['Montserrat','Arial','sans-serif'], sans:['Plus Jakarta Sans','Arial','sans-serif'] },
      backgroundImage: { metal:'linear-gradient(135deg, #DFBD7C 0%, #C5A059 50%, #9E7B3B 100%)' },
      boxShadow: { luxury:'0 15px 35px -10px rgba(0,0,0,.6), 0 0 20px rgba(197,160,89,.06)' }
    }
  }
};
