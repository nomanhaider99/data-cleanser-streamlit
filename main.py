import streamlit as st

def main():
    st.set_page_config(page_title="Growth Mindset Challenge", page_icon="📈", layout="centered")
    
    st.title("Growth Mindset Challenge")
    
    st.header("What is a Growth Mindset?")
    st.write("A growth mindset is the belief that your abilities and intelligence can be developed through hard work, perseverance, and learning from your mistakes.")
    
    st.header("Why Adopt a Growth Mindset?")
    st.markdown("- **Embrace Challenges:** View obstacles as opportunities to learn rather than as setbacks.")
    st.markdown("- **Learn from Mistakes:** Making mistakes is a natural part of learning and improvement.")
    st.markdown("- **Persist Through Difficulties:** Stay determined, even when things get tough.")
    st.markdown("- **Celebrate Effort:** Recognize and reward the effort put into learning.")
    st.markdown("- **Keep an Open Mind:** Stay curious and adaptable.")
    
    st.header("How Can You Practice a Growth Mindset?")
    st.write("1. **Set Learning Goals:** Focus on developing new skills and understanding complex concepts.")
    st.write("2. **Reflect on Your Learning:** Take time to evaluate what you've learned from successes and challenges.")
    st.write("3. **Seek Feedback:** Embrace constructive criticism for improvement.")
    st.write("4. **Stay Positive:** Believe in your ability to grow and encourage others to do the same.")
    
    st.subheader("Your Growth Mindset Commitment")
    name = st.text_input("Enter your name")
    commitment = st.text_area("How will you adopt a growth mindset?")
    if st.button("Submit"):
        if name and commitment:
            st.success(f"Thank you, {name}! Your commitment to a growth mindset has been recorded.")
        else:
            st.warning("Please fill out both fields before submitting.")
    
if __name__ == "__main__":
    main()
