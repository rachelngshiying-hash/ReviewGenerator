
import streamlit as st

st.title("Customer Feedback & Review Portal")
st.write("We value your feedback! Please let us know about your experience today.")

# 1. Customer Type Selection
cust_type = st.radio("Are you a new or existing customer?", ["New Customer", "Existing Customer"])

# 2. Basic Information
cust_name = st.text_input("Your Name")
cust_phone = st.text_input("Phone Number (for follow-up if needed)")

# 3. Rating Selection
rating = st.slider("How would you rate your experience?", 1, 5, 5)

# 4. Photo Upload for Authenticity
uploaded_file = st.file_uploader("Upload a photo of your car/service experience (Optional)", type=["png", "jpg", "jpeg"])

# 5. Comments/Keywords
keywords = st.text_input("Describe your experience in a few keywords (e.g., supper glossy, fast, friendly)", "")

if st.button("Submit Feedback"):
    if not cust_name or not cust_phone:
        st.warning("Please enter your name and phone number to proceed.")
    else:
        # Check if it's a bad review (1 or 2 stars) vs good review (3, 4, 5 stars)
        if rating <= 2:
            st.error("Thank you for your feedback. We sincerely apologize that your experience didn't meet expectations.")
            st.info("Our management team has received your submission and our staff will contact you shortly to resolve this matter.")
        else:
            st.success("Thank you so much for your wonderful feedback!")
            
            # Simple spellcheck / keyword cleanup simulation
            # In production with Ollama, you would prompt the AI to auto-correct typos like "supper" -> "super"
            corrected_keywords = keywords.replace("supper", "super")
            
            star_str = "⭐" * rating
            generated_reviews = [
                f"{star_str}\nAbsolute game-changer! As a {cust_type.lower()}, I experienced top-tier service. {corrected_keywords}. Highly recommend! #CustomerReview #LocalBusiness",
                f"{star_str}\nSuper impressed with the service today! ({corrected_keywords}). Will definitely be coming back again! 🚗✨ #Review #TopService",
                f"{star_str}\nA fantastic experience. They are truly professional and handled everything with care. {corrected_keywords}. 5/5 stars easily! 🙌 #Excellence"
            ]
            
            st.markdown("### Share Your Experience!")
            st.write("Copy your favorite review below, then tap a button to open your preferred social app:")
            
            for i, rev in enumerate(generated_reviews, 1):
                st.text_area(f"Review Option {i}", rev, height=100)
                
            # HTML/JS buttons for deep-linking into Instagram and Xiaohongshu (XHS)
            st.markdown("""
                <div style="display: flex; gap: 10px; margin-top: 15px;">
                    <a href="instagram://" target="_blank" style="flex: 1; text-align: center; background: #E1306C; color: white; padding: 12px; border-radius: 8px; text-decoration: none; font-weight: bold;">Open Instagram 📸</a>
                    <a href="xhs://app" target="_blank" style="flex: 1; text-align: center; background: #FF2442; color: white; padding: 12px; border-radius: 8px; text-decoration: none; font-weight: bold;">Open Xiaohongshu (小红书) 📕</a>
                </div>
            """, unsafe_allow_html=True)
            
            st.info("💡 **Tip:** Copy your review text above first, then click the button to launch the app!")
