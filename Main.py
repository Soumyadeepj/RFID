import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials
import time
import gspread
import json
from Delete import deletepage
from Issue import issue
from Issue import ret
from Add import addpage
import pandas as pd
st.set_page_config(
    page_title="RFID",
    page_icon="👋",
)

# doing sceret management
credentials_info = st.secrets['service_account']


SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets"
]

def get_sheet(database):
    if 'sheet_database' not in st.session_state:
        # Authenticate with the Google Sheets API using the downloaded JSON key file
        gc = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_dict(credentials_info,SCOPE))
        spreadsheet = gc.open('RFID')
        st.session_state['sheet_database'] = spreadsheet
    return st.session_state['sheet_database']

work = get_sheet("mydb").get_worksheet(0)
first_col = work.col_values(1) # get values of first column(A)

if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'main'

def main():
    st.write("# 👋Welcome to RFID Inventory Mangement System")

    if st.button("Scan"):

        'Scanning in progress...'

        # Add a placeholder>>>
        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
        # Update the progress bar with each iteration.
            latest_iteration.text(f'Progress {i+1}%')
            bar.progress(i + 1)
            time.sleep(0.001)
            
    cell = work.cell(1,9)  #cell I1 will store the scan id
   
    #st.session_state
    if 'name' not in st.session_state:
        st.session_state.name = ""
        
    if cell.value != None:
        try:
            index = first_col.index(cell.value)
            values = work.row_values(index+1)
            #print(values[4])
            'Found the product...'
            st.write(f"Prduct id : {values[0]}")
            st.write(f"Prduct name : {values[1]}")
            st.write(f"Status : {values[4]}")
            
            #print(work.cell(index+1,4).value) 
             
            if work.cell(index+1,4).value != None:

                json_string = work.cell(index + 1, 4).value
                # Parse the JSON string into a pandas DataFrame
                df = pd.DataFrame(json.loads(json_string))
                st.write("History of the product")
                st.dataframe(df, use_container_width=False)
                            

            else: st.write("Congratulation You are the first user🎉")    
                    # user input
            success_slot = st.empty()          
            if values[4] == "Not Available":
                if st.checkbox( "**Want to return ?**"):
                    
                    st.button("Proceed" ,key ="proceed",on_click = ret, args = (work,index,success_slot))        

            else:
                
                if st.checkbox("**Want to Issue ?**") or st.session_state.name != "": 
                    Name = st.text_input("Your name", key ="name")
                    email = st.text_input("Email id", key ="email")
                    date = st.date_input("Expected Return Date",value = None, key = "date")
                    if(Name and email and date):
                       st.button("submit",key = 'submit',on_click = issue,args= (work,index,Name,email,date,success_slot))

        except ValueError:
            st.error("Product is not registered, please register first") 
            
    else:st.write("No product found :cry:") 
    
    
          

def go2page(whichpage):
    st.session_state['current_page'] = whichpage
    
with st.sidebar:
    st.button("Home🏡",on_click=go2page,args=['main'])   
    st.button("Add➕",on_click=go2page,args=['add'])
    st.button("Delete🧼",on_click=go2page,args=['delete'])
    st.markdown("[Feedback](http://wa.me/7076523590?text=Hi%20Soumyadeep%20some%20suggestion)")

current_page = st.session_state['current_page']
if current_page == 'main':
    main()
elif current_page == 'add':
    addpage(work)
elif current_page == 'delete':
    deletepage(work)
