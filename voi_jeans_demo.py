import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import networkx as nx
import random
from PIL import Image
import io
import base64

def show_voi_jeans_demo():
    """Display a demo focused on Voi Jeans and their departmental structure"""
    
    st.title("🧥 Voi Jeans Organization & Synergyze Implementation")
    
    # Create tabs for different views
    tab1, tab2, tab3 = st.tabs(["🏢 Organizational Structure", "🔄 Department Workflows", "📊 Integration Demo"])
    
    with tab1:
        show_org_structure()
    
    with tab2:
        show_department_workflows()
    
    with tab3:
        show_integration_demo()

def show_org_structure():
    """Show Voi Jeans organizational structure and how it maps to Synergyze"""
    
    st.subheader("Voi Jeans Organizational Structure")
    
    st.markdown("""
    Voi Jeans Retail India Pvt Ltd operates with a unique organizational structure that leverages 
    Scotts Garments as their CMP (Cut, Make, Pack) manufacturing partner. The Synergyze platform 
    connects these entities through specialized modules for each department.
    """)
    
    # Organization chart using Plotly
    org_chart_data = {
        'id': [
            'CEO', 
            'Head of Design', 'Head of Manufacturing', 'Head of Retail', 'Head of Finance', 'Head of Marketing',
            'Design Team', 'Product Development', 'QA Team',
            'Scotts Garments', 'Production Planning', 'Material Procurement',
            'Store Operations', 'E-commerce', 'Inventory Management',
            'Financial Planning', 'Accounts', 'Audit',
            'Digital Marketing', 'Brand Management', 'Customer Relations'
        ],
        'parent': [
            '',
            'CEO', 'CEO', 'CEO', 'CEO', 'CEO',
            'Head of Design', 'Head of Design', 'Head of Design',
            'Head of Manufacturing', 'Head of Manufacturing', 'Head of Manufacturing',
            'Head of Retail', 'Head of Retail', 'Head of Retail',
            'Head of Finance', 'Head of Finance', 'Head of Finance',
            'Head of Marketing', 'Head of Marketing', 'Head of Marketing'
        ],
        'value': [50, 10, 10, 10, 10, 10, 3, 3, 4, 3, 3, 4, 3, 3, 4, 3, 3, 4, 3, 3, 4],
        'label': [
            'CEO', 
            'Head of Design', 'Head of Manufacturing', 'Head of Retail', 'Head of Finance', 'Head of Marketing',
            'Design Team', 'Product Development', 'QA Team',
            'Scotts Garments', 'Production Planning', 'Material Procurement',
            'Store Operations', 'E-commerce', 'Inventory Management',
            'Financial Planning', 'Accounts', 'Audit',
            'Digital Marketing', 'Brand Management', 'Customer Relations'
        ],
        'module': [
            'Synergyze Hub',
            'Woven Supply', 'Woven Supply', 'Commune Connect', 'Synergyze Hub', 'Commune Connect',
            'Woven Supply', 'Woven Supply', 'Woven Supply',
            'Woven Supply', 'Woven Supply', 'Woven Supply',
            'Commune Connect', 'Commune Connect', 'Commune Connect',
            'Synergyze Hub', 'Synergyze Hub', 'Synergyze Hub',
            'Commune Connect', 'Commune Connect', 'Commune Connect'
        ]
    }
    
    # Create a color map
    color_map = {
        'Woven Supply': 'royalblue',
        'Commune Connect': 'mediumseagreen',
        'Synergyze Hub': 'darkorchid'
    }
    
    # Map colors
    colors = [color_map[module] for module in org_chart_data['module']]
    
    # Create sunburst chart
    fig = px.sunburst(
        org_chart_data,
        ids='id',
        parents='parent',
        values='value',
        names='label',
        color='module',
        color_discrete_map=color_map,
        title="Voi Jeans Organization Structure with Synergyze Module Mapping",
        height=700
    )
    
    fig.update_layout(margin=dict(t=60, l=25, r=25, b=25))
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Department breakdown with Synergyze mapping
    st.subheader("Department Breakdown with Synergyze Module Mapping")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🏭 Woven Supply Departments
        **Manufacturing Side**
        
        - **Design Team**  
          *SS25 collection design, tech packs*
        
        - **Product Development**  
          *Prototyping, material testing*
        
        - **QA Team**  
          *Quality standards, inspections*
        
        - **Scotts Garments**  
          *CMP manufacturing partner*
        
        - **Production Planning**  
          *Scheduling, capacity management*
        
        - **Material Procurement**  
          *Sourcing, vendor management*
        """)
    
    with col2:
        st.markdown("""
        ### 🏬 Commune Connect Departments
        **Retail Side**
        
        - **Store Operations**  
          *20 retail stores management*
        
        - **E-commerce**  
          *Online store, digital sales*
        
        - **Inventory Management**  
          *Stock allocation, replenishment*
        
        - **Digital Marketing**  
          *Social media, SEO, SEM*
        
        - **Brand Management**  
          *Brand identity, campaigns*
        
        - **Customer Relations**  
          *Loyalty program, service*
        """)
    
    with col3:
        st.markdown("""
        ### ⚙️ Synergyze Hub Departments
        **Governance Layer**
        
        - **CEO Office**  
          *Executive dashboard, strategic KPIs*
        
        - **Financial Planning**  
          *Budgeting, forecasting*
        
        - **Accounts**  
          *Payments, receivables*
        
        - **Audit**  
          *Compliance, reporting*
        
        - **IT Services**  
          *System maintenance, security*
        
        - **HR Department**  
          *Recruitment, training, payroll*
        """)

def show_department_workflows():
    """Show department workflows with interactive elements"""
    
    st.subheader("Voi Jeans Department Workflows")
    
    st.markdown("""
    Each department at Voi Jeans follows specific workflows optimized by the Synergyze platform.
    Below are the key workflows for major departments, highlighting how information and processes flow.
    """)
    
    # Create expandable sections for each department's workflow
    
    with st.expander("🧵 Design to Manufacturing Workflow", expanded=True):
        st.markdown("""
        ### Design to Manufacturing Process
        
        1. **Design Conceptualization** (Design Team)
           - Trend research and market analysis
           - Creation of mood boards and design concepts
           - Synergyze Integration: Real-time trend data and historical performance metrics
        
        2. **Sample Development** (Product Development)
           - Creation of prototypes and samples
           - Material selection and testing
           - Synergyze Integration: Digital tech pack creation and version control
        
        3. **Tech Pack Generation** (Design Team)
           - Detailed specifications for production
           - Size charts and grading
           - Synergyze Integration: Automated spec sheet generation with production requirements
        
        4. **Production Order Creation** (Production Planning)
           - Style-wise order creation with quantities
           - Timeline establishment
           - Synergyze Integration: Capacity planning and automatic timeline suggestions
        
        5. **Manufacturing at Scotts Garments** (CMP Partner)
           - Cutting, Making, Packing operations
           - Quality checks and approvals
           - Synergyze Integration: Real-time production tracking and quality reporting
        
        6. **Final QA and Dispatch** (QA Team)
           - Final quality inspection
           - Packaging verification
           - Synergyze Integration: Automated quality reports with defect tracking
        """)
        
        # Create a basic workflow diagram
        nodes = ["Design", "Product Development", "Tech Pack", "Production Order", "Manufacturing", "QA & Dispatch"]
        edges = [(0,1), (1,2), (2,3), (3,4), (4,5)]
        
        G = nx.DiGraph()
        for i, node in enumerate(nodes):
            G.add_node(i, name=node)
        G.add_edges_from(edges)
        
        pos = {i: (i, 0) for i in range(len(nodes))}
        
        # Create edge trace
        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
        
        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=2, color='#888'),
            hoverinfo='none',
            mode='lines')
        
        # Create node trace
        node_x = []
        node_y = []
        node_text = []
        
        for node, attr in G.nodes(data=True):
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            node_text.append(attr['name'])
        
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            text=node_text,
            textposition="top center",
            marker=dict(
                size=30,
                color='royalblue',
                line=dict(width=2, color='DarkSlateGrey')),
        )
        
        # Create figure
        fig = go.Figure(data=[edge_trace, node_trace],
                     layout=go.Layout(
                        title="Design to Manufacturing Workflow",
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20,l=5,r=5,t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        height=300,
                        plot_bgcolor='rgba(248,248,248,1)'
                    ))
        
        st.plotly_chart(fig, use_container_width=True)
    
    with st.expander("🏬 Retail Distribution Workflow"):
        st.markdown("""
        ### Retail Distribution Process
        
        1. **Inventory Planning** (Inventory Management)
           - Forecasting and demand planning
           - Store-wise allocation planning
           - Synergyze Integration: AI-driven sales forecasting by store and style
        
        2. **Warehouse Operations** (Inventory Management)
           - Receiving finished goods from Scotts Garments
           - Quality verification and storage
           - Synergyze Integration: Automated receiving and put-away tracking
        
        3. **Store Allocation** (Store Operations)
           - Style and size distribution to 20 stores
           - E-commerce stock allocation
           - Synergyze Integration: Algorithm-based allocation optimization by store performance
        
        4. **Store Merchandising** (Store Operations)
           - Visual merchandising guidelines
           - In-store product placement
           - Synergyze Integration: Planogram compliance tracking and best practices sharing
        
        5. **Sales Operations** (Store Operations)
           - Daily sales tracking vs targets
           - Promotion management
           - Synergyze Integration: Real-time sales dashboards and alerts
        
        6. **Replenishment** (Inventory Management)
           - Stock level monitoring
           - Inter-store transfers
           - Synergyze Integration: Automated replenishment suggestions and transfer orders
        """)
        
        # Create a basic workflow diagram for retail
        retail_nodes = ["Inventory Planning", "Warehouse", "Store Allocation", "Store Merchandising", "Sales", "Replenishment"]
        retail_edges = [(0,1), (1,2), (2,3), (3,4), (4,5), (5,1)]
        
        G_retail = nx.DiGraph()
        for i, node in enumerate(retail_nodes):
            G_retail.add_node(i, name=node)
        G_retail.add_edges_from(retail_edges)
        
        # Position nodes in a circle
        pos_retail = nx.circular_layout(G_retail)
        
        # Create edge trace
        edge_x = []
        edge_y = []
        for edge in G_retail.edges():
            x0, y0 = pos_retail[edge[0]]
            x1, y1 = pos_retail[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
        
        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=2, color='#888'),
            hoverinfo='none',
            mode='lines')
        
        # Create node trace
        node_x = []
        node_y = []
        node_text = []
        
        for node, attr in G_retail.nodes(data=True):
            x, y = pos_retail[node]
            node_x.append(x)
            node_y.append(y)
            node_text.append(attr['name'])
        
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            text=node_text,
            textposition="top center",
            marker=dict(
                size=30,
                color='mediumseagreen',
                line=dict(width=2, color='DarkSlateGrey')),
        )
        
        # Create figure
        fig = go.Figure(data=[edge_trace, node_trace],
                     layout=go.Layout(
                        title="Retail Distribution Workflow",
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20,l=5,r=5,t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        height=400,
                        plot_bgcolor='rgba(248,248,248,1)'
                    ))
        
        st.plotly_chart(fig, use_container_width=True)
    
    with st.expander("💰 Finance and Governance Workflow"):
        st.markdown("""
        ### Finance and Governance Process
        
        1. **Financial Planning** (Finance Department)
           - Budget creation and allocation
           - Capital expenditure planning
           - Synergyze Integration: Automated budget vs actual tracking
        
        2. **Procurement Management** (Finance Department)
           - Vendor payment processing
           - CMP cost management with Scotts Garments
           - Synergyze Integration: Vendor performance metrics and payment scheduling
        
        3. **Sales Reconciliation** (Finance Department)
           - Daily sales reconciliation
           - Store-wise performance analysis
           - Synergyze Integration: Automated sales reconciliation and exception flagging
        
        4. **Cost Analysis** (Finance Department)
           - Product costing and margin analysis
           - Profitability reporting
           - Synergyze Integration: Style-wise profitability dashboards with drill-down capability
        
        5. **Compliance Management** (Audit Team)
           - Statutory compliance tracking
           - Internal policy adherence
           - Synergyze Integration: Compliance calendar with automated alerts and documentation
        
        6. **Performance Reporting** (CEO Office)
           - Executive dashboards
           - KPI tracking
           - Synergyze Integration: Real-time performance metrics with predictive analytics
        """)
        
        # Create a hierarchical diagram for finance
        finance_data = {
            'id': [
                'Financial Governance', 
                'Planning', 'Operations', 'Reporting',
                'Budgeting', 'Forecasting',
                'Procurement', 'Payments', 'Reconciliation',
                'Performance', 'Compliance', 'Executive'
            ],
            'parent': [
                '', 
                'Financial Governance', 'Financial Governance', 'Financial Governance',
                'Planning', 'Planning',
                'Operations', 'Operations', 'Operations',
                'Reporting', 'Reporting', 'Reporting'
            ],
            'value': [50, 20, 20, 20, 10, 10, 7, 7, 6, 7, 7, 6]
        }
        
        # Create treemap
        fig = px.treemap(
            finance_data,
            ids='id',
            parents='parent',
            values='value',
            color_discrete_sequence=px.colors.qualitative.Plotly,
            title="Finance and Governance Structure"
        )
        
        fig.update_layout(
            margin=dict(t=50, l=25, r=25, b=25),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)

def show_integration_demo():
    """Show integration between departments and data flow"""
    
    st.subheader("Voi Jeans Integration Demonstration")
    
    st.markdown("""
    ### Cross-Departmental Integration via Synergyze
    
    The true power of the Synergyze platform is in how it connects all departments and external partners
    within the Voi Jeans ecosystem. This demonstration shows the data flow and integration points.
    """)
    
    # Create a network graph showing integration
    G = nx.DiGraph()
    
    # Define nodes with their groups
    nodes = [
        ("Design", 1), ("Production Planning", 1), ("Scotts Garments", 1), 
        ("Inventory Management", 2), ("Store Operations", 2), ("E-commerce", 2),
        ("Finance", 3), ("CEO Dashboard", 3), ("CRO Dashboard", 3), ("CIO Dashboard", 3), ("CFO Dashboard", 3)
    ]
    
    # Add nodes
    for name, group in nodes:
        G.add_node(name, group=group)
    
    # Define edges with weights
    edges = [
        ("Design", "Production Planning", 5),
        ("Production Planning", "Scotts Garments", 7),
        ("Scotts Garments", "Inventory Management", 6),
        ("Inventory Management", "Store Operations", 8),
        ("Inventory Management", "E-commerce", 5),
        ("Store Operations", "Finance", 4),
        ("E-commerce", "Finance", 4),
        ("Finance", "CEO Dashboard", 3),
        ("CEO Dashboard", "Design", 2),
        ("Store Operations", "Design", 3),
        ("E-commerce", "Design", 3),
        # CRO connections (Revenue focus)
        ("Store Operations", "CRO Dashboard", 4),
        ("E-commerce", "CRO Dashboard", 5),
        ("CRO Dashboard", "CEO Dashboard", 2),
        # CIO connections (Technology focus)
        ("E-commerce", "CIO Dashboard", 4),
        ("Inventory Management", "CIO Dashboard", 4),
        ("CIO Dashboard", "CEO Dashboard", 2),
        # CFO connections (Financial focus)
        ("Finance", "CFO Dashboard", 5),
        ("CFO Dashboard", "CEO Dashboard", 3)
    ]
    
    # Add edges
    for source, target, weight in edges:
        G.add_edge(source, target, weight=weight)
    
    # Create positions
    pos = nx.spring_layout(G, k=0.5, iterations=50, seed=42)
    
    # Create edge trace
    edge_x = []
    edge_y = []
    edge_text = []
    
    for edge in G.edges(data=True):
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        edge_text.append(f"Data flow: {edge[0]} to {edge[1]}")
    
    # Create different node traces for different groups
    node_traces = []
    colors = ['royalblue', 'mediumseagreen', 'darkorchid']
    groups = {}
    
    for name, group in nodes:
        if group not in groups:
            groups[group] = {
                'x': [],
                'y': [],
                'text': [],
                'color': colors[group-1]
            }
        x, y = pos[name]
        groups[group]['x'].append(x)
        groups[group]['y'].append(y)
        groups[group]['text'].append(name)
    
    # Create a trace for each group
    for group_id, group_data in groups.items():
        node_trace = go.Scatter(
            x=group_data['x'],
            y=group_data['y'],
            text=group_data['text'],
            mode='markers+text',
            textposition="top center",
            marker=dict(
                size=30,
                color=group_data['color'],
                line=dict(width=2, color='DarkSlateGrey')),
            name=f"Group {group_id}"
        )
        node_traces.append(node_trace)
    
    # Create edge trace
    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=2, color='#888'),
        hoverinfo='text',
        text=edge_text,
        mode='lines'
    )
    
    # Create figure with all traces
    fig = go.Figure(data=[edge_trace] + node_traces,
                 layout=go.Layout(
                    title="Voi Jeans Integration Map - Data Flow Between Departments",
                    showlegend=True,
                    legend=dict(
                        title="Department Groups",
                        x=0,
                        y=1,
                        traceorder="normal",
                        itemsizing="constant"
                    ),
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    height=600,
                    plot_bgcolor='rgba(248,248,248,1)'
                ))
    
    # Update node trace legends
    fig.data[1].name = "Woven Supply (Manufacturing)"
    fig.data[2].name = "Commune Connect (Retail)"
    fig.data[3].name = "Synergyze Hub (Governance)"
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Add ECG Governance Layer with company selection
    st.subheader("ECG Governance Layer - Executive Intelligence")
    
    # Create a selection interface for companies with improved UI
    st.markdown("### 🏢 Company Selection Interface")
    st.markdown("Select the company you want to analyze through the ECG Governance Layer:")
    
    # Company selection with performance scores and additional metadata
    company_data = {
        "Voi Jeans Retail India Pvt Ltd": {
            "score": 87, 
            "industry": "Retail Fashion", 
            "region": "South Asia",
            "stores": 20,
            "employees": 1250,
            "annual_revenue": "₹128.5 Cr",
            "growth": 12.4,
            "logo_emoji": "👖"
        },
        "Scotts Garments LLP": {
            "score": 82, 
            "industry": "Manufacturing", 
            "region": "South Asia",
            "factories": 3,
            "employees": 850,
            "annual_revenue": "₹93.2 Cr",
            "growth": 8.7,
            "logo_emoji": "🏭"
        },
        "Lifestyle International": {
            "score": 76, 
            "industry": "Department Store", 
            "region": "Pan India",
            "stores": 35,
            "employees": 4200,
            "annual_revenue": "₹876.3 Cr",
            "growth": 5.2,
            "logo_emoji": "🛍️"
        },
        "Reliance Trends": {
            "score": 84, 
            "industry": "Fashion Retail", 
            "region": "Pan India",
            "stores": 125,
            "employees": 9800,
            "annual_revenue": "₹1,245.8 Cr",
            "growth": 14.3,
            "logo_emoji": "👔"
        },
        "Shoppers Stop": {
            "score": 79, 
            "industry": "Department Store", 
            "region": "Pan India",
            "stores": 42,
            "employees": 5600,
            "annual_revenue": "₹954.7 Cr",
            "growth": 7.9,
            "logo_emoji": "🛒"
        }
    }
    
    # Create company selection cards for a more visual selection experience
    cols = st.columns(5)
    
    # Determine if we have a selected company already
    if 'selected_company' not in st.session_state:
        st.session_state.selected_company = "Voi Jeans Retail India Pvt Ltd"
    
    # Display company cards
    for i, (company_name, data) in enumerate(company_data.items()):
        with cols[i % 5]:
            selected = st.session_state.selected_company == company_name
            card_color = "#1E3A8A" if selected else "#F0F2F6"
            text_color = "white" if selected else "black"
            emoji = data["logo_emoji"]
            score = data["score"]
            
            st.markdown(f"""
            <div style="
                padding: 10px; 
                border-radius: 5px; 
                background-color: {card_color}; 
                color: {text_color}; 
                text-align: center;
                margin-bottom: 10px;
                cursor: pointer;
                height: 120px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                border: 2px solid {'#0D1B43' if selected else '#E5E7EB'};
                " 
                onclick="alert('Clicked {company_name}')">
                <div style="font-size: 24px;">{emoji}</div>
                <div style="font-weight: bold; margin-top: 5px;">{company_name.split(' ')[0]}</div>
                <div style="margin-top: 5px;">Score: {score}/100</div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Select {company_name.split(' ')[0]}", key=f"btn_{company_name}"):
                st.session_state.selected_company = company_name
                st.rerun()
    
    # Use the selected company
    selected_company = st.session_state.selected_company
    
    # Display full company selection dropdown for alternative selection method
    st.selectbox(
        "Or select company from dropdown:", 
        list(company_data.keys()),
        index=list(company_data.keys()).index(selected_company),
        key="company_dropdown",
        on_change=lambda: setattr(st.session_state, 'selected_company', st.session_state.company_dropdown)
    )
    
    # Initialize session state for the selected company if not present
    if 'selected_company_data' not in st.session_state:
        st.session_state.selected_company_data = company_data[selected_company]
    
    # Update session state when selection changes
    if st.session_state.get('selected_company_data', {}).get('company_name', '') != selected_company:
        st.session_state.selected_company_data = company_data[selected_company]
        st.session_state.selected_company_data['company_name'] = selected_company
    
    # Display company performance score and metrics
    company_score = company_data[selected_company]["score"]
    company_industry = company_data[selected_company]["industry"]
    company_region = company_data[selected_company]["region"]
    
    # Create metrics display
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("ECG Performance Score", f"{company_score}/100", 
                 delta=f"{company_score - 75}" if company_score > 75 else f"{company_score - 75}")
    with col2:
        st.metric("Industry", company_industry)
    with col3:
        st.metric("Region", company_region)
    
    # Generate recommended team based on company score
    st.markdown("### Recommended ECG Implementation Team")
    
    # Team mapping based on score ranges
    if company_score >= 85:
        team_level = "Premium"
        team_members = ["Senior Consultant (15+ yrs)", "Technical Architect", "Industry Expert", "Data Analyst", "Implementation Lead"]
        team_color = "success"
    elif company_score >= 80:
        team_level = "Advanced"
        team_members = ["Senior Consultant (10+ yrs)", "Technical Lead", "Industry Specialist", "Implementation Specialist"]
        team_color = "primary"
    elif company_score >= 75:
        team_level = "Standard"
        team_members = ["Consultant (5+ yrs)", "Technical Specialist", "Implementation Associate"]
        team_color = "warning"
    else:
        team_level = "Basic"
        team_members = ["Junior Consultant", "Technical Associate"]
        team_color = "danger"
    
    # Display the recommended team
    st.markdown(f"""
    <div style='background-color: {'#1E3A8A' if team_level == 'Premium' else '#2563EB' if team_level == 'Advanced' else '#F59E0B' if team_level == 'Standard' else '#EF4444'}; 
        padding: 10px; border-radius: 5px; color: white;'>
    <h4 style='margin-top: 0;'>{team_level} Implementation Team</h4>
    <p>Based on {selected_company}'s ECG Performance Score of {company_score}/100</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Show team members
    st.markdown("#### Team Composition:")
    for member in team_members:
        st.markdown(f"- {member}")
    
    # Add interactive clickable dashboards for C-suite executives
    st.subheader(f"C-Suite Executive Dashboards for {selected_company}")
    st.markdown("Click on any dashboard to view its specific metrics and KPIs:")
    
    # Create tabs for each executive dashboard
    executive_tabs = st.tabs(["CEO Dashboard", "CRO Dashboard", "CIO Dashboard", "CFO Dashboard"])
    
    with executive_tabs[0]:  # CEO Dashboard
        st.markdown("### 🏢 CEO Dashboard")
        st.markdown("""
        The CEO Dashboard provides a holistic view of the entire Voi Jeans operation, with a focus on:
        
        - **Company Performance**: Key financial and operational KPIs
        - **Strategic Initiatives**: Progress tracking on major organizational initiatives
        - **Market Position**: Competitive analysis and market share information
        - **Organizational Health**: Cross-departmental performance metrics
        
        *This dashboard aggregates insights from all other executive dashboards to provide a complete 
        overview of the business for strategic decision-making.*
        """)
        
        # Create a sample dashboard visualization for CEO
        kpi_cols = st.columns(4)
        with kpi_cols[0]:
            st.metric("Revenue YTD", "₹128.5 Cr", "+12.4%")
        with kpi_cols[1]:
            st.metric("EBITDA", "₹24.3 Cr", "+8.2%")
        with kpi_cols[2]:
            st.metric("Market Share", "16.8%", "+2.1%")
        with kpi_cols[3]:
            st.metric("Stores", "20", "+3")
            
        # Sample executive chart
        org_data = pd.DataFrame({
            'Department': ['Design', 'Manufacturing', 'Retail', 'Finance', 'Marketing'],
            'Performance': [92, 87, 95, 89, 91],
            'Target': [90, 85, 90, 90, 90]
        })
        
        fig = px.bar(org_data, x='Department', y=['Performance', 'Target'], 
                    title="Departmental Performance vs Target",
                    barmode='group', height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with executive_tabs[1]:  # CRO Dashboard
        st.markdown("### 💰 CRO Dashboard")
        st.markdown("""
        The Chief Revenue Officer Dashboard focuses on sales and revenue metrics:
        
        - **Revenue Streams**: Breakdown by channel (stores vs e-commerce)
        - **Sales Performance**: Trend analysis and forecasting
        - **Customer Acquisition**: New customer metrics and conversion rates
        - **Regional Performance**: Store-by-store comparison
        
        *This dashboard helps the CRO optimize revenue generation across all Voi Jeans channels.*
        """)
        
        # Create a sample dashboard visualization for CRO
        revenue_cols = st.columns(4)
        with revenue_cols[0]:
            st.metric("Retail Revenue", "₹98.2 Cr", "+10.2%")
        with revenue_cols[1]:
            st.metric("E-commerce Revenue", "₹30.3 Cr", "+18.7%")
        with revenue_cols[2]:
            st.metric("Customer Acquisition", "125K", "+22.4%")
        with revenue_cols[3]:
            st.metric("Avg. Order Value", "₹3,842", "+5.3%")
            
        # Sample revenue chart
        channels = ['In-store', 'Website', 'Marketplace', 'Social Commerce']
        values = [45, 25, 20, 10]
        fig = px.pie(values=values, names=channels, title="Revenue by Channel",
                     hole=0.4, color_discrete_sequence=px.colors.sequential.Plasma_r)
        st.plotly_chart(fig, use_container_width=True)
    
    with executive_tabs[2]:  # CIO Dashboard
        st.markdown("### 💻 CIO Dashboard")
        st.markdown("""
        The Chief Information Officer Dashboard focuses on technology and systems:
        
        - **System Performance**: Uptime and response times for key platforms
        - **Digital Transformation**: Progress on tech initiatives
        - **Data Security**: Security metrics and compliance status
        - **Technology ROI**: Investment tracking and impact assessment
        
        *This dashboard helps the CIO ensure that Voi Jeans' technology infrastructure 
        supports the business effectively and securely.*
        """)
        
        # Create a sample dashboard visualization for CIO
        tech_cols = st.columns(4)
        with tech_cols[0]:
            st.metric("Platform Uptime", "99.97%", "+0.03%")
        with tech_cols[1]:
            st.metric("API Calls/Day", "3.2M", "+15.4%")
        with tech_cols[2]:
            st.metric("Tech ROI", "342%", "+27%")
        with tech_cols[3]:
            st.metric("Security Score", "94/100", "+6")
            
        # Sample technology chart
        tech_data = pd.DataFrame({
            'System': ['Synergyze Platform', 'E-commerce', 'ERP', 'CRM', 'Mobile App'],
            'Response Time (ms)': [120, 230, 180, 150, 95]
        })
        fig = px.bar(tech_data, x='System', y='Response Time (ms)', 
                    title="System Performance - Response Times",
                    color='Response Time (ms)', height=400,
                    color_continuous_scale=px.colors.sequential.Viridis)
        st.plotly_chart(fig, use_container_width=True)
    
    with executive_tabs[3]:  # CFO Dashboard
        st.markdown("### 📊 CFO Dashboard")
        st.markdown("""
        The Chief Financial Officer Dashboard focuses on financial health:
        
        - **Financial Performance**: P&L, balance sheet, and cash flow metrics
        - **Cost Management**: Expense tracking and optimization
        - **Investment Analysis**: ROI on major investments
        - **Risk Management**: Financial risk assessment and mitigation
        
        *This dashboard helps the CFO maintain financial stability and drive growth 
        through strategic financial management.*
        """)
        
        # Create a sample dashboard visualization for CFO
        finance_cols = st.columns(4)
        with finance_cols[0]:
            st.metric("Gross Margin", "52.3%", "+3.1%")
        with finance_cols[1]:
            st.metric("Cash Balance", "₹32.7 Cr", "+18.4%")
        with finance_cols[2]:
            st.metric("Op. Expenses", "₹21.4 Cr", "-2.7%")
        with finance_cols[3]:
            st.metric("Working Capital", "₹47.2 Cr", "+7.8%")
            
        # Sample finance chart
        categories = ['Cost of Goods', 'Store Operations', 'Marketing', 'Technology', 'Admin', 'Other']
        values = [48, 20, 15, 8, 7, 2]
        expense_df = pd.DataFrame({'Category': categories, 'Percentage': values})
        fig = px.treemap(expense_df, path=['Category'], values='Percentage',
                 title="Expense Breakdown", height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Show key integration examples
    st.subheader("Key Integration Examples")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📊 Design to Sales Feedback Loop
        
        1. **Sales Performance Data** collected from all 20 Voi Jeans stores
        2. **Style-wise Analysis** processed through Synergyze Hub
        3. **Performance Insights** shared with Design team
        4. **Design Adjustments** made for future collections
        5. **Production Planning** updated based on sales trends
        
        *Synergyze enables real-time data flow from retail stores back to design, 
        creating a closed feedback loop that optimizes product development.*
        """)
    
    with col2:
        st.markdown("""
        ### 💼 Scotts Garments CMP Integration
        
        1. **Production Orders** sent to Scotts Garments via Synergyze
        2. **Material Procurement** tracked in shared platform
        3. **Production Progress** updated daily by factory team
        4. **Quality Metrics** reported in real-time
        5. **Shipping Information** integrated with Voi Jeans inventory
        
        *The CMP (Cut, Make, Pack) relationship with Scotts Garments is fully
        digitized through Synergyze, providing transparency and efficiency.*
        """)
    
    # Demo data flow visualization
    st.subheader("Real-time Data Flow Visualization")
    
    # Create sample data for demonstration
    dates = pd.date_range(start='2025-01-01', periods=90, freq='D')
    
    # Generate sample design approval data (increasing and then plateau)
    design_data = np.cumsum(np.random.normal(3, 1, size=90))
    design_data = np.clip(design_data, 0, 100)
    
    # Generate sample production data (follows design with delay)
    production_data = np.concatenate([np.zeros(10), design_data[:-10]])
    
    # Generate sample shipping data (follows production with delay)
    shipping_data = np.concatenate([np.zeros(20), production_data[:-20]])
    
    # Generate sample sales data (follows shipping with delay)
    sales_data = np.concatenate([np.zeros(30), shipping_data[:-30]])
    
    # Create DataFrame
    flow_data = pd.DataFrame({
        'Date': dates,
        'Design Approvals': design_data,
        'Production Completion': production_data,
        'Store Inventory': shipping_data,
        'Sales': sales_data
    })
    
    # Create line chart
    fig = px.line(
        flow_data, 
        x='Date', 
        y=['Design Approvals', 'Production Completion', 'Store Inventory', 'Sales'],
        title='SS25 Collection - Data Flow Timeline',
        labels={'value': 'Cumulative Units', 'variable': 'Process Stage'},
        height=500
    )
    
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Cumulative Units",
        legend_title="Process Stage",
        template="plotly_white"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("""
    This visualization demonstrates how Synergyze enables end-to-end visibility of the product lifecycle. 
    From design approval through production at Scotts Garments to inventory receipt at Voi Jeans stores 
    and finally to sales, all data is connected in a unified platform with appropriate time lags between stages.
    """)
    
    # Add Executive Suite License Deployment Network
    st.subheader("🔌 ECG Governance Network & License Deployment")
    
    st.markdown(f"""
    This interactive network shows how executive licenses are deployed across {selected_company}'s operations.
    Similar to ECG's license management process, executive dashboards are provided to key stakeholders with appropriate
    access permissions and data visibility based on their role.
    """)
    
    # Create role-license mapping
    role_licenses = {
        "CEO Dashboard": {
            "access_level": "Full Access", 
            "visibility": "All Divisions",
            "data_types": ["Strategic", "Financial", "Operational", "Market"],
            "connected_devices": ["Desktop", "Tablet", "Mobile", "Digital Display"]
        },
        "CRO Dashboard": {
            "access_level": "Department Access", 
            "visibility": "Revenue Divisions",
            "data_types": ["Sales", "Marketing", "Customer", "Product"],
            "connected_devices": ["Desktop", "Tablet", "Mobile"]
        },
        "CIO Dashboard": {
            "access_level": "Department Access", 
            "visibility": "Tech Divisions",
            "data_types": ["System", "Security", "Development", "Integration"],
            "connected_devices": ["Desktop", "Mobile", "Network Monitors"]
        },
        "CFO Dashboard": {
            "access_level": "Department Access", 
            "visibility": "Finance Divisions",
            "data_types": ["Financial", "Treasury", "Risk", "Compliance"],
            "connected_devices": ["Desktop", "Secure Tablet", "Financial Terminals"]
        }
    }
    
    # Create tabs to show Executive Network, License Details, Connected Devices, Company Owner View, and Empire View
    exec_tabs = st.tabs(["Executive Network", "Executive License Details", "Connected Devices", "🏢 Owner's View", "👑 Empire View"])
    
    with exec_tabs[0]:
        # Create a simple network visualization
        st.markdown("### Executive Dashboard Deployment Network")
        
        # Create a network graph showing executive dashboard relationships
        G = nx.DiGraph()
        
        # Add nodes for the company, executives, and systems
        G.add_node(selected_company, group=1, size=25)
        
        for role in role_licenses.keys():
            G.add_node(role, group=2, size=20)
        
        departments = ["Finance Department", "Technology Department", "Marketing Department", 
                     "Sales Department", "Operations Department", "HR Department"]
        
        for dept in departments:
            G.add_node(dept, group=3, size=15)
        
        # Add connections between company and dashboards
        for role in role_licenses.keys():
            G.add_edge(selected_company, role, weight=5)
        
        # Add connections between dashboards and departments
        G.add_edge("CEO Dashboard", "Finance Department", weight=3)
        G.add_edge("CEO Dashboard", "Technology Department", weight=3)
        G.add_edge("CEO Dashboard", "Marketing Department", weight=3)
        G.add_edge("CEO Dashboard", "Sales Department", weight=3)
        G.add_edge("CEO Dashboard", "Operations Department", weight=3)
        G.add_edge("CEO Dashboard", "HR Department", weight=3)
        
        G.add_edge("CRO Dashboard", "Marketing Department", weight=4)
        G.add_edge("CRO Dashboard", "Sales Department", weight=4)
        
        G.add_edge("CIO Dashboard", "Technology Department", weight=4)
        G.add_edge("CIO Dashboard", "Operations Department", weight=2)
        
        G.add_edge("CFO Dashboard", "Finance Department", weight=4)
        G.add_edge("CFO Dashboard", "Operations Department", weight=2)
        
        # Create position layout
        pos = nx.spring_layout(G, k=0.3, seed=42)
        
        # Prepare node traces by group
        node_traces = []
        colors = ['#1E3A8A', '#7C3AED', '#10B981']
        groups = {}
        
        # Collect nodes by group
        for node in G.nodes():
            group = G.nodes[node]['group']
            size = G.nodes[node]['size']
            if group not in groups:
                groups[group] = {
                    'x': [],
                    'y': [],
                    'text': [],
                    'size': [],
                    'color': colors[group-1]
                }
            x, y = pos[node]
            groups[group]['x'].append(x)
            groups[group]['y'].append(y)
            groups[group]['text'].append(node)
            groups[group]['size'].append(size)
        
        # Create a trace for each group
        for group_id, group_data in groups.items():
            node_trace = go.Scatter(
                x=group_data['x'],
                y=group_data['y'],
                text=group_data['text'],
                mode='markers+text',
                textposition="top center",
                marker=dict(
                    size=group_data['size'],
                    color=group_data['color'],
                    line=dict(width=2, color='DarkSlateGrey')),
                name=f"Group {group_id}"
            )
            node_traces.append(node_trace)
        
        # Create edge trace
        edge_x = []
        edge_y = []
        
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
        
        edge_trace = go.Scatter(
            x=edge_x,
            y=edge_y,
            line=dict(width=1.5, color='#888'),
            hoverinfo='none',
            mode='lines'
        )
        
        # Create figure
        fig = go.Figure(data=[edge_trace] + node_traces,
                     layout=go.Layout(
                        title=f"Executive Dashboard Deployment - {selected_company}",
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20,l=5,r=5,t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        height=500,
                        plot_bgcolor='rgba(248,248,248,1)'
                    ))
        
        # Update node trace legends
        fig.data[1].name = "Company"
        fig.data[2].name = "Executive Dashboards"
        fig.data[3].name = "Departments"
        
        st.plotly_chart(fig, use_container_width=True)
    
    with exec_tabs[1]:
        st.markdown("### Executive License Details")
        st.markdown(f"""
        Each executive dashboard is deployed with a specific license that determines access levels, 
        data visibility, and integration capabilities. Below are the license details for {selected_company}'s 
        executive team:
        """)
        
        # Create license details table
        license_data = {
            "Dashboard": list(role_licenses.keys()),
            "Access Level": [data["access_level"] for data in role_licenses.values()],
            "Visibility": [data["visibility"] for data in role_licenses.values()],
            "Primary Data Types": [", ".join(data["data_types"]) for data in role_licenses.values()]
        }
        
        license_df = pd.DataFrame(license_data)
        st.dataframe(license_df, use_container_width=True)
        
        # Add dynamic license activation UI
        st.markdown("### License Management")
        
        license_cols = st.columns(4)
        for i, role in enumerate(role_licenses.keys()):
            with license_cols[i]:
                st.markdown(f"**{role}**")
                st.toggle(f"Active License", value=True, key=f"license_{role}")
                st.selectbox(f"Renewal Period", ["Annual", "Bi-Annual", "Quarterly", "Monthly"], key=f"renewal_{role}")
    
    with exec_tabs[2]:
        st.markdown("### Connected Device Integration")
        st.markdown(f"""
        ECG's executive dashboards can be accessed through various connected devices, each providing 
        appropriate information based on the device type and executive role. This ensures that key metrics 
        are always accessible, regardless of location or device type.
        """)
        
        # Show device integration mapping
        device_cols = st.columns(4)
        
        for i, (role, data) in enumerate(role_licenses.items()):
            with device_cols[i]:
                st.markdown(f"**{role}**")
                st.markdown("##### Connected Devices:")
                for device in data["connected_devices"]:
                    device_icon = "💻" if device == "Desktop" else "📱" if device == "Mobile" else "📟" if device == "Network Monitors" else "💰" if device == "Financial Terminals" else "📋" if device == "Tablet" else "📱" if device == "Secure Tablet" else "📺" if device == "Digital Display" else "📟"
                    st.markdown(f"{device_icon} {device}")
                
                # Add device linking button
                st.button(f"Link New Device", key=f"link_device_{role}")
    
    with exec_tabs[3]:
        st.markdown("### 👑 Empire OS View (ECG Owner Access)")
        st.markdown("""
        This is the Emperor's View - exclusive to ECG's owner. This view provides complete governance oversight
        across all companies in the network, showing the entire empire from a single command center.
        """)
        
        # Add Empire access authentication with special message
        st.warning("⚠️ Restricted Access: Empire OS View is exclusively for ECG's owner")
        
        empire_auth_col1, empire_auth_col2 = st.columns([1, 3])
        with empire_auth_col1:
            st.image("https://i.imgur.com/wMAD9K3.png", width=150)
        with empire_auth_col2:
            st.markdown("### Empire OS Authentication")
            st.text_input("Emperor ID", value="ECG-EMPEROR-001", disabled=True)
            st.text_input("Authentication Token", type="password", value="••••••••••••••••")
            empire_login = st.button("Access Empire OS", key="empire_login")
        
        if empire_login or 'empire_view_active' in st.session_state:
            st.session_state.empire_view_active = True
            
            # Create Empire OS view with all company data
            st.success("Empire OS Access Granted - Welcome, Emperor")
            
            # Create master company stats display
            st.markdown("## Empire Overview - All Companies")
            
            # Calculate empire metrics
            total_companies = len(company_data)
            avg_score = sum(data["score"] for data in company_data.values()) / total_companies
            premium_companies = sum(1 for data in company_data.values() if data["score"] >= 85)
            advanced_companies = sum(1 for data in company_data.values() if 80 <= data["score"] < 85)
            standard_companies = sum(1 for data in company_data.values() if 75 <= data["score"] < 80)
            basic_companies = sum(1 for data in company_data.values() if data["score"] < 75)
            
            # Display empire KPIs
            empire_cols = st.columns(5)
            with empire_cols[0]:
                st.metric("Total Companies", f"{total_companies}")
            with empire_cols[1]:
                st.metric("Avg. Score", f"{avg_score:.1f}/100")
            with empire_cols[2]:
                st.metric("Premium Tier", f"{premium_companies}")
            with empire_cols[3]:
                st.metric("Advanced Tier", f"{advanced_companies}")
            with empire_cols[4]:
                st.metric("Standard Tier", f"{standard_companies}")
            
            # Create company comparison chart
            company_score_data = {
                "Company": list(company_data.keys()),
                "Score": [data["score"] for data in company_data.values()]
            }
            company_score_df = pd.DataFrame(company_score_data)
            
            fig = px.bar(
                company_score_df, 
                x="Company", 
                y="Score", 
                title="Empire View - Company Performance Comparison",
                color="Score",
                color_continuous_scale=["red", "orange", "green"],
                range_color=[70, 90],
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Create multi-company management interface
            st.markdown("## Empire Management - All Companies")
            st.markdown("Manage licenses, implementations, and governance across your entire empire.")
            
            # Company management table
            empire_mgmt_data = {
                "Company": list(company_data.keys()),
                "Industry": [data["industry"] for data in company_data.values()],
                "Score": [data["score"] for data in company_data.values()],
                "Implementation Tier": [
                    "Premium" if data["score"] >= 85 else 
                    "Advanced" if data["score"] >= 80 else 
                    "Standard" if data["score"] >= 75 else 
                    "Basic" for data in company_data.values()
                ],
                "Governance Status": ["Active" for _ in company_data]
            }
            empire_mgmt_df = pd.DataFrame(empire_mgmt_data)
            
            # Make grid editable and clickable for the emperor
            edited_df = st.data_editor(
                empire_mgmt_df,
                column_config={
                    "Company": st.column_config.TextColumn("Company", width="medium"),
                    "Industry": st.column_config.TextColumn("Industry", width="medium"),
                    "Score": st.column_config.NumberColumn("Score", format="%d/100", width="small"),
                    "Implementation Tier": st.column_config.SelectboxColumn(
                        "Implementation Tier",
                        options=["Premium", "Advanced", "Standard", "Basic"],
                        width="medium"
                    ),
                    "Governance Status": st.column_config.SelectboxColumn(
                        "Governance Status",
                        options=["Active", "Pending", "Paused", "Inactive"],
                        width="medium"
                    )
                },
                hide_index=True,
                use_container_width=True
            )
            
            # Add action buttons for emperor control
            emperor_action_cols = st.columns(3)
            with emperor_action_cols[0]:
                st.button("👑 Push Governance Updates", key="push_updates")
            with emperor_action_cols[1]:
                st.button("📊 Generate Empire Report", key="empire_report")
            with emperor_action_cols[2]:
                st.button("🔄 Synchronize All Companies", key="sync_companies")
            
            # Add consolidated cross-company visualization
            st.markdown("## Empire OS - Cross-Company Visualization")
            st.markdown("This view shows connections and data flow between all companies in your empire.")
            
            # Create company nodes for visualization
            G_empire = nx.DiGraph()
            
            # Add ECG owner node at center
            G_empire.add_node("ECG Emperor", group=0, size=35)
            
            # Add all companies as nodes
            for company_name in company_data.keys():
                G_empire.add_node(company_name, group=1, size=25)
                # Connect Emperor to each company
                G_empire.add_edge("ECG Emperor", company_name, weight=5)
            
            # Add executive dashboard nodes for each company
            for company_name in company_data.keys():
                for role in role_licenses.keys():
                    node_name = f"{company_name} - {role}"
                    G_empire.add_node(node_name, group=2, size=15)
                    # Connect company to its dashboards
                    G_empire.add_edge(company_name, node_name, weight=2)
            
            # Create position layout for empire network
            pos_empire = nx.spring_layout(G_empire, k=0.3, seed=42)
            
            # Prepare node traces by group
            empire_node_traces = []
            empire_colors = ['#FFD700', '#1E3A8A', '#7C3AED']  # Gold for Emperor, blue for companies, purple for dashboards
            empire_groups = {}
            
            # Collect nodes by group
            for node in G_empire.nodes():
                group = G_empire.nodes[node]['group']
                size = G_empire.nodes[node]['size']
                if group not in empire_groups:
                    empire_groups[group] = {
                        'x': [],
                        'y': [],
                        'text': [],
                        'size': [],
                        'color': empire_colors[group]
                    }
                x, y = pos_empire[node]
                empire_groups[group]['x'].append(x)
                empire_groups[group]['y'].append(y)
                empire_groups[group]['text'].append(node)
                empire_groups[group]['size'].append(size)
            
            # Create a trace for each group
            for group_id, group_data in empire_groups.items():
                node_trace = go.Scatter(
                    x=group_data['x'],
                    y=group_data['y'],
                    text=group_data['text'],
                    mode='markers+text',
                    textposition="top center",
                    marker=dict(
                        size=group_data['size'],
                        color=group_data['color'],
                        line=dict(width=2, color='DarkSlateGrey')),
                    name=["Emperor", "Companies", "Dashboards"][group_id]
                )
                empire_node_traces.append(node_trace)
            
            # Create edge trace
            empire_edge_x = []
            empire_edge_y = []
            
            for edge in G_empire.edges():
                x0, y0 = pos_empire[edge[0]]
                x1, y1 = pos_empire[edge[1]]
                empire_edge_x.extend([x0, x1, None])
                empire_edge_y.extend([y0, y1, None])
            
            empire_edge_trace = go.Scatter(
                x=empire_edge_x,
                y=empire_edge_y,
                line=dict(width=1.5, color='#888'),
                hoverinfo='none',
                mode='lines'
            )
            
            # Create figure
            empire_fig = go.Figure(data=[empire_edge_trace] + empire_node_traces,
                             layout=go.Layout(
                                title="Empire OS - Full Governance Network",
                                showlegend=True,
                                hovermode='closest',
                                margin=dict(b=20,l=5,r=5,t=40),
                                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                height=600,
                                plot_bgcolor='rgba(248,248,248,1)',
                                legend=dict(
                                    title="Network Components",
                                    x=0.01,
                                    y=0.99,
                                    bordercolor="Black",
                                    borderwidth=1
                                )
                            ))
            
            st.plotly_chart(empire_fig, use_container_width=True)
            
            # Add empire-wide command center
            st.markdown("## Empire Command Center")
            
            command_tabs = st.tabs(["License Deployment", "Team Assignment", "Performance Monitoring"])
            
            with command_tabs[0]:
                st.markdown("### Empire-wide License Deployment")
                st.markdown("Deploy, revoke, or modify licenses across all companies from a central command.")
                
                license_deployment_cols = st.columns(3)
                with license_deployment_cols[0]:
                    st.selectbox("Select Company", company_data.keys(), key="license_company")
                with license_deployment_cols[1]:
                    st.selectbox("Select Dashboard", role_licenses.keys(), key="license_dashboard")
                with license_deployment_cols[2]:
                    st.selectbox("License Action", ["Deploy", "Modify", "Revoke", "Renew"], key="license_action")
                
                st.button("Execute License Action", key="execute_license")
            
            with command_tabs[1]:
                st.markdown("### Empire-wide Team Assignment")
                st.markdown("Manage implementation teams across all companies from a central view.")
                
                team_cols = st.columns(2)
                with team_cols[0]:
                    team_company = st.selectbox("Select Company", company_data.keys(), key="team_company")
                    st.metric("Company Score", f"{company_data[team_company]['score']}/100")
                    
                    if company_data[team_company]['score'] >= 85:
                        team_type = "Premium"
                    elif company_data[team_company]['score'] >= 80:
                        team_type = "Advanced"
                    elif company_data[team_company]['score'] >= 75:
                        team_type = "Standard"
                    else:
                        team_type = "Basic"
                    
                    st.metric("Recommended Team", team_type)
                    
                with team_cols[1]:
                    st.markdown("**Team Members**")
                    if team_type == "Premium":
                        team = ["Senior Consultant (15+ yrs)", "Technical Architect", "Industry Expert", "Data Analyst", "Implementation Lead"]
                    elif team_type == "Advanced":
                        team = ["Senior Consultant (10+ yrs)", "Technical Lead", "Industry Specialist", "Implementation Specialist"]
                    elif team_type == "Standard":
                        team = ["Consultant (5+ yrs)", "Technical Specialist", "Implementation Associate"]
                    else:
                        team = ["Junior Consultant", "Technical Associate"]
                    
                    for member in team:
                        st.checkbox(member, value=True)
                    
                    st.button("Update Team Assignment", key="update_team")
            
            with command_tabs[2]:
                st.markdown("### Empire-wide Performance Monitoring")
                st.markdown("Monitor implementation performance across all companies.")
                
                # Create performance data
                performance_data = {
                    "Company": list(company_data.keys()),
                    "Implementation Progress": [random.randint(25, 100) for _ in company_data],
                    "User Adoption": [random.randint(30, 95) for _ in company_data],
                    "Data Quality": [random.randint(40, 98) for _ in company_data],
                    "Support Tickets": [random.randint(0, 15) for _ in company_data]
                }
                
                performance_df = pd.DataFrame(performance_data)
                
                # Create performance heatmap
                fig = px.imshow(
                    performance_df.iloc[:, 1:].values,
                    x=performance_df.columns[1:],
                    y=performance_df["Company"],
                    color_continuous_scale=["red", "yellow", "green"],
                    aspect="auto",
                    title="Empire Implementation Performance Heatmap"
                )
                
                st.plotly_chart(fig, use_container_width=True)
                st.button("Generate Detailed Performance Report", key="performance_report")
    
    # Add ECG AI Assistant
    st.subheader("🤖 ECG AI Implementation Assistant")
    
    # Create AI chat interface
    st.markdown("""
    Our AI-powered implementation assistant can provide contextual information about:
    - Company-specific implementation strategies
    - Dashboard explanations and insights
    - Best practices for your industry
    - Implementation team coordination
    - Connected device deployment
    - License activation and management
    
    Try asking a question related to the selected company or dashboards.
    """)
    
    # Create a chat interface
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = [
            {"role": "assistant", "content": f"Hello! I'm your ECG Implementation Assistant for {selected_company}. How can I help you today?"}
        ]
    
    # Display chat messages
    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    user_query = st.chat_input("Ask a question about the dashboards or implementation...")
    
    if user_query:
        # Add user message to chat history
        st.session_state.chat_messages.append({"role": "user", "content": user_query})
        
        # Display user message
        with st.chat_message("user"):
            st.write(user_query)
        
        # Generate response based on the query and selected company
        response = generate_ai_response(user_query, selected_company, company_data[selected_company], team_level)
        
        # Add assistant response to chat history
        st.session_state.chat_messages.append({"role": "assistant", "content": response})
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.write(response)

# Function to generate AI responses
def generate_ai_response(query, company_name, company_info, team_level):
    """Generate contextual AI responses based on the query and company information"""
    
    query = query.lower()
    
    # Company-specific responses
    if "implementation" in query or "process" in query or "timeline" in query:
        return f"""
        For {company_name} with a performance score of {company_info['score']}/100, we recommend our {team_level} implementation approach.
        
        The implementation process typically involves:
        1. Initial assessment and team assignment (1-2 weeks)
        2. System configuration and data integration (3-4 weeks)
        3. Dashboard customization for your C-suite executives (2 weeks)
        4. User training and onboarding (1 week)
        5. Post-implementation support (ongoing)
        
        Given your industry ({company_info['industry']}), we will focus on industry-specific KPIs and benchmarks.
        """
    
    elif "dashboard" in query or "ceo" in query or "cro" in query or "cio" in query or "cfo" in query:
        # Determine which dashboard the user is asking about
        if "ceo" in query:
            return f"""
            The CEO Dashboard for {company_name} provides a holistic view of the business with access to all divisions.
            
            Key features include:
            - Executive metrics showing overall company performance
            - Departmental performance comparisons and targets
            - Strategic initiative tracking with completion percentages
            - Market position analysis with competitive benchmarking
            
            This dashboard is typically used by the CEO and board members to make high-level strategic decisions.
            It aggregates data from all other executive dashboards for comprehensive oversight.
            
            The CEO can access this dashboard from multiple device types including desktop, tablet, mobile, and office displays.
            """
        elif "cro" in query:
            return f"""
            The CRO Dashboard for {company_name} focuses on revenue generation and sales performance.
            
            Key features include:
            - Channel breakdown showing performance across retail and e-commerce
            - Customer acquisition metrics and conversion rates
            - Sales forecasting with trend analysis
            - Regional performance comparisons
            
            This dashboard is optimized for the Chief Revenue Officer and sales leadership team.
            It helps identify growth opportunities and optimize the sales funnel.
            
            The dashboard has department-level access with visibility into revenue-generating divisions.
            It's accessible on desktop computers, tablets, and mobile devices for on-the-go decision making.
            """
        elif "cio" in query:
            return f"""
            The CIO Dashboard for {company_name} provides technology infrastructure and digital metrics.
            
            Key features include:
            - System performance monitoring with uptime and response times
            - Digital transformation initiative tracking
            - Security and compliance status across all systems
            - Technology ROI metrics and investment tracking
            
            This dashboard helps the Chief Information Officer ensure that technology investments
            are delivering value and systems are operating efficiently.
            
            The dashboard provides visibility into the technology stack with department-level access.
            It can be accessed from desktops, mobile devices, and network monitoring stations.
            """
        elif "cfo" in query:
            return f"""
            The CFO Dashboard for {company_name} delivers financial health and performance metrics.
            
            Key features include:
            - Real-time financial KPIs including gross margin and working capital
            - Expense breakdowns by category for cost management
            - Cash flow and balance sheet visualizations
            - Investment and ROI analysis tools
            
            This dashboard gives the Chief Financial Officer complete visibility into the company's
            financial position and helps identify optimization opportunities.
            
            The dashboard has department-level access with visibility into financial systems.
            It's accessible via secure desktop workstations, secure tablets, and financial terminals
            with enhanced security protocols.
            """
        else:
            return f"""
            The C-suite dashboards for {company_name} provide tailored insights based on your performance score of {company_info['score']}/100 and industry benchmarks.
            
            Each dashboard serves a specific purpose:
            - CEO Dashboard: Holistic business view with cross-functional KPIs
            - CRO Dashboard: Revenue optimization and sales channel performance
            - CIO Dashboard: Technology infrastructure and digital transformation tracking
            - CFO Dashboard: Financial health metrics and risk management indicators
            
            These are completely customizable to match your specific business goals and management style.
            Each dashboard has appropriate access controls and can be accessed through various devices.
            
            Which specific executive dashboard would you like to learn more about?
            """
    
    elif "network" in query or "deployment" in query or "integration" in query:
        return f"""
        The ECG Governance Network for {company_name} creates a centralized system where executive
        dashboards are deployed based on role-specific needs.
        
        The network architecture includes:
        - Central company hub with connections to all executive dashboards
        - Executive dashboards with role-appropriate connections to departments
        - Department-level access controls and data flow management
        - Device integration for multi-platform accessibility
        
        This network ensures that information flows securely to the right stakeholders
        at the right time, similar to how our license management system works.
        
        Each connection in the network represents data flow and system integration,
        with appropriate security and access controls in place.
        """
    
    elif "license" in query or "access" in query or "permission" in query:
        return f"""
        ECG's license management for {company_name} provides role-based access control for all executives:
        
        - CEO Dashboard License: Full access to all divisions with comprehensive data types
        - CRO Dashboard License: Department access focused on revenue generation
        - CIO Dashboard License: Department access centered on technology infrastructure
        - CFO Dashboard License: Department access for financial management
        
        Each license determines what data is visible, which system features are accessible,
        and how dashboards can be customized. Licenses are managed centrally and can be
        activated or deactivated as needed.
        
        The licenses automatically adjust access privileges based on user roles,
        ensuring security and compliance while providing the necessary insights
        for decision-making.
        """
    
    elif "device" in query or "mobile" in query or "tablet" in query or "desktop" in query:
        return f"""
        ECG's executive dashboards for {company_name} support various connected devices:
        
        - Desktop Computers: Full dashboard experience with advanced analytics
        - Tablets: Optimized interface for touch with core metrics
        - Mobile Phones: Essential KPIs and alerts for on-the-go access
        - Specialized Devices: Role-specific terminals (financial, network monitoring)
        - Digital Displays: For office visualization of key metrics
        
        Each device provides an appropriate level of detail and interaction based on
        the form factor and typical use case. All devices sync in real-time to ensure
        consistent data across platforms.
        
        The system detects the device type and automatically adapts the interface while
        maintaining the necessary security controls based on the executive's role.
        """
    
    elif "team" in query or "consultant" in query or "specialist" in query:
        return f"""
        Based on {company_name}'s performance score of {company_info['score']}/100, we've assigned a {team_level} implementation team.
        
        This team has deep expertise in the {company_info['industry']} industry and has successfully implemented Synergyze for similar companies in the {company_info['region']} region.
        
        The team composition includes:
        {', '.join(team_members)}
        
        Each team member brings specialized skills that match your company's specific needs
        and challenges, ensuring efficient implementation and knowledge transfer.
        
        The team will work directly with your executives to customize dashboards, integrate
        systems, and provide training on best practices for governance.
        """
    
    elif "industry" in query or "benchmark" in query or "comparison" in query:
        return f"""
        {company_name} operates in the {company_info['industry']} industry, where the average ECG performance score is approximately 72/100.
        
        With your score of {company_info['score']}/100, you're performing above industry average, which indicates strong operational practices and readiness for digital transformation.
        
        Your key strengths relative to industry peers include:
        - {get_strength_for_industry(company_info['industry'])}
        - {get_strength_for_score(company_info['score'])}
        
        Our implementation will leverage these strengths while addressing specific optimization opportunities we've identified for companies in your sector.
        """
    
    elif "emporal score" in query or "performance score" in query or "score" in query:
        return f"""
        The ECG Performance Score (also known as Emporal Score) for {company_name} is {company_info['score']}/100.
        
        This score is calculated based on multiple factors:
        - Operational efficiency and process maturity
        - Data quality and systems integration
        - Governance structure and compliance
        - Responsiveness to market changes
        - Innovation and digital readiness
        
        Your score of {company_info['score']} places you in the {team_level} implementation category.
        
        This score determines the appropriate implementation team assignment and approach,
        ensuring you receive the right level of expertise and support for your specific
        organizational maturity level.
        """
    
    elif "shop" in query or "shopping" in query or "b2b" in query:
        return f"""
        The ECG B2B shopping experience for {company_name} provides a seamless, enterprise-grade
        procurement process for your governance software needs.
        
        Key features include:
        - Customized company portal with your branding and user hierarchy
        - Role-based module selection with appropriate license assignment
        - Enterprise pricing with volume discounts based on user count
        - Secure checkout with multiple payment options including invoice
        - Automatic license provisioning and deployment after purchase
        
        The B2B shopping experience is fully integrated with the implementation process,
        ensuring that purchased licenses are immediately available and properly configured
        for your executive team.
        
        Would you like to see a demonstration of the B2B shopping portal?
        """
    
    else:
        return f"""
        I'm here to assist with your ECG implementation for {company_name}. I can provide information about:
        
        - Implementation process and timeline
        - Executive dashboard features and customization
        - License management and access controls
        - Connected device deployment and integration
        - Team structure and industry benchmarks
        - ECG Performance Score (Emporal Score) significance
        - B2B shopping experience for governance solutions
        
        Please feel free to ask specific questions about these or other aspects of the ECG governance layer implementation.
        """

# Helper functions for AI responses
def get_strength_for_industry(industry):
    """Return a strength based on the industry"""
    industry_strengths = {
        "Retail Fashion": "Strong customer data collection and trend analysis",
        "Manufacturing": "Robust operational tracking and quality control metrics",
        "Department Store": "Comprehensive inventory management across diverse categories",
        "Fashion Retail": "Advanced omnichannel integration and customer journey tracking"
    }
    return industry_strengths.get(industry, "Industry-specific operational excellence")

def get_strength_for_score(score):
    """Return a strength based on the score range"""
    if score >= 85:
        return "Exceptional data governance and cross-departmental integration"
    elif score >= 80:
        return "Strong digital transformation readiness and systems architecture"
    elif score >= 75:
        return "Good foundational systems with clear improvement roadmap"
    else:
        return "Core operational systems with digitization potential"

if __name__ == "__main__":
    show_voi_jeans_demo()