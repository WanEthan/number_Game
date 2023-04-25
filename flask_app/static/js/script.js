
var output, started, duration, delay;

// Constants
delay = 80;
increment = 0;
total = 60;
display = 30;

// Initial setup
output = $('#output');

// Animate!
animationTimer = setInterval(function() {
    increment = (increment + 1) % total;
    if (increment <= display) {
        output.text(''+ Math.floor(Math.random() * 101));
        randomColor = Math.floor(Math.random()*16777215).toString(16);
        output.css({'color': '#' + randomColor, 'background': "url('https://media3.giphy.com/media/MdvHuCfkvXO39xyDFL/200w.webp?cid=ecf05e476xevtrkbg4mkqcc6h0cqrjnnqnhr2k0h54uka6x3&rid=200w.webp&ct=s') no-repeat", 'background-size': '270px 270px', 'background-position-x': '70%'});
    } else {
        output.css({'background': "url('https://media1.giphy.com/media/gJ1zlEIw4c30qpyooF/giphy.gif?cid=ecf05e472oqqes7pibbaqp99tkbs6g657xf4uif2e4181bs8&rid=giphy.gif&ct=s') no-repeat center"} )
    }

}, delay);
