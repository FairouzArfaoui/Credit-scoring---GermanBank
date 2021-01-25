  
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    duration = IntegerField('Duration in month', validators=[DataRequired()])

    credit = IntegerField('Credit amount', validators=[DataRequired()])

    rate = IntegerField('Installment rate in percentage of disposable income', validators=[DataRequired()])
    
    residence = IntegerField('Present residence since', validators=[DataRequired()])

    age = IntegerField("Age in years",validators=[DataRequired()])

    nbrcredit= IntegerField("Number of existing credits at this bank",validators=[DataRequired()])

    nbrperson= IntegerField("Number of people being liable to provide maintenance for",validators=[DataRequired()])

    credh = SelectField('Credit history', choices=[('no credits taken / all credits paid back duly', 'A30'),('all credits at this bank paid back duly','A31'),('existing credits paid back duly till now','A32'),('delay in paying off in the past','A33'),('critical account / other credits existing (not at this bank)','A34')])

    status = SelectField('Status of existing checking account', choices=[('... <    0 DM','A11'), ('0 <= ... <  200 DM','A12'),('... >= 200 DM / salary assignments for at least 1 year','A13'),('no checking account','A14')])

    purpose = SelectField('Purpose', choices=[('car (new)','A40'),('car (used)','A41'),('furniture/equipment','A42'),('radio/television','A43'),('domestic appliances','A44'),('repairs','A45'),('education','A46'),('(vacation - does not exist?)','A47'),('retraining','A48'),('business','A49'),('others','A410')])

    saving = SelectField('Savings account/bonds', choices=[('... <  100 DM','A61'),('100 <= ... <  500 DM','A62'),('500 <= ... < 1000 DM','A63'),('.. >= 1000 DM','A64'),('unknown/ no savings account','A65')])

    present = SelectField('Present employment since', choices=[('unemployed','A71'),('... < 1 year','A72'),('1  <= ... < 4 years','A73'),('4  <= ... < 7 years','A74'),('.. >= 7 years','A75')])

    personal = SelectField('Personal status and sex', choices=[('male:divorced/separated','A91'),('female:divorced/separated/married','A92'),('male:single','A93'),('male:married/widowed','A94'),('female:single','A95')])

    other = SelectField('Other debtors / guarantors', choices=[('none','101'),('co-applicant','A102'),('guarantor','A103')])

    otherInst = SelectField('Other installment plans', choices=[('bank','141'),('stores','142'),('none','A143')])

    proper = SelectField('Property', choices=[('real estate','A121'),('building society savings agreement / life insurance','A122'),('car or other','A123'),('unknown / no property','A124')])
    
    housing = SelectField('Housing', choices=[('rent','A151'),('own','A152'),('for free','A153')])

    job = SelectField('Job', choices=[('unemployed/ unskilled  - non-resident','A171'),('unskilled - resident','A172'),('skilled employee / official','A173'),('management/ self-employed/highly qualified employee/ officer','A174')])

    telephone = SelectField('Telephone', choices=[('none','A191'),('yes, registered under the customers name','A192')])

    foreign=SelectField('foreign worker', choices=[('yes','A201'),('no','A202')])




    submit = SubmitField('Process !')


class LoginForm(FlaskForm):
    email = StringField('Bank Name', validators=[DataRequired(), Length(min=5, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')