import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Software Developer Career Hub",
    page_icon="💻",
    layout="wide"
)

# Custom CSS for styling (no external libraries)
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #00B4D8;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .section-header {
        font-size: 2rem;
        color: #0077B6;
        border-bottom: 2px solid #00B4D8;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    .info-card {
        background-color: #f0f4f8;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #0077B6;
        margin: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .highlight-box {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #00B4D8;
        margin: 0.5rem 0;
    }
    .company-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
        border: 1px solid #e0e0e0;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.title("📊 Navigation")
    page = st.radio(
        "Go to:",
        ["🏠 Home", "💰 Salaries", "📚 Study Pathway", "🎓 Top Colleges", "🏢 Top Companies", "📈 Trends"]
    )
    st.divider()
    st.caption("Made with ❤️ for aspiring developers")

# ---------- HOME PAGE ----------
if page == "🏠 Home":
    st.markdown('<h1 class="main-header">💻 Software Developer Career Hub</h1>', unsafe_allow_html=True)
    st.markdown("### Your complete guide to becoming a successful software developer")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><h3>💰 $110K</h3><p>Average US Salary</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>🚀 22%</h3><p>Job Growth (2022-2032)</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>🏆 #3</h3><p>Best Jobs in America</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><h3>🌍 4M+</h3><p>Developers in US</p></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
    <h3>🌟 Why Software Development?</h3>
    <ul>
        <li><b>High Salary:</b> One of the highest-paying careers globally</li>
        <li><b>Flexibility:</b> Work from anywhere, remote opportunities</li>
        <li><b>Innovation:</b> Build products that millions use daily</li>
        <li><b>Continuous Learning:</b> Ever-evolving field with new technologies</li>
        <li><b>Job Security:</b> Consistently high demand across industries</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
    <b>🎯 Quick Stats:</b> 73% of developers are self-taught or bootcamp graduates. 
    Your passion matters more than your degree!
    </div>
    """, unsafe_allow_html=True)

# ---------- SALARIES PAGE ----------
elif page == "💰 Salaries":
    st.markdown('<h2 class="section-header">💰 Software Developer Salaries</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📊 Salary by Experience Level")
        
        # Display as table with conditional formatting
        salary_data = {
            "Role": ["Frontend", "Backend", "Full Stack", "DevOps", "Mobile", "Data Engineer", "AI/ML", "Game Dev"],
            "Entry (0-2 yrs)": ["$65K", "$70K", "$72K", "$75K", "$68K", "$78K", "$85K", "$62K"],
            "Mid (3-5 yrs)": ["$90K", "$95K", "$98K", "$102K", "$92K", "$105K", "$115K", "$88K"],
            "Senior (6+ yrs)": ["$125K", "$135K", "$140K", "$145K", "$130K", "$150K", "$160K", "$120K"]
        }
        
        st.table(salary_data)
        
        # Simple bar chart using st.bar_chart (built-in)
        chart_data = {
            "Entry": [65000, 70000, 72000, 75000, 68000, 78000, 85000, 62000],
            "Mid": [90000, 95000, 98000, 102000, 92000, 105000, 115000, 88000],
            "Senior": [125000, 135000, 140000, 145000, 130000, 150000, 160000, 120000]
        }
        st.bar_chart(chart_data, height=300)
    
    with col2:
        st.markdown("""
        <div class="info-card">
        <h4>💡 Key Insights</h4>
        <ul>
            <li><b>Highest Paying:</b> AI/ML ($160K senior)</li>
            <li><b>Fastest Growth:</b> DevOps (+45% entry to senior)</li>
            <li><b>Entry Level:</b> Average $72K starting</li>
            <li><b>Location Matters:</b> Silicon Valley pays 30% more</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------- STUDY PATHWAY ----------
elif page == "📚 Study Pathway":
    st.markdown('<h2 class="section-header">📚 Study Pathway to Become a Developer</h2>', unsafe_allow_html=True)
    
    st.markdown("### 🗺️ Roadmap (12-24 Months)")
    
    # Progress tracking
    st.subheader("Your Learning Progress")
    progress = st.slider("How far along are you?", 0, 100, 0, key="progress_slider")
    st.progress(progress/100)
    
    steps = [
        ("📖 Phase 1: Fundamentals (2-3 months)", 
         "HTML, CSS, JavaScript basics, Git, Terminal"),
        ("🎯 Phase 2: Specialization (4-6 months)", 
         "Choose: Web (React/Angular), Mobile (React Native), Backend (Python/Node.js), or Data"),
        ("🚀 Phase 3: Advanced (3-4 months)", 
         "APIs, Databases (SQL/NoSQL), Docker, Cloud (AWS/Azure)"),
        ("💼 Phase 4: Portfolio Building (2-3 months)", 
         "Build 3-5 full projects, contribute to open source"),
        ("📝 Phase 5: Interview Prep (1-2 months)", 
         "LeetCode, system design, behavioral questions")
    ]
    
    for title, desc in steps:
        with st.expander(title):
            st.write(desc)
            st.caption(f"⏱️ {title.split('(')[1].replace(')', '')}")
    
    st.markdown("""
    <div class="info-card">
    <h4>🎓 Recommended Learning Resources</h4>
    <ul>
        <li><b>Free:</b> freeCodeCamp, The Odin Project, CS50, YouTube</li>
        <li><b>Paid:</b> Coursera, Udemy, Pluralsight, Frontend Masters</li>
        <li><b>Books:</b> "Clean Code", "Pragmatic Programmer", "Cracking the Coding Interview"</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------- TOP COLLEGES ----------
elif page == "🎓 Top Colleges":
    st.markdown('<h2 class="section-header">🎓 Top CS Colleges</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🏫 Top 10 CS Programs")
        
        colleges = [
            ["MIT", "1", "$58,000", "7%"],
            ["Stanford", "2", "$56,000", "4%"],
            ["CMU", "3", "$59,000", "11%"],
            ["UC Berkeley", "4", "$44,000", "14%"],
            ["Harvard", "5", "$54,000", "4%"],
            ["Caltech", "6", "$58,000", "6%"],
            ["Georgia Tech", "7", "$33,000", "18%"],
            ["UIUC", "8", "$36,000", "44%"],
            ["Cornell", "9", "$61,000", "9%"],
            ["Princeton", "10", "$56,000", "6%"]
        ]
        
        st.table({"College": [c[0] for c in colleges], 
                 "CS Ranking": [c[1] for c in colleges],
                 "Avg Tuition": [c[2] for c in colleges],
                 "Acceptance Rate": [c[3] for c in colleges]})
    
    with col2:
        st.markdown("""
        <div class="info-card">
        <h4>🏆 Top 3</h4>
        <ol>
            <li><b>MIT</b> - #1 CS program</li>
            <li><b>Stanford</b> - Silicon Valley connection</li>
            <li><b>CMU</b> - AI & robotics focus</li>
        </ol>
        <h4>💡 Tip</h4>
        <p>College matters less than skills! Many successful devs come from non-CS backgrounds.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-box">
        <b>📊 ROI Calculator:</b> Top CS grads earn ~$100K starting salary,
        recouping tuition in 2-3 years.
        </div>
        """, unsafe_allow_html=True)

# ---------- TOP COMPANIES ----------
elif page == "🏢 Top Companies":
    st.markdown('<h2 class="section-header">🏢 Top Companies for Developers</h2>', unsafe_allow_html=True)
    
    st.subheader("💼 Best Employers (2026)")
    
    companies = [
        ["Google", "$185K", "4.4", "Yes", "🏠"],
        ["Microsoft", "$175K", "4.3", "Yes", "💻"],
        ["Apple", "$180K", "4.2", "Hybrid", "🍎"],
        ["Amazon", "$170K", "4.0", "Hybrid", "📦"],
        ["Meta", "$190K", "4.1", "Yes", "🔵"],
        ["Netflix", "$200K", "4.5", "No", "🎬"],
        ["Salesforce", "$165K", "4.2", "Yes", "☁️"],
        ["Uber", "$160K", "4.0", "Yes", "🚗"]
    ]
    
    st.table({"Company": [c[0] for c in companies],
             "Avg Salary": [c[1] for c in companies],
             "Rating": [c[2] for c in companies],
             "Remote": [c[3] for c in companies]})
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
        <h4>🌟 Best Perks</h4>
        <ul>
            <li><b>Google:</b> Free meals, gym, on-site healthcare</li>
            <li><b>Netflix:</b> Unlimited vacation, stock options</li>
            <li><b>Microsoft:</b> Work-life balance, education budget</li>
            <li><b>Meta:</b> High bonuses, remote options</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
        <h4>📈 Hiring Trends</h4>
        <p>Companies are prioritizing:</p>
        <ul>
            <li>AI/ML skills</li>
            <li>Cloud expertise (AWS/Azure)</li>
            <li>Full-stack capabilities</li>
            <li>System design knowledge</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------- TRENDS PAGE ----------
elif page == "📈 Trends":
    st.markdown('<h2 class="section-header">📈 Industry Trends 2026</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔝 Most In-Demand Skills")
        
        skill_data = {
            "Skill": ["Python", "AI/ML", "JavaScript", "Cloud", "DevOps", "React", "SQL", "Docker"],
            "Demand": [95, 92, 88, 85, 80, 78, 75, 70]
        }
        st.bar_chart(skill_data, x="Skill", y="Demand", height=300)
        st.caption("Demand Score (out of 100)")
    
    with col2:
        st.subheader("📊 Salary Growth by Role")
        
        growth_data = {
            "Role": ["AI/ML", "Blockchain", "Cloud", "DevOps", "Full Stack", "Mobile", "Frontend"],
            "Growth %": [45, 38, 32, 28, 20, 15, 12]
        }
        st.bar_chart(growth_data, x="Role", y="Growth %", height=300)
        st.caption("Salary Growth (2024-2026)")
    
    st.markdown("""
    <div class="info-card">
    <h4>🔮 Future Outlook</h4>
    <ul>
        <li><b>AI/ML:</b> Expected 60% growth by 2028</li>
        <li><b>Remote Work:</b> 73% of devs prefer hybrid/remote</li>
        <li><b>No-Code:</b> Rising but won't replace developers</li>
        <li><b>Green Tech:</b> Sustainable coding practices emerging</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
    <b>💡 Pro Tip:</b> Focus on AI/ML and cloud skills - they're the fastest-growing 
    areas with the highest salaries!
    </div>
    """, unsafe_allow_html=True)

# Footer
st.divider()
st.markdown("""
<p style='text-align: center; color: #666;'>
    📧 Have questions? Reach out to career counselors | 🔄 Data updated 2026
</p>
""", unsafe_allow_html=True)
