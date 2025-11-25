docker build -t dockerfile:v1 .

docker run dockerfile:v1

**Changes done added server.ppy and ran a flask api to check the model status**

docker-compose up --build

### When the Server is up run in another terminal
1. curl http://localhost:5000/health

'''
2. curl -X POST http://localhost:5000/predict \
 -H "Content-Type: application/json" \
 -d '{"features": [17.99, 10.38, 122.8, 1001, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053, 8.589, 153.4, 0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189]}'
'''

3. To check you can go to http://localhost:5000/health


