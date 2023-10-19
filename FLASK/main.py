from flask import Flask, request,jsonify
from flask_cors import CORS
from flask_mail import Mail, Message

app = Flask(__name__)
CORS(app)

#xppghghngfmfklyp
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "capitalentclinic159@gmail.com"
app.config['MAIL_PASSWORD'] = "vdbatazz ztcirymz"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER']="capitalentclinic159@gmail.com"

mail = Mail(app)

@app.route('/submit-form',methods=['POST'])
def submit_form():
    try:
      if (request.method == 'POST'):
       data = request.get_json()
       
       fname = data.get('name')
       email = data.get('email')
       date = data.get('date')
       phone = data.get('phone')
       service = data.get('service')
       doctor_name = data.get('doctor')
       message = data.get('message')
       
       #configuring email parameters
       subject = 'Notification of Patient Appointment'
       body  = f"I hope this email finds you well. I am writing to inform you about a recent appointment booking by one of our patients.Please find the details below:\nPatient Name: {fname.upper()}\nPhone number: {phone}\n Email: {email}\nDate of Appointment: {date}\nService requested: {service}\nDoctor in charge:{doctor_name}\n This patient has chosen to avail themselves of {service} on {date}.Please make the necessary arrangement to assist the patient."
       
       message = Message(subject=subject,body=body,recipients=["gakiokevin5@gmail.com"])
       mail.send(message)
      return jsonify({'message':'Sent successfully.You will be contacted soon!'})
    except Exception as e:
      print(e)
      app.logger.error(f"Error sending email{str(e)}")
      return "Failed to send the email,check for logs", 500

if __name__ == "__main__":
    app.run(debug=True)







#     # try:
    #     name = request.form["name"]
    #     day = request.form["day"]
    #     subject = "Appointment"
    #     body = f"{name} has booked an appointment on {day}"
    #     recepients = ["jacksonkimani05@gmail.com","Vinnykututa@gmail.com","customercare@capitalentclinic-fortis.com"]
    #     message = Message(subject=subject, body=body, recipients=recepients)
    #     mail.send(message)
    #     return "Email succesfully sent"
    # except Exception as e:
    #     app.logger.error(f"Error sending email{str(e)}")
    #     return "Failed to send the email,check for logs", 500


