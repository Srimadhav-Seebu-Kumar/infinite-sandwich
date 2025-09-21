import streamlit as st
import random
import requests
from PIL import Image
import pandas as pd
from datetime import datetime

# Mock data for demonstration
INGREDIENTS = [
    "quantum mustard", "dream bread", "crystallized bacon", "temporal lettuce", 
    "interdimensional cheese", "probability pickles", "synthetic salami", "holographic ham",
    "nano-tomatoes", "virtual vinegar", "algorithmic avocado", "binary bologna",
    "digital dill", "fractal fish", "compressed cucumber", "encrypted eggplant"
]

FLAVORS = [
    "bewildering", "transcendent", "questionable", "revolutionary", "abstract",
    "paradoxical", "ephemeral", "chaotic", "sublime", "absurd", "magnificent",
    "incomprehensible", "surreal", "mystical", "bizarre", "extraordinary"
]

def generate_sandwich():
    """Generate a random nonsense sandwich with scoring."""
    num_ingredients = random.randint(3, 8)
    ingredients = random.sample(INGREDIENTS, num_ingredients)
    flavor = random.choice(FLAVORS)
    
    # Mock scoring based on "trained models"
    absurdity_score = round(random.uniform(1, 10), 2)
    creativity_score = round(random.uniform(1, 10), 2) 
    edibility_score = round(random.uniform(0.1, 3.2), 2)  # Intentionally low
    
    total_score = round((absurdity_score + creativity_score + edibility_score) / 3, 2)
    
    return {
        "name": f"The {flavor.title()} {random.choice(['Delight', 'Surprise', 'Mystery', 'Experience', 'Adventure'])}",
        "ingredients": ingredients,
        "flavor_profile": flavor,
        "scores": {
            "absurdity": absurdity_score,
            "creativity": creativity_score,
            "edibility": edibility_score,
            "total": total_score
        },
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def main():
    st.set_page_config(
        page_title="Infinite Sandwich Generator",
        page_icon="🥪",
        layout="wide"
    )
    
    st.title("🥪 Infinite Sandwich Generator")
    st.markdown(
        """**Absurdist, generative project that builds nonsense sandwiches from real and fictional ingredients, 
        scored by models trained on random data.**"""
    )
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col2:
        if st.button("Generate New Sandwich", type="primary"):
            if "sandwich_history" not in st.session_state:
                st.session_state.sandwich_history = []
            
            new_sandwich = generate_sandwich()
            st.session_state.sandwich_history.insert(0, new_sandwich)
            st.session_state.current_sandwich = new_sandwich
    
    with col3:
        if st.button("Clear History"):
            st.session_state.sandwich_history = []
            if "current_sandwich" in st.session_state:
                del st.session_state.current_sandwich
    
    # Display current sandwich
    if "current_sandwich" in st.session_state:
        sandwich = st.session_state.current_sandwich
        
        st.header(f"✨ {sandwich['name']}")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("🥗 Ingredients")
            for ingredient in sandwich['ingredients']:
                st.write(f"• {ingredient}")
            
            st.subheader(f"🎭 Flavor Profile: {sandwich['flavor_profile'].title()}")
        
        with col2:
            st.subheader("📊 AI Scores")
            scores = sandwich['scores']
            st.metric("Absurdity", f"{scores['absurdity']}/10")
            st.metric("Creativity", f"{scores['creativity']}/10")
            st.metric("Edibility", f"{scores['edibility']}/10", help="Lower is more realistic")
            st.metric("**Total Score**", f"**{scores['total']}/10**")
        
        st.info(f"Generated at: {sandwich['generated_at']}")
    
    # Sandwich history
    if "sandwich_history" in st.session_state and st.session_state.sandwich_history:
        st.header("📜 Sandwich History")
        
        # Create dataframe for history
        history_data = []
        for sandwich in st.session_state.sandwich_history[:10]:  # Show last 10
            history_data.append({
                "Name": sandwich['name'],
                "Ingredients": len(sandwich['ingredients']),
                "Flavor": sandwich['flavor_profile'].title(),
                "Total Score": sandwich['scores']['total'],
                "Generated": sandwich['generated_at']
            })
        
        df = pd.DataFrame(history_data)
        st.dataframe(df, use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "🤖 *Powered by completely fictional AI models and random number generators. "
        "No actual sandwiches were harmed in the making of this application.*"
    )

if __name__ == "__main__":
    main()
