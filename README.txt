
Created on Fri Nov 12 00:32:34 2021

@author: Ege Dogan Dursun
Phone Number: +90(507)0558665
E-Mail: edogandursun@gmail.com

Please feel free to reach me out and give feedbacks about the code!


=====================================================================================================


"CRYPTO-MINER & PREDICTOR"

--- This application is a basic cryptocurrency data retrieval and forecasting tool.


=====================================================================================================


---!!! BEFORE RUNNING THE APPLICATION !!!---
	1. You need to install the "requirements.txt".
	2. Run "pip install -r requirements.txt" from your terminal.


=====================================================================================================


---(1) MINING CRYPTOCURRENCY DATA
	1. Run "chmod u+x data_miner.py" from your terminal.
	2. Run "./data_miner.py" from your terminal.
	
	Explanation:
		This module will mine cryptocurrency price information from the
		internet by using a third-party API. After the retrieval of the
		price information, the currenct date-time will be retrieved and
		after the information is parsed to an adequate state, the information
		will be stored in an SQLite database.
		

=====================================================================================================


---(2) FORECASTING CRYPTOCURRENCY PREDICTIONS
	1. Run "chmod u+x data_forecaster.py" from your terminal.
	2. Run "./data_forecaster.py" from your terminal.
	
	Explanation:
		This module will retrieve the last N-price information for cryptocurrencies
		in the SQLite database and apply the principles of LSTM method in order
		to generate forecasts for the cryptocurrencies. It does not use the
		API, as it already retrieves the information from the local database.
		

=====================================================================================================


---(3) CHANGING THE DATA MINING / FORECASTING PARAMETERS:
	1. Modify the variables in "constants.py"
	
	Explanation:
		This module contains the hyper-parameters for the mining and forecasting
		operations. You can change them freely according to your own needs.
		

=====================================================================================================
	

---(4) BROWSING THE DATABASE:
	1. Install a "SQLite Browser Application". (It could be any kind.)
	2. Open the file in "data_house" directory, named "coins.db".
	3. Now, you can see, modify or delete the mined cryptocurrency data.
	

=====================================================================================================
	

---(5) SCREENSHOTS FOLDER:
	1. You can check the screenshots folder to see some previous results of
	the application. The folder is designed with the sole purpose of giving
	an idea about how the application works, and the look and feel of it.


=====================================================================================================

    
