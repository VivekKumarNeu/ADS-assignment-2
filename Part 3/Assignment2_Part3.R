#Measures of predictive accuracy
install.packages("forecast")
install.packages("devtools")
install.packages("broom")
install.packages("ROCR")
install.packages("zoo")
setwd("C:\\Northeastern\\Semester4\\ADS\\Assignment2\\Assignment2\\")

#80% of the sample size
inputRead <- read.csv("merged.csv")
#inputRead$Temperature<-na.locf(inputRead$Temperature)
names(inputRead)

read_size <- floor(0.80 * nrow(inputRead))

#Set the seed to make your partition reproductible
set.seed(80)
train_data_ind <- sample(seq_len(nrow(inputRead)), size = read_size)

#Split the data into train_dataing and test_dataing
train_data <- inputRead[train_data_ind, ]
lm.fit <- lm(kWh ~ hour+Peakhour+month+Humidity+Dew_PointF+Temperature, data = train_data)

preditRead <- read.csv("forecastInput.csv")

test_data_ind <- sample(seq_len(nrow(preditRead)))
#Output.csv data is read to predict and is used as test data
test_data <- preditRead[test_data_ind, ]

install.packages("forecast")
library(forecast)
pred = predict(lm.fit, test_data)
df<-as.data.frame(pred)
accuracy(pred, test_data$kWh)
write.csv(pred, "Prediction.csv")

readAgain <- read.csv("Prediction.csv")
KWH<-readAgain[order(readAgain$X),]
KWH <- KWH[,c("x")]

dataframe1<-preditRead[,c("Date","hour","Temperature")]
dfFinal<-cbind(dataframe1,KWH)
write.csv(dfFinal,paste("forecastOutput_",unique(inputRead$Account),".csv",sep = ""),row.names=FALSE)
