"""
Pagination utilities for the Synergy Hub application
"""
import streamlit as st
import math

def create_pagination_ui(total_records, current_page, per_page, key_prefix=""):
    """
    Create a consistent pagination UI for Streamlit pages
    
    Args:
        total_records (int): Total number of records
        current_page (int): Current page (1-indexed)
        per_page (int): Number of items per page
        key_prefix (str): Prefix for session state keys to make them unique
    
    Returns:
        tuple: (prev_button, next_button, total_pages, page_info_text)
    """
    total_pages = math.ceil(total_records / per_page) if total_records > 0 else 1
    
    # Create column layout for pagination
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        prev_disabled = current_page <= 1
        prev_button = st.button(
            "← Previous", 
            disabled=prev_disabled,
            key=f"{key_prefix}_prev_button",
            use_container_width=True
        )
    
    with col2:
        page_info_text = st.markdown(
            f"<div style='text-align: center;'>Page {current_page} of {total_pages} "
            f"({total_records} items)</div>", 
            unsafe_allow_html=True
        )
    
    with col3:
        next_disabled = current_page >= total_pages
        next_button = st.button(
            "Next →", 
            disabled=next_disabled,
            key=f"{key_prefix}_next_button",
            use_container_width=True
        )
    
    return prev_button, next_button, total_pages, page_info_text

def initialize_pagination_state(key_prefix):
    """
    Initialize or reset pagination state variables
    
    Args:
        key_prefix (str): Prefix for session state keys to make them unique
    """
    page_key = f"{key_prefix}_page"
    per_page_key = f"{key_prefix}_per_page"
    search_key = f"{key_prefix}_search"
    
    if page_key not in st.session_state:
        st.session_state[page_key] = 1
    
    if per_page_key not in st.session_state:
        st.session_state[per_page_key] = 10
        
    if search_key not in st.session_state:
        st.session_state[search_key] = ""
    
def create_search_filter_ui(key_prefix, filters=None):
    """
    Create a consistent search and filter UI for Streamlit pages
    
    Args:
        key_prefix (str): Prefix for session state keys to make them unique
        filters (dict, optional): Dictionary of filter options {filter_name: options_list}
    
    Returns:
        tuple: (search_term, filter_values)
    """
    search_key = f"{key_prefix}_search"
    per_page_key = f"{key_prefix}_per_page"
    filter_values = {}
    
    # Create search UI
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search_term = st.text_input(
            "Search", 
            value=st.session_state.get(search_key, ""),
            key=search_key,
            placeholder="Search..."
        )
    
    with col2:
        per_page = st.selectbox(
            "Items per page",
            options=[10, 20, 50, 100],
            index=0 if per_page_key not in st.session_state else [10, 20, 50, 100].index(st.session_state[per_page_key]),
            key=per_page_key
        )
    
    # Add filters if provided
    if filters:
        st.markdown("**Filters**")
        filter_cols = st.columns(min(len(filters), 4))  # Maximum 4 filters in a row
        
        for i, (filter_name, options) in enumerate(filters.items()):
            filter_key = f"{key_prefix}_{filter_name}_filter"
            
            # Initialize filter in session state if not present
            if filter_key not in st.session_state:
                st.session_state[filter_key] = None
            
            with filter_cols[i % min(len(filters), 4)]:
                filter_values[filter_name] = st.selectbox(
                    filter_name.replace('_', ' ').title(),
                    options=["All"] + options,
                    index=0 if st.session_state[filter_key] is None else options.index(st.session_state[filter_key]) + 1,
                    key=filter_key
                )
                
                # Convert "All" to None for backend filtering
                if filter_values[filter_name] == "All":
                    filter_values[filter_name] = None
    
    return search_term, filter_values