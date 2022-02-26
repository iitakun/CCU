#!/usr/bin/env python
# coding: utf-8

# In[51]:


from flask import Flask


# In[52]:


app = Flask(__name__)


# In[53]:


from flask import request, render_template
import joblib

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        purchases = request.form.get("purchases")
        suppcard = request.form.get("suppcard")
        print(purchases, suppcard)
        model = joblib.load("CCU_Reg")
        pred = model.predict([[float(purchases), float(suppcard)]])
        print(pred)
        if pred[0] == 0:
            decision = "No"
        elif pred[0] == 1:
            decision = "Yes"
        print(decision)
        s_reg = "Predicted Upgrading decision based on Linear Regression model is: " + str(decision)
        model = joblib.load("CCU_DT")
        pred = model.predict([[float(purchases), float(suppcard)]])
        print(pred)
        if pred[0] == 0:
            decision = "No"
        elif pred[0] == 1:
            decision = "Yes"
        print(decision)
        s_dt = "Predicted Upgrading decision based on Decision Tree model is: " + str(decision)
        model = joblib.load("CCU_RF")
        pred = model.predict([[float(purchases), float(suppcard)]])
        print(pred)
        if pred[0] == 0:
            decision = "No"
        elif pred[0] == 1:
            decision = "Yes"
        print(decision)
        s_rf = "Predicted Upgrading decision based on Random Forest model is: " + str(decision)
        model = joblib.load("CCU_GB")
        pred = model.predict([[float(purchases), float(suppcard)]])
        print(pred)
        if pred[0] == 0:
            decision = "No"
        elif pred[0] == 1:
            decision = "Yes"
        print(decision)
        s_gb = "Predicted Upgrading decision based on XGBoost model is: " + str(decision)
        model = joblib.load("CCU_NN")
        pred = model.predict([[float(purchases), float(suppcard)]])
        print(pred)
        if pred[0] == 0:
            decision = "No"
        elif pred[0] == 1:
            decision = "Yes"
        print(decision)
        s_nn = "Predicted Upgrading decision based on Neural Network model is: " + str(decision)
        return(render_template("index.html", result1=s_reg, result2=s_dt, result3=s_rf, result4=s_gb, result5=s_nn))
    else:
        return(render_template("index.html", result1="2", result2="2", result3="2", result4="2", result5="2"))


# In[ ]:


if __name__=="__main__":
    app.run()


# In[ ]:




