import streamlit as st
from instagrapi import Client

# Streamlit UI
st.set_page_config(page_title="Instagram Unfollowers Checker", layout="wide")

st.title("📸 Instagram Unfollowers Checker")
st.markdown("Find out who **unfollowed** you on Instagram!")

# Input fields for login
username = st.text_input("📧 Instagram Username", value="", placeholder="Enter your username")
password = st.text_input("🔒 Instagram Password", value="", type="password", placeholder="Enter your password")

# Login button
if st.button("🔑 Login & Fetch Data"):
    if username and password:
        try:
            # Initialize Instagram Client
            cl = Client()
            cl.login(username, password)

            # Fetch followers
            st.info("Fetching followers... ⏳")
            followers = cl.user_followers(cl.user_id)
            followers_set = set(followers.keys())

            # # Fetch following
            st.info("Fetching following... ⏳")
            following = cl.user_following(cl.user_id)
            following_set = set(following.keys())

            # Find Unfollowers (People you follow but they don't follow back)
            unfollowers = following_set - followers_set

            if unfollowers:
                st.warning("🚨 Unfollowers found!")
                for user_id in unfollowers:
                    user_info = cl.user_info(user_id)
                    col1, col2, col3 = st.columns([1, 3, 1])
                    
                    with col1:
                        str_image_url = str(user_info.profile_pic_url)
                        st.image(str_image_url, width=50)
                    
                    with col2:
                        str_url = f"[{user_info.full_name}](https://instagram.com/{user_info.username})"
                        st.write(str_url)
                    
                    with col3:
                        str_unfollow = f"Unfollow {user_info.username}"
                        if st.button(str_unfollow, key=user_info.username):
                            cl.user_unfollow(user_id)
                            st.success(f"✅ Unfollowed {user_info.username}")

            else:
                st.success("✅ No unfollowers! Everyone follows you back.")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

    else:
        st.warning("⚠️ Please enter both username and password!")
