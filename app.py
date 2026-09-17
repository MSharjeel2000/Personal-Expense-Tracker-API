import datetime
from flask import Flask , jsonify , request
from main import daily_expense , add_expense as add_expense_to_tracker , save_expenses , calculate_total , calculate_category_total

app = Flask(__name__)

@app.route("/")
def home():
    return "Personal Expense API Tracker is running"

@app.route("/expenses")
def expenses():
    return jsonify (daily_expense)

@app.route("/expenses" , methods = ["POST"])
def add_expense():
    data = request.get_json(silent=True)
    
    if data is None:
        return jsonify ({
            "error" : "JSON is required"
        }) , 400
       
    if "amount" not in data or "category" not in data or "date" not in data:
        return jsonify ({
            "error" : "amount , category and date are required"
        }) , 400
    
    if not isinstance(data["amount"] , (int, float)):
        return jsonify ({
            "error" : "amount must be a number"
        }) , 400
        
    if not isinstance(data["category"], str) or data["category"] == "" or data["category"].isdigit():
        return jsonify ({
            "error" : "category must be valid"
        }) , 400
    
    if not isinstance (data["date"], str):
        return jsonify ({
            "error" : "date must be in DD-MM-YYYY format"
        }) , 400
    
    try:
        datetime.datetime.strptime(data["date"], "%d-%m-%Y")
    except ValueError:
        return jsonify ({
            "error" : "date must be in DD-MM-YYYY format"
        }) , 400
             
    add_expense_to_tracker(
        data["amount"],
        data["category"],
        data["date"]
    )
    
    return jsonify({
        "message" : "Expense added successfully",
        "expense" : data
        }) , 201

@app.route("/expenses/<int:index>", methods = ["PUT"])
def update_expense(index):
   
    if index < 0 or index >= len(daily_expense):
        return jsonify ({
            "error" : "Expense not found"
        }) , 404
        
    data = request.get_json(silent=True)
    
    if data is None:
        return jsonify ({
            "error" : "JSON is required"
        }) , 400
        
    if "amount" not in data or "category" not in data or "date" not in data:
        return jsonify({
            "error": "amount, category and date are required"
        }), 400
    
    if not isinstance(data["amount"] , (int, float)):
        return jsonify ({
            "error" : "amount must be a number"
        }) , 400
            
    if not isinstance(data["category"], str) or data["category"] == "" or data["category"].isdigit():
        return jsonify ({
            "error" : "category must be valid"
        }) , 400
        
    if not isinstance (data["date"], str):
        return jsonify ({
            "error" : "date must be in DD-MM-YYYY format"
        }) , 400
        
    try:
        datetime.datetime.strptime(data["date"], "%d-%m-%Y")
    except ValueError:
        return jsonify ({
            "error" : "date must be in DD-MM-YYYY format"
        }) , 400
    
    daily_expense[index]["amount"] = data["amount"]
    daily_expense[index]["category"] = data["category"]
    daily_expense[index]["date"] = datetime.datetime.strptime(data["date"] , "%d-%m-%Y").date()
    
    save_expenses()
    
    return jsonify (data)

@app.route("/expenses/<int:index>" , methods = ["DELETE"])
def delete_expense(index):
    if index < 0 or index >= len(daily_expense):
        return jsonify ({
            "error" : "Expense not found"
        }) , 404
            
    del daily_expense[index]
    
    save_expenses()
    
    return jsonify ({"message" : "Expense deleted successfully"})

@app.route("/expenses/total")
def total_expenses():
    total = calculate_total()
    
    return jsonify ({
        "total" : total
    })
    
@app.route("/expenses/category/<category>")
def category_total(category):
    existing_category , category_total = calculate_category_total(category)
    
    if not existing_category:
        return jsonify ({
            "error" : "Category not found"
        }) , 404
        
    return jsonify ({
        "category" : category ,
        "total" : category_total
    })
    
@app.route("/expenses/search/<category>")
def search_expenses(category):
    results = []
    
    for expense in daily_expense:
        if expense["category"] == category:
            results.append(expense)
    
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0" , debug=True)