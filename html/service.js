let constraints = { video: { facingMode: "user"}, audio: false};
const cameraView = document.querySelector("#camera--view");
const cameraOutput = document.querySelector("#camera--output");
const cameraSensor = document.querySelector("#camera--sensor");
const cameraTrigger = document.querySelector("#camera--trigger");


function cameraStart(){
    navigator.mediaDevices.getUserMedia(constraints)
        .then(function(stream){
            track = stream.getTracks()[0];
            cameraView.srcObject = stream;

        })
        .catch(function(error){
            console.error("카메라에 문제가 있습니다.", error);
        })
};

//촬영 버튼 클릭 리스너
cameraTrigger.addEventListener("click", function(){
    
    cameraSensor.width = cameraView.videoWidth; //640으로 정해져서 나오네?
    cameraSensor.height = cameraView.videoHeight;
    cameraSensor.getContext("2d").drawImage(cameraView, 0, 0);
    cameraOutput.src = cameraSensor.toDataURL("image/webp");
    cameraOutput.classList.add("taken");
    console.log(cameraSensor.height);
});

// 페이지가 로드되면 함수 실행
window.addEventListener("load", cameraStart, false);