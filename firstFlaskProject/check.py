import cv2
from flask import Flask, render_template, redirect, url_for, Response
app=  Flask(__name__)
camera=cv2.VideoCapture(0)
# =====================>>><<<=====================
def generate_frames():
    if not camera.isOpened():
        print("Could not open the camera.")
    while True:
        success, frame = camera.read()        
        if not success:
            print("camera isnt working")
            break
        else:
            print("camrea is working")
            ret,buffer=cv2.imencode(".jpg", frame)
            frame=buffer.tobytes()
       
@app.route('/')
def index():
    return render_template("kha.html")


@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundry=frame')
if __name__=="__main__":
    app.run(debug=True)