-- SQL version of 'n_business_days.py'.

DECLARE @RunDate datetime
DECLARE @counter INT 
DECLARE @yesterday datetime 
DECLARE @holidayExists INT 
DECLARE @saturday INT, @sunday INT 
DECLARE @convertDateFormat varchar(3) = 101

SET @RunDate=getdate() 
SET @counter = 0 
SET @yesterday = '2019-06-11' --ENTER TEST DATE HERE 
SET @saturday = 1 
SET @sunday = 7

WHILE @counter <> 2
   BEGIN 
      SET @yesterday=dateadd(dd, -1, @yesterday)
         SELECT @holidayExists = COUNT(Processing_DTM)
         FROM amsworkflow.dbo.processing_date_List AS PDL 
         WHERE Processing_DTM = CONVERT(VARCHAR(10), @yesterday, 110)
      IF @holdayExisits = 1 or DATEPART(WEEKDAY, @yesterday) = @saturday or DATEPART(WEEKDAY, @yesterday) = @sunday
         BEGIN 
            SET @counter = @counter + 0
         END 
      ELSE
         BEGIN 
            SET @counter = @counter + 1
         END
      Print @counter 
   END 
SELECT @yesterday 

