import streamlit as st
import gspread
# Open Spreadsheet by URL
def addpage(work):
    #add data to the database
    def adddata(data):
        work.append_row(data)
        #success_slot.success("Product added successfully 🎉")
        
    st.write("# Want to add Product :gift: ?")
    
    first_col = work.col_values(1) # get the list of id in the first col
    id = st.session_state.cell # get the id from I1 cell
    
    #work.update_cell(1,9,id)
    
    st.write(f"Prduct id : {id}")
    # checking the id already present or not
    if id != None:
        if id not in first_col:
            st.write("please enter the product details")
            name =st.text_input("Product name", key="pro_name")
            #id = st.text_input("UID", key="id")
            location = st.text_input("Location", key="location")
            left_col, right_col = st.columns(2) 
            dsr = left_col.text_input("DSR no.", key = "dsr")
            serial = right_col.text_input("Serial No.", key = "serial")
            
            success_slot = st.empty()  
            if name and id and location and dsr and serial:
                    data = [id, name, location, dsr, serial, "","Available"]
                    st.button("submit",on_click = adddata,args= (data,))
                
        else: st.success("Product registered")            
    else:st.error("Scan Failed :cry:")