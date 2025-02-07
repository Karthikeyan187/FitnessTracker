import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(
    page_title="Fitness Tracker Presentation",
    page_icon="🏋️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation - Refined Terminology
with st.sidebar:
    st.title("Presentation Outline")
    section = option_menu(
        menu_title="Select a Section",  # Improved wording for sidebar menu
        options=["Project Overview", "System Analysis", "Modules Overview", "System Architecture", "Database Structure", "System Requirements"], 
        icons=["book", "bar-chart", "list-task", "diagram-3", "table", "gear"],  # Icons for each section
        default_index=0,
    )

# Project Title at the top
st.title("Fitness Tracker - Project Presentation")

# Sections Based on Sidebar Selection
if section == "Project Overview":
    st.header("Project Overview")
    st.write(
        """
        The **Fitness Tracker** is a system designed to help users monitor and improve their physical health. 
        It tracks activities like workouts, steps, calories burned, and dietary intake. 
        The system provides personalized fitness recommendations, progress tracking, and goal-setting features. 
        It integrates with wearable devices and fitness APIs for real-time data.
        """
    )
    st.subheader("Domain")
    st.write("Health and Fitness Technology")
    st.subheader("Technology Stack")
    st.write("""
    - **Backend**: Python and Django
    - **Frontend**: React Native (mobile) or HTML/CSS/JavaScript (web)
    - **Database**: MySQL
    - **APIs**: Google Fit, Fitbit, Apple Health
    """)

elif section == "System Analysis":
    st.header("System Analysis")
    st.subheader("Problem Statement")
    st.write(
        "Many people struggle to stay consistent with their fitness goals due to a lack of structured tracking and personalized recommendations."
    )
    st.subheader("Objectives")
    st.write(
        """
        - Provide a platform for tracking exercises, steps, and calories.
        - Allow users to set fitness goals and measure progress.
        - Integrate health metrics from devices like smartwatches.
        - Offer diet and workout recommendations tailored to user goals.
        """
    )
    st.subheader("Feasibility Study")
    st.write(
        """
        - **Technical Feasibility**: Modern frameworks and APIs make this viable.
        - **Operational Feasibility**: User-friendly interfaces ensure accessibility.
        - **Economic Feasibility**: Open-source tools minimize costs.
        """
    )

elif section == "Modules Overview":
    st.header("Modules Overview")
    st.write("Below are the key modules of the **Fitness Tracker** system, each contributing to user engagement and efficient fitness management.")
    
    module_details = [
        ("User Management", "Manages user registration, authentication, and profile setup, including fitness goal setting."),
        ("Activity Tracking", "Records steps, calories burned, and specific workouts. Syncs with wearable devices for accuracy."),
        ("Diet & Nutrition", "Logs food intake, provides a nutritional database, and suggests diet plans based on fitness goals."),
        ("Workout Recommendations", "Recommends workouts tailored to user goals with guided tutorials and progress adaptation."),
        ("Health Metrics", "Monitors BMI, heart rate, hydration levels, and other vital health parameters in real time."),
        ("Goal-Setting & Progress Tracking", "Allows users to define and track fitness goals with visual progress indicators and notifications."),
        ("Community & Social Engagement", "Enables social engagement through leaderboards, challenges, and group fitness activities."),
        ("Admin Management", "Oversees user management, fitness content updates, and system analytics through an admin dashboard.")
    ]
    
    for title, description in module_details:
        st.subheader(title)
        st.write(description)
        st.code("""# Add respective module code and screenshot here""", language='python')

elif section == "System Architecture":
    st.header("System Architecture")
    st.write(
        """
        The **Fitness Tracker** system architecture consists of:
        - **Frontend**: Web interface for user interaction.
        - **Backend**: Django handles requests and data processing.
        - **Database**: MySQL stores user data, activity logs, and fitness content.
        - **Integration**: APIs like Fitbit, Google Fit, and Apple Health enable real-time data collection.
        """
    )
    st.subheader("System Architecture Diagram")
    st.image("https://via.placeholder.com/800x400.png?text=System+Architecture+Diagram", caption="System Architecture")

elif section == "Database Structure":
    st.header("Database Structure")
    st.write("The database schema of the **Fitness Tracker** system is structured as follows:")
    
    db_schema = [
        ("Users", "Stores user credentials and fitness goals.", "UserID (PK), Name, Email, Password, Goals"),
        ("Activities", "Logs user activities and calorie tracking.", "ActivityID (PK), UserID (FK), Type, Duration, CaloriesBurned"),
        ("Meals", "Tracks user food intake and calorie count.", "MealID (PK), UserID (FK), FoodItem, Calories, Date"),
        ("Workouts", "Stores predefined and user-created workout routines.", "WorkoutID (PK), Name, Category, Equipment"),
        ("Health Metrics", "Monitors real-time health indicators.", "MetricID (PK), UserID (FK), BMI, HeartRate, SleepHours")
    ]
    
    for table, description, fields in db_schema:
        st.subheader(table)
        st.write(f"**Description:** {description}")
        st.write(f"**Fields:** {fields}")

elif section == "System Requirements":
    st.header("System Requirements")
    st.subheader("Development Environment")
    st.write(
        """
        - **Device**: MacBook Air M3
        - **RAM**: 16 GB
        - **Storage**: 512 GB SSD
        """
    )
    st.subheader("Minimum Requirements to Run")
    st.write(
        """
        - **OS**: Windows 10, macOS 11, or Linux
        - **Processor**: Dual-core 2.5 GHz or higher
        - **RAM**: 4 GB (8 GB recommended)
        - **Storage**: 500 MB for the application; additional space for user data
        - **Internet**: Required for API integration and syncing
        """
    )
