import streamlit as st
from demo_seed_policy import sample_seed_permitted
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from onboarding import show_onboarding
from product_catalog import show_product_catalog
from product_detail import show_product_detail
from order_booking import show_order_booking
from order_confirmation import show_order_confirmation
from merchandiser_agent import show_merchandiser_agent
from retailer_analysis import show_retailer_analysis

# Import manufacturing portal modules
from manufacturing_dashboard import show_manufacturing_dashboard
from order_style_management import show_order_style_management
from material_tracker import show_material_tracker
from production_timeline import show_production_timeline
from line_plan import show_line_plan
from reports import show_reports
from init_db import show_db_initialization, initialize_database

# Import visualization modules
from supply_chain_visualization import show_supply_chain_visualization
from synergy_visualization import show_synergy_visualization
from voi_jeans_demo import show_voi_jeans_demo
from market_price_intelligence import show_market_price_intelligence
from synergy_hub import show_synergy_hub, show_voice_over_demo
from inventory_export import show_inventory_export

# Configure the page
st.set_page_config(
    page_title="Synergy Hub Demo",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.warning("DEMONSTRATION — this interface does not authenticate users or validate live licences. Connect only a disposable SQLite demonstration database; it is not approved for production business data.")

# Synthetic sample data is opt-in and restricted to explicitly configured SQLite demos.
# Ordinary app startup never seeds, overwrites, resets, or migrates a business database.
if 'db_initialized' not in st.session_state:
    st.session_state.db_initialized = False
    if sample_seed_permitted():
        inserted = initialize_database()
        st.session_state.db_initialized = True
        if inserted:
            st.caption("Synthetic demonstration records were inserted into the explicitly configured SQLite demo database.")
        else:
            st.caption("Existing SQLite demonstration records detected; no new sample records inserted.")

# Initialize session state for app flow
if 'page' not in st.session_state:
    st.session_state.page = 'synergy_hub'  # Start with the SynergyHub as the landing page

if 'completed_onboarding' not in st.session_state:
    st.session_state.completed_onboarding = True  # Skip onboarding for testing

if 'selected_product' not in st.session_state:
    st.session_state.selected_product = None

if 'cart' not in st.session_state:
    st.session_state.cart = []

if 'order_submitted' not in st.session_state:
    st.session_state.order_submitted = False

# Sidebar navigation
with st.sidebar:
    st.title("Synergy Hub Demo")
    
    # Demo button with a prominent style
    st.markdown(
        """
        <div style='background-color: #1E3A8A; padding: 10px; border-radius: 5px; text-align: center; margin-bottom: 15px;'>
            <p style='margin: 0; font-weight: bold; color: white;'>✨ FEATURED DEMO</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    if st.button("🔄 SYNERGY HUB DEMO", use_container_width=True, type="primary"):
        st.session_state.page = 'voi_jeans_demo'
    
    st.markdown("---")
    
    # Add Management Hub as a prominent button before tabs
    st.markdown(
        """
        <div style='background-color: #e63946; padding: 10px; border-radius: 5px; text-align: center; margin-bottom: 15px; cursor: pointer;'>
            <p style='margin: 0; font-weight: bold; color: white;'>🔮 GOVERNANCE PORTAL</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    if st.button("🔮 ENTER GOVERNANCE PORTAL", use_container_width=True, type="primary", key="enter_management_hub"):
        st.session_state.page = 'voi_jeans_demo'
        
    # Create tabs for main navigation sections
    tab1, tab2 = st.tabs(["🏭 Manufacturing (Scotts)", "🏬 Retail Distribution"])
    
    with tab1:
        # Manufacturing Portal Navigation
        st.markdown("### Manufacturing (Scotts Garments - CMP)")
        
        # Procurement System section
        st.markdown("#### Denim Procurement")
        if st.button("👖 SS25 Denim Styles", use_container_width=True, key="material_tracker"):
            st.session_state.page = 'material_tracker'
            
        if st.button("🏭 Scotts Garments Management", use_container_width=True, key="order_style_mgmt"):
            st.session_state.page = 'order_style_management'
            
        if st.button("💰 CMP Cost Calculation", use_container_width=True, key="reports"):
            st.session_state.page = 'reports'
            
        if st.button("📝 Production Order Placement", use_container_width=True, key="order_placement"):
            st.session_state.page = 'order_style_management'
            
        if st.button("📦 Denim Fabric Tracking", use_container_width=True, key="material_tracking"):
            st.session_state.page = 'material_tracker'
            
        # Manufacturing Management section
        st.markdown("#### Manufacturing Management")
        if st.button("📋 Production Planning", use_container_width=True, key="line_plan"):
            st.session_state.page = 'line_plan'
            
        if st.button("📅 Production Scheduling", use_container_width=True, key="production_timeline"):
            st.session_state.page = 'production_timeline'
            
        if st.button("⚙️ Quality Control Tracking", use_container_width=True, key="quality_control"):
            st.session_state.page = 'production_timeline'
            
        if st.button("📊 Capacity Management", use_container_width=True, key="capacity_mgmt"):
            st.session_state.page = 'manufacturing_dashboard'
            
        if st.button("📈 Production Reporting", use_container_width=True, key="prod_reporting"):
            st.session_state.page = 'reports'
            
        # Fabric and Vendor Synchronization section
        st.markdown("#### Fabric and Vendor Synchronization")
        if st.button("📚 Material Library", use_container_width=True, key="material_library"):
            st.session_state.page = 'material_tracker'
            
        if st.button("📊 Vendor Capability Matrix", use_container_width=True, key="vendor_capability"):
            st.session_state.page = 'reports'
            
        if st.button("🔄 Material-vendor Matching", use_container_width=True, key="material_vendor_matching"):
            st.session_state.page = 'order_style_management'
            
        if st.button("📈 Performance Tracking", use_container_width=True, key="vendor_performance"):
            st.session_state.page = 'manufacturing_dashboard'
            
        # Factory Operations Dashboard section
        st.markdown("#### Factory Operations Dashboard")
        if st.button("👚 Factory Merchandiser View", use_container_width=True, key="factory_merchandiser"):
            st.session_state.page = 'merchandiser_agent'
            
        if st.button("⏱ Production Tracking Timeline", use_container_width=True, key="prod_tracking_timeline"):
            st.session_state.page = 'production_timeline'
            
        if st.button("🚚 Delivery Scheduling", use_container_width=True, key="delivery_scheduling"):
            st.session_state.page = 'line_plan'
            
        if st.button("📋 Compliance Tracking", use_container_width=True, key="compliance_tracking"):
            st.session_state.page = 'reports'
            
        if st.button("🔄 Supply Chain Visualization", use_container_width=True, key="supply_chain_viz"):
            st.session_state.page = 'supply_chain_visualization'
            
        # HSN-Based Forecasting section
        st.markdown("#### HSN-Based Forecasting")
        if st.button("📡 Demand Signal Integration", use_container_width=True, key="demand_signal"):
            st.session_state.page = 'manufacturing_dashboard'
            
        if st.button("📊 Supply Requirement Projections", use_container_width=True, key="supply_projections"):
            st.session_state.page = 'reports'
            
        if st.button("⏳ Timeline Forecasting", use_container_width=True, key="timeline_forecasting"):
            st.session_state.page = 'line_plan'
            
        if st.button("📉 Raw Material Demand Prediction", use_container_width=True, key="raw_material_prediction"):
            st.session_state.page = 'material_tracker'
            
        # NEW! Inventory Export Feature
        st.markdown("""
        <div style='background-color: #4CAF50; padding: 5px; border-radius: 5px; text-align: center; margin: 10px 0;'>
            <p style='margin: 0; color: white; font-size: 0.8em;'>✨ NEW FEATURE</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🖼️ Export Inventory to PowerPoint", use_container_width=True, key="inventory_export_mfg", type="primary"):
            st.session_state.page = 'inventory_export'
        
        # Database initialization (hidden in an expander to not clutter the UI)
        with st.expander("⚙️ Database Management"):
            if st.button("Database Setup", use_container_width=True, key="db_init"):
                st.session_state.page = 'db_initialization'
    
    with tab2:
        # Commune Connect Portal Navigation
        st.markdown("### Voi Jeans Retail Distribution")
        
        # Store Management
        st.markdown("#### Store Management")
        if st.button("🏬 Retail Store Network", use_container_width=True, key="browse_products"):
            st.session_state.page = 'product_catalog'
        
        if st.button("📊 Daily Sales vs Target", use_container_width=True, key="daily_sales"):
            st.session_state.page = 'retailer_analysis'
        
        if st.button("🔖 E-Wards Loyalty Program", use_container_width=True, key="loyalty_program"):
            st.session_state.page = 'product_detail'
        
        if st.button("📦 Store Inventory Management", use_container_width=True, key="view_order"):
            st.session_state.page = 'order_booking'
        
        # Product Management
        st.markdown("#### Product Management")
        
        if st.button("👖 Denim Collection", use_container_width=True, key="denim_collection"):
            st.session_state.page = 'product_catalog'
            
        if st.button("🎯 SS25 Collection Planning", use_container_width=True, key="ss25_planning"):
            st.session_state.page = 'order_style_management'
            
        if st.button("🔍 Style Performance Analysis", use_container_width=True, key="style_performance"):
            st.session_state.page = 'retailer_analysis'
        
        # Market Intelligence Section
        st.markdown("#### Retail Analytics")
        
        if st.button("📈 Sales Performance Dashboard", use_container_width=True, key="market_health"):
            st.session_state.page = 'retailer_analysis'
        
        if st.button("📱 Online vs In-Store Analysis", use_container_width=True, key="online_vs_store"):
            st.session_state.page = 'manufacturing_dashboard'
            
        if st.button("🏙️ Regional Market Insights", use_container_width=True, key="regional_insights"):
            st.session_state.page = 'reports'
            
        # NEW! Inventory Export Feature
        st.markdown("""
        <div style='background-color: #4CAF50; padding: 5px; border-radius: 5px; text-align: center; margin: 10px 0;'>
            <p style='margin: 0; color: white; font-size: 0.8em;'>✨ NEW FEATURE</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🖼️ Export Inventory to PowerPoint", use_container_width=True, key="inventory_export", type="primary"):
            st.session_state.page = 'inventory_export'
        
        # Add a hint about the retail analytics
        st.info("Access real-time sales analytics and performance metrics across all Voi Jeans retail locations.")
        
        # Add access to the merchandiser agent
        st.markdown("### Your Support Team")
        
        # Merchandiser button with notification badge style
        if st.button("👩‍💼 Your Merchandiser Agent", use_container_width=True, key="merchandiser"):
            st.session_state.page = 'merchandiser_agent'
        
        # Show a hint about the merchandiser
        if 'merchandiser' in st.session_state and isinstance(st.session_state.merchandiser, dict):
            # Display merchandiser info if already assigned and valid
            st.markdown(f"""
            <div style='background-color: #1E3A8A; padding: 10px; border-radius: 5px; margin-top: 10px;'>
                <p style='margin: 0; font-size: 0.9em;'>You're working with:</p>
                <p style='margin: 0; font-weight: bold;'>{st.session_state.merchandiser.get('name', 'Your Merchandiser')}</p>
                <p style='margin: 0; font-size: 0.8em;'>{st.session_state.merchandiser.get('specialization', 'Denim Expert')}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Show a teaser about having a merchandiser
            st.info("Connect with your dedicated merchandising agent for personalized support throughout your order process.")
    
    # Management Hub section moved to main button above
    
    # Additional resources
    st.markdown("### Resources")
    resources_expander = st.expander("Helpful Resources")
    with resources_expander:
        st.markdown("- [Fabric Guide]()")
        st.markdown("- [Size Charts]()")
        st.markdown("- [Customization Options]()")
        st.markdown("- [Production Process]()")
        st.markdown("- [Manufacturing Handbook]()")
                
    # Reset button at the bottom
    st.markdown("---")
    if st.button("🔄 Reset Application", use_container_width=True):
        st.session_state.page = 'onboarding'
        st.session_state.completed_onboarding = False
        st.session_state.selected_product = None
        st.session_state.cart = []
        st.session_state.order_submitted = False
        # Also reset merchandiser
        if 'merchandiser' in st.session_state:
            del st.session_state.merchandiser
        if 'conversation' in st.session_state:
            del st.session_state.conversation
        st.rerun()

# Database-backed demo pages remain unavailable unless the explicit SQLite
# sample-data foundation is enabled. This prevents failed queries on a missing
# schema as well as unapproved access to data through those routes.
DATABASE_BACKED_DEMO_PAGES = frozenset({
    'manufacturing_dashboard', 'order_style_management', 'material_tracker',
    'production_timeline', 'line_plan', 'reports', 'db_initialization',
    'supply_chain_visualization', 'inventory_export',
})
if st.session_state.page in DATABASE_BACKED_DEMO_PAGES and not sample_seed_permitted():
    st.warning(
        "This database-backed demonstration area is unavailable. "
        "It requires an explicitly configured disposable SQLite demo. "
        "No live database connection or production access is offered."
    )
elif st.session_state.page == 'onboarding':
    show_onboarding()
elif st.session_state.page == 'product_catalog':
    show_product_catalog()
elif st.session_state.page == 'product_detail':
    show_product_detail()
elif st.session_state.page == 'order_booking':
    show_order_booking()
elif st.session_state.page == 'order_confirmation':
    show_order_confirmation()
elif st.session_state.page == 'merchandiser_agent':
    show_merchandiser_agent()
elif st.session_state.page == 'retailer_analysis':
    show_retailer_analysis()
# Manufacturing portal pages
elif st.session_state.page == 'manufacturing_dashboard':
    show_manufacturing_dashboard()
elif st.session_state.page == 'order_style_management':
    show_order_style_management()
elif st.session_state.page == 'material_tracker':
    show_material_tracker()
elif st.session_state.page == 'production_timeline':
    show_production_timeline()
elif st.session_state.page == 'line_plan':
    show_line_plan()
elif st.session_state.page == 'reports':
    show_reports()
elif st.session_state.page == 'db_initialization':
    show_db_initialization()
elif st.session_state.page == 'supply_chain_visualization':
    show_supply_chain_visualization()
elif st.session_state.page == 'synergy_visualization':
    show_synergy_visualization()
elif st.session_state.page == 'voi_jeans_demo':
    if (st.session_state.get('demo_mode') is True
            and st.session_state.get('demo_company')
            and st.session_state.get('demo_role')):
        sample_company = st.session_state['demo_company']
        sample_role = st.session_state['demo_role']
        st.caption(
            f"Demonstration selection: {sample_company} / {sample_role}. "
            "The screens below are static VOI examples, NOT records or rights "
            "of the selected organization."
        )
    show_voi_jeans_demo()
elif st.session_state.page == 'market_price_intelligence':
    show_market_price_intelligence()
elif st.session_state.page == 'synergy_hub':
    show_synergy_hub()
elif st.session_state.page == 'voice_over_demo':
    show_voice_over_demo()
elif st.session_state.page == 'inventory_export':
    show_inventory_export()

# Footer
st.markdown("---")
st.markdown("""
<div style='display: flex; justify-content: space-between; align-items: center;'>
    <div style='text-align: left;'>
        <p style='margin: 0; font-size: 0.8em;'>© Synergy Hub™ Platform</p>
        <p style='margin: 0; font-size: 0.7em;'>Powering Woven Supply™ and Commune Connect™</p>
    </div>
    <div style='text-align: right;'>
        <p style='margin: 0; font-size: 0.8em;'>Historical demonstration participant: VOI Jeans Retail India Pvt Ltd</p>
        <p style='margin: 0; font-size: 0.7em;'>Historical licence reference: April 2026; current entitlement NOT verified</p>
    </div>
</div>
""", unsafe_allow_html=True)
