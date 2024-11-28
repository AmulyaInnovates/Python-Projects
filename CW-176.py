import speedtest 

def speedtest1():
    st= speedtest.Speedtest()
    download_speed= round(st.download()/1000000,2)
    print(download_speed)
    
    upload_speed= round(st.upload()/1000000,2)
    print(upload_speed)

speedtest1()
    