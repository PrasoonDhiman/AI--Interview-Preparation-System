import {
    FaceLandmarker,
    FilesetResolver
} from "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.22-rc.20250304/vision_bundle.mjs";


console.log("=================================");
console.log("CAMERA.JS STARTED");
console.log("=================================");


const video =
    document.getElementById("webcam");

const canvas =
    document.getElementById("landmarkCanvas");

const cameraStatus =
    document.getElementById("cameraStatus");

const faceStatus =
    document.getElementById("faceStatus");

const stopButton =
    document.getElementById("stopCamera");

const ctx =
    canvas.getContext("2d");


console.log("Video element:", video);
console.log("Canvas element:", canvas);


// ==================================================
// MEDIAPIPE
// ==================================================

let faceLandmarker = null;

let lastVideoTime = -1;

let animationFrameId = null;


// ==================================================
// START CAMERA
// ==================================================

async function startCamera() {

    console.log("Starting camera...");

    try {

        cameraStatus.textContent =
            "Requesting camera permission...";


        if (
            !navigator.mediaDevices ||
            !navigator.mediaDevices.getUserMedia
        ) {

            throw new Error(
                "Camera API is not supported."
            );

        }


        const stream =
            await navigator.mediaDevices.getUserMedia({

                video: {
                    width: { ideal: 640 },
                    height: { ideal: 480 },
                    facingMode: "user"
                },

                audio: false

            });


        console.log(
            "Camera permission granted"
        );


        video.srcObject = stream;

        video.muted = true;

        video.autoplay = true;

        video.playsInline = true;


        await video.play();


        console.log(
            "Video started:",
            video.videoWidth,
            "x",
            video.videoHeight
        );


        canvas.width =
            video.videoWidth;

        canvas.height =
            video.videoHeight;


        cameraStatus.textContent =
            "Camera active";


        await initializeMediaPipe();


    } catch (error) {

        console.error(
            "CAMERA ERROR:",
            error
        );

        cameraStatus.textContent =
            "Camera error";

        faceStatus.textContent =
            error.name + ": " +
            error.message;

    }

}


// ==================================================
// INITIALIZE MEDIAPIPE
// ==================================================

async function initializeMediaPipe() {

    try {

        console.log(
            "Loading MediaPipe..."
        );


        cameraStatus.textContent =
            "Loading MediaPipe...";


        const vision =
            await FilesetResolver.forVisionTasks(

                "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.22-rc.20250304/wasm"

            );


        console.log(
            "MediaPipe WASM loaded"
        );


        faceLandmarker =
            await FaceLandmarker.createFromOptions(

                vision,

                {

                    baseOptions: {

                        modelAssetPath:
                            "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task"

                    },

                    runningMode: "VIDEO",

                    numFaces: 1,

                    minFaceDetectionConfidence: 0.5,

                    minFacePresenceConfidence: 0.5,

                    minTrackingConfidence: 0.5

                }

            );


        console.log(
            "================================="
        );

        console.log(
            "MEDIAPIPE INITIALIZED"
        );

        console.log(
            "================================="
        );


        cameraStatus.textContent =
            "Camera + MediaPipe active";

        faceStatus.textContent =
            "Detecting face...";


        processFrames();


    } catch (error) {

        console.error(
            "MEDIAPIPE ERROR:",
            error
        );

        cameraStatus.textContent =
            "MediaPipe error";

        faceStatus.textContent =
            error.message;

    }

}


// ==================================================
// PROCESS FRAMES
// ==================================================

function processFrames() {

    if (!faceLandmarker) {

        animationFrameId =
            requestAnimationFrame(
                processFrames
            );

        return;

    }


    if (
        video.readyState >=
        HTMLMediaElement.HAVE_CURRENT_DATA
    ) {

        if (
            video.currentTime !==
            lastVideoTime
        ) {

            lastVideoTime =
                video.currentTime;


            try {

                const results =
                    faceLandmarker.detectForVideo(

                        video,

                        performance.now()

                    );


                processResults(results);


            } catch (error) {

                console.error(
                    "FRAME ERROR:",
                    error
                );

            }

        }

    }


    animationFrameId =
        requestAnimationFrame(
            processFrames
        );

}


// ==================================================
// PROCESS RESULTS
// ==================================================

function processResults(results) {

    ctx.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );


    if (
        !results ||
        !results.faceLandmarks ||
        results.faceLandmarks.length === 0
    ) {

        faceStatus.textContent =
            "No face detected";

        return;

    }


    const landmarks =
        results.faceLandmarks[0];


    faceStatus.textContent =
        "Face detected";


    console.log(
        "Frame detected:",
        landmarks.length,
        "landmarks"
    );


    drawLandmarks(
        landmarks
    );

}


// ==================================================
// DRAW LANDMARKS
// ==================================================

function drawLandmarks(landmarks) {

    ctx.fillStyle =
        "lime";


    for (
        const landmark of landmarks
    ) {

        const x =
            landmark.x *
            canvas.width;

        const y =
            landmark.y *
            canvas.height;


        ctx.beginPath();

        ctx.arc(
            x,
            y,
            2,
            0,
            Math.PI * 2
        );

        ctx.fill();

    }

}


// ==================================================
// STOP CAMERA
// ==================================================

function stopCamera() {

    if (animationFrameId) {

        cancelAnimationFrame(
            animationFrameId
        );

        animationFrameId = null;

    }


    if (video.srcObject) {

        video.srcObject
            .getTracks()
            .forEach(track => {
                track.stop();
            });

        video.srcObject = null;

    }


    ctx.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );


    cameraStatus.textContent =
        "Camera stopped";

    faceStatus.textContent =
        "Camera stopped";

}


// ==================================================
// BUTTON
// ==================================================

stopButton.addEventListener(
    "click",
    stopCamera
);


// ==================================================
// START
// ==================================================

startCamera();