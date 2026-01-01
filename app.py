import streamlit as st

# Page configuration
st.set_page_config(page_title="Business Comeback", page_icon="🚚")

st.title("🚚 Business Comeback Story Generator")

# Inputs for the user
name = st.text_input("Business/Your Name", "My Landscaping")
goal = st.number_input("Goal Amount ($)", value=5000)
raised = st.number_input("Amount Raised ($)", value=0)

# Progress Bar
progress = raised / goal if goal > 0 else 0
st.progress(min(progress, 1.0))
st.write(f"**{progress:.0%}** of the way to the goal!")

# The Story Template
story_text = f"""{name} is making a comeback! 
After a major move and losing essential equipment, we are rebuilding from scratch. 
The funds raised will go directly toward a work truck and professional landscaping tools. 
We aim to be back on the road by Spring 2026. Thank you for your support!"""

# Display Section
if st.button("Preview Story"):
    st.subheader("Your Story:")
    st.info(story_text)
    
    # Download Button
    st.download_button(
        label="📥 Download Story as Text File",
        data=story_text,
        file_name="comeback_story.txt",
        mime="text/plain"
    )

st.divider()
st.write("Copy this story into your GoFundMe or share it on social media!")
