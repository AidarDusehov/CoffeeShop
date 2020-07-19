from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)

file_name = ''

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/components.html')
def components():
    return render_template('components.html')


@app.route('/data_name.html')
def test():
    return render_template('data_name.html')

@app.route('/data.html')
def data():
    return render_template('data.html')



#Date and Name. Creation of new file
# def write_to_csv1(data1, num):
#     file_name = data1['date']+data1['name']+'.csv'
#     if(num == 0):
#         try:
#             with open(file_name, mode = 'a',newline='') as database:
#                 csv_writer = csv.writer(database, delimiter = ',' , quotechar = '"', quoting=csv.QUOTE_MINIMAL ) 
#                 csv_writer.writerow(['Product','Size','Quantity'])
#         except:
#             return 0
#     else:   
#         write_to_csv(data1)

#     def write_to_csv(data):
#         try:
#             with open(, mode = 'a',newline='') as database1:
#                 product = data['product']
#                 size = data['size']
#                 number = data['number']
#                 csv_writer = csv.writer(database1, delimiter = ',' , quotechar = '"', quoting=csv.QUOTE_MINIMAL ) 
#                 csv_writer.writerow([product,size,number])
#         except:
#             return 0
    
# @app.route('/submit_form1', methods=['POST', 'GET'])
# def submit_form1():
#     if request.method == 'POST':
#         data1 = request.form.to_dict()
#         write_to_csv1(data1,0)
#         return redirect('/data.html')
#     else:
#         return 0

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         write_to_csv1(data,1)
#         return redirect('/data.html')
#     else:
#         return 0

# #Fillind data


# # name = data ["name"]
# # age = data ["age"]
# # ln = data ["last_name"]
# #csv_writer = csv.writer(database, delimiter = ',' , quotechar = '"', quoting=csv.QUOTE_MINIMAL ) 
# # csv_writer.writerow([name,ln, age])