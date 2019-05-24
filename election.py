import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

elector_14 = pd.read_csv("/Users/snehamitta/Desktop/india-general-election-data-2009-and-2014/LS2014Electors.csv")
elector_09 = pd.read_csv("/Users/snehamitta/Desktop/india-general-election-data-2009-and-2014/LS2009Electors.csv")
candidate_14 = pd.read_csv("/Users/snehamitta/Desktop/india-general-election-data-2009-and-2014/LS2014Candidate.csv")
candidate_09 = pd.read_csv("/Users/snehamitta/Desktop/india-general-election-data-2009-and-2014/LS2009Candidate.csv")

##Voter turnout in 2009 vs 2014

total_electors09 = elector_09["Total_Electors"].sum()

total_voters09 = elector_09["Total voters"].sum()

total_turnout09 = total_voters09/total_electors09 * 100
print("voter turnout in 2009 is",+round(total_turnout09,2))

total_electors14 = elector_14["Total_Electors"].sum()

total_voters14 = elector_14["Total voters"].sum()

total_turnout14 = total_voters14/total_electors14 * 100
print("voter turnout in 2014 is",+round(total_turnout14,2))

##2009 candidates gender distribution

candidate_sex09 = candidate_09["Candidate Sex"].value_counts()
print(candidate_sex09)

##2009 candidate distribution INC vs BJP

plt.figure(figsize=(10,5))
explode = (0, 0.1)
colors = ['#4169E1','#FF69B4']
plt.subplot(1,2,1)

plt.pie(candidate_09[(candidate_09["Party Abbreviation"]=='INC')]['Candidate Sex'].value_counts(), colors = colors, explode = explode, labels=['Male','Female'],autopct='%1.1f%%', startangle=90)

fig = plt.gcf() 
fig.suptitle("Gender Distribution of Candidates in 2009 - INC vs BJP", fontsize=14) 
ax = fig.gca() 
label = ax.annotate("INC", xy=(-1.1,-1), fontsize=30, ha="center",va="center")
ax.axis('off')
ax.set_aspect('equal')
ax.autoscale_view()

plt.subplot(1,2,2)
plt.pie(candidate_09[(candidate_09["Party Abbreviation"]=='BJP')]['Candidate Sex'].value_counts(), colors = colors, explode= explode, labels=['Male','Female'],autopct='%1.1f%%', startangle=90)
fig = plt.gcf() 
ax = fig.gca() 
label = ax.annotate("BJP", xy=(-1.1,-1), fontsize=30, ha="center",va="center")
ax.axis('off')
ax.set_aspect('equal')
ax.autoscale_view()
plt.show();

##2014 candidates gender distribution

candidate_sex14 = candidate_14["Candidate Sex"].value_counts()
print(candidate_sex14)

##2014 candidate distribution INC vs BJP

plt.figure(figsize=(10,5))
explode = (0, 0.1)
colors = ['#4169E1','#FF69B4']
plt.subplot(1,2,1)

plt.pie(candidate_14[(candidate_14["Party Abbreviation"]=='INC')]['Candidate Sex'].value_counts(), colors = colors, explode = explode, labels=['Male','Female'],autopct='%1.1f%%', startangle=90)

fig = plt.gcf() 
fig.suptitle("Gender Distribution of Candidates in 2014 - INC vs BJP", fontsize=14) 
ax = fig.gca() 
label = ax.annotate("INC", xy=(-1.1,-1), fontsize=30, ha="center",va="center")
ax.axis('off')
ax.set_aspect('equal')
ax.autoscale_view()

plt.subplot(1,2,2)
plt.pie(candidate_14[(candidate_14["Party Abbreviation"]=='BJP')]['Candidate Sex'].value_counts(), colors = colors, explode= explode, labels=['Male','Female'],autopct='%1.1f%%', startangle=90)
fig = plt.gcf() 
ax = fig.gca() 
label = ax.annotate("BJP", xy=(-1.1,-1), fontsize=30, ha="center",va="center")
ax.axis('off')
ax.set_aspect('equal')
ax.autoscale_view()
plt.show();

##Party wise winning women candidates in 2009

womenwinners09 = candidate_09[(candidate_09['Position']==1)&(candidate_09["Candidate Sex"]=="F")]
 
ax1 = womenwinners09["Party Abbreviation"].value_counts().plot(kind = "pie", radius = 1, autopct = '%1.1f%%', startangle = 90)
x1 = womenwinners09["Party Abbreviation"].value_counts()
print(x1)
plt.show()

##Party wise winning women candidates in 2014

womenwinners14 = candidate_14[(candidate_14['Position']==1)&(candidate_14["Candidate Sex"]=="F")]

ax2 = womenwinners14["Party Abbreviation"].value_counts().plot(kind = "pie", radius = 1, autopct = '%1.1f%%', startangle = 90)
x2 = womenwinners14["Party Abbreviation"].value_counts()
print(x2)
plt.show()

# ##Party wise winning men candidates in 2009

# menwinners09 = candidate_09[(candidate_09['Position']==1)&(candidate_09["Candidate Sex"]=="M")]
 
# bx1 = menwinners09["Party Abbreviation"].value_counts().plot(kind = "pie", radius = 1, autopct = '%1.1f%%', startangle = 90)
# x3 = menwinners09["Party Abbreviation"].value_counts()
# print(x3)

# ##Party wise winning men candidates in 2014

# menwinners14 = candidate_14[(candidate_14['Position']==1)&(candidate_09["Candidate Sex"]=="M")]
 
# bx2 = menwinners14["Party Abbreviation"].value_counts().plot(kind = "pie", radius = 1, autopct = '%1.1f%%', startangle = 90)
# x4 = menwinners14["Party Abbreviation"].value_counts()
# print(x4)

##Age distribution of winners

Age09 = candidate_09[(candidate_09.Position == 1) & (candidate_09.Year==2009)]['Candidate Age'].tolist()
Age14 = candidate_14[(candidate_14.Position == 1) & (candidate_14.Year==2014)]['Candidate Age'].tolist()
bins = np.linspace(20, 90, 10)
plt.hist([Age09, Age14], bins, label=['2009', '2014'])

plt.legend(loc='upper right')
plt.xlabel('Age Of winners in years')
plt.ylabel('Total Number of winners')
plt.title('Distribution of Age of the winners')
plt.show()

## Alliances in 2009

candidate_09["Alliance"] = candidate_09["Party Abbreviation"]

candidate_09["Alliance"] = candidate_09["Alliance"].replace(to_replace =["INC","AITC","DMK","NCP","NC","JMM","MUL","VCK","KEC(M)","AIMIM"],value="UPA")
candidate_09["Alliance"] = candidate_09["Alliance"].replace(to_replace =["BJP","JD(U)","SHS","RLD","SAD","TRS","AGP","INLD"],value="NDA")
candidate_09["Alliance"] = candidate_09["Alliance"].replace(to_replace =["CPM","CPI","RSP","AIFB","BSP","BJD","ADMK","TDP","JD(S)","MDMK","HJS","PMK"],value="Third Front")
candidate_09["Alliance"] = candidate_09["Alliance"].replace(to_replace =["SP","RJD","LJP"],value="Fourth Front")
candidate_09["Alliance"] = candidate_09["Alliance"].replace(to_replace =["AUDF","JKM(P)","NPF","BOPF","SWP","BKA","SDF","IND","JKN","HJCBL","BVA","JVN","JVM"],value="Others")

## Alliances in 2014

candidate_14["Alliance"] = candidate_14["Party Abbreviation"]

candidate_14["Alliance"] = candidate_14["Alliance"].replace(to_replace =['INC','NCP', 'RJD', 'DMK', 'IUML', 'JMM','JD(s)','KC(M)','RLD','RSP','CMP(J)','KC(J)','PPI','MD'],value="UPA")
candidate_14["Alliance"] = candidate_14["Alliance"].replace(to_replace =['BJP','SHS', 'LJP', 'SAD', 'RLSP', 'AD','PMK','NPP','AINRC','NPF','RPI(A)','BPF','JD(U)','SDF','NDPP','MNF','RIDALOS','KMDK','IJK','PNK','JSP','GJM','MGP','GFP','GVP','AJSU','IPFT','MPP','KPP','JKPC','KC(T)','BDJS','AGP','JSS','PPA','UDP','HSPDP','PSP','JRS','KVC','PNP','SBSP','KC(N)','PDF','MDPF'],value="NDA")
candidate_14["Alliance"] = candidate_14["Alliance"].replace(to_replace =['YSRCP',"AITC",'AAAP',"BJD","ADMK",'IND', 'AIUDF', 'BLSP', 'JKPDP',"CPM","TRS","TDP","SP", 'JD(S)', 'INLD', 'CPI', 'AIMIM', 'KEC(M)','SWP', 'NPEP', 'JKN', 'AIFB', 'MUL', 'AUDF', 'BOPF', 'BVA', 'HJCBL', 'JVM','MDMK'],value="Others")

##Alliance grouped age distribution of the winners

Age09UPA = candidate_09[(candidate_09.Position == 1) & (candidate_09.Year == 2009) & (candidate_09.Alliance == "UPA")]['Candidate Age'].tolist()
Age09NDA = candidate_09[(candidate_09.Position == 1) & (candidate_09.Year == 2009) & (candidate_09.Alliance == "NDA")]['Candidate Age'].tolist()
bins = np.linspace(20, 90, 10)
plt.hist([Age09UPA, Age09NDA], bins, label=['UPA', 'NDA'])
plt.legend(loc='upper right')
plt.xlabel('Age Of winners in years')
plt.ylabel('Total Number of winners')
plt.title('Alliance wise Distribution of Age of the winners in 2009')
plt.show()

Age14UPA = candidate_14[(candidate_14.Position == 1) & (candidate_14.Year == 2014) & (candidate_14.Alliance == "UPA")]['Candidate Age'].tolist()
Age14NDA = candidate_14[(candidate_14.Position == 1) & (candidate_14.Year == 2014) & (candidate_14.Alliance == "NDA")]['Candidate Age'].tolist()
bins = np.linspace(20, 90, 10)
plt.hist([Age14UPA, Age14NDA], bins, label=['UPA', 'NDA'])
plt.legend(loc='upper right')
plt.xlabel('Age Of winners in years')
plt.ylabel('Total Number of winners')
plt.title('Alliance wise Distribution of Age of the winners in 2014')
plt.show()

## 2009 vs 2014 party wise seat winners

## 2009 Party wise seat winners
winners09 = candidate_09[candidate_09['Position']==1]
# df09 = winners09['Party Abbreviation'].value_counts().head(10)

df09 = winners09['Party Abbreviation'].value_counts().head().to_dict()
s09 = sum(winners09['Party Abbreviation'].value_counts().tolist())
df09['Other Regional Parties'] = s09 - sum(winners09['Party Abbreviation'].value_counts().head().tolist())

fig = plt.figure()
ax09 = fig.add_axes([0, 0, 1, 1], aspect=1)
colors = ["#264CE4","#FF5106","#E426A4","#44A122","#F2EC3A","#C96F58"]
ax09.pie(df09.values(),labels=df09.keys(),autopct='%1.1f%%', pctdistance=0.8,radius = 1,colors = colors)
ax09.set_title("2009",loc="center",fontdict={'fontsize':20},position=(0.5,1.55))
plt.show()

## 2014 Party wise seat winners
winners14 = candidate_14[candidate_14['Position']==1]
#df14 = winners14['Party Abbreviation'].value_counts().head(10)
#print(df14)

df14 = winners14['Party Abbreviation'].value_counts().head().to_dict()
s14 = sum(winners14['Party Abbreviation'].value_counts().tolist())
df14['Other Regional Parties'] = s14 - sum(winners14['Party Abbreviation'].value_counts().head().tolist())
fig = plt.figure()

ax14 = fig.add_axes([0, 0,1,1], aspect=1)
colors = ["#FF5106","#264CE4","#E426A4","#44A122","#F2EC3A","#C96F58"]
ax14.pie(df14.values(),labels=df14.keys(),autopct='%1.1f%%',pctdistance=0.8,radius = 1,colors=colors)
ax14.set_title("2014",loc="center",fontdict={'fontsize':20},position=(0.5,1.55))
plt.show()

## 2009 party wise voter share

votespartywise09 = candidate_09.groupby('Party Abbreviation')['Total Votes Polled'].sum()
x09 = votespartywise09.sort_values(ascending=False)[:10].plot(kind="bar")
x09.set_xlabel('Party Abbrevations')
x09.set_ylabel('Votes in Million(100)')
votespartywise09.sort_values(ascending=False)[:10]
plt.show()

## 2014 party wise voter share

votespartywise14 = candidate_14.groupby('Party Abbreviation')['Total Votes Polled'].sum()
x14 = votespartywise14.sort_values(ascending=False)[:10].plot(kind="bar")
x14.set_xlabel('Party Abbrevations')
x14.set_ylabel('Votes in Million(100)')
votespartywise14.sort_values(ascending=False)[:10]
plt.show()

## State wise poll percentage 2009

pollper = elector_09.groupby("STATE").mean()
LS09 = pollper[['POLL PERCENTAGE']].round(1).sort_values('POLL PERCENTAGE',ascending=False)
ax1 = LS09['POLL PERCENTAGE'].plot(kind='bar',figsize=(10, 5))
for p in ax1.patches:
    ax1.annotate(format(p.get_height()), (p.get_x()+0.1, p.get_height()+2),fontsize=12)

plt.show()

## State wise poll percentage 2014

pollper = elector_14.groupby("STATE").mean()
LS14 = pollper[['POLL PERCENTAGE']].round(1).sort_values('POLL PERCENTAGE',ascending=False)
ax1 = LS14['POLL PERCENTAGE'].plot(kind='bar',figsize=(10, 5))
for p in ax1.patches:
    ax1.annotate(format(p.get_height()), (p.get_x()+0.1, p.get_height()+2),fontsize=12)

plt.show()

## State wise poll percentage 2009 vs 2014

pollper = elector_09.groupby("STATE").mean()
LS09 = pollper[['POLL PERCENTAGE']].sort_values('POLL PERCENTAGE',ascending=False).to_dict()
Y09=[2009 for i in range(35)]
S09=list(LS09['POLL PERCENTAGE'].keys())
P09=list(LS09['POLL PERCENTAGE'].values())

pollper14 = elector_14.groupby("STATE").mean()
LS14 = pollper14[['POLL PERCENTAGE']].sort_values('POLL PERCENTAGE',ascending=False).to_dict()
Y14=[2014 for i in range(35)]
S14=list(LS14['POLL PERCENTAGE'].keys())
P14=list(LS14['POLL PERCENTAGE'].values())


Data = {'YEAR':Y09+Y14,'STATE':S09+S14,'Poll_Percentage':P09+P14}
DF = pd.DataFrame(data=Data)
ax = plt.subplots(figsize=(6, 9))
sns.barplot(x=DF.Poll_Percentage,y=DF.STATE,hue=DF.YEAR)
plt.show()

## Seats won by alliances in 2009

SeatsWin = candidate_09[(candidate_09.Position==1)].groupby(['Alliance'])['Position'].sum()
SeatsWin.plot(kind ="pie",autopct='%1.1f%%',pctdistance=0.8,radius = 1)
plt.show()

## Seats won by alliances in 2014

SeatsWin14 = candidate_14[(candidate_14.Position==1)].groupby(['Alliance'])['Position'].sum()
SeatsWin14.plot(kind ="pie",autopct='%1.1f%%',pctdistance=0.8,radius = 1)
plt.show()

## State wise seats won per alliance

s09 = candidate_09[candidate_09["Position"]==1].groupby("State name")["Alliance"].value_counts()
alliance09 = candidate_09[candidate_09["Position"]==1]["Alliance"].unique()

l = []
for v in ["Andhra Pradesh", 'Arunachal Pradesh', 'Assam', 'Bihar', 'Goa',
       'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
       'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
       'Meghalaya', 'Mizoram', 'Nagaland', 'Orissa', 'Punjab',
       'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh',
       'West Bengal', 'Chattisgarh', 'Jharkhand', 'Uttarakhand',
       'Andaman & Nicobar Islands', 'Chandigarh', 'Dadra & Nagar Haveli',
       'Daman & Diu', 'NCT OF Delhi', 'Lakshadweep', 'Puducherry']:
         win_party09 = s09[v][alliance09]
         l.append(win_party09.values)
            
df = pd.DataFrame(l,index=["Andhra Pradesh", 'Arunachal Pradesh', 'Assam', 'Bihar', 'Goa',
       'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
       'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
       'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
       'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh',
       'West Bengal', 'Chattisgarh', 'Jharkhand', 'Uttarakhand',
       'Andaman & Nicobar Islands', 'Chandigarh', 'Dadra & Nagar Haveli',
       'Daman & Diu', 'NCT OF Delhi', 'Lakshadweep', 'Puducherry'],columns=alliance09)
s = df.plot(kind="bar",stacked=True,figsize=(18,8),fontsize=15)
s.set_title("State wise seats won per Alliance (2009)",color='g',fontsize=30)
s.set_xlabel("States",color='b',fontsize=20)
s.set_ylabel("No. of seats",color='b',fontsize=20)
plt.show()

s14 = candidate_14[candidate_14["Position"]==1].groupby("State name")["Alliance"].value_counts()
alliance14 = candidate_14[candidate_14["Position"]==1]["Alliance"].unique()

l = []
for v in ["Andhra Pradesh", 'Arunachal Pradesh', 'Assam', 'Bihar', 'Goa',
       'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
       'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
       'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
       'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh',
       'West Bengal', 'Chattisgarh', 'Jharkhand', 'Uttarakhand',
       'Andaman & Nicobar Islands', 'Chandigarh', 'Dadra & Nagar Haveli',
       'Daman & Diu', 'NCT OF Delhi', 'Lakshadweep', 'Puducherry']:
         win_party = s14[v][alliance14]
         l.append(win_party.values)
            
df = pd.DataFrame(l,index=["Andhra Pradesh", 'Arunachal Pradesh', 'Assam', 'Bihar', 'Goa',
       'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
       'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
       'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab',
       'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh',
       'West Bengal', 'Chattisgarh', 'Jharkhand', 'Uttarakhand',
       'Andaman & Nicobar Islands', 'Chandigarh', 'Dadra & Nagar Haveli',
       'Daman & Diu', 'NCT OF Delhi', 'Lakshadweep', 'Puducherry'],columns=alliance14)
s=df.plot(kind="bar",stacked=True,figsize=(18,8),fontsize=15)
s.set_title("Statewise seats won per Alliances (2014)",color='g',fontsize=30)
s.set_xlabel("States",color='b',fontsize=20)
s.set_ylabel("Seats",color='b',fontsize=20)
plt.show()




