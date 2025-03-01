import streamlit as st


genai.configure(api_key="AIzaSyAmfGknEYmN6fNQJlk8TG1kWkEUKFH96e8")

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_itinerary(destination, duration):
    """Generates a travel itinerary using Gemini API."""
    prompt = f"""
    Generate a complete travel itinerary for a trip to {destination} lasting {duration}.

    Include:
    - Places to visit (with brief descriptions)
    - Food recommendations (local cuisine)
    - Activities (e.g., tours, experiences)

    Format the itinerary in a structured way, separating each day and section clearly.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating itinerary: {e}"

# Streamlit App
def main():
    st.title("AI-Based Travel Itinerary Generator")

    destination = st.text_input("Enter your travel destination:")
    duration = st.text_input("Enter the duration of your trip (e.g., 3 days, 1 week):")

    if st.button("Generate Itinerary"):
        if destination and duration:
            with st.spinner("Generating itinerary..."):
                itinerary = generate_itinerary(destination, duration)
                st.markdown(itinerary)
        else:
            st.warning("Please enter both destination and duration.")

if __name__ == "__main__":
    main()
