`git clone https://github.com/square/certstrap
./certstrap init --common-name "Example App"
./certstrap request-cert --domain  "client"
./certstrap request-cert --domain  "localhost"
./certstrap sign localhost --CA ExampleCA
./certstrap sign localhost --CA Example_App`