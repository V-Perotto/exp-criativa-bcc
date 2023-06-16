import paho.mqtt.client as mqtt

mqtt_broker = "broker.hivemq.com"
mqtt_port = 1883
mqtt_topic = "/pjbl3/leitura"

class MQTT():

    # def MQTT(self):
    #     self.broker = broker

    def on_connect(self, client, userdata, flags, rc):
        print("Conectado ao broker MQTT.")
        client.subscribe(mqtt_topic)

    def on_message(self, client, userdata, msg):
        if msg.topic == mqtt_topic:
            data = msg.payload.decode("utf-8")
            self.humidity, self.temperature = data.split(",")

            print("Umidade:", self.humidity, "%")
            print("Temperatura:", self.temperature, "°C")

            self.humidity, self.temperature = map(float, data.split(","))
            if self.humidity > 20 and self.temperature > 50:
                client.publish("/pjbl3/buzzer", "1")

    def run(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        client.connect(mqtt_broker, mqtt_port, 60)

        client.loop_forever()
