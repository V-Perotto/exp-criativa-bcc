import paho.mqtt.client as mqtt
from models import Read, User, Sensor

class MQTT:

    def __init__(self):
        self.broker = "broker.hivemq.com"
        self.port = 1883
        self.topic = "/pjbl3/leitura"

    def on_connect(self, client, userdata, flags, rc):
        print("Conectado ao broker MQTT.")
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        if msg.topic == self.topic:
            data = msg.payload.decode("utf-8")
            self.humidity, self.temperature = data.split(",")

            print("Umidade:", self.humidity, "%")
            print("Temperatura:", self.temperature, "°C")

            self.humidity, self.temperature = map(float, data.split(","))
            if self.humidity > 20 and self.temperature > 50:
                client.publish("/pjbl3/buzzer", "1")

    # def save_reads(self):
    #     sensors = Sensor.get_sensors()
    #     users = User.get_user()        

    #     Read.save_read(user_id=users[0].id, 
    #                 sensor_id=sensors[0].id, 
    #                 umid=self.humidity,
    #                 temp=self.temperature)
    
    def run(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        client.connect(self.broker, self.port, 60)

        # self.save_reads()

        client.loop_forever()

