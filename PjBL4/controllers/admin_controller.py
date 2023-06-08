from flask import Blueprint, render_template, redirect,url_for
from flask_login import current_user, login_required
from controllers.user_controller import user
from controllers.iot_controller import iot

admin = Blueprint("admin", __name__, 
                    template_folder="./views/", 
                    static_folder='./static/', 
                    root_path="./")

admin.register_blueprint(user, url_prefix='/user')
admin.register_blueprint(iot, url_prefix='/iot')

@admin.route("/")
@admin.route("/admin")
#@login_required
def admin_index():
    """
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))
    else:
        return render_template("admin/admin_base.html", name = current_user.name)
    """
    return render_template("admin/admin_index.html")
    
    