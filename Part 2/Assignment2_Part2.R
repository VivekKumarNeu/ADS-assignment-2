install.packages("forecast")
install.packages("devtools")
install.packages("broom")
install.packages("ROCR")

setwd("C:\\Northeastern\\Semester4\\ADS\\Assignment2\\Assignment2\\")

#80% of the sample size
inputRead <- read.csv("merged.csv")
names(inputRead)

###################### 
#Exhaustive search
###################### 

install.packages("leaps")
library(leaps)
regfit.full=regsubsets(kWh~hour+Temperature+Dew_PointF+Humidity+Sea_Level_PressureIn+VisibilityMPH+Wind_SpeedMPH+WindDirDegrees,data=inputRead)


reg.summary=summary(regfit.full)
names(reg.summary)
reg.summary$rss
reg.summary$adjr2

coef(regfit.full,7)
reg.summary
##########################
#Forward Selection
##########################
regfit.fwd=regsubsets(kWh~hour+Temperature+Dew_PointF+Humidity+Sea_Level_PressureIn+VisibilityMPH+Wind_SpeedMPH+WindDirDegrees,data=inputRead,nvmax=8,method="forward")
F=summary(regfit.fwd)
names(F)
F
coef(regfit.full,7)
##########################
#Backward Selection
##########################
regfit.bwd=regsubsets(kWh~hour+Peakhour+month+Humidity+Dew_PointF+Temperature,data=inputRead,nvmax=8,method="backward")
F=summary(regfit.bwd)
names(F)
F
coef(regfit.full,7)

##############

read_size <- floor(0.80 * nrow(inputRead))

#Set the seed to make your partition reproductible
set.seed(80)
train_data_ind <- sample(seq_len(nrow(inputRead)), size = read_size)

#Split the data into train_dataing and test_dataing
train_data <- inputRead[train_data_ind, ]
test_data <- inputRead[-train_data_ind, ]

#Modified Linear Model
lm.fit <- lm(kWh ~ hour+Peakhour+month+Humidity+Dew_PointF+Temperature, data = train_data)


#Summary of the fit
summary(lm.fit)

#Measures of predictive accuracy
#install.packages("forecast")
library(forecast)
pred = predict(lm.fit, test_data)
accuracy_pred=accuracy(pred, test_data$kWh)
#View(pred)
library(ROCR)
account <- c("Account", unique(inputRead$Account))
write.csv(accuracy_pred, file = "PerformanceMetrics.csv",row.names=FALSE)

library(devtools)
#getting tidy output
library(broom)
tidy_lmfit <- tidy(coef(lm.fit))
tidy_lmfit[,1:2]
account <- c("Account", unique(inputRead$Account))
tidy_lmfit <- rbind(account,(tidy_lmfit[,1:2]))
write.csv(tidy_lmfit[,1:2], file = "RegressionOutputs.csv",row.names=FALSE)



