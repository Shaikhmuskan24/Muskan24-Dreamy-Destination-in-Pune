import requests
import streamlit as st


st.set_page_config(page_title="DREAMY DESTINATION IN PUNE",page_icon=":tada:",layout="wide")


st. title("DREAMY DESTINATION IN PUNE")
st.header("It's Time To Travel :bus:")
st.subheader("Let's gooo...")
st.markdown("I LOVE TRAVELLING, PLAN YOUR TRIP.")

name=st.text_input("Enter your name:")
venue=st.text_input("Enter your venue:")
adr=st.text_input("Enter your travelling date:")
ph=st.text_input("Enter your contact number:")
classmethod=st.selectbox("How many days want to stay:",(1,2,3,4,5,6,7))

button=st.button("Done")
if button:
    st.markdown(f"""
    name:{name}
    address:{adr}
    venue:{...}
    ph:{...}
    class:{classmethod}
    """)


st.markdown("Enjoy your holiday with our tour packages from Pune that let you dive into the beauties of nature;"
            " enjoy your vacation with our ranges customized just for your needs and preferences.")

with st.container():
    st.write("---")
    left_column, right_column=st.columns(2)
    with left_column:
        st.subheader("Tour Packages From Pune")
        st.markdown("""
              * Dagdusheth Temple
              * Tamini ghat
              * malshej ghat
              * Purandhar
              * Singhar
              * Panshet
              * Pavna Dam
              * Alibag
              * Murud
              * Lonavala
              """)

        with right_column:
            st.subheader("Packages")
            st.markdown("""
            * solo               -   5000
            * Couples            -   10000
            * Family(8/10 limit) -   20000
            """)

st.snow()
st.subheader("Different Types Of Tour Packages")
st.markdown("While you are planning to visit any of these above places for "
            "a vacation, here are a few tour options that you can choose to take")

st.markdown("""
            * 1. Adventure Tour:djhf Best Places: Khansum Yulley-Bhutan, Palm Jumeirah-Dubai, iFly Singapore
            Safety Measures: Wear comfortable pair of shoes, Walk carefully through the path, follow all the instructions given by 
            the instructors
            Is Adventure tour right for: If you love to go on trekking and hiking expeditions or indulge 
            in activities like rafting and rock climbing, this tour is best for you.
            What to do: Hiking, trekking, rock climbing, kayaking
            The adventure tour to these places will include all the activities that will give you thrills on your vacation. 
            These include activities like hiking, trekking, camping and other such adventure activities.
            * 2. Wildlife Tour:Best Places: Jigme Singye Wangchuck National Park, Night safari- Singapore 
            Safety Measures: Avoid wearing dark colored clothes, do not step out of the safari till asked to do so, carry
            torches on night safari Is wildlife tour right for us: If you are a nature lover and also a wildlife enthusiast,
            this tour is perfect for you What to do: Night safari, jungle safari, walking tours A tour through the natural 
            jungles is the best way to get to know the wildlife of the area. The wildlife tour will get you close to the 
            flora and fauna in Bhutan. There are a lot of places at these destinations where you can venture out for
            this tour.
            * 3. Religious Tour:Best Places: Tashichho Dzong, Buddha Tooth Relic Temple-Singapore, Birla Mandir-Rajasthan 
            Safety Measures: Take care of your belongings Is religious tour right for us: If you are interested to explore 
            the monasteries and temples in Bhutan What to do: Sightseeing Those who wish to experience the spiritual side
            of Bhutan can venture on a religious tour. Bhutan is lined with beautiful monasteries and temples allowing 
            people to spend a peaceful time on their religious tour.   
            * 4. Camping Tour:Best Places: Bhutan, Dubai, Himachal, Rajasthan Safety Measures: Carry torches, take power
             backups, take care of your belongings Is Adventure tour right for us: If you love to do stargazing and enjoy
            mesmerizing views, this is the tour for you, What to do: Bonfire If you bored of the usual hotel rooms,
            taking a camping tour is a great option. You will get to stay in tents setup in beautiful locations and 
            offer mesmerising views.
            * 5. Trekking Tour:Best Places: Himachal, Bhutan Safety Measures: Wear sports shoes, carry extra battery
            backup Is Adventure tour right for us: If you love adventure, then this tour is perfect for you What to do:
            Exploring the wildlife The best tour for travelers who love to on trekking expeditions, this tour will let
            you enjoy the pleasant weather and serene surroundings of the place and also let you et close to the 
            natural wildlife of Pune.
            """)

st.markdown("_ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")