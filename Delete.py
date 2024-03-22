import streamlit as st

def deletepage(work):
    st.warning("Warning! It will permanantly delete the item")

    id = work.cell(1,9).value # get the id from I1 cell

    first_col = work.col_values(1) # get values of first column(A)

    def delete(row_index):

        work.delete_rows(row_index)
        
    
    def delete_hist(row_indices):
  
        work.update_cell(row_indices, 4, '')

    try:
        index = first_col.index(id)
        #note: row starts from 1,2,3...
        #values(list) starts from 0,1,2...
        values = work.row_values(index+1)
        #print(index+1)
        #print(type(values)) #lis
        'Found the product...'
        st.write(f"Prduct id : {values[0]}")
        st.write(f"Prduct name : {values[1]}")
        success_slot = st.empty() 
        left_column, right_column = st.columns(2)
        if left_column.button("Delete", key='delete'):
            delete(index+1)
            success_slot.success("Product deleted")
        if right_column.button("Delete History", key='History'):
            delete_hist(index+1)
            success_slot.success("History deleted")
            
    except ValueError:
        st.error("Product is not registered, please register first")    
                
