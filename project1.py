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
        menu_title="Select a Section",
        options=["Project Overview", "Company Profile", "System Analysis", "Modules Overview", "System Architecture", "Database Schema", "System Requirements", "ScreenShots"], 
        icons=["book", "building", "bar-chart", "list-task", "diagram-3", "table", "gear"],
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

elif section == "Company Profile":
    st.header("Company Profile")
    st.write(
        """
        **Vinsup Infotech** is a leading IT services company based in **Kalavasal, Madurai, Tamil Nadu, India**.
        The company specializes in providing a range of software development, IT solutions, and consulting services to businesses globally.
        """
    )
    st.subheader("Key Services")
    st.write("""
    - **Custom Software Development**
    - **Web and Mobile App Development**
    - **Cloud Solutions**
    - **IT Consulting**
    """)
    st.subheader("Vision & Mission")
    st.write("""
    - **Vision**: To be a globally recognized IT services provider, delivering exceptional solutions that transform businesses.
    - **Mission**: To empower businesses with innovative technology solutions and exceptional customer service.
    """)
    st.subheader("Company Location")
    st.write("Kalavasal, Madurai, Tamil Nadu, India")

elif section == "System Analysis":
    st.header("System Analysis")
    st.subheader("Problem Statement")
    st.write("Many people struggle to stay consistent with their fitness goals due to a lack of structured tracking and personalized recommendations.")
    st.subheader("Objectives")
    st.write("""
    - Provide a platform for tracking exercises, steps, and calories.
    - Allow users to set fitness goals and measure progress.
    - Integrate health metrics from devices like smartwatches.
    - Offer diet and workout recommendations tailored to user goals.
    """)
    st.subheader("Feasibility Study")
    st.write("""
    - **Technical Feasibility**: Modern frameworks and APIs make this viable.
    - **Operational Feasibility**: User-friendly interfaces ensure accessibility.
    - **Economic Feasibility**: Open-source tools minimize costs.
    """)

elif section == "Modules Overview":
    st.header("Modules Overview")
    modules = [
        ("User Management", "Handles user registration, authentication, and profile setup, including fitness goal setting.", """
from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    """),

        ("Activity Tracking", "Records steps, calories burned, and specific workouts. Syncs with wearable devices for accuracy.", """
from django.db import models
from django.conf import settings

class Activity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    duration_minutes = models.IntegerField(blank=True, null=True)
    distance_km = models.FloatField(blank=True, null=True)
    calories_burned = models.IntegerField(blank=True, null=True)
    """),
        ("Diet & Nutrition", "Logs food intake, provides a nutritional database, and suggests diet plans based on fitness goals.", """
from django.db import models
from django.conf import settings

class Nutrition(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=255)
    food_name = models.CharField(max_length=255)
    calories = models.IntegerField()
    protein_grams = models.FloatField(blank=True, null=True)
    carbs_grams = models.FloatField(blank=True, null=True)
    fat_grams = models.FloatField(blank=True, null=True)
    """),
        ("Workout Recommendations", "Suggests personalized workouts based on user preferences and fitness level."),
        ("Goal-Setting & Progress Tracking", "Allows users to define and track fitness goals with visual progress indicators and reminders."),
        ("Community & Social Engagement", "Provides social engagement features like leaderboards, challenges, and workout sharing."),
        ("Admin Management", "Enables administrators to manage user accounts, update content, and monitor system analytics.")
    ]
    for title, description, *code in modules:
        st.subheader(title)
        st.write(description)
        if code:
            st.code(code[0], language='python')

elif section == "System Architecture":
    st.header("System Architecture")
    st.write("""
    The **Fitness Tracker** system architecture includes:
    - **Frontend**: React Native (mobile) and HTML/CSS/JavaScript (web).
    - **Backend**: Django handles authentication, data processing, and API interactions.
    - **Database**: MySQL stores user profiles, activity logs, and health metrics.
    - **Integration**: Google Fit, Fitbit, and Apple Health enable real-time data syncing.
    """)
    st.subheader("System Architecture Diagram")
    st.image("diagram.png", caption="System Architecture")

elif section == "Database Schema":
    st.header("Database Schema")
    db_schema = [
        ("Users Table", "Stores user credentials and fitness goals.", "UserID (PK), Name, Email, Password, Goals"),
        ("Activities Table", "Logs user activities and calorie tracking.", "ActivityID (PK), UserID (FK), Type, Duration, CaloriesBurned"),
        ("Meals Table", "Tracks user food intake and calorie count.", "MealID (PK), UserID (FK), FoodItem, Calories, Date"),
        ("Workouts Table", "Stores predefined and user-created workout routines.", "WorkoutID (PK), Name, Category, Equipment"),
        ("Health Metrics Table", "Monitors real-time health indicators.", "MetricID (PK), UserID (FK), BMI, HeartRate, SleepHours")
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
        - **IDE**: VS Code, PyCharm
        - **Local Server**: XAMPP for database management
        """
    )
    st.subheader("Minimum Requirements to Run")
    st.write(
        """
        - **Operating System**: Windows 10, macOS 11, or Linux
        - **Processor**: Dual-core 2.5 GHz or higher
        - **RAM**: 4 GB (8 GB recommended)
        - **Storage**: 500 MB for the application; additional space for user data
        - **Internet**: Required for API integration and real-time syncing
        - **Software Dependencies**: Python 3.9+, Django, MySQL, React Native (for mobile deployment)
        """
    )

elif section == "ScreenShots":
    st.header("Login Page")
    st.image("./images/login.png", caption="Login Page")
    st.header("Dashboard")
    st.image("./images/dashboard.png", caption="Dashboard")
    st.header("User Profile")
    st.image("./images/user.png", caption="User Profile")
    st.header("Activity Tracking")
    st.image("./images/activity.png", caption="Activity Tracking")
    st.header("Diet & Nutrition")
    st.image("./images/nutrition.png", caption="Diet & Nutrition")
    
