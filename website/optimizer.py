from flask import Blueprint, render_template, request, flash, redirect, url_for

from website.functions import validateStock

optimizer = Blueprint('optimizer', __name__)


@optimizer.route('/Optimizer', methods=['GET', 'POST'])        #<--Route from main page
def optimizer_():
    data = request.form
    print(data)

    #We'll take input from user to validate errors before running optimizer
    if request.method == "POST":
        asset1 = request.form.get('Asset1').strip()
        asset2 = request.form.get('Asset2').strip()
        asset3 = request.form.get('Asset3').strip()
        investmentAmount = request.form.get('Amount').strip()

        assetList = [asset1, asset2, asset3]
        
        if not validateStock(assetList):
            flash("Write at least 1 asset", category = "error")

        elif investmentAmount == None or investmentAmount == "":
            flash("You must write an investment amount", category = "error")
        else:
            flash("Processing request!", category = "success")
            return redirect(url_for('views.index'))

    return render_template("optimizer.html", boolean = True)


@optimizer.route('/OptimalPortfolio', methods=['GET', 'POST'])
def logout():

    return render_template("optimal_portfolio.html")
