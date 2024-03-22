import streamlit as st
import gspread
# Open Spreadsheet by URL
def addpage(work):
    # st.session_state
    def clear_text():
        st.session_state["pro_name"] = ""
        #st.session_state["id"] = ""
        st.session_state["details"] = ""
        
    st.write("# Want to add Product :gift: ?")
    
    first_col = work.col_values(1) # get the list of id in the first col
    id = work.cell(1,9).value # get the id from I1 cell
    
    st.write(f"Prduct id : {id}")
    # checking the id already present or not
    if id not in first_col:
        st.write("please enter the product details")
        name =st.text_input("Product name", key="pro_name")
        #id = st.text_input("UID", key="id")
        details = st.text_input("Details", key="details")


        if st.button("Submit"):
            if name and id and details:
                    data = [id, name, details,"","Available"]
                    work.append_row(data)
                    st.success("Product added successfully!")
                    st.button("+ADD",on_click=clear_text)
                    
                # else:
                    
                #     st.error("Product with the same ID already exists. Please enter a unique ID.")
            else:
                st.warning("Please enter all the fields")
    else: st.success("Product already present in the database")            
