USE cs415website;

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'Main','User','muser@email.com','12345','2024-01-18 10:15:03',1,'2024-02-28 09:59:07'),
    (2,'Willie','Nelson','willie.nelson@email.com','12345','2024-01-18 21:40:15',1,'2024-02-08 18:52:27'),
    (3,'James','Hetfield','jhetfield@email.com','12345','2024-01-25 05:12:45',1,'2024-02-27 15:09:51'),
    (4,'Amelia','Earhart','aearhart@email.com','12345','2024-01-29 16:24:33',1,'2024-02-08 18:52:27'),
    (5,'Peewee','Herman','pherman@email.com','12345','2024-01-25 05:12:45',1,'2024-02-08 18:52:27'),
    (6,'Steve','Rogers','srogers@email.com','12345','2024-01-30 05:29:22',1,'2024-01-30 20:37:15'),
    (7,'Jimmy','John','jjohn@email.com','12345','2024-01-25 05:12:45',1,'2024-02-08 18:52:27'),
    (8,'Ronald','McDonald','rmcdonald@email.com','12345','2024-02-08 18:41:45',1,'2024-02-08 18:52:27'),
    (9,'Mario','Jumpman','mjumpman@email.com','12345','2024-02-08 18:53:37',1,'2024-02-08 18:54:02'),
    (10,'Abraham','Lincoln','alincoln@email.com','12345','2024-02-08 19:26:06',1,'2024-02-28 09:59:07'),
    (11,'Jimmy','Dean','jdean@email.com','12345','2024-02-08 19:38:18',1,'2024-02-28 09:59:07'),
    (12,'Sam','Adams','sadams@email.com','12345','2024-02-09 00:38:52',1,'2024-02-28 09:59:07'),
    (13,'George','Washington','gwashington@eamil.com','12345','2024-02-09 00:40:21',1,'2024-02-28 09:59:07'),
    (14,'Thomas','Edison','tedison@email.com','12345','2024-02-09 00:42:45',1,'2024-02-28 09:59:07'),
    (15,'Albert','Einstein','aeinstein@email.com','12345','2024-02-09 00:44:42',1,'2024-02-28 09:59:07'),
    (16,'Jack','Frost','jfrost@email.com','12345','2024-02-09 00:47:24',1,'2024-02-28 09:59:07');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `AddressType` WRITE;
/*!40000 ALTER TABLE `AddressType` DISABLE KEYS */;
INSERT INTO `AddressType` VALUES (1,'Home'),(2,'Work'),(3,'Billing'),(4,'Shipping'),(5,'Vacation');
/*!40000 ALTER TABLE `AddressType` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `PhoneType` WRITE;
/*!40000 ALTER TABLE `PhoneType` DISABLE KEYS */;
INSERT INTO `PhoneType` VALUES (1,'Mobile'),(2,'Home'),(3,'Work'),(4,'Emergency');
/*!40000 ALTER TABLE `PhoneType` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `UserAddress` WRITE;
/*!40000 ALTER TABLE `UserAddress` DISABLE KEYS */;
INSERT INTO `UserAddress` VALUES (1,1,'100 Fake St','','Fake City','UT','84032','United States',1),
    (2,1,'200 Fake Ave','','Faker City','UT','84033','United States',3),
    (3,2,'200 Fake Ave','','Fakie City','UT','84033','United States',1),
    (4,6,'101 Fake St','','Fake City','UT','12345','United States',2),
    (5,7,'101 Fake St','','Fake City','UT','12345','United States',3),
    (6,3,'100 Fake St','','Fake City','UT','84032','United States',1),
    (7,4,'100 Fake St','','Fake City','UT','84032','United States',3),
    (8,5,'100 Fake St','','Fake City','UT','84032','United States',2),
    (9,8,'100 Fake St','','Fake City','UT','84032','United States',1),
    (10,9,'100 Fake St','','Fake City','UT','84032','United States',3),
    (11,10,'100 Fake St','','Fake City','UT','84032','United States',2),
    (12,11,'100 Fake St','','Fake City','UT','84032','United States',1),
    (13,12,'100 Fake St','','Fake City','UT','84032','United States',1),
    (14,13,'100 Fake St','','Fake City','UT','84032','United States',2),
    (15,14,'100 Fake St','','Fake City','UT','84032','United States',3),
    (16,15,'100 Fake St','','Fake City','UT','84032','United States',1),
    (17,16,'100 Fake St','','Fake City','UT','84032','United States',2);
/*!40000 ALTER TABLE `UserAddress` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `UserPhone` WRITE;
/*!40000 ALTER TABLE `UserPhone` DISABLE KEYS */;
INSERT INTO `UserPhone` VALUES (1,1,1,'4564564564','2024-01-25 06:07:09',1),
    (2,2,2,'7897897897','2024-01-25 06:07:27',1),
    (3,3,3,'1231231231','2024-01-25 06:07:43',1),
    (4,1,4,'4564564564','2024-01-25 06:07:09',1),
    (5,2,5,'7897897897','2024-01-25 06:07:09',1),
    (6,3,6,'4564564564','2024-01-25 06:07:09',1),
    (7,1,7,'4564564564','2024-01-25 06:07:09',1),
    (8,2,8,'7897897897','2024-01-25 06:07:09',1),
    (9,3,9,'4564564564','2024-01-25 06:07:09',1),
    (10,1,10,'4564564564','2024-01-25 06:07:09',1),
    (11,3,11,'7897897897','2024-01-25 06:07:09',1),
    (12,2,12,'4564564564','2024-01-25 06:07:09',1),
    (13,1,13,'4564564564','2024-01-25 06:07:09',1),
    (14,2,14,'7897897897','2024-01-25 06:07:09',1),
    (15,3,15,'4564564564','2024-01-25 06:07:09',1),
    (16,1,16,'4564564564','2024-01-25 06:07:09',1),
    (17,2,1,'7897897897','2024-01-25 06:07:09',1);
/*!40000 ALTER TABLE `UserPhone` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `UserInfo` WRITE;
/*!40000 ALTER TABLE `UserInfo` DISABLE KEYS */;
INSERT INTO `UserInfo` VALUES (1,1,'Computer Geek','https://storage.googleapis.com/pai-images/4e3bd28f9417448187a0bdfdf3c1222a.jpeg','2024-01-25 06:05:01','2024-01-25 06:05:04'),
    (2,2,'Old Singer','https://is1-ssl.mzstatic.com/image/thumb/Features125/v4/b4/c2/9a/b4c29a1e-3b45-2b60-be65-dbb96d21e42a/mza_1383128222591135178.png/375x375bb.jpg','2024-01-25 06:05:27','2024-01-25 06:05:28'),
    (3,3,'Heavy Metal Guy','https://live.staticflickr.com/3164/2551435941_21e961bf01.jpg','2024-01-25 06:05:47','2024-01-25 06:05:49'),
    (4,4,'Fly Girl','https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/1-amelia-earhart-bettmann.jpg','2024-01-25 06:05:27','2024-01-25 06:05:28'),
    (5,5,'Weird Man-Child','https://img.buzzfeed.com/buzzfeed-static/static/2023-07/31/17/asset/67722853cb23/sub-buzz-5907-1690824698-4.jpg','2024-01-25 06:05:27','2024-01-25 06:05:28'),
    (6,6,'American Captain','https://i.pinimg.com/originals/f2/a7/42/f2a742ec86bba7efe2b7f048d80d8fd5.jpg','2024-01-25 06:05:01','2024-01-25 06:05:04'),
    (7,7,'Sandwich Maker','https://upload.wikimedia.org/wikipedia/commons/a/a1/Jimmy_John_Liautaud_2018_Headshot.jpg','2024-01-25 06:05:01','2024-01-25 06:05:04'),
    (8,8,'Creepy Burger Clown','https://welltempered.files.wordpress.com/2017/03/ronald-mcdonald.jpg','2024-01-25 06:05:01','2024-01-25 06:05:04'),
    (9,9,'OG Arcade Stud','https://easydrawingguides.com/wp-content/uploads/2017/04/how-to-draw-super-mario-featured-image-1200.png','2024-01-25 06:05:01','2024-01-25 06:05:04'),
    (10,10,'Civil Leader','https://upload.wikimedia.org/wikipedia/commons/4/44/Abraham_Lincoln_head_on_shoulders_photo_portrait.jpg','2024-01-25 06:05:01','2024-01-25 06:05:04'),
    (11,11,'Makes Good Sausages','https://upload.wikimedia.org/wikipedia/commons/e/e6/James_Dean_in_Rebel_Without_a_Cause.jpg','2024-01-25 06:05:01','2024-01-25 06:05:04'),
    (12,12,'A Father who found US','https://hips.hearstapps.com/hmg-prod/images/samuel-adams-gettyimages-517357384.jpg','2024-01-25 06:05:01','2024-01-25 06:05:04'),
    (13,13,'Very Presidential','https://csac.history.wisc.edu/wp-content/uploads/sites/281/2017/07/george_washington.jpg','2024-01-25 06:05:01','2024-01-25 06:05:04'),
    (14,14,'Has Bright Ideas','https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/1-thomas-edison-keystone.jpg','2024-01-25 06:05:01','2024-01-25 06:05:04'),
    (15,15,'E=MC2...  Wise Guy','https://m.media-amazon.com/images/I/51ArQaCkkZL._AC_UF894,1000_QL80_.jpg','2024-01-25 06:05:01','2024-01-25 06:05:04'),
    (16,16,'Cold Hearted','https://cdn.openart.ai/published/nf6fpu5Sbw0Bg5YwNlcF/z-k7xsLc_iczt_1024.webp','2024-01-25 06:05:01','2024-01-25 06:05:04');
/*!40000 ALTER TABLE `UserInfo` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `PageData` WRITE;
/*!40000 ALTER TABLE `PageData` DISABLE KEYS */;
INSERT INTO `PageData` VALUES (1,'Module 1 - Week 1','VM, Repo, and DB Server','Setting up a Virtual Machine, Github Repository and a MySQL Database Server','https://pbs.twimg.com/media/DbJfBz8UwAEgZtB?format=png&name=360x360','Module 1 - Database VM'),
    (2,'Module 2 - Weeks 2 & 3','Django, DB Connect','Connect to the Database Server remotely, Install Django locally and connect to DB server.  Add all tables to Django Admin','https://miro.medium.com/v2/resize:fit:720/format:webp/1*Bd5dYeGhFGhYuqJUpHjrNA.png','Module 2 - Django API'),
    (3,'Module 3 - Week 4','Create Custom Endpoints','Create webpage flow diagram with needed custom endpoints.  Implement custom endpoints in django.  Discuss JSON Web Token authentication','https://miro.medium.com/v2/resize:fit:720/format:webp/0*prut14lFoArZnPK5.jpg','Module 3 - Custom Endpoints'),
    (4,'Module 4 - Week 5','UI and Local Execution','Creating the User Interface, running API and Website locally connected together','https://www.devopsschool.com/blog/wp-content/uploads/2022/03/reactjs-benefits-1024x512.jpg','Module 4 - React UI'),
    (5,'Module 5 - Week 6','Create VMs for UI and API','Create and configure EC2 instances for the Website and API - install Apache and AWS CodeDeploy Agent.  Verify and update UI and API projects','https://miro.medium.com/v2/resize:fit:720/format:webp/1*bEOOOxnCV2nXpGvXkOErRg.png','Module 5 - Apache VM'),
    (6,'Module 6 - Week 7','Deploy Distributed System','Create CodeDeploy Applications and deployment groups for UI and API.  Deploy both applications and verify functionality','https://media.geeksforgeeks.org/wp-content/uploads/20231108115918/Three-Tier-architecture.png','Module 6 - Deploy Code to VMs'),
    (7,'Module 7 - Week 8','Midterm Assignment','Summary of all activities so far in the semester.  Go over midterm assignment','https://thehawkeye.org/wp-content/uploads/2019/04/Midterm-exams-857x900.png','Module 7 - Midterm Assignment');
/*!40000 ALTER TABLE `PageData` ENABLE KEYS */;
UNLOCK TABLES;
