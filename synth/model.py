import random
import numpy as np
import pandas as pd

def get_model_output(complaint_type):
    if complaint_type == 'Checking or savings account':
        data = pd.read_csv('Checking_or_savings_account.csv')
    elif complaint_type == 'Mortgage':
        data = pd.read_csv('Mortgage.csv')
    elif complaint_type == 'Credit card or pre paid card':
        data = pd.read_csv('Checking_or_savings_account.csv')
    elif complaint_type == 'Money transfer, virtual currency, or money service':
        data = pd.read_csv('Money_transfer_virtual_currency_or_money_service.csv')
    else:
        return None
    list_data = data['Consumer complaint narrative'].str.split(".").apply(lambda x : [y for y in x if y != ''])
    list_data = pd.DataFrame(list_data.to_list())
    sentence_length = np.random.binomial(list_data.shape[1], 0.02)
    sentence = ''
    for i in range(sentence_length):
        sentence = sentence + random.choice(list(filter(None, list_data[i].to_list()))).strip() + '.'
    
    return sentence

# get_model_output('Mortgage')
