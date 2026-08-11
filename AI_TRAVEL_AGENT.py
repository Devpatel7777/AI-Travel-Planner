from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import tool
from langchain.agents import create_agent


# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="Smart AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)


# ============================================================
# MODEL
# ============================================================

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2,
    max_tokens=1800
)


# ============================================================
# GOOGLE SEARCH
# ============================================================

search = GoogleSerperAPIWrapper()


@tool
def google_search(query: str) -> str:
    """
    Search current travel information using Google.
    """
    return search.run(query)


# ============================================================
# SYSTEM PROMPT
# ============================================================

system_prompt = """
You are Smart AI Travel Planner.

Your job is to create realistic, personalized and budget-aware
travel plans.

IMPORTANT:
Do NOT blindly create a trip.

First analyze:

1. Destination
2. Domestic or International
3. Number of travelers
4. Travel type
5. Number of days
6. Budget
7. Hotel preference
8. Food preference
9. Interests

============================================================
TRANSPORT RULES
============================================================

INTERNATIONAL:

Origin City
→ Origin Airport
→ International Flight
→ Destination Airport
→ Airport Transfer
→ Hotel
→ Local Transport
→ Attractions
→ Destination Airport
→ Return Flight
→ Origin Airport

International trips must normally use flight for
origin-to-destination travel.

Also consider:
- Visa
- Passport requirements
- Travel insurance
- Baggage
- Airport transfers

DOMESTIC:

Choose the best practical option:

Flight / Train / Bus / Car

Consider:
- Distance
- Travel time
- Cost
- Comfort
- Budget

============================================================
TRAVELER PERSONALIZATION
============================================================

SOLO:
Flexible, affordable, safe and experience-focused.

FAMILY:
Comfortable hotels, family-friendly attractions,
less exhausting schedule.

COUPLE / HUSBAND & WIFE:
Romantic experiences, scenic places, comfortable hotels,
romantic restaurants and relaxation.

FRIENDS:
Adventure, fun, nightlife, group activities and budget sharing.

FRIENDS + COUPLE:
Balance group activities with couple-friendly experiences.

CHILDREN:
Include child-friendly places.

SENIORS:
Reduce walking and keep the itinerary relaxed.

============================================================
BUDGET FEASIBILITY
============================================================

Calculate approximate:

Transport
+ Hotel
+ Food
+ Local Transport
+ Activities
+ Airport Transfers
+ Visa (if applicable)
+ Insurance
+ Baggage
+ Miscellaneous

Compare the estimated total with the user's budget.

STATUS:

🟢 FEASIBLE
Estimated cost <= budget

🟡 FEASIBLE WITH CONDITIONS
Slightly above budget but can work by reducing cost.

🔴 NOT FEASIBLE
Clearly above budget.

If NOT FEASIBLE:

DO NOT create a fake itinerary.

Instead show:

- User Budget
- Minimum Estimated Cost
- Budget Gap
- Main Reasons
- Cheaper Alternatives

Possible alternatives:
- Reduce number of days
- Budget hotel
- Change transport
- Remove expensive activities
- Travel in cheaper season
- Suggest a cheaper destination

============================================================
CURRENT INFORMATION
============================================================

Use Google Search ONLY when current information is required.

Examples:
- Current flight information
- Current weather
- Current hotel prices
- Current transport information
- Current travel restrictions

Do not claim that general monthly weather is "current weather".

============================================================
OUTPUT
============================================================

Return concise but useful sections:

# Trip Feasibility

# Traveler Profile

# Transportation Plan

# Budget Analysis

# Hotel Suggestions

# Day-wise Itinerary

# Restaurants

# Shopping

# Current Weather

# Packing List

# Important Travel Warnings

# Best Alternative

Use tables when useful.

Never guarantee:
- Flight prices
- Hotel availability
- Visa approval
- Weather
- Transport schedules

Clearly mention that prices and availability must be verified.
"""


# ============================================================
# CREATE AGENT
# ============================================================

agent = create_agent(
    model=llm,
    tools=[google_search],
    system_prompt=system_prompt
)


# ============================================================
# HELPER
# ============================================================

def get_trip_profile(
    trip_type,
    members,
    children,
    seniors
):

    if trip_type == "Solo":
        return "Solo traveler: flexible, safe, affordable"

    if trip_type == "Couple / Husband & Wife":
        return "Couple: romantic, comfortable, scenic and relaxed"

    if trip_type == "Family":
        return (
            f"Family trip with {members} people, "
            f"{children} children and {seniors} seniors"
        )

    if trip_type == "Friends":
        return (
            f"Friends trip with {members} people: "
            "fun, adventure and group activities"
        )

    if trip_type == "Friends + Couple":
        return (
            f"Mixed friends/couple group with {members} people: "
            "group activities + couple-friendly experiences"
        )

    return "General travelers"


# ============================================================
# UI
# ============================================================

st.title("✈️ Smart AI Travel Planner")
st.caption(
    "AI-powered trip feasibility, transportation, budget and itinerary planning"
)


st.subheader("🌍 Trip Details")


col1, col2 = st.columns(2)


with col1:

    trip_type = st.selectbox(
        "Trip Type",
        [
            "Domestic",
            "International"
        ]
    )

    origin = st.text_input(
        "Starting City",
        placeholder="Example: Ahmedabad"
    )

    days = st.number_input(
        "Number of Days",
        min_value=1,
        max_value=30,
        value=4
    )


with col2:

    destination = st.text_input(
        "Destination City / Country",
        placeholder="Example: Leh, Dubai, Paris"
    )

    budget = st.number_input(
        "Total Budget (₹)",
        min_value=1000,
        value=50000,
        step=1000
    )


# ============================================================
# TRAVELER
# ============================================================

st.subheader("👥 Traveler Details")


travel_type = st.selectbox(
    "Who is travelling?",
    [
        "Solo",
        "Family",
        "Couple / Husband & Wife",
        "Friends",
        "Friends + Couple"
    ]
)


members = 1
children = 0
seniors = 0


if travel_type == "Solo":

    members = 1


elif travel_type == "Couple / Husband & Wife":

    members = 2

    st.info(
        "💑 Couple trip: romantic and comfortable planning will be used."
    )


elif travel_type == "Family":

    members = st.number_input(
        "Total Family Members",
        min_value=2,
        max_value=20,
        value=4
    )

    children = st.number_input(
        "Number of Children",
        min_value=0,
        max_value=15,
        value=0
    )

    seniors = st.number_input(
        "Senior Citizens",
        min_value=0,
        max_value=10,
        value=0
    )


elif travel_type == "Friends":

    members = st.number_input(
        "Number of Friends",
        min_value=2,
        max_value=20,
        value=3
    )


elif travel_type == "Friends + Couple":

    members = st.number_input(
        "Total People",
        min_value=3,
        max_value=20,
        value=4
    )


# ============================================================
# PREFERENCES
# ============================================================

st.subheader("🏨 Preferences")


col3, col4 = st.columns(2)


with col3:

    hotel_type = st.selectbox(
        "Hotel Preference",
        [
            "Budget",
            "Standard",
            "Luxury"
        ]
    )


with col4:

    food_type = st.selectbox(
        "Food Preference",
        [
            "Veg",
            "Non-Veg",
            "Both"
        ]
    )


interests = st.multiselect(
    "Interests",
    [
        "Adventure",
        "Nature",
        "Beaches",
        "Historical Places",
        "Culture",
        "Shopping",
        "Nightlife",
        "Food",
        "Photography",
        "Relaxation",
        "Romantic Experiences",
        "Spiritual Places"
    ]
)


trip_pace = st.select_slider(
    "Trip Pace",
    options=[
        "Relaxed",
        "Balanced",
        "Fast"
    ],
    value="Balanced"
)


# ============================================================
# GENERATE
# ============================================================

st.divider()


if st.button(
    "🚀 Check Feasibility & Create Trip",
    use_container_width=True
):

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    if not origin.strip():

        st.warning("Please enter starting city.")

        st.stop()


    if not destination.strip():

        st.warning("Please enter destination.")

        st.stop()


    # --------------------------------------------------------
    # PROFILE
    # --------------------------------------------------------

    profile = get_trip_profile(
        travel_type,
        members,
        children,
        seniors
    )


    interest_text = (
        ", ".join(interests)
        if interests
        else "General sightseeing"
    )


    # --------------------------------------------------------
    # COMPACT PROMPT
    # --------------------------------------------------------

    prompt = f"""
Create a realistic travel plan.

ORIGIN:
{origin}

DESTINATION:
{destination}

TRIP TYPE:
{trip_type}

DAYS:
{days}

BUDGET:
₹{budget}

TRAVEL GROUP:
{travel_type}

MEMBERS:
{members}

CHILDREN:
{children}

SENIORS:
{seniors}

HOTEL:
{hotel_type}

FOOD:
{food_type}

INTERESTS:
{interest_text}

TRIP PACE:
{trip_pace}

TRAVELER PROFILE:
{profile}

==================================================
FIRST: FEASIBILITY
==================================================

Estimate realistic total cost.

Include:

Transport
Hotel
Food
Local Transport
Activities
Airport Transfer
Visa if international
Insurance
Baggage
Miscellaneous

Compare total with ₹{budget}.

If clearly impossible:

Status = 🔴 NOT FEASIBLE

Show:
- Budget
- Estimated minimum cost
- Budget gap
- Why impossible
- 3 cheaper alternatives

DO NOT generate a fake day-wise itinerary.

If slightly difficult:

Status = 🟡 FEASIBLE WITH CONDITIONS

Explain conditions.

If realistic:

Status = 🟢 FEASIBLE

Create complete plan.

==================================================
TRANSPORT
==================================================

International:
Flight for origin → destination.

Domestic:
Choose Flight / Train / Bus / Car based on
cost, time and convenience.

Include:

Origin → Airport/Station
→ Main Transport
→ Destination
→ Local Transport
→ Attractions
→ Return Transport
→ Origin

==================================================
FINAL OUTPUT
==================================================

# ✈️ Trip Feasibility

# 👥 Traveler Profile

# 🚆✈️ Transportation Plan

# 💰 Budget Analysis

# 🏨 Hotel Suggestions

# 📅 Day-wise Itinerary

# 🍽️ Restaurants

# 🛍️ Shopping

# 🌦️ Current Weather

# 🎒 Packing List

# ⚠️ Important Travel Warnings

# 💡 Best Alternative

Use tables where useful.

Be concise.

Use Google Search only where current information is needed.

Never guarantee prices or availability.
"""


    # ========================================================
    # AI
    # ========================================================

    with st.spinner(
        "✈️ Checking feasibility and planning your trip..."
    ):

        try:

            response = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                }
            )


            answer = response[
                "messages"
            ][-1].content


            st.success(
                "✅ Trip analysis completed!"
            )


            st.divider()


            st.markdown(answer)


            st.divider()


            st.caption(
                "⚠️ Travel prices, availability, weather, "
                "visa rules and transport schedules can change. "
                "Verify final information before booking."
            )


        except Exception as e:

            error = str(e)


            if (
                "413" in error
                or "tokens per minute" in error
                or "rate_limit_exceeded" in error
            ):

                st.error(
                    "⚠️ Free API token limit reached. "
                    "Please wait and try again."
                )

            else:

                st.error(
                    "Unable to generate the trip plan."
                )

                st.exception(e)


