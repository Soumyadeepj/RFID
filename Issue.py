import streamlit as st 
from datetime import date
import json
def issue(work,index,customer_name,email,contact,date,remark,success_slot):
    existing_data = work.cell(index+1, 6).value

    # Create a dictionary with the new customer information
    new_customer_data = {
        "Name": customer_name,
        "Email": email,
        "Contact": contact,
        "Issue": str(date.today()),
        "Retrun": str(date),  # Convert date to string if it's not already
        "Remarks": remark
    }

    # Convert the new data to a JSON string
    new_customer_info_json = json.dumps(new_customer_data)

    # Parse existing JSON string into a Python list
    existing_data_list = json.loads(existing_data) if existing_data else []

    # Append new customer data to the list
    new_customer_data = json.loads(new_customer_info_json)
    existing_data_list.append(new_customer_data)
    updated_data = json.dumps(existing_data_list)

    # Update the cell with the combined JSON string
    work.update_cell(index+1, 6, updated_data)
    work.update_cell(index+1, 14,email)
    work.update_cell(index+1, 15,str(date))
    work.update_cell(index+1,7, "Issued")
    # st.session_state["name"] = ""
    # st.session_state["email"] = ""
    # st.session_state["date"] = None
    success_slot.success("🎉")
    
def ret(work,index,remark,success_slot):
    existing_data = work.cell(index+1, 6).value
    #print(existing_data)
    existing_data = json.loads(existing_data)  # Parse JSON string to Python list

    # Identify the last element in the list
    last_element = existing_data[-1]

    # Update the "Return" date of the last element to today's date
    last_element["Retrun"] = str(date.today())
    last_element["Remarks"] = last_element["Remarks"] + "," + remark

    # Convert the updated list back to a JSON string
    updated_existing_data = json.dumps(existing_data)

    # Print the updated existing_data
    #print(updated_existing_data)

    # Update the cell with the updated JSON string
    work.update_cell(index + 1, 6, updated_existing_data)
    work.update_cell(index+1,15, str(date.today()))    
    work.update_cell(index+1, 7, "Available")
    success_slot.success("🎉")

