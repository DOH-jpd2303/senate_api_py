#Load modules
import pandas as pd

def flatten_filing_info(record_list):
    #Here are the columns we want to keep
    get_cols = ['url', 'document_url',
            'reg_id', 'reg_name', 
            'reg_addr1', 'reg_addr2', 'reg_addr3', 'reg_addr4',
            'reg_city', 'reg_state', 'reg_zip', 'reg_country',
            'contact_name', 'contact_telephone',
            'client_name', 'client_id', 
            'client_government_entity', 'client_self_select']
    df = pd.DataFrame(columns = get_cols)
    for record in record_list:
        row = flatten_filing_info_single(record)
        df = df.append(row, ignore_index = True)
        del row
    return df
        
def flatten_filing_info_single(record):
    #Initialize the row
    row = pd.Series()
    
    #URLs
    row['url'] = record['url']
    row['document_url'] = record['filing_document_url']
    
    #Registrant main info
    row['reg_id'] = record['registrant']['id']    
    row['reg_name'] = record['registrant']['name']
    
    #Registrant address lines   
    row['reg_addr1'] = record['registrant']['address_1']
    row['reg_addr2'] = record['registrant']['address_2']
    row['reg_addr3'] = record['registrant']['address_3']
    row['reg_addr4'] = record['registrant']['address_4']
    
    #Registrant city/state/zip    
    row['reg_city'] = record['registrant']['city']
    row['reg_state'] = record['registrant']['state']
    row['reg_zip'] = record['registrant']['zip']
    row['reg_country'] = record['registrant']['country']
    
    #Registrant contact name/phone
    row['contact_name'] = record['registrant']['contact_name']
    row['contact_telephone'] = record['registrant']['contact_telephone']
    
    #Client name/id    
    row['client_name'] = record['client']['name']
    row['client_id'] = record['client']['id']
    
    #Whether client is government entity or self representing    
    row['client_government_entity'] = record['client']['client_government_entity']
    row['client_self_select'] = record['client']['client_self_select']
    
    #Return result
    return(row)
    
