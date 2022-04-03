# Intelligent-assistant_Model

## Crypto 

### Support 10 cryptocurrency 

    1: BTC(Bitcoin)  
    2: ETH(Ethereum)  
    3: LUNA(Terra)
    4: SHIB(Shiba lnu)  
    5: SOL(Solana)  
    6: XRP(XRP)  
    7: ADA(Cardano)  
    8: WAVES(Waves)  
    9: AVAX(Avalanche)  
    10: USDT(Tether)

### Create Crypto Model 

    import Create_Crypto_model 
    Create_Crypto_model.Crypto_model(Crypto_Name)

#### Format 

##### Input: (string) Crypto_Name 
    ex: Create_Crypto_model.Crypto_model('BTC') 

### Predict Crypto Price

    import Predict_BTC 
    predict_price, predict_per = Predict_BTC.Predict(Crypto_Name)    

#### Format 

##### Input: (string) Crypto_Name
        ex: predict_price, predict_per = Predict_BTC.Predict('BTC') 
    
##### Output: (string) predict_price, (string) predict_per 
       ex: 2022-04-03 09:00:00 46303.97 
        預測會下跌0.0892% 
