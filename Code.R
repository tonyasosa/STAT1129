#1
matrix1 <- matrix(c(7,2,9,4,12,13), nrow=2,ncol=3)

matrix2<- matrix(c(1,2,3,7,8,9,12,13,14,19,20,21), nrow=3,ncol=4)

matrix1 %*% matrix2
#Question 2
df <- data.frame(id= c(1,2,3,4,5),
                 name= c("Peter","Amy","Ryan","Gary","Michelle"),
                 salary= c(623.30,515.20,611.00,729.00,843.25))
df
newdf<- cbind(df, department=c("IT","Math","Music","Art","Science"))

newdf
new <- newdf[-c(1),-c(2)]
new
new2 <- new[-c(2),-c(2)]
new2
new3 <- new2[-c(3),-c(5)]
new3

x<- c("Peter","Gary","Michelle")
y<- c(623.30,729.00,843.25)
barplot(y,names.arg=x)
x2 <- c(515.00,843.25,623.30)
labels<- c("Lowest","Highest","Median")
colors <-c("blue","green","yellow")
pie(x2,label=labels,main="Salaries",col=colors)
legend("bottomright",labels,fill=colors)

data<-read.csv(file ="/Users/tsosa/OneDrive/Desktop/STAT 1129/amazon2021.csv")
data[is.na(data)] = 0
data$Total.Charged = as.numeric(gsub("\\$", "", data$Total.Charged))
data
sum(data$Total.Charged)
mean(data$Total.Charged)
median(data$Total.Charged)
max(data$Total.Charged)
min(data$Total.Charged)
barplot(data$Total.Charged)
x3 <- c(mean(data$Total.Charged),
        median(data$Total.Charged),
        max(data$Total.Charged),
        min(data$Total.Charged))
labels2<- c("Mean","Median","Highest","Lowest")
colors2 <-c("blue","green","yellow", "pink")
pie(x3,label=labels2,main="Purchases",col=colors2)
legend("bottomright",labels2,fill=colors2)
