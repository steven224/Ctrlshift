#Create table
CREATE TABLE traindata(
id INT NOT NULL AUTO_INCREMENT,
impressions FLOAT (5,2),
clicks int,
total_spend_cpm FLOAT (5,2),
D2FD int,
type0 int,
type1 int,
type2 int,
Australia int,
Hong_Kong int,
Indonesia int,
Malaysia int,
NewZealand int,
Philippines int,
Somalia int,
reserved_private int,
Friday int,
Monday int,
Saturday int,
Sunday int,
Thursday int,
Tuesday int,
Wednesday int,
Display int,
Mobile int,
channelunknown int,
Finance int,
bvunknown int,
PRIMARY KEY (id)
);



#batch insertion
insert into traindata(
impressions,clicks,total_spend_cpm,D2FD,type0,type1,type2,Australia,Hong Kong,Indonesia,Malaysia,New Zealand,Philippines,Somalia,reserved/private,Friday,Monday,Saturday,Sunday,Thursday,Tuesday,Wednesday,Display,Mobile,channelunknown,Finance,bvunknown
)
values
(0,48.0,0.0,149.56542499999995,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0),
(1,124.0,1.0,291.5161689999998,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0),
(2,415.0,0.0,509.0191470000008,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0),
.
.
.
(75204,333.0,0.0,1339.681990999995,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0)
;
