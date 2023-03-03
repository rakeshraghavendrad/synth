#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template
import pandas as pd
import joblib
import random
import numpy as np
import pandas as pd



# Declare a Flask app
app = Flask(__name__)

# Main function here
@app.route('/', methods=['GET', 'POST'])
def main():
    
    # If a form is submitted
    if request.method == "POST":
        
        # classifier
        def get_model_output(complaint_type):
            if complaint_type == 'Checking_or_savings_account':
                data = pd.read_csv('./New folder/Checking_or_savings_account.csv')
            elif complaint_type == 'Mortgage':
                data = pd.read_csv('./New folder/Mortgage.csv')
            elif complaint_type == 'Credit_card_or_pre_paid_card':
                data = pd.read_csv('./New folder/Checking_or_savings_account.csv')
            elif complaint_type == 'Money_transfer_virtual_currency_or_money_service':
                data = pd.read_csv('./New folder/Money_transfer_virtual_currency_or_money_service.csv')
            else:
                return None
            list_data = data['Consumer complaint narrative'].str.split(".").apply(lambda x : [y for y in x if y != ''])
            list_data = pd.DataFrame(list_data.to_list())
            sentence_length = np.random.binomial(list_data.shape[1], 0.02)
            sentence = ''
            for i in range(sentence_length):
                sentence = sentence + random.choice(list(filter(None, list_data[i].to_list()))).strip() + '.'
    
            return sentence
        
        # Get values through input bars
        height = request.form.get("height")
        #weight = request.form.get("weight")
        
        # Put inputs to dataframe
        #X = pd.DataFrame([[height, weight]], columns = ["Height", "Weight"])
        
        # Get prediction
        prediction = get_model_output(str(height))
        
    else:
        prediction = ""
        
    return render_template("website.html", output = prediction)

# Running the app
if __name__ == '__main__':
    app.run(debug = False)


# In[ ]:




