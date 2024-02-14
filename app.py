from bottle import *


shopping_list = {
    "Milk" : "Lucrene Fat Free",
    "Bagel" : "Sally Raisin",
    "Protein Powder": "Gold Whey",
    "Cookie Dough" :  "Pilsberry"
}

deals = {
    "Milk" : "25% off",
    "Smoked Salmon" : "Buy one get one 25% off",
    "Filet Mignon" : "$2 off per pound"
    
}

app = Bottle()

@route('/')
def welcome():
    response.set_header('Vary', 'Accept')

    if 'text/html' in request.headers.get('Accept', '*/*'):

        response.content_type = 'text/html'

        html_string = '''
        <!DOCTYPE html>
        <head>
            <title>DangerWay Homepage</title>
        </head>
        <body style="background-color: red; text-align: center;">
            <div style="background-color: yellow; padding: 20px; border-radius: 10px; width: 300px; margin: 20px auto;">
                <h1>Welcome to DangerWay Market Website</h1>
            </div>
        </body>
        </html>
        '''

        return html_string

    response.content_type = 'text/plain'

    return 'Welcome to DangerWay Market'

 

@route('/list')
def show_list():

    response.content_type = 'text/html'
    response.set_header('Cache-Control', 'max-age=3')

    html_list =  '''
            <!DOCTYPE html>
        <head>
            <title>DangerWay Homepage</title>
        </head>
        <body style="background-color: #e6f2ff; text-align: center;">
        <h1> Your Shopping List </h1>
        '''
    html_list += "<ul>\n"
    for key, value in shopping_list.items():
        html_list += f"<li><b>{key}:</b> {value}</li>\n"
    html_list += "</ul>"
    
    html_list += '''
                </div>
        </body>
        </html>'''
    return html_list;


@route('/add/<item>/<brand>')
def add_item(item,brand):
    
    response.content_type = 'text/html'
    shopping_list[item] = brand;
    
    return f'<h1>Added item: {item}, brand: {brand} to the shopping list</h1>'
 
@route('/deals')
def deal_listing():

    response.content_type = 'text/html'

    html_list =  '''
            <!DOCTYPE html>
        <head>
            <title>DangerWay Homepage</title>
        </head>
        <body style="background-color: #e6f2ff; text-align: center;">
        <h1> February Deals </h1>
        '''
    html_list += "<ul>\n"
    for key, value in deals.items():
        html_list += f"<li><b>{key}:</b> {value}</li>\n"
    html_list += "</ul>"
    
    html_list += '''
                </div>
        </body>
        </html>'''
    return html_list;

@route('/checkout/<item>/<brand>')
def remove_item(item,brand):
    
    
    response.content_type = 'text/html'
    
    if item in shopping_list:
        shopping_list.pop(item)
        return '<body style="background-color: #e6f2ff; text-align: center;"> <h1> Removed Item: ' , item, ' and Brand: ' , brand , ' from the shopping list </h1> </body>'
    else:
        return '<body style= "background-color: blue; text-align: center; color: yellow;"> <h2>Item: ', item, ' and Brand: ', brand, ' doesn\'t exist.'
        
 

if __name__ == '__main__':

    run(host='0.0.0.0', port='8080')