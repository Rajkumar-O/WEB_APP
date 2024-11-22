import streamlit as st
st.title("2205A21028-PS4")

def STAR_DELTA(R1, R2, R3):
    R12=((R1*1000)*(R2*1000)+(R2*1000)*(R3*1000)+(R3*1000)*(R1*1000))/(R3*1000)
    R23=((R1*1000)*(R2*1000)+(R2*1000)*(R3*1000)+(R3*1000)*(R1*1000))/(R3*1000)
    R31=((R1*1000)*(R2*1000)+(R2*1000)*(R3*1000)+(R3*1000)*(R1*1000))/(R3*1000)
    return R12,R23,R31

  

st.write("Calulate the resistive values (R12,R23,R31)of the Delta connection network for the given STAR connection network having resistance R1,R2,R3")

    # Layout with two columns
col1, col2 = st.columns(2)

    # Input values in the first column
with col1:
    R1 = st.number_input("R1:KiloOhms", value=100)
    R2 = st.number_input("R2:KiloOhms", value=100)
    R3 = st.number_input("R3:KiloOhms", value=100)
    compute = st.button("Compute")

    # Output values in the second column
with col2:
    if compute:
        R12,R23,R31 = STAR_DELTA(R1, R2, R3)
        st.write(f"R12 = {R12:.2f} Ohms")
        st.write(f"R23 = {R23:.2f} Ohms")
        st.write(f"R31 = {R31:.2f} Ohms")



