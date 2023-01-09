var myVideoStream = document.getElementById('myVideo')     // make it a global variable
var myStoredInterval = 0

function getVideo(){
navigator.getMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
navigator.getMedia({video: true, audio: false},
                   
  function(stream) {
    myVideoStream.srcObject = stream   
    myVideoStream.play();
}, 
                   
 function(error) {
   alert('webcam not working');
});
}

function takeSnapshot() {
 var myCanvasElement = document.getElementById('myCanvas');
 var myCTX = myCanvasElement.getContext('2d');
 myCTX.drawImage(myVideoStream, 0, 0, myCanvasElement.width, myCanvasElement.height);
 
}

function takeAuto() {
  // takeSnapshot() // get snapshot right away then wait and repeat
//   clearInterval(myStoredInterval)
//   myStoredInterval = setInterval(function(){                                                                                         
//      takeSnapshot()
//  }, document.getElementById('myInterval').value);   

  // var canvas = document.getElementById('myCanvas');
  // var myImage = document.getElementById('myImage');
  // myImage.src = canvas.toDataURL();

  // const link = document.createElement("a");
  // link.href = myImage;
  // link.download = "MyDesignSocks";
  // link.click();


  // var canvas = document.querySelector('myCanvas')
  // canvas.toDataURL()

  var canvas = document.getElementById('myCanvas');
  const image = canvas.toDataURL("image/png");
  alert(image)
  ///////// 실행 가능
  // console.log(image);

  // const link = document.createElement("a");

  // link.src = "./images";
  // link.href = image;
  // link.download = "PaintJS[🎨]";
  // link.click();

  ///////

  // link.setAttribute('href','/');
  // link.setAttribute('download', 'filename');
  // document.body.appendChild(link);
  // link.click();
  
}



