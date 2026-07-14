import streamlit as st

# Page configuration
st.set_page_config(
    page_title="SOFTWARE DEVELOPER BY ARHAAN",
    page_icon="👨‍💻",
    layout="wide"
)

# Custom CSS for styling with fixed color issues
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #FF6B35;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .section-header {
        font-size: 2rem;
        color: #E03A1C;
        border-bottom: 2px solid #FF6B35;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    .info-card {
        background-color: #FFF8F0;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #FF6B35;
        margin: 1rem 0;
        color: #1a1a1a;
    }
    .info-card ul, .info-card li {
        color: #1a1a1a;
    }
    .metric-card {
        background: linear-gradient(135deg, #FF6B35 0%, #FF3D00 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .metric-card h3, .metric-card p {
        color: white;
    }
    .highlight-box {
        background-color: #FFF3E6;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #FF6B35;
        margin: 0.5rem 0;
        color: #1a1a1a;
    }
    .company-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
        border: 1px solid #e0e0e0;
        color: #1a1a1a;
    }
    .stTable {
        background-color: white;
    }
    .stTable td, .stTable th {
        color: #1a1a1a !important;
    }
    .footer {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #FF6B35 0%, #FF3D00 100%);
        color: white;
        border-radius: 10px;
        margin-top: 2rem;
    }
    .footer h3 {
        color: white;
    }
    .india-flag {
        font-size: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.title("🇮🇳 Navigation")
    page = st.radio(
        "Go to:",
        ["🏠 Home", "💰 Salaries", "📚 Study Pathway", "🎓 Top Indian Colleges", "🏢 Top Indian Companies", "📈 Trends"]
    )
    st.divider()
    st.caption("Made with ❤️ for Indian developers")

# ---------- HOME PAGE ----------
if page == "🏠 Home":
    st.markdown('<h1 class="main-header">🇮🇳 Indian Software Developer Career Hub</h1>', unsafe_allow_html=True)
    st.markdown("### Your complete guide to becoming a successful software developer in India")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><h3>💰 ₹15 LPA</h3><p>Average Indian Salary</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>🚀 25%</h3><p>Job Growth (2022-2032)</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>🏆 #2</h3><p>Best Jobs in India</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><h3>🌍 5M+</h3><p>Developers in India</p></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
    <h3>🌟 Why Software Development in India?</h3>
    <ul>
        <li><b>High Salary:</b> One of the highest-paying careers in India</li>
        <li><b>Global Opportunities:</b> Work with MNCs and startups worldwide</li>
        <li><b>Innovation Hub:</b> India is becoming a global tech leader</li>
        <li><b>Remote Work:</b> Work from anywhere in India or abroad</li>
        <li><b>Job Security:</b> Consistently high demand across all sectors</li>
        <li><b>Startup Culture:</b> India has over 100 unicorn startups</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
    <b>🎯 Quick Stats:</b> 65% of Indian developers are self-taught or bootcamp graduates. 
    India produces the highest number of engineers globally!
    </div>
    """, unsafe_allow_html=True)

# ---------- SALARIES PAGE ----------
elif page == "💰 Salaries":
    st.markdown('<h2 class="section-header">💰 Indian Software Developer Salaries</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📊 Salary by Experience Level (₹ LPA)")
        
        # Indian salary data in LPA (Lakhs Per Annum)
        salary_data = {
            "Role": ["Frontend", "Backend", "Full Stack", "DevOps", "Mobile", "Data Engineer", "AI/ML", "Cloud"],
            "Entry (0-2 yrs)": ["₹6L", "₹7L", "₹8L", "₹8L", "₹7L", "₹9L", "₹10L", "₹9L"],
            "Mid (3-5 yrs)": ["₹12L", "₹14L", "₹15L", "₹16L", "₹13L", "₹18L", "₹22L", "₹17L"],
            "Senior (6+ yrs)": ["₹20L", "₹24L", "₹26L", "₹28L", "₹22L", "₹32L", "₹40L", "₹30L"]
        }
        
        st.table(salary_data)
        
        # Convert to numeric for chart
        chart_data = {
            "Entry": [6, 7, 8, 8, 7, 9, 10, 9],
            "Mid": [12, 14, 15, 16, 13, 18, 22, 17],
            "Senior": [20, 24, 26, 28, 22, 32, 40, 30]
        }
        st.bar_chart(chart_data, height=300)
        st.caption("Salaries in ₹ Lakhs Per Annum (LPA)")
    
    with col2:
        st.markdown("""
        <div class="info-card">
        <h4>💡 Key Insights</h4>
        <ul>
            <li><b>Highest Paying:</b> AI/ML (₹40L senior)</li>
            <li><b>Fastest Growth:</b> Cloud (+200% entry to senior)</li>
            <li><b>Entry Level:</b> Average ₹7.5L starting</li>
            <li><b>Location Matters:</b> Bangalore pays 30% more</li>
            <li><b>Top Cities:</b> Bangalore, Hyderabad, Pune</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------- STUDY PATHWAY ----------
elif page == "📚 Study Pathway":
    st.markdown('<h2 class="section-header">📚 Study Pathway to Become a Developer in India</h2>', unsafe_allow_html=True)
    
    st.markdown("### 🗺️ Roadmap (12-24 Months)")
    
    # Progress tracking
    st.subheader("Your Learning Progress")
    progress = st.slider("How far along are you?", 0, 100, 0, key="progress_slider")
    st.progress(progress/100)
    
    steps = [
        ("📖 Phase 1: Fundamentals (2-3 months)", 
         "HTML, CSS, JavaScript basics, Git, Terminal - Focus on Indian edtech platforms"),
        ("🎯 Phase 2: Specialization (4-6 months)", 
         "Choose: Web (React/Angular), Mobile (React Native/Flutter), Backend (Python/Java), or Data Science"),
        ("🚀 Phase 3: Advanced (3-4 months)", 
         "APIs, Databases (SQL/NoSQL), Docker, Cloud (AWS/Azure/GCP)"),
        ("💼 Phase 4: Portfolio Building (2-3 months)", 
         "Build 3-5 projects, contribute to open source, participate in Indian hackathons"),
        ("📝 Phase 5: Interview Prep (1-2 months)", 
         "LeetCode, GeeksforGeeks, System Design, Behavioral questions")
    ]
    
    for title, desc in steps:
        with st.expander(title):
            st.write(desc)
            st.caption(f"⏱️ {title.split('(')[1].replace(')', '')}")
    
    st.markdown("""
    <div class="info-card">
    <h4>🎓 Best Indian Learning Resources</h4>
    <ul>
        <li><b>Free:</b> NPTEL, SWAYAM, YouTube (CodeWithHarry, Apna College)</li>
        <li><b>Paid:</b> Coursera (Indian pricing), Udemy (₹400 courses), upGrad, Scaler</li>
        <li><b>Indian Platforms:</b> GeeksforGeeks, InterviewBit, Coding Ninjas</li>
        <li><b>Books:</b> "Let Us C", "Head First Java", "Cracking the Coding Interview"</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------- TOP INDIAN COLLEGES ----------
elif page == "🎓 Top Indian Colleges":
    st.markdown('<h2 class="section-header">🎓 Top Indian Engineering Colleges</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🏫 Top 10 Indian CS Programs")
        
        colleges = [
            ["IIT Bombay", "#1", "₹2.2L", "2.5%", "Mumbai"],
            ["IIT Delhi", "#2", "₹2.1L", "2.8%", "Delhi"],
            ["IIT Madras", "#3", "₹2.0L", "3.0%", "Chennai"],
            ["IIT Kanpur", "#4", "₹1.9L", "3.2%", "Kanpur"],
            ["IIT Kharagpur", "#5", "₹1.8L", "3.5%", "Kharagpur"],
            ["BITS Pilani", "#6", "₹4.5L", "15%", "Pilani"],
            ["IIT Roorkee", "#7", "₹1.7L", "3.8%", "Roorkee"],
            ["NIT Trichy", "#8", "₹1.5L", "20%", "Trichy"],
            ["IIIT Hyderabad", "#9", "₹2.5L", "12%", "Hyderabad"],
            ["DTU Delhi", "#10", "₹1.4L", "25%", "Delhi"]
        ]
        
        st.table({"College": [c[0] for c in colleges], 
                 "Ranking": [c[1] for c in colleges],
                 "Fees (Annual)": [c[2] for c in colleges],
                 "Acceptance Rate": [c[3] for c in colleges],
                 "Location": [c[4] for c in colleges]})
    
    with col2:
        st.markdown("""
        <div class="info-card">
        <h4>🏆 Top 3</h4>
        <ol>
            <li><b>IIT Bombay</b> - Best CS program</li>
            <li><b>IIT Delhi</b> - Strong placement record</li>
            <li><b>IIT Madras</b> - Research excellence</li>
        </ol>
        <h4>💡 Tip</h4>
        <p>IITs & NITs offer great placements, but skills matter more than college name!</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="highlight-box">
        <b>📊 ROI Calculator:</b> IIT CS grads earn ₹20-30 LPA starting,
        recouping fees in 1-2 years.
        </div>
        """, unsafe_allow_html=True)

# ---------- TOP INDIAN COMPANIES ----------
elif page == "🏢 Top Indian Companies":
    st.markdown('<h2 class="section-header">🏢 Top Companies in India for Developers</h2>', unsafe_allow_html=True)
    
    st.subheader("💼 Best Employers in India (2026)")
    
    companies = [
        ["Google India", "₹30L", "4.4", "Yes", "Bangalore", "Hybrid"],
        ["Microsoft India", "₹28L", "4.3", "Yes", "Hyderabad", "Hybrid"],
        ["Amazon India", "₹25L", "4.0", "Yes", "Bangalore", "Hybrid"],
        ["Flipkart", "₹24L", "4.2", "Yes", "Bangalore", "Hybrid"],
        ["Swiggy", "₹22L", "4.1", "Yes", "Bangalore", "Hybrid"],
        ["Zomato", "₹21L", "4.0", "Yes", "Gurgaon", "Hybrid"],
        ["TCS", "₹12L", "3.8", "Yes", "Multiple", "Hybrid"],
        ["Infosys", "₹11L", "3.9", "Yes", "Multiple", "Hybrid"],
        ["Wipro", "₹10L", "3.7", "Yes", "Multiple", "Hybrid"],
        ["Razorpay", "₹26L", "4.3", "Yes", "Bangalore", "Hybrid"]
    ]
    
    st.table({"Company": [c[0] for c in companies],
             "Avg Salary": [c[1] for c in companies],
             "Rating": [c[2] for c in companies],
             "Remote": [c[3] for c in companies],
             "Location": [c[4] for c in companies],
             "Work Mode": [c[5] for c in companies]})
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
        <h4>🌟 Best Perks</h4>
        <ul>
            <li><b>Google India:</b> Free meals, gym, stock options</li>
            <li><b>Microsoft India:</b> Work-life balance, education budget</li>
            <li><b>Flipkart:</b> Big Billion Day bonuses, ESOPs</li>
            <li><b>Razorpay:</b> ESOPs, flexible work hours</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
        <h4>📈 Hiring Trends in India</h4>
        <p>Indian companies are prioritizing:</p>
        <ul>
            <li>AI/ML skills (50% salary premium)</li>
            <li>Cloud expertise (AWS/Azure/GCP)</li>
            <li>Full-stack development</li>
            <li>DevOps & SRE roles</li>
            <li>Product-based companies vs Service-based</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------- TRENDS PAGE ----------
elif page == "📈 Trends":
    st.markdown('<h2 class="section-header">📈 Indian Tech Industry Trends 2026</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔝 Most In-Demand Skills in India")
        
        skill_data = {
            "Skill": ["Python", "AI/ML", "Java", "JavaScript", "Cloud", "DevOps", "SQL", "React"],
            "Demand": [95, 92, 85, 88, 82, 78, 75, 80]
        }
        st.bar_chart(skill_data, x="Skill", y="Demand", height=300)
        st.caption("Demand Score (out of 100)")
    
    with col2:
        st.subheader("📊 Salary Growth in India")
        
        growth_data = {
            "Role": ["AI/ML", "Cloud", "DevOps", "Data Science", "Full Stack", "Mobile", "Frontend"],
            "Growth %": [45, 35, 30, 28, 22, 18, 15]
        }
        st.bar_chart(growth_data, x="Role", y="Growth %", height=300)
        st.caption("Salary Growth (2024-2026)")
    
    st.markdown("""
    <div class="info-card">
    <h4>🔮 Future Outlook for Indian Tech</h4>
    <ul>
        <li><b>AI/ML:</b> Expected 70% growth by 2028 in India</li>
        <li><b>Remote Work:</b> 65% of Indian devs prefer hybrid/remote</li>
        <li><b>Startup Boom:</b> India to have 200+ unicorns by 2028</li>
        <li><b>Digital India:</b> Govt. initiatives creating 1M+ tech jobs</li>
        <li><b>Global Centers:</b> India becoming R&D hub for MNCs</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
    <b>💡 Pro Tip:</b> Focus on AI/ML, Cloud, and Full-stack skills - they're the fastest-growing 
    areas with the highest salaries in India!
    </div>
    """, unsafe_allow_html=True)

# ---------- FOOTER ----------
st.divider()
st.markdown("""
<div class="footer">
    <h3>🇮🇳 Developed by Arhaan</h3>
    <p style="color: white; margin-top: 0.5rem;">
        Building the future of Indian tech, one developer at a time ✨<br>
        📧 Connect with me for career guidance | 📱 Follow for more tech insights
    </p>
    <p style="color: #FFD4C4; font-size: 0.9rem; margin-top: 1rem;">
        Made with ❤️ for the Indian developer community
    </p>
</div>
""", unsafe_allow_html=True)
