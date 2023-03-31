from flask import Flask, render_template, request
import game
print(__name__)
app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def hello():
    work = request.form.get("work")
    message = request.form.get("message")
    shift = request.form.get("shift")
    if message == None or work == None or shift == None or shift == "":
        work = "encode"
        message = "message"
        shift = 3
      
    output = game.ceaser_cipher(work, message, int(shift))
    if message == "" or work == "" and shift != "":
        output_line = "Not entered either message or command properly. Fix it." 
    else:
        output_line = f"Your {work}d message for {message} is {output}" 
    

    return render_template("index.html",
                           message=message,
                           command=work,
                           shift=shift,
                           output_line=output_line,)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)