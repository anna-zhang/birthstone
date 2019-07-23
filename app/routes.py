from flask import render_template, request, redirect
from app import app
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/results', methods = ['POST'])
def results():
    user_month = request.form
    month = user_month["month"]
    birthstone = ""
    print(month)
    print(request.form)
    print(user_month)
    if month == "january":
        birthstone = "Garnet"
        image = "https://www.thepearlsource.com/blog/wp-content/uploads/2018/06/garnet.png"
    if month == "february":
        birthstone = "Amethyst"
        image = "https://www.heartcrafted.com/wp-content/uploads/2018/05/february-birthstone-amethyst-by-heart-crafted-handmade-jewelry-275x241.png"
    if month == "march":
        birthstone = "Aquamarine"
        image = "https://cdn11.bigcommerce.com/s-wdv53jt/images/stencil/500x659/products/2544/8218/1122_SS_39_AQUAMARINE_F__80327.1498058556.png?c=2"
    if month == "april":
        birthstone = "Diamond"
        image = "https://cdn.ymaws.com/www.americangemsociety.org/resource/resmgr/images/Birthstones/DIAMOND.png"
    if month == "may":
        birthstone = "Emerald"
        image = "https://cdn.ymaws.com/www.americangemsociety.org/resource/resmgr/images/Birthstones/emerald.png"
    if month == "june":
        birthstone = "Moonstone, Pearl, and Alexandrite"
        image = "https://cdn.shopify.com/s/files/1/2378/0799/articles/Pearl_Moonstone_Alexandrite_767x.png?v=1563415746"
    if month == "july":
        birthstone = "Ruby"
        image = "https://www.whiteflash.com/articlefiles/july-birthstone-ruby.png"
    if month == "august":
        birthstone = "Peridot"
        image = "http://blog.petersuchyjewelers.com/wp-content/uploads/2018/07/peridot.png"
    if month == "september":
        birthstone = "Sapphire"
        image = "https://cdn.shopify.com/s/files/1/0019/0496/7745/files/bs-september.png?2989399673632461840"
    if month == "october":
        birthstone = "Opal and Tourmaline"
        image = "https://i.dlpng.com/static/png/1852473-opal-png-image-opal-png-500_500_preview.png"
    if month == "november":
        birthstone = "Citrine and Topaz"
        image = "https://cdn.ymaws.com/www.americangemsociety.org/resource/resmgr/images/Birthstones/Citrine.png"
    if month == "december":
        birthstone = "Tanzanite, Zircon, and Turquoise"
        image = "http://static.shoplightspeed.com/shops/614058/files/005890666/dec.png"

    
    return render_template('results.html', month=month.capitalize(), birthstone=birthstone, image=image)


# @app.route('/results', methods = )


