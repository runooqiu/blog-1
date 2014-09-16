from wtforms import Form, TextField, BooleanField


class LoginForm(Form):
    openid = TextField('openid')
    remember_me = BooleanField('remember_me', default = False)
