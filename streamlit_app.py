import streamlit as st


def classify_sleep_personality(data):
    if "Irregular" in data["schedule_consistency"] or "Very irregular" in data["schedule_consistency"]:
        return "Irregular Sleeper"
    if "Always" or "Often" or "Sometimes" or "Never" in data["screens_after_10pm"]:
        if data["stress_level"] >= 3:
            if "Studying" in data["reason_for_sleep_late"] :
                return "Stressed Student"
    if "Always" in data["screens_after_10pm"] or "Often" in data["screens_after_10pm"]:
        if "Social media scrolling" in data["reason_for_sleep_late"]:
            return "Doom Scroller"
    elif not "Never" in data["screens_after_10pm"]:
        if "Social media scrolling" in data["reason_for_sleep_late"]:
            return "Revenge Bedtime Procrastinator"
    else:
        return "Balanced Sleeper"


def get_recommendations(profile):
    recs = {
        "Doom Scroller": ["Set app limits after 10pm", "Switch to offline activities like journaling or reading"],
        "Revenge Bedtime Procrastinator": ["Set a fixed bedtime alarm", "Reward yourself with morning leisure instead of late-night scrolling"],
        "Stressed Student": ["Try meditation or breathing exercises before bed", "Finish school tasks earlier in the evening"],
        "Irregular Sleeper": ["Stick to consistent sleep/wake times", "Avoid late meals and caffeine"],
        "Balanced Sleeper": ["Maintain your current routine", "Keep screens limited before bed"]
    }
    return recs.get(profile, [])


st.title("🌙 Sleep Tracker & Advisor")


#QUESTIONS FOR USERS TO CALC THEIR SLEEP QUALITY SCORE
sleep_quality = st.selectbox("How do you usually feel after waking up?", ["Energised", "Normal", "Slightly tired", "Very tired"])
sleep_latency = st.selectbox("How long does it usually take for you to fall asleep?", ["Less than 10 mins", "10-20 mins", "20-40 mins", "More than 40 mins"])
#sleep_duration = st.selectbox("How many hours of sleep do you usually get?", ["More than 9 hours", "7-9 hours", "4-6 hours", "Less than 4 hours"])
sleep_disturbance = st.selectbox("How often do you wake up during the night?", ["Never", "Rarely", "Sometimes", "Often", "Always"])
daytime_dysfunction = st.selectbox("How often do you struggle to stay awake and focus during the day?", ["Never", "Rarely", "Sometimes", "Often", "Always"])

go_to_sleep = st.select_slider("What time do you usually go to sleep? (option starts from 8pm till 3am)", [8,9,10,11,12,1,2,3])
wake_up = st.slider("What time do you usually wake up? (option starts from 5am till 12pm)", 5,12)
score = 0

if go_to_sleep>=8 and go_to_sleep <=12:
    sleep_duration = (12-go_to_sleep) + wake_up
elif go_to_sleep>=1 and go_to_sleep<=3:
    sleep_duration = wake_up-go_to_sleep

sleep_button = st.checkbox("Calculate sleep duration")
if sleep_button:
    st.write(sleep_duration)



#Calculating sleep quality
if sleep_quality == "Energised":
    score +=0
elif sleep_quality == "Normal":
    score +=1
elif sleep_quality == "Slightly tired":
    score +=2
elif sleep_quality == "Very tired":
    score +=3


#Calculating sleep latency
if sleep_latency == "Less than 10 mins":
    score +=0
elif sleep_latency == "10-20 mins":
    score +=1
elif sleep_latency == "20-40 mins":
    score +=2
elif sleep_latency == "More than 40 mins":
    score +=3


#Calculating sleep duration
if (sleep_duration>=7 and sleep_duration <=9):
    score +=0
elif (sleep_duration>9):
    score +=1
elif (sleep_duration>=4 and sleep_duration <7):
    score +=2
elif (sleep_duration <4):
    score +=3


#Calculating sleep disturbance
if sleep_disturbance == "Never":
    score +=0
elif sleep_disturbance == "Rarely":
    score +=1
elif sleep_disturbance == "Sometimes":
    score +=2
elif sleep_disturbance == "Often":
    score +=3
elif sleep_disturbance == "Always":
    score +=4


#Calculating daytime dysfunction
if daytime_dysfunction == "Never":
    score +=0
elif daytime_dysfunction == "Rarely":
    score +=1
elif daytime_dysfunction == "Sometimes":
    score +=2
elif daytime_dysfunction == "Often":
    score +=3
elif daytime_dysfunction == "Always":
    score +=4


score_button = st.checkbox("Calculate sleep score")
if score_button:
    if score <= 4:
        st.write(score)
        st.write("Amazing! You have a good sleep quality, keep it up!")
    else:
        st.write(score)
        #with st.form("Poor sleep score"):
            #st.write(score)
        st.write("Yikes! Your sleep quality is poor. :( But don’t worry! Please answer a few more questions below to discover your sleep personality and how to improve your sleep.")
            #st.image("https://i.pinimg.com/vwebp/736x/6b/d8/b3/6bd8b3c64dbce48dc60d37e735ddbb50.webp", width=100)




        screens = st.selectbox("How often do you use screens after 10pm?", ["Never","Sometimes","Often","Always"])
        stress = st.slider("How stressed do you feel before sleeping? (1:No stress, 5:Very stressed)", 1, 5, 3)
        schedule = st.selectbox("How consistent is your sleep schedule?", ["Mostly consistent","Irregular","Very irregular"])
        reason = st.multiselect("What activities do you usually do before sleeping?(Multiple choices allowed)", ["Social media scrolling", "Studying", "Gaming", "Watching shows/videos/movies", "Texting", "Listening to music", "Reading"])


        user_data = {
        "screens_after_10pm": screens,
        "stress_level": stress,
        "schedule_consistency": schedule,
        "reason_for_sleep_late": reason
            }


        profile = classify_sleep_personality(user_data)


        profile_output = st.checkbox("Generate sleep profile")
        if profile_output:    
            st.write("## :blue[😴 Your Sleep Personality]")
            st.write(f"### **{profile}**")

            if profile == "Irregular Sleeper":
                st.image("irregular slipper.jpg", width=300)
            elif profile == "Stressed Student":
                st.image("stressed student.jpg", width=300)
            elif profile == "Doom Scroller":
                st.image("doomscroller.jpg", width=300)
            elif profile == "Balanced Sleeper":
                st.image("IMG_0842.png", width=300)
            elif profile == "Revenge Bedtime Procrastinator":
                st.image("revenge procrastinator.jpg", width=300)


            st.write("## :yellow[💡 Recommendations]")
            for rec in get_recommendations(profile):
                st.write(f"- {rec}")
           
           
            st.write("Great! Now you know what to work on. You can enhance your sleep habits by following the recommendations provided above :D")




