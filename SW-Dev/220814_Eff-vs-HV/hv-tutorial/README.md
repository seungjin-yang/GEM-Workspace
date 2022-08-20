-  /afs/cern.ch/user/f/fivone/public/HV_Fetch_Data/DCS_Fetcher 
- `python GEMDCSP5Monitor.pyc 2022-04-01_15:22:31 2022-04-02_15:22:31 HV 0 -c all`
- https://github.com/gem-dpg-pfa/PFA_MaskGenerator



## [Email thread] Tool to retrieve HV data from database 
### From: [Francesco Ivone](francesco.ivone@cern.ch); Sent: Wednesday, August 17, 2022 1:36 AM
> Hi, </br>
At [1] you can find a version of the script provided by Simone to fetch the DCS database.  </br>
The exact name of the db and the password are taken from env variables.  </br>
The details of password and username can be provided by Simone in cc.  </br>
If the psw can’t be shared, we might think to get a compiled version of the code, having the psw hard coded.  </br>
>  </br>
> Best, </br>
Francesco </br>
> * [1] https://github.com/gem-dpg-pfa/P5GEMOfflineMonitor

### From: [Kamon, Teruki](kamon@physics.tamu.edu); Sent: 17 Aug 2022, at 17:21
> Thanks! </br>
Q1: Can we share the P.W. with Seungjin? </br>
Q2: What will Simone take his vacation? How long? </br>
Q3: Will you could have efficiencies some time in this week? </br>
Also: how much data (luminosity) for efficiency will be requited? </br>
In Run2 slice test, with 200 nb-1, we had ~ 4500 muons (pT > 20) per chamber. </br>
Approximately 200 per VFAT.  This is a good amount. </br>
Teruki

### From: [Francesco Ivone](francesco.ivone@cern.ch); Sent: Aug 17, 2022 12:51 PM
> Hi Teruki, </br>
Q3: I have produced efficiencies for runs taken Thursday and Friday last week. Data take few days before being available. I can produce some more plots.  </br>
> </br>
> On the statistics: </br>
the analyzed data were taken from the Express dataset. Therefore they have pretty low statistics (order of 50 prop hits per vfat). I’m now trying to use a different dataset to get more hits.  </br>
The runs I have analyzed have delivered a lot of luminosity (50pb^-1) per run.  </br>
> </br>
>Best, </br>
Francesco
 
 
### From: [Kamon, Teruki](kamon@physics.tamu.edu); Sent: Wednesday, August 17, 2022 7:56 PM
> Thanks. </br> 
A question is the efficiency at 690 uA, and do we need to go up to 700 uA. </br>
Teruki 

### From: [Francesco Ivone](francesco.ivone@cern.ch); Sent: Thursday, August 18, 2022 11:04 AM
> Hi Teruki, </br>
> </br>
> the tool to fetch DCS HV data is available at [1] </br>
At [2] there is a typical usage, that will fetch HV data for all chambers. Time range will be from 2022-04-01_15:22:31 to  2022-04-02_15:22:31
> </br>
> The tool [1] can be combined with the tool [3] to get HV points from run number. </br>
Let me know if anyone needs more input on how to integrate [1] and [3]. </br>
> </br>
> Best, </br>
> Francesco </br>
> </br>
> * [1] /afs/cern.ch/user/f/fivone/public/HV_Fetch_Data/DCS_Fetcher </br>
> * [2] python GEMDCSP5Monitor.pyc 2022-04-01_15:22:31 2022-04-02_15:22:31 HV 0 -c all </br>
> * [3] https://github.com/gem-dpg-pfa/PFA_MaskGenerator


### From: [Kamon, Teruki](kamon@physics.tamu.edu); Sent:  19 August 2022 01:10 
> Francesco: Great! </br>
> </br>
> Seungin: please take a look. You could perform it with offline DQM. </br>
One might see this is a duplicate effoet with PFA. </br>
But nice too see a correkation between DQM and PFA
