from machine import Pin
import network
import socket

ssid = 'Kannatham_2.4GHz'
password = 'Kannatham[2022]'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)
# For more details and step by step guide visit: Microcontrollerslab.com
led_state = "OFF"
def web_page():
    html = """ <!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
     <style>
        body {
            font-family: 'apple-system';
            /* display: inline-block; */
            margin: 0px auto;
            text-align: center;
        }
        .navbar {
            display: flex;
            background-color: #333;
            color: white;
            /* border: 1px solid red; */
        }
        .lab {
            /* border: 1px solid red; */
            width: 20%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        
        ul {
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            list-style: none;
            /* border: 1px solid red; */
        }
        ul li {
            margin: 0  1rem;
        }
        ul li a {
            color: #fff;
            text-decoration: none;
        }
        header {
            height: 450px;
            display: flex;
            justify-content: center;
            align-items: center;
             background-color: #333;
             
        }
        .header-info {
            width: 200px;
            color: #fff;
             
        }
        .btnON {
            font-family: Arial;
            text-align: center;
            color: #fff;
            padding: 1rem; 
          /* display:flex;  เรียงแนวนอน */
           display:block; /* เรียงแนวตั้ง */
           /* height: 50px;  
           width: 50px;
           /* border-radius: 50%;  */
          background-color: green;
           font-size: 50px; 
          text-decoration-line: none;
        
        }
        .btnOFF {
          font-family: Arial;
            text-align: center;
            color: #333;
            padding: 1rem; 
          /* display:flex;  เรียงแนวนอน */
           display:block; /* เรียงแนวตั้ง */
           /* height: 50px;  
           width: 50px;
           /* border-radius: 50%;  */
          background-color: #ffe600;
           font-size: 50px; 
          text-decoration-line: none;
        
        
        }
        footer {
            background-color: #00000;
            padding: 1rem;
            text-align: center;
        }
    </style>
</head>
<body>
    <section class="navbar">
        <div class="lab">
            <h1>MyLab</h1>
            <!-- <h6>ESP MicroPython Web Server</h6> -->
        </div>
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Project</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
        
    </section>
    <header>
        <div class="header-info">
        <p>LED state: <strong>""" + led_state + """</strong></p>
     <p>
         <a href=\"?led_on\" class="btnON">ON</a></p>
     <p>
         <a href=\"?led_off\" class="btnOFF">OFF</a>
    </p>
</div>
</header>
</body>
<footer>
    <p>&copy;|4Q-2022</p>
</footer>
</html>"""
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Received HTTP GET connection request from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print('GET Rquest Content = %s' % request)
        led_on = request.find('/?led_on')
        led_off = request.find('/?led_off')
        if led_on == 6:
            print('ON -> GPIO2')
            led_state = "ON"
            led.off()
        if led_off == 6:
            print('OFF -> GPIO2')
            led_state = "OFF"
            led.on()
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')