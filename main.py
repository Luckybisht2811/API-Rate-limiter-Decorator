import time
from functools import wraps
import streamlit as st

def token_bucket(rate_limit, window_reset):
    tokens = rate_limit
    window_start = time.time()

    while True:
        current_time = time.time()
        elapsed = current_time - window_start

        if elapsed >= window_reset:
            st.toast("Tokens reset after window expired.")
            tokens = rate_limit
            window_start = current_time

        if tokens > 0:
            yield tokens, int(window_reset - elapsed)
            tokens -= 1
        else:
            yield 0, int(window_reset - elapsed)
        
        time.sleep(0.5)

def rate_limiter_decorator(generator):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            tokens, remaining_time = next(generator)
            if tokens > 0:
                st.success(f"Allowed. Tokens left: {tokens}")
                st.progress(tokens / 3, text="Token usage")
                st.write(f"Window resets in {remaining_time} seconds.")
                return func(*args, **kwargs)
            else:
                st.error(f"Rate limit exceeded. Try again after {remaining_time} sec.")
                st.progress(0, text="No tokens left")
        return wrapper
    return decorator

# ---------- Streamlit UI Code -----------
st.set_page_config(page_title="API Rate Limiter Demo", layout="centered")

st.title("🚦 API Rate Limiter with Streamlit")
st.caption("**This app allows up to 3 API requests every 10 minutes (600 sec window).**")

# store generator across reruns
if "token_gen" not in st.session_state:
    st.session_state.token_gen = token_bucket(rate_limit=3, window_reset=600)
    st.session_state.rate_limiter = rate_limiter_decorator(st.session_state.token_gen)
    st.session_state.last_call = None

@st.session_state.rate_limiter
def fetch_data():
    st.success("Data fetched successfully!")
    st.session_state.last_call = time.strftime("%Y-%m-%d %H:%M:%S")

# Layout
col1, col2 = st.columns(2)
with col1:
    if st.button("Fetch Data"):
        fetch_data()
with col2:
    st.metric("Last Fetch Time", st.session_state.last_call or "Never")

st.info("Try hitting the button multiple times to see the rate limiter in action.")

st.markdown(
    """
    ---
    **Tech Stack:** Python + Streamlit + Decorators + Generators  
    **Author:** Your Name  
    """
)
