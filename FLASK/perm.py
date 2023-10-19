from docx import Document

from itertools import permutations

def read_docx(file_path):
    doc = Document(file_path)

    # Extract text from paragraphs
    text_content = []
    for paragraph in doc.paragraphs:
        text_content.append(paragraph.text)

    return '\n'.join(text_content)
def identify_permutations_within_subgroups(data):
    # Iterate over all possible subgroup sizes from 1 to 360
    for subgroup_size in range(1, 361):
        # Initialize an index to keep track of the current position in the data
        index = 0

        # Iterate over subgroups
        while index + subgroup_size <= len(data):
            # Extract the current subgroup
            subgroup = data[index:index + subgroup_size]

            # Identify permutations within the subgroup
            for perm in permutations(subgroup):
                print(perm)

            # Move the index to the start of the next subgroup
            index += 1



if __name__ == "__main__":
    docx_file_path = "SUBGROUPS OF A6.docx"  # Replace with the actual path to your .docx file
      # Adjust the subgroup size based on your data

    content = read_docx(docx_file_path)
    identify_permutations_within_subgroups(content)



# app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://kevin:pass@localhost/persons'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# db = SQLAlchemy(app)

# class Users(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     username = db.Column(db.String(70),unique=True)
#     password = db.Column(db.String(100),unique=True)
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password

# with app.app_context() :
# #  db.create_all()

# #  user = Users('sam','hellome')

# #  db.session.add(user)
# #  db.session.commit()
#  all_users = Users.query.all()
# for user in all_users:
#  print( f"Username: {user.username}")


# if __name__ =="__main__" :

#   app.run(debug=True)
# # @app.route('/appointment', methods=['POST'])
# # def book_appointment():
# #     try:
# #        # name = request.form['name']
# #         #email = request.form['email']
# #         data = request.get_json()


# #         response_data = {
# #             'status': 'success',
# #             'message': 'data successfully saved',
# #             'data': data
# #         }
# #         return jsonify(response_data), 200
# #     except Exception as e:
# #         error_response = {
# #             'status': 'error',
# #             'message': 'Failed to process form data',
# #             'error': str(e)
# #         }
# #         return jsonify(error_response), 500  # Internal Server Error