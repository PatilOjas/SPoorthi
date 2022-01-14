var controller = new ScrollMagic.Controller();
TweenMax.set('#timeline',{visibility:0});

var tweenOne =
new TweenMax.fromTo('#timeline',5,{drawSVG:"0%"}, {drawSVG:"6.25%"});  
 
var scene1 = new ScrollMagic.ScrollScene({
  triggerElement: '#timeline',
  offset: 10,
  duration: 30
}).setTween(tweenOne).addTo(controller); 
    
var tweenTwo =
new TweenMax.fromTo('#timeline',1,{drawSVG:"6.25%"}, {drawSVG:"12.5%"});

var scene2 = new ScrollMagic.ScrollScene({
  triggerElement: '.dayTwo',
}).setTween(tweenTwo).addTo(controller); 


var tweenThree =
new TweenMax.fromTo('#timeline',1,{drawSVG:"12.5%"}, {drawSVG:"18.75%"});

var scene3 = new ScrollMagic.ScrollScene({
  triggerElement: '.dayThree',
}).setTween(tweenThree).addTo(controller); 


var tweenFour =
new TweenMax.fromTo('#timeline',1,{drawSVG:"18.75%"}, {drawSVG:"25%"});

var scene4 = new ScrollMagic.ScrollScene({
  triggerElement: '.dayFour',
}).setTween(tweenFour).addTo(controller); 
 
var tweenFive =
new TweenMax.fromTo('#timeline',1,{drawSVG:"25%"}, {drawSVG:"31.25%"});

var scene5 = new ScrollMagic.ScrollScene({
  triggerElement: '.dayFive',
}).setTween(tweenFive).addTo(controller); 

var tweenSix =
new TweenMax.fromTo('#timeline',1,{drawSVG:"31.25%"}, {drawSVG:"37.5%"});

var scene6 = new ScrollMagic.ScrollScene({
  triggerElement: '.daySix',
}).setTween(tweenSix).addTo(controller); 
// 
var tweenSeven =
new TweenMax.fromTo('#timeline',1,{drawSVG:"37.5%"}, {drawSVG:"43.75%"});

var scene7 = new ScrollMagic.ScrollScene({
  triggerElement: '.daySeven',
}).setTween(tweenSeven).addTo(controller); 
// 
var tweenEight =
new TweenMax.fromTo('#timeline',1,{drawSVG:"43.75%"}, {drawSVG:"50%"});

var scene8 = new ScrollMagic.ScrollScene({
  triggerElement: '.dayEight',
}).setTween(tweenEight).addTo(controller); 
// 
var tweenNine =
new TweenMax.fromTo('#timeline',1,{drawSVG:"50%"}, {drawSVG:"56.25%"});

var scene9 = new ScrollMagic.ScrollScene({
  triggerElement: '.dayNine',
}).setTween(tweenNine).addTo(controller); 
// 
var tweenTen =
new TweenMax.fromTo('#timeline',1,{drawSVG:"56.25%"}, {drawSVG:"62.5%"});

var scene10 = new ScrollMagic.ScrollScene({
  triggerElement: '.dayTen',
}).setTween(tweenTen).addTo(controller); 
// 
var tweenEleven =
new TweenMax.fromTo('#timeline',1,{drawSVG:"62.5%"}, {drawSVG:"68.75%"});

var scene11 = new ScrollMagic.ScrollScene({
  triggerElement: '.dayEleven',
}).setTween(tweenEleven).addTo(controller); 
// 
var tweenTwelve =
new TweenMax.fromTo('#timeline',1,{drawSVG:"68.75%"}, {drawSVG:"75%"});

var scene12 = new ScrollMagic.ScrollScene({
  triggerElement: '.dayTwelve',
}).setTween(tweenTwelve).addTo(controller); 
// 
var tweenThirteen =
new TweenMax.fromTo('#timeline',1,{drawSVG:"75%"}, {drawSVG:"81.25%"});

var scene13 = new ScrollMagic.ScrollScene({
  triggerElement: '.dayThirteen',
}).setTween(tweenThirteen).addTo(controller); 
// 
var tweenForteen =
new TweenMax.fromTo('#timeline',1,{drawSVG:"81.25%"}, {drawSVG:"87.5%"});

var scene14 = new ScrollMagic.ScrollScene({
  triggerElement: '.dayForteen',
}).setTween(tweenForteen).addTo(controller); 
// 
var tweenFifteen =
new TweenMax.fromTo('#timeline',1,{drawSVG:"87.5%"}, {drawSVG:"93.75%"});

var scene15 = new ScrollMagic.ScrollScene({
  triggerElement: '.dayFifteen',
}).setTween(tweenFifteen).addTo(controller); 
// 
var tweenSixteen =
new TweenMax.fromTo('#timeline',1,{drawSVG:"93.75%"}, {drawSVG:"100%"});

var scene16 = new ScrollMagic.ScrollScene({
  triggerElement: '.daySixteen',
}).setTween(tweenSixteen).addTo(controller); 
// 

if (new Date().getTime() >= new Date(2021, 11, 24)){
	console.log("Execute")
}










// let timeScroll = document.getElementById('verticalLine');

// timeScroll.addEventListener('mouseover', ()=>{
//   timeScroll.style.backgroundColor = "#000000"
// })
// timeScroll.addEventListener('mouseout', ()=>{
//   timeScroll.style.backgroundColor = "#ffffff"
// })


// window.addEventListener('load' ,()=>{
//   let timeScroll1 = document.getElementById('verticalLine');
//   console.log(timeScroll1.offsetHeight);
//   console.log(window.pageYOffset || document.documentElement.scrollTop);
//   window.onscroll = (()=>{
//     let progress = window.pageYOffset - timeScroll.offsetHeight;
//     timeScroll.style.height = progress + "px";
//   })
//   // let totalHeight = document.body.scrollHeight - window.innerHeight;
// })