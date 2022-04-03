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

####    Format 

#####   Input: (string) Crypto_Name 
    ex: 
        Create_Crypto_model.Crypto_model('BTC') 

### Predict Crypto Price

    import Predict_Crypto 
    predict_price, predict_per = Predict_Crypto.Predict(Crypto_Name)    

####    Format 

#####   Input: (string) Crypto_Name
    ex: 
        predict_price, predict_per = Predict_Crypto.Predict('BTC') 
    
#####   Output: (string) predict_price, (string) predict_per 
    ex:     
        2022-04-03 09:00:00 46303.97 
        預測會下跌0.0892% 

## Stock 

### Support 10 Stock

    1: 2330(台積電) 
    2: 2603(長榮)   
    3: 2454(聯發科)
    4: 3035(智原)  
    5: 2609(陽明)  
    6: 1708(東鹼)  
    7: 4919(新唐)  
    8: 3037(欣興)  
    9: 2303(2618)  
    10: 2618(長榮航)

### Create Stock Model 

    import Create_Stock_model 
    Create_Stock_model.Crypto_model(Stock_Name)

####    Format 

#####   Input: (string) Stock_Name 
    ex: 
        Create_Stock_model.Stock_model('BTC') 

### Predict Stock Price

    import Predict_Stock 
    predict_price, predict_per = Predict_Stock.Predict(Stock_Name)    

####    Format 

#####   Input: (string) Stock_Name
    ex: 
        predict_price, predict_per = Predict_Stock.Predict('BTC') 
    
#####   Output: (string) predict_price, (string) predict_per 
    ex:     
        2022-04-03 09:00:00 46303.97 
        預測會下跌0.0892% 
