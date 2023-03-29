from flask import Blueprint, render_template, redirect, url_for, request

product = Blueprint("product", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

registered_products = []
registered_ingredients = []

hrefs = ["/product/register", "/product/ingredient"]
descriptions = ["Registrar Produto", "Registrar Ingrediente"]

@product.route('/')
def product_index():
    return render_template('/product/index.html', hrefs=hrefs, descriptions=descriptions)

# register product
@product.route('/register')
def register():
    global registered_products
    return render_template('/product/register.html', hrefs=hrefs, descriptions=descriptions, product_list = registered_products)

@product.route('/save_product', methods=['POST', 'GET'])
def save_product():
    name_product = request.form.get("name_product", None)
    desc_product = request.form.get("desc_product", None)
    value_product = request.form.get("value_product", None)
    qntd_product = request.form.get("qntd_product", None)
    
    global registered_products
    registered_products.append(f"Produto: {name_product} | Tipo: {desc_product} | R$ {value_product} | {qntd_product} itens no Estoque.")
    return redirect(url_for("product.register"))

# register ingredient
@product.route('/ingredient')
def ingredient():
    global registered_ingredients
    return render_template('/product/ingredient.html', hrefs=hrefs, descriptions=descriptions, ingredient_list = registered_ingredients)

@product.route('/save_ingredient', methods=['POST', 'GET'])
def save_ingredient():
    name_ingredient = request.form.get("name_ingredient", None)
    qntd_ingredient = request.form.get("qntd_ingredient", None)
    
    global registered_ingredients
    registered_ingredients.append(f"Ingrediente: {name_ingredient} | {qntd_ingredient} ingredientes no Estoque.")
    return redirect(url_for("product.ingredient"))
