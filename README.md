# Job-Matchmaker
MLDA Hackathon 2020 
Team: Hello World

**Proof of concept** of building a job recommending system based on the context of resume.

# How it works
1. Embed the large amount of job post into high dimensional vector space using TF-IDF
2. Embed the user's resume into the high dimensional space using same TF-IDF vectorizer
3. Get the K-NN (K Nearest Neighbor) of the resume vector point, the output will be the top k suitable jobs from the dataset

# Getting Started
## Installation
1. Clone the github
```bash
git clone https://github.com/heng98/Job-Matchmaker.git
```
2. Install dependencies
```bash
pip install -r requirement.txt
```

## Download Dataset
Download the dataset from https://www.kaggle.com/shivamb/real-or-fake-fake-jobposting-prediction

## Preprocess dataset
```bash
create_training_file.py --data_dir <path-with-fake_job_postings.csv> --save_path <directory-path-of-preprocessed-data>
```

## Obtain result
```bash
job_matchmaking.py --data_dir <directory-path-of-preprocessed-data> --resume_path <resume_path>
```
**Note**: Currently support txt file and pdf file format for resume

# Result
Resume:
```
Skills * Programming Languages: Python (pandas, numpy, scipy, scikit-learn, matplotlib), Sql, Java, JavaScript/JQuery. * Machine learning: Regression, SVM, NaÃ¯ve Bayes, KNN, Random Forest, Decision Trees, Boosting techniques, Cluster Analysis, Word Embedding, Sentiment Analysis, Natural Language processing, Dimensionality reduction, Topic Modelling (LDA, NMF), PCA & Neural Nets. * Database Visualizations: Mysql, SqlServer, Cassandra, Hbase, ElasticSearch D3.js, DC.js, Plotly, kibana, matplotlib, ggplot, Tableau. * Others: Regular Expression, HTML, CSS, Angular 6, Logstash, Kafka, Python Flask, Git, Docker, computer vision - Open CV and understanding of Deep learning.Education Details 
Data Science Assurance AssociateData Science Assurance Associate - Ernst & Young LLPSkill Details 
JAVASCRIPT- Exprience - 24 months
jQuery- Exprience - 24 months
Python- Exprience - 24 monthsCompany Details 
company - Ernst & Young LLP
description - Fraud Investigations and Dispute Services   Assurance
TECHNOLOGY ASSISTED REVIEW
TAR (Technology Assisted Review) assists in accelerating the review process and run analytics and generate reports.
* Core member of a team helped in developing automated review platform tool from scratch for assisting E discovery domain, this tool implements predictive coding and topic modelling by automating reviews, resulting in reduced labor costs and time spent during the lawyers review.
* Understand the end to end flow of the solution, doing research and development for classification models, predictive analysis and mining of the information present in text data. Worked on analyzing the outputs and precision monitoring for the entire tool.
* TAR assists in predictive coding, topic modelling from the evidence by following EY standards. Developed the classifier models in order to identify "red flags" and fraud-related issues.

Tools & Technologies: Python, scikit-learn, tfidf, word2vec, doc2vec, cosine similarity, NaÃ¯ve Bayes, LDA, NMF for topic modelling, Vader and text blob for sentiment analysis. Matplot lib, Tableau dashboard for reporting.

MULTIPLE DATA SCIENCE AND ANALYTIC PROJECTS (USA CLIENTS)
TEXT ANALYTICS - MOTOR VEHICLE CUSTOMER REVIEW DATA * Received customer feedback survey data for past one year. Performed sentiment (Positive, Negative & Neutral) and time series analysis on customer comments across all 4 categories.
* Created heat map of terms by survey category based on frequency of words * Extracted Positive and Negative words across all the Survey categories and plotted Word cloud.
* Created customized tableau dashboards for effective reporting and visualizations.
CHATBOT * Developed a user friendly chatbot for one of our Products which handle simple questions about hours of operation, reservation options and so on.
* This chat bot serves entire product related questions. Giving overview of tool via QA platform and also give recommendation responses so that user question to build chain of relevant answer.
* This too has intelligence to build the pipeline of questions as per user requirement and asks the relevant /recommended questions.

Tools & Technologies: Python, Natural language processing, NLTK, spacy, topic modelling, Sentiment analysis, Word Embedding, scikit-learn, JavaScript/JQuery, SqlServer

INFORMATION GOVERNANCE
Organizations to make informed decisions about all of the information they store. The integrated Information Governance portfolio synthesizes intelligence across unstructured data sources and facilitates action to ensure organizations are best positioned to counter information risk.
* Scan data from multiple sources of formats and parse different file formats, extract Meta data information, push results for indexing elastic search and created customized, interactive dashboards using kibana.
* Preforming ROT Analysis on the data which give information of data which helps identify content that is either Redundant, Outdated, or Trivial.
* Preforming full-text search analysis on elastic search with predefined methods which can tag as (PII) personally identifiable information (social security numbers, addresses, names, etc.) which frequently targeted during cyber-attacks.
Tools & Technologies: Python, Flask, Elastic Search, Kibana

FRAUD ANALYTIC PLATFORM
Fraud Analytics and investigative platform to review all red flag cases.
â¢ FAP is a Fraud Analytics and investigative platform with inbuilt case manager and suite of Analytics for various ERP systems.
* It can be used by clients to interrogate their Accounting systems for identifying the anomalies which can be indicators of fraud by running advanced analytics
Tools & Technologies: HTML, JavaScript, SqlServer, JQuery, CSS, Bootstrap, Node.js, D3.js, DC.js
```

Output
```
Data Scientist / Data Architect
REQUIRED QUALIFICATIONS:PhD in Data Science, Machine Learning, Statistics, Applied Mathematics, Algorithms, or a related field OR alternatively, an MSc in a related field with 5+ years proven research experienceStrong knowledge of data mining algorithms (decision trees, clustering, regression analysis, neural networks, pattern analysis, outlier analysis, optimization techniques, etc)Ability to perform advanced analytics on large unstructured and structured data sets to measure, interpret and predict trends and patterns to inform on key decisions (e.g. financial, budget, outcomes, and impact).Ability to research and design statistical models to answer target questions, optimize processes &amp; outcomes and inform decision-making.Ability to explore and apply new data visualization techniques to increase insight and visibility to data trends and opportunities.Demonstrated experience using data mining to solve business problemsData Modeling and Data Warehousing (modeling, design, integration, replication, processing, cloud computing, unstructured Data) experienceGood knowledge of software development and programming language. Examples: SQL, Matlab, Mathematica, SPSS, SAS, R, Python, Scripting LanguagesAbility to view data through a quantitative lens and derive insights from dataAttention to detail and data accuracyExcellent use of the English language (written and oral)DESIRED QUALIFICATIONS:Predictive Analytics (statistical analysis, modeling, etc.)Experienced in advanced methods for forecasting, data classification and pattern recognition (e.g. regression analysis, logistic regression, survival and reliability analysis, Auto-Regressive Integrated Moving Average (ARIMA) modeling etc.)Conduct applied research in Big Data and high impact business problems.Business Intelligence (reporting, dashboards, visualization, etc.)Innovation thinking with good sense of customer focus and Business acumenKnowledge of the business across the value chain, from marketing, sales, distribution, operations, products, finance, etc.Ability to generate static and dynamic visualizations in a variety of visual mediaAbility to work independently and in a multicultural team to design innovate solution for challenging problemsAbility to engage with senior management and translate the data-driven insights into decisions and actions

Click Fraud Analyst
Required Skills &amp; ExperienceProven expertise in risk management, fraud detection, or investigationsStrong working knowledge of fraud policies, procedures and applicationsExperience in logs and data analysisAwareness of new fraud trendsAbility to work in self-directed and team environments with the ability to adapt to changeStrong multi-tasking attitude and technology competenceAbility to write scripts and use of log analysis toolFluent EnglishPreferred Skills &amp; ExperienceExpertise in fraud analysis tools developmentKnowledge about machine learningBe able to take initiative, propose new solutions, processes and tools.Team player ( should feel good to be a part of the big team)

Data Scientist
Our Requirements:Degree qualification BSc, MSc or PhD in Math, Computer Science, Statistics or Econometrics;Experience with database management and Google Analytics;Knowledge of SQL and how to use APIs (JSON and/or XML etc.);Experience with programming (Python, VBA, Java) as well as web-logs and web-scraping tools;Experience with retrieval and processing large data sets and the ability to integrate and make sense of data from varied sources;Ideally some experience with data visualisation tools such as Tableau;Experience with data mining, statistical analysis, pattern detection and credit risk modelling experience gained at a consulting or major financial institution;Pro-active, self-starter with excellent communication skills;Experience with NoSQL, Linux, Java, Hadoop is a plus as is knowledge of statistical packages (SAS, SPSS, Matlab, R, etc) and MS ExcelYour Responsibilities:Develop a comprehensive business intelligence and data management system with responsibility for identifying and tracking Key Performance Indicators to aid strategic decision making;Provide analytical support for assessing credit risk and develop a credit risk model to increasingly automate the underwriting process;Expand existing set of data used in the credit underwriting process by evaluating information value of non-traditional data sources and by re-engineering use of existing datasets;Collect structured and unstructured data from the web, digital media and other social platforms;Evaluate ‘Big Data’ opportunities and work with technology to deploy new data sources;Perform various ad-hoc analysis for the marketing and business development functions
```
