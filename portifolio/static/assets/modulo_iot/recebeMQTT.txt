//Exemplo recebe informação via MQTT pelo ESP32
#include <WiFi.h>
#include <PubSubClient.h>

//Conexão com o WiFI
const char *SSID = "VISITANTES";
const char *PWD = "";

//configurações de conexão MQTT
WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient); 
char *mqttServer = "broker.hivemq.com";
int mqttPort = 1883;

//função para conectar ao WiFi
void ConectaNoWiFi() {
  Serial.print("Conectando ao WiFi");
  WiFi.begin(SSID, PWD);
  //Caso tenha dificuldades em conectar, imprime um “.” 
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  //Se conectado, imprime “Conectado” 
  Serial.print("Conectado.");
}

//Realiza as configurações do MQTT 
void setupMQTT() {
  mqttClient.setServer(mqttServer, mqttPort);
}


//A função callback é responsável por receber as msgs. Toda vez que uma novoa msg chega, a função será ativada.  
void callback(char* topic, byte* payload, unsigned int length) {
  
  //Como todos os tópicos vão entrar nessa função, é interessante desenvolver um “if” para definir qual tópico você pretende ler.  
  if (strcmp(topic,"/NomeDoTopico")==0){
    Serial.println("Mensagem recebida do tópico “/NomeDoTopico");
    //A informação chega em um vetor de bytes. Você pode imprimir direto, ou salvar em outra variável para realizar as conversões desejadas.  
    //Neste caso, está sendo realizado a impressão direta do vetor de bytes (payload) 
    for (int i = 0; i < length; i++) {
      Serial.print((char)payload[i]);
    }
    Serial.print("\n");
  }

  //Se a msg chega do tópico “/NomeDoSegundoTopico” ela chega aqui.  
  if (strcmp(topic,"/NomeDoSegundoTopico")==0){
    Serial.println("Mensagem recebida do tópico “/NomeDoSegundoTopico");
    //Vamos salvar os dados recebidos em um vetor de Char 
    char dadosChar[length];
    for (int i = 0; i < length; i++) {
        dadosChar[i] = ((char)payload[i]);
    }
    //a função atof() converte char em float. Para converter em int, pode ser utilizado a função atoi() 
    float dadosFloat = atof(dadosChar);
    Serial.print(dadosFloat);
    Serial.print("\n");
  }
 
}


//Realiza a conceção com o Broker MQTT 
void conectaBrokerMQTT() {
  Serial.println("Conectando ao broker");
  //A função mqttClient.connected() verifica se existe uma conexão ativa.  Depende do Broker, a conexão pode se manter ativa, ou desativar a cada envio de msg.  
  while (!mqttClient.connected()) {
      //Se entrou aqui, é porque não está conectado. Então será feito uma tentativa de conexão infinita, até ser conectado.  
      Serial.println("Conectando ao Broker MQTT");
      //define o nome da ESP na conexão. Está sendo gerado um nome aleatório, para evitar ter duas ESPs com o mesmo nome. Neste caso, uma derrubaria a outra.  
      String clientId = "ESP32Client-";
      clientId += String(random(0xffff), HEX);
      //Realiza a conexão com a função “mqttClient.connect”. Caso seja um sucesso, entra no if e imprime “Conectado ao Broker MQTT.” 
      if (mqttClient.connect(clientId.c_str())) {
        Serial.println("Conectado ao Broker MQTT.");
      }
      
  }
}

//setup
void setup() {
  Serial.begin(9600);
  ConectaNoWiFi();
  setupMQTT();
}

//loop
void loop() {
  //Verifica se a conexão está ativa, caso não esteja, tenta conectar novamente.  
  if (!mqttClient.connected()){
      conectaBrokerMQTT();
      //Define quais tópicos vão ser assinados, ou seja, toda vez que alguma informação chegar destes tópicos, receberemos a informação.  
      //Está adicionado dentro deste if, pois se a cair a conexão com o broker, será possível reativa-la.  
      mqttClient.subscribe("/NomeDoTopico");
      mqttClient.subscribe("/NomeDoSegundoTopico");
      //Define o nome da função que será o callback, ou seja, toda vez que uma novo msg chegar de um dos tópicos, ela será enviada para a função ‘callback’ 
      mqttClient.setCallback(callback);
  }

  //realiza o sincronismo com o Broker, por exemplo, verifica se existem msgs para ler se estiver inscrito em algum tópico 
  mqttClient.loop();

}