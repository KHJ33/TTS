var myVideoStream = document.getElementById('myVideo')     // make it a global variable
var myStoredInterval = 0

// webcam 구현 함수
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

// webcam 캡쳐 이미지 canvas 에 그리기
function takeSnapshot() {
    var myCanvasElement = document.getElementById('myCanvas');
    
    var myCTX = myCanvasElement.getContext('2d');
    myCTX.drawImage(myVideoStream, 0, 0, myCanvasElement.width, myCanvasElement.height);
}

// canvas 이미지
function saveImg() {
    var canvas = document.getElementById('myCanvas');
    const image = canvas.toDataURL("image/png", 1.0);
   
    const link = document.createElement("a");

    // link.src = "./images";
    link.href = image;
    link.download = "text_img";
    link.click();

    // 클릭시 saveImg 폴더 내로 저장 -- 미구현

}



