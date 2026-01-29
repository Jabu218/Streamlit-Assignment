# -*- coding: utf-8 -*-
"""
Researcher Profile Page - Streamlit App
Created on Jan 28, 2026
"""

import streamlit as st
from datetime import datetime
import os
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Jabulile I. Lubisi - Researcher Profile",
    page_icon="👩‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Poppins:wght@300;400;600&display=swap');
    
    .main > div {
        padding-top: 0rem;
    }
    
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        margin-top: 0rem;
    }
    
    .main-header {
        font-size: 3em;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        margin-bottom: 5px;
        margin-top: 0px;
        padding-top: 0px;
        font-family: 'Playfair Display', serif;
        text-align: center;
    }
    .subtitle {
        font-size: 1.3em;
        color: #764ba2;
        margin-bottom: 20px;
        margin-top: 5px;
        font-weight: 400;
        text-align: center;
        font-family: 'Poppins', sans-serif;
    }
    .section-header {
        font-size: 2em;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        margin-top: 30px;
        margin-bottom: 15px;
        border-bottom: 3px solid #667eea;
        padding-bottom: 10px;
        font-family: 'Playfair Display', serif;
    }
    .research-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 20px;
        border-radius: 15px;
        margin: 15px 0;
        border-left: 5px solid #667eea;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    .research-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        border: none;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: transform 0.3s ease;
    }
    .metric-box:hover {
        transform: scale(1.05);
    }
    .metric-box h3 {
        color: white;
        font-size: 2.5em;
        margin: 0;
        font-weight: 700;
    }
    .metric-box p {
        color: #f0f0f0;
        margin: 5px 0 0 0;
    }
    .profile-container {
        text-align: center;
        margin-bottom: 10px;
        margin-top: 0px;
        padding-top: 0px;
    }
    .stImage {
        border-radius: 50%;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        margin-top: 0px;
    }
    
    .intro-text {
        font-size: 1.1em;
        line-height: 1.8;
        color: #2c3e50;
        text-align: center;
        padding: 10px;
        margin-top: 10px;
        font-family: 'Poppins', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("## 🌟 Navigation")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Explore My Profile:",
    ["👩‍💻 About Me", "🔬 Research Areas", "📚 Publications", "🚀 Projects", "📧 Contact"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
### 💜 Quick Links
- 🎓 University of Mpumalanga
- 💻 Data Science Portfolio
- 🔐 Cybersecurity Research
""")

# About Me Section
if page == "👩‍💻 About Me":
    # Header with profile image centered
    st.markdown("<div class='profile-container'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([0.5, 3, 0.5])
    with col2:
        # Load profile image
        profile_path = os.path.join(os.path.dirname(__file__), "assets", "profile.jpg")
        if os.path.exists(profile_path):
            profile_img = Image.open(profile_path)
            # Crop from bottom - keep top, remove bottom
            width, height = profile_img.size
            new_height = int(height * 0.5)  # Keep only top 50%
            profile_img = profile_img.crop((0, 0, width, new_height))
            st.image(profile_img, use_container_width=True)
        else:
            st.image("https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400&h=400&fit=crop", 
                    caption="", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='main-header'>Jabulile Ingrith Lubisi</div>", 
               unsafe_allow_html=True)
    st.markdown("""
    <div class='subtitle'>Data Science & Cybersecurity Researcher 💜<br>University of Mpumalanga 🎓</div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='intro-text'>
    Welcome to my research portfolio! I am a dedicated researcher passionate about leveraging 
    <strong>data science</strong> and <strong>cybersecurity</strong> to solve real-world challenges. 
    At the University of Mpumalanga, I explore innovative approaches to data-driven security solutions, 
    combining analytical rigor with cutting-edge technology to create safer digital environments.
    <br><br>
    My research journey is driven by curiosity, innovation, and a commitment to making technology 
    more secure and accessible for everyone. 🌍✨
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Statistics with beautiful gradient boxes
    st.markdown("<h2 style='text-align: center; color: #764ba2;'>📊 Research Impact</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("<div class='metric-box'><h3>12+</h3><p>Research Papers</p></div>", 
                   unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='metric-box'><h3>6</h3><p>Active Projects</p></div>", 
                   unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='metric-box'><h3>150+</h3><p>Citations</p></div>", 
                   unsafe_allow_html=True)
    with col4:
        st.markdown("<div class='metric-box'><h3>5</h3><p>Awards</p></div>", 
                   unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Add visual elements
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='section-header'>🎓 Academic Journey</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='research-box'>
        <h4>🎯 Current Research Position</h4>
        <p><strong>Institution:</strong> University of Mpumalanga</p>
        <p><strong>Department:</strong> Computer Science & Information Systems</p>
        <p><strong>Focus Areas:</strong> Data Science & Cybersecurity</p>
        </div>
        
        <div class='research-box'>
        <h4>📖 Research Interests</h4>
        <p>• Advanced data analytics and visualization</p>
        <p>• Machine learning for security applications</p>
        <p>• Network threat detection and prevention</p>
        <p>• Privacy-preserving data mining</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&h=400&fit=crop", 
                caption="Data Science & Analytics", use_container_width=True)
    
    with col2:
        st.markdown("<div class='section-header'>💼 Research Focus</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class='research-box'>
        <h4>📊 Data Science Research</h4>
        <p>Exploring advanced statistical methods, predictive modeling, and big data analytics 
        to extract meaningful insights from complex datasets. My work focuses on developing 
        scalable solutions for real-world data challenges.</p>
        </div>
        
        <div class='research-box'>
        <h4>🔐 Cybersecurity Research</h4>
        <p>Investigating cutting-edge security protocols, threat detection systems, and 
        vulnerability assessment techniques. I am passionate about creating robust defense 
        mechanisms against evolving cyber threats.</p>
        </div>
        
        <div class='research-box'>
        <h4>🤝 Interdisciplinary Innovation</h4>
        <p>Bridging data science and cybersecurity to develop intelligent security systems 
        that can predict, detect, and respond to threats in real-time using machine learning 
        and advanced analytics.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=600&h=400&fit=crop", 
                caption="Cybersecurity & Protection", use_container_width=True)

# Research Areas Section
elif page == "🔬 Research Areas":
    st.markdown("<div class='section-header'>🔬 My Research Domains</div>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&h=400&fit=crop", 
            caption="Technology & Innovation", use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    research_areas = {
        "📊 Data Science & Analytics": {
            "desc": "Advanced statistical analysis, data mining, predictive modeling, and big data analytics. Developing innovative approaches to extract actionable insights from complex, multi-dimensional datasets.",
            "icon": "📈",
            "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&h=300&fit=crop"
        },
        "🔐 Cybersecurity": {
            "desc": "Network security, threat detection, vulnerability assessment, and security protocol development. Creating robust defense mechanisms to protect against sophisticated cyber attacks.",
            "icon": "🛡️",
            "image": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=400&h=300&fit=crop"
        },
        "🤖 Machine Learning for Security": {
            "desc": "Applying advanced ML algorithms for intrusion detection, anomaly detection, and behavioral analysis. Building intelligent systems that can predict and prevent security breaches.",
            "icon": "🧠",
            "image": "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?w=400&h=300&fit=crop"
        },
        "🔒 Data Privacy & Protection": {
            "desc": "Secure data handling, encryption techniques, and privacy-preserving methodologies. Ensuring data confidentiality while enabling meaningful analysis and insights.",
            "icon": "🔐",
            "image": "https://images.unsplash.com/photo-1614064641938-3bbee52942c7?w=400&h=300&fit=crop"
        },
        "⚠️ Threat Intelligence": {
            "desc": "Data-driven approaches to identifying, analyzing, and mitigating cyber threats. Developing proactive strategies for threat hunting and incident response.",
            "icon": "🎯",
            "image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=400&h=300&fit=crop"
        }
    }
    
    for i, (area, details) in enumerate(research_areas.items()):
        if i % 2 == 0:
            col1, col2 = st.columns([1, 1])
            with col1:
                st.image(details["image"], use_container_width=True)
            with col2:
                st.markdown(f"""
                <div class='research-box'>
                    <h3>{details['icon']} {area}</h3>
                    <p style='font-size: 1.05em; line-height: 1.6;'>{details['desc']}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown(f"""
                <div class='research-box'>
                    <h3>{details['icon']} {area}</h3>
                    <p style='font-size: 1.05em; line-height: 1.6;'>{details['desc']}</p>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.image(details["image"], use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

# Publications Section
elif page == "📚 Publications":
    st.markdown("<div class='section-header'>📚 Research Publications</div>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=1200&h=400&fit=crop", 
            caption="Knowledge & Research", use_container_width=True)
    
    st.markdown("""
    <p style='text-align: center; font-size: 1.2em; color: #764ba2; margin: 20px 0;'>
    My research contributions span across data science and cybersecurity, 
    focusing on innovative solutions for emerging technological challenges.
    </p>
    """, unsafe_allow_html=True)
    
    publications = [
        {
            "title": "Machine Learning Approaches for Advanced Cybersecurity Threat Detection",
            "authors": "Lubisi, J.I., Mthembu, P., & Ndlovu, S.",
            "venue": "International Journal of Cybersecurity and Digital Forensics",
            "year": 2025,
            "citations": 18,
            "type": "Journal Article",
            "abstract": "This paper presents novel machine learning techniques for detecting sophisticated cyber threats in real-time network environments."
        },
        {
            "title": "Data-Driven Security Analytics: A Comprehensive Framework for Network Traffic Analysis",
            "authors": "Lubisi, J.I., Research Consortium",
            "venue": "African Conference on Data Science and Machine Learning",
            "year": 2024,
            "citations": 12,
            "type": "Conference Paper",
            "abstract": "Introducing a comprehensive framework for analyzing network traffic patterns using advanced data science methodologies."
        },
        {
            "title": "Privacy-Preserving Data Analytics in Healthcare: Balancing Security and Utility",
            "authors": "Lubisi, J.I., Khumalo, T., & Associates",
            "venue": "Journal of Secure Computing and Information Systems",
            "year": 2024,
            "citations": 9,
            "type": "Journal Article",
            "abstract": "Exploring techniques for maintaining patient privacy while enabling meaningful healthcare data analytics."
        },
        {
            "title": "Anomaly Detection in IoT Networks Using Deep Learning",
            "authors": "Lubisi, J.I., & Collaboration Team",
            "venue": "IEEE International Conference on IoT Security",
            "year": 2024,
            "citations": 7,
            "type": "Conference Paper",
            "abstract": "Novel approaches to identifying abnormal behaviors in Internet of Things networks using deep learning architectures."
        }
    ]
    
    for i, pub in enumerate(publications, 1):
        with st.expander(f"📄 {pub['title']}", expanded=(i==1)):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"""
                <div class='research-box'>
                    <h4 style='color: #667eea;'>{pub['title']}</h4>
                    <p><strong>✍️ Authors:</strong> {pub['authors']}</p>
                    <p><strong>📖 Published in:</strong> {pub['venue']} ({pub['year']})</p>
                    <p><strong>📊 Type:</strong> {pub['type']}</p>
                    <p><strong>📈 Citations:</strong> {pub['citations']}</p>
                    <hr>
                    <p><strong>Abstract:</strong> {pub['abstract']}</p>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.metric("Year", pub['year'])
                st.metric("Citations", pub['citations'])

# Projects Section
elif page == "🚀 Projects":
    st.markdown("<div class='section-header'>🚀 Current Research Projects</div>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&h=400&fit=crop", 
            caption="Innovation in Action", use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    projects = [
        {
            "name": "🔍 AI-Powered Cybersecurity Threat Detection System",
            "status": "Active",
            "progress": 80,
            "description": "Developing an advanced machine learning system for real-time detection and classification of cyber threats. This project integrates deep learning algorithms with network traffic analysis to identify sophisticated attack patterns.",
            "technologies": "Python, TensorFlow, Scikit-learn, Network Analysis Tools",
            "duration": "Jan 2024 - Present",
            "image": "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=600&h=400&fit=crop"
        },
        {
            "name": "📊 Secure Data Analytics Platform for Healthcare",
            "status": "Active",
            "progress": 65,
            "description": "Building a privacy-preserving data analytics platform that enables healthcare organizations to derive insights while maintaining patient confidentiality through advanced encryption and anonymization techniques.",
            "technologies": "Python, Pandas, SQL, Encryption Libraries",
            "duration": "Aug 2024 - Present",
            "image": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=600&h=400&fit=crop"
        },
        {
            "name": "🌐 Network Security Vulnerability Assessment Framework",
            "status": "Active",
            "progress": 55,
            "description": "Creating a comprehensive framework for automated vulnerability scanning and risk assessment in enterprise networks. The system provides actionable recommendations for security improvements.",
            "technologies": "Python, Network Security Tools, Vulnerability Scanners",
            "duration": "Oct 2024 - Present",
            "image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&h=400&fit=crop"
        },
        {
            "name": "💡 Predictive Threat Intelligence System",
            "status": "Planning",
            "progress": 40,
            "description": "Designing a predictive system that uses historical threat data and machine learning to forecast potential security incidents before they occur, enabling proactive defense strategies.",
            "technologies": "Machine Learning, Big Data Analytics, Threat Intelligence APIs",
            "duration": "Dec 2024 - Present",
            "image": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=600&h=400&fit=crop"
        }
    ]
    
    for project in projects:
        with st.container():
            col1, col2 = st.columns([1, 1])
            with col1:
                st.image(project['image'], use_container_width=True)
            with col2:
                st.markdown(f"""
                <div class='research-box'>
                    <h3>{project['name']}</h3>
                    <p style='font-size: 1.05em;'>{project['description']}</p>
                    <p><strong>🛠️ Technologies:</strong> {project['technologies']}</p>
                    <p><strong>📅 Duration:</strong> {project['duration']}</p>
                    <p><strong>📊 Status:</strong> <span style='color: #667eea; font-weight: 600;'>{project['status']}</span></p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown(f"<p style='text-align: center; color: #764ba2; font-weight: 600;'>Progress: {project['progress']}%</p>", unsafe_allow_html=True)
            st.progress(project['progress'] / 100)
            st.markdown("<br>", unsafe_allow_html=True)

# Contact Section
elif page == "📧 Contact":
    st.markdown("<div class='section-header'>📧 Let's Connect!</div>", unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1423666639041-f56000c27a9a?w=1200&h=400&fit=crop", 
            caption="Let's Collaborate", use_container_width=True)
    
    st.markdown("""
    <p style='text-align: center; font-size: 1.2em; color: #764ba2; margin: 20px 0;'>
    I'm always excited to collaborate on research projects, discuss innovative ideas, 
    or explore opportunities in data science and cybersecurity! 💜
    </p>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='research-box'>
        <h3>📬 Contact Information</h3>
        <p style='font-size: 1.1em;'>
        <strong>📧 Email:</strong> lubisijabulile@gmail.com<br><br>
        <strong>🏛️ University:</strong> University of Mpumalanga<br><br>
        <strong>🎓 Department:</strong> Computer Science & Information Systems<br><br>
        <strong>🔬 Research Focus:</strong> Data Science & Cybersecurity<br><br>
        <strong>📍 Location:</strong> Mpumalanga, South Africa
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.image("https://images.unsplash.com/photo-1596526131083-e8c633c948d2?w=600&h=400&fit=crop", 
                caption="University of Mpumalanga", use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class='research-box'>
        <h3>🌐 Follow My Work</h3>
        <p style='font-size: 1.1em;'>
        <strong>💼 LinkedIn:</strong> <a href='https://www.linkedin.com/in/jabulile-ingrith-lubisi-b11148209/' target='_blank'>linkedin.com/in/jabulile-ingrith-lubisi</a><br><br>
        <strong>💻 GitHub:</strong> <a href='https://github.com/Jabu218' target='_blank'>github.com/Jabu218</a><br><br>
        <strong>📧 Email:</strong> <a href='mailto:lubisijabulile@gmail.com'>lubisijabulile@gmail.com</a><br><br>
        <strong>🎓 University Email:</strong> <a href='mailto:jabulile.lubisi@ump.ac.za'>jabulile.lubisi@ump.ac.za</a>
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.image("https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600&h=400&fit=crop", 
                caption="Collaboration & Networking", use_container_width=True)
    
    st.markdown("---")
    
    # Contact Form with beautiful styling
    st.markdown("<h2 style='text-align: center; color: #764ba2;'>💌 Send Me a Message</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; margin-bottom: 30px;'>Have a question or want to collaborate? I'd love to hear from you!</p>", unsafe_allow_html=True)
    
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Your Name *", placeholder="Enter your full name")
            email = st.text_input("Your Email *", placeholder="your.email@example.com")
        with col2:
            subject = st.text_input("Subject *", placeholder="What's this about?")
            interest = st.selectbox("Area of Interest", 
                                   ["General Inquiry", "Research Collaboration", 
                                    "Data Science Project", "Cybersecurity Consultation", 
                                    "Academic Partnership", "Other"])
        
        message = st.text_area("Your Message *", height=150, 
                              placeholder="Tell me more about your inquiry...")
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            submitted = st.form_submit_button("✉️ Send Message", use_container_width=True)
        
        if submitted:
            if name and email and message and subject:
                st.success(f"✨ Thank you, {name}! Your message has been received. I'll get back to you within 24-48 hours!")
                st.balloons()
            else:
                st.warning("⚠️ Please fill in all required fields marked with *")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white; margin-top: 50px;'>
    <h3 style='color: white; margin-bottom: 15px;'>✨ Jabulile Ingrith Lubisi</h3>
    <p style='font-size: 1.1em; margin-bottom: 10px;'>Data Science & Cybersecurity Researcher</p>
    <p style='font-size: 0.95em; margin-bottom: 20px;'>University of Mpumalanga 🎓</p>
    <p style='font-size: 0.9em; color: #f0f0f0;'>© 2026 | Last Updated: January 28, 2026</p>
    <p style='font-size: 0.85em; color: #e0e0e0; margin-top: 10px;'>Empowering Security Through Data-Driven Innovation 💜</p>
</div>
""", unsafe_allow_html=True)