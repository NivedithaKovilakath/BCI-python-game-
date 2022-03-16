def socket_thread():
    global attention, meditation, blinkstrength

    tn = Telnet ('127.0.0.1', 13854)
    tn.write ('{"enableRawOutput": false, "format":"Json"}'.encode('ascii'))

    # --- read attention, meditation and blinkstrength from mindwave
    while True:
        pkt = tn.read_until(b'\r')
        dict=json.loads(pkt.decode('utf-8'))
        if 'blinkStrength' in dict: 
              blinkstrength = dict['blinkStrength']
              print ('B=',blinkstrength)
        elif 'eSense' in dict: 
              attention = dict['eSense']['attention']
              meditation = dict['eSense']['meditation']
              #print (attention, meditation)
              print ('A=',attention)

        #attention = math.floor(100 * random.random())
        #meditation = math.floor(100 * random.random())
        #blinkstrength = math.floor(255 * random.random())
  
        time.sleep(1)
