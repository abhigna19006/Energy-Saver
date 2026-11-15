import streamlit as st
from pathlib import Path

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Energy Saver Bot",
    page_icon="💬",
    layout="wide"
)

# LOAD CSS
ROOT = Path(__file__).resolve().parents[1]
css_path = ROOT / "styles" / "style.css"

if css_path.exists():
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True
    )

# CHATBOT KNOWLEDGE BASE
responses = {
    "fan": (
        "🌀 **Fan Saving Tips**\n\n"
        "- Switch off fans when leaving a room.\n"
        "- Use a suitable speed instead of maximum speed all the time.\n"
        "- Clean fan blades regularly.\n"
        "- Consider energy-efficient fans when replacing old ones."
    ),
    "light": (
        "💡 **Lighting Saving Tips**\n\n"
        "- Switch off lights when not needed.\n"
        "- Replace traditional bulbs with LED bulbs.\n"
        "- Make maximum use of natural sunlight.\n"
        "- Avoid unnecessary outdoor lighting."
    ),
    "ac": (
        "❄️ **Air Conditioner Saving Tips**\n\n"
        "- Set a comfortable temperature, such as 24–26°C.\n"
        "- Clean AC filters regularly.\n"
        "- Keep doors and windows closed while cooling.\n"
        "- Use fans along with AC when appropriate."
    ),
    "bill": (
        "💰 **Electricity Bill Reduction Tips**\n\n"
        "- Switch off unused appliances.\n"
        "- Avoid leaving devices on standby.\n"
        "- Use energy-efficient appliances.\n"
        "- Monitor monthly electricity consumption."
    ),
    "saving": (
        "🌱 **General Energy-Saving Tips**\n\n"
        "- Turn off unused electrical devices.\n"
        "- Prefer LED lighting.\n"
        "- Use natural ventilation whenever possible.\n"
        "- Monitor electricity consumption regularly.\n"
        "- Avoid unnecessary energy wastage."
    ),
    "washing": (
        "🧺 **Washing Machine Tips**\n\n"
        "- Run full loads when practical.\n"
        "- Prefer cold-water washing when suitable.\n"
        "- Avoid unnecessary wash cycles.\n"
        "- Switch off the machine after use."
    ),
    "fridge": (
        "🧊 **Refrigerator Saving Tips**\n\n"
        "- Avoid opening the refrigerator frequently.\n"
        "- Check that the door seals properly.\n"
        "- Allow hot food to cool before storing it.\n"
        "- Maintain suitable temperature settings."
    ),
    "solar": (
        "☀️ **Solar Energy Information**\n\n"
        "- Solar panels convert sunlight into electricity.\n"
        "- Use solar energy during available sunlight hours.\n"
        "- Keep solar panels clean for better performance.\n"
        "- Monitor solar energy generation regularly."
    ),
    "battery": (
        "🔋 **Battery Energy Tips**\n\n"
        "- Use stored battery energy efficiently.\n"
        "- Avoid unnecessary charging and discharging.\n"
        "- Follow the manufacturer's maintenance instructions.\n"
        "- Monitor battery performance regularly."
    ),
    "grid": (
        "⚡ **Grid Electricity Information**\n\n"
        "- Grid electricity is supplied through the electrical power network.\n"
        "- Switch off unused appliances.\n"
        "- Use energy-efficient devices.\n"
        "- Make use of available solar energy."
    ),
    "peak": (
        "📊 **Peak Consumption Information**\n\n"
        "Peak consumption refers to periods or records where electricity "
        "usage is relatively high.\n\n"
        "- Identify high-consumption periods.\n"
        "- Avoid running multiple high-power appliances unnecessarily.\n"
        "- Monitor electricity usage regularly."
    ),
    "electricity": (
        "⚡ **Electricity Consumption Tips**\n\n"
        "- Switch off appliances when not in use.\n"
        "- Use LED lights and efficient appliances.\n"
        "- Avoid unnecessary standby power.\n"
        "- Monitor electricity consumption regularly."
    )
}


# RESPONSE FUNCTION
def get_response(message):
    message = message.lower().strip()
    words = message.split()

    if any(word in words for word in ["hello", "hi", "hey"]):
        return (
            "Hello! 👋 Welcome to Energy Saver Bot.\n\n"
            "I'm here to help you understand electricity usage "
            "and discover practical ways to save energy. "
            "What would you like to know?"
        )

    if "thank" in message:
        return (
            "You're welcome! 🌱\n\n"
            "Keep saving energy and protecting our planet."
        )

    if any(phrase in message for phrase in [
        "who are you", "your name", "what can you do"
    ]):
        return (
            "🤖 I'm Energy Saver Bot!\n\n"
            "I provide simple guidance about electricity consumption, "
            "energy-saving methods, solar power, batteries, and appliances."
        )

    if any(word in message for word in ["peak consumption", "peak usage", "peak"]):
        return responses["peak"]

    if any(word in message for word in ["electricity bill", "power bill", "bill"]):
        return responses["bill"]

    if any(word in message for word in ["washing machine", "washing", "laundry"]):
        return responses["washing"]

    if any(word in message for word in ["refrigerator", "fridge"]):
        return responses["fridge"]

    if "air conditioner" in message or "ac" in words:
        return responses["ac"]

    if "solar" in message or "sunlight" in message:
        return responses["solar"]

    if "battery" in message or "batteries" in message:
        return responses["battery"]

    if "grid" in words:
        return responses["grid"]

    if "fan" in words or "fans" in words:
        return responses["fan"]

    if "light" in words or "lights" in words or "bulb" in words:
        return responses["light"]

    if any(word in message for word in ["electricity", "consumption", "power usage"]):
        return responses["electricity"]

    if any(word in message for word in ["save", "saving", "energy", "wastage"]):
        return responses["saving"]

    return (
        "I'm still learning about that topic. 😊\n\n"
        "You can ask me about:\n"
        "- Fans and lights\n"
        "- Air conditioners\n"
        "- Electricity bills\n"
        "- Solar energy and batteries\n"
        "- Peak consumption\n"
        "- General energy-saving tips"
    )


# HEADER
st.title("💬 Energy Saver Bot")
st.caption("Your smart companion for everyday energy-saving guidance.")
st.divider()

# INTRODUCTION
st.markdown(
    """
    <div class="hero">
        <div class="hero-tag">🌿 YOUR ENERGY-SAVING ASSISTANT</div>
        <h1>Ask. Learn.<br>Save Energy.</h1>
        <p>
            Get simple and practical suggestions for reducing
            electricity consumption in your daily life.
        </p>
        <div class="hero-icon">🤖</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-heading">Start a Conversation</div>',
    unsafe_allow_html=True
)

# INITIALIZE CHAT
if "energy_messages" not in st.session_state:
    st.session_state.energy_messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋 I'm your Energy Saver Bot. "
                "Ask me how to save electricity at home."
            )
        }
    ]

# DISPLAY CHAT HISTORY
for message in st.session_state.energy_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# USER INPUT
user_input = st.chat_input("Ask me about saving electricity...")

if user_input:
    st.session_state.energy_messages.append(
        {"role": "user", "content": user_input}
    )

    answer = get_response(user_input)

    st.session_state.energy_messages.append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()

# SUGGESTED QUESTIONS
st.markdown(
    '<div class="section-heading">Quick Questions</div>',
    unsafe_allow_html=True
)

questions = [
    "How can I save electricity using AC?",
    "How can I reduce my electricity bill?",
    "How can I save energy using fans?",
    "What is peak consumption?",
    "How does solar energy help?",
    "Give me general energy-saving tips."
]

for question in questions:
    if st.button(question, use_container_width=True):
        st.session_state.energy_messages.append(
            {"role": "user", "content": question}
        )

        answer = get_response(question)

        st.session_state.energy_messages.append(
            {"role": "assistant", "content": answer}
        )

        st.rerun()

# CLEAR CHAT
if st.button("🗑️ Clear Conversation"):
    st.session_state.energy_messages = [
        {
            "role": "assistant",
            "content": "Hello! 👋 I'm your Energy Saver Bot. How can I help you?"
        }
    ]
    st.rerun()

# FOOTER
st.markdown(
    '<div class="footer">ENERGY SAVER | Smart Energy Assistant</div>',
    unsafe_allow_html=True
)