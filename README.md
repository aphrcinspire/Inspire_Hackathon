 # INSPIRE Hackathon 2024: Record Linkage Challenge



The Implementation Network for Sharing Population Information from Research Entities (INSPIRE) collaborates with over 15 Health and Demographic Surveillance Sites (HDSS) in 7 African countries. INSPIRE network is keen to devise novel means of improving record linkage at community level. Record linkage tools have the ability to identify a person who lives in the HDSS catchment area and link them to the social services that they receive in the community. The social services include health and education services in HDSS catchment area.  Effective record linkage to social services in HDSS communities has the following potential advantages;

1. Ability to correlate household social characteristics with health seeking behavior
2. Can identify early solutions to improve quality of life at household and community level
3. Support the prediction of early warning epidemics at community level
4. Correlate household demographic social characteristics with school attendance among children living in catchment area
5. Support economic modelling and further estimation of the SDG indicators at community level

The INSPIRE network leveraged experience from collaborating institutions to launch a competitive hackathon to design an innovative approach to record linkage in the HDSS. The team aims to explore the use of artificial intelligence tools and advances in machine learning algorithms to design a record linkage application or tool. 

This repository contains a machine learning approach to record linkage as explained below


## Probabilistic record linkage and fuzzy matching techniques

Probabilistic record linkage uses statistical models to estimate the likelihood that two records refer to the same entity, based on similarities across various fields. This process involves learning from the data to understand how different attributes contribute to the likelihood of a match, which aligns with the fundamental principle of ML: learning from data to make decisions or predictions.

### 1. Learning from Data
This process involves learning from the data to understand how different attributes contribute to the likelihood of a match, which aligns with the fundamental principle of ML: learning from data to make decisions or predictions.

### 2. Feature Engineering
The process involves significant feature engineering, a critical step in most machine learning workflows. Features are engineered by calculating similarities between corresponding fields in records from different datasets (e.g., using Jaro-Winkler similarity for names). These features then serve as input for the model, determining the likelihood of records matching. This transformation of raw data into a format that a model can understand is a hallmark of ML practices.

### 3. Model Training and Prediction
Even though the method might not involve explicit "training" in the traditional supervised learning sense, the probabilistic models used in record linkage are based on principles of statistical inference and prediction. These models make predictions about whether records match, similar to how a supervised ML model would predict outcomes based on input features. The "training" in this context could involve tuning parameters (such as similarity thresholds) based on a subset of data where true matches are known.

### 4. Use of Algorithms and Statistical Methods
The method utilizes algorithms and statistical methods to analyze data and make decisions. Algorithms like the Expectation-Maximization algorithm are often used in probabilistic record linkage to iteratively improve the estimation of matching probabilities. The choice and optimization of these algorithms based on data is a process closely associated with machine learning.

### 5. Handling Uncertainty and Making Probabilistic Decisions
Machine learning, particularly in its probabilistic forms, is adept at handling uncertainty and making decisions under uncertainty. Probabilistic record linkage explicitly deals with the uncertainty inherent in determining whether records from different datasets refer to the same entity by computing probabilities of matches. This approach of making decisions based on probabilistic reasoning is a key aspect of many ML systems.
