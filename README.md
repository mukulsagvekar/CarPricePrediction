# Car Price Prediction

**Objective**: To built a model which can help predict the price of used cars so the users(buyers) will get an idea of the pricing of the used car.

**Solution**: Build a model using Random Forest Regressor (r2_score = 0.9465). The model takes Year, KM driven, Mileage, Engine CC, Power, number of seats, Fuel type, Transmission type, Seller type, number of owners as input and gives the predicted price as output.

**Random Forest Regressor**

![image](https://user-images.githubusercontent.com/83829614/143775431-26aef3f9-fdb2-474d-9f8e-9496758bb456.png)

Did Hyperprameter tuning Random Search CV and got the folloing best parameters:
<br> {'n_estimators': 1000, <br>
 'min_samples_split': 2,<br>
 'min_samples_leaf': 1,<br>
 'max_features': 'sqrt',<br>
 'max_depth': 25}<br>
 
 **Screenshots:**
 
![image](https://user-images.githubusercontent.com/83829614/143775572-6e6b5760-8a08-47b5-bd3e-57de10478108.png)

![image](https://user-images.githubusercontent.com/83829614/143775580-7e820495-3ba2-4849-b89c-78d7449c5c7e.png)
