import Predict_Crypto
import Predict_Stock

if __name__ == '__main__':
    predict_price, predict_per = Predict_Crypto.Predict('SOL')
    #predict_price, predict_per = Predict_Stock.Predict('4919')
    print(predict_price)
    print(predict_per)
