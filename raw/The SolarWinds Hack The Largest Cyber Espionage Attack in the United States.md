---
title: "The SolarWinds Hack: The Largest Cyber Espionage Attack in the United States"
source: "https://www.youtube.com/watch?v=Kf7Motm36Go"
author:
  - "[[The TWS Channel]]"
published: 2021-07-11
created: 2026-05-05
description: "In December of 2020, one of the worst cyber espionage incidents in the United States was uncovered, this is the story of the SolarWinds hack.Chapters:Intro - 00:00Chapter 1 - 01:10Chapter 2 - 05"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=Kf7Motm36Go)

In December of 2020, one of the worst cyber espionage incidents in the United States was uncovered, this is the story of the SolarWinds hack.  
  
Chapters:  
  
Intro - 00:00  
Chapter 1 - 01:10  
Chapter 2 - 05:07  
Chapter 3 - 10:42  
Chapter 4 - 20:01  
Song - 23:34  
  
You can support me on: https://www.buymeacoffee.com/thetwschannel  
  
References:  
https://pastebin.com/iCRvJBRV

## Transcript

### Intro

**0:02** · \[Music\] december of 2020 during the fallout of the american presidential election between former president donald trump and current president joe

**0:21** · biden the chaos that ensued would effectively dampen the amount of attention that would be brought to what is said to be possibly one of the worst cyber espionage incidents in united states history in this attack multiple fortune 500 companies as well as government organizations were compromised prompting bitter relationships between two large nations and some even anticipating the prospect of war

### Chapter 1

**1:14** · december 8 2020 a member of the security team in the cyber security company fireeye discovers that a new unknown device has been registered to an employee in order to perform multi-factor or two-factor authentication you may be familiar with this process as it's often used to authenticate most of our devices and accounts you put in your username and password you get a unique code to your mobile device or email and then you enter the code to get access this is the same process that is

**1:44** · required in order to connect to fireeye's private network or vpn by owning a device that receives this unique code the attackers can almost stealthily access fireeye's internal network but whether it was stroke of luck or a heightened awareness and caution of the security team at fireeye due to the ongoing election this wouldn't go unnoticed so they call up the employee to confirm and sure enough this employee had not registered any new

**2:12** · devices it then became apparent that someone outside was watching secretly lying in wait who knows what they've seen or what they've taken try and put your feet in the shoes of a company whose primary target is to develop cyber security solutions whose vision is to keep their customers and the community at large safe from cyber attacks and then you find that you yourself have become a victim

**2:37** · in addition to the compromise fireeye discovers that a bunch of penetration testing and assessment tools which were said to replicate some of the most sophisticated hacking tools in the world was stolen red team assessment tools like these are often used to test the defense of organizations with their permission resulting in an assessment of how secure the organization is but if someone malicious were to gain access to these they could essentially use it to find vulnerabilities in other organizations and then rather than report it exploit

**3:06** · it instead and so needless to say this became a major concern we don't know what went through the ceo of fireeye kevin mandia's mind at that particular moment of realization but in an interview with npr he did mention that and i quote it just felt like the breach that i was always worried about from fire's initial blog post we'd also find out that the attack was not attributed to anyone particular as of yet but was identified to be the work of some state-sponsored attacker

**3:38** · and so frighteningly a nation-state attack investigations would then proceed to probe further into the hack and according to their blog post fireride then begins working with the fbi and microsoft and on friday the 11th of december they would trace the attack back to the source the earliest evidence of compromise pointing to a network monitoring tool by solarwinds called orion with approximately 4 000 lines of malicious code in the updates released to the software between march and june of 2020. the name of the attack

**4:08** · can vary depending on who you ask fireeye would call this attack sunburst and microsoft would refer to it as solarigate on sunday december 13th all this would become public when fireeye solarwinds and the cisa released a statement along with a breakdown of how the attack worked the attack would be classed as a supply chain attack and we'll get to what that is in a bit at this point it is surmised that the threat actors unc 2452 which was the name to the

**4:37** · perpetrators given by fireeye had begun their campaign as early as spring putting the earliest possible intrusion or initial compromise in the timeline to somewhere between march and june of 2020 but as you'll come to find out soon this is far far from accurate

### Chapter 2

**5:12** · a supplier purchases raw materials they decide what they want it to become then they pass it on to the manufacturer who follows a strict set of processes before it is turned into the finished product it is then handed to a distributor whose job is to safely transport the product to a retail outlet where it is shelved with a price at which point we the consumers have the liberty to purchase the product

**5:35** · if it is defective or not what we expected there are return refund processors in place this is the traditional supply chain model software development has a similar supply chain starting from planning the features and the code to be used in the software then the sourcing stage consists of deciding which code to produce in-house

**5:55** · and which to source externally then there's distribution concerned with how the product will be delivered to the customer and then there's maintenance and support post purchase by definition a supply chain attack is a type of cyber attack that targets the weakest component in this supply chain to gain access to something down the line that is more secure

**6:16** · since the supply chain in itself is quite vast and consists of many minute procedures within each component supply chain attacks can be difficult to take measures against since you can't exactly control the security of every single player that is part of the process in the case of sunburst solarwinds was a third party within the supply chain of many large organizations they provided a bunch of softwares one of which was their flagship network management platform orion

**6:44** · orion consists of a variety of products all aimed towards giving organizations visibility and control over their iit network routers switches printers servers firewalls every network device in an organization could be monitored with this tool and with a simple dashboard it presents the data in a unified manner as well as if needed provides necessary controls to act and remediate issues in order to do any of this the

**7:11** · orion platform is required to be in a privileged role to be trusted by all these devices that is feeding the platform data customers trust vendors customer machines trust bend applications trust the keyword that provides effectiveness to a supply chain attack any organization that decides to incorporate a third-party vendor into their supply chain does so with an assumed trust therefore

**7:36** · when a malicious individual is able to take advantage and compromise this trust it can truly lead to devastating circumstances in addition to assume trust being a major benefit to the attackers what's even more terrifying with supply chain attacks is that the targeting of vendors leads to a multitude of victims vendors like solarwinds who provide their service to large organizations often have a boatload of customers at the time of the hack solarwinds had 300 000 customers 33 000 of them which were

**8:05** · actively using the orion platform out of these 33 000 18 000 had downloaded these update versions which were the updates that were released by solarwinds between march and june of 2020 and were the updates that carried the tainted 4000 lines of malicious code entering into unsuspecting systems as a trojan horse and implanting a back door in order to gain access in the future however thankfully there were specific

**8:31** · conditions that determine the real victims simply downloading the update would not be enough it would need to be installed and deployed as well along with an active internet connection perhaps what saved most organizations was how extremely targeted the attack was even if there were 18 000 backdoors implanted in 18 000 organizations

**8:51** · which were exposed to this vulnerability in order to not trip any wires and alert their victims by running automatic functions the attackers would need to have manually accessed through this backdoor 18 000 times in order to escalate privilege and view or steal data from every single victim

**9:08** · it's doubtful that this supposed to be too much of a problem for the attackers since it's probably safe to say that they initially decided to hack solarwinds solely because of their most high profile clients how would they know who their clients are well prior to the hack solarwinds actually had a list of their customers on their website clearly stating that they provide to 425 of the us fortune 500 every single branch of the military the us pentagon nasa nsa and as you can see tons and

**9:38** · tons more however since the hack this customer list has been taken down and whether it was right to display this so openly in the first place is up for debate i mean there are a lot of organizations that do tend to do this but maybe when your customers consist of the entire military as well as the majority of the government it's probably a good idea not to publicize that to the world think

**10:04** · margaret it's important to note everybody says this is potentially the biggest intrusion in our history the reality is the blast radius for this i kind of explain it with a a funnel it's true that over 300 000 companies use solarwinds but you come down from that total number down to about 18 000 or so companies

**10:26** · that actually had the backdoor or malicious code on the network and then you come down to the next part it's probably only about 50 organizations or companies some are in that zone that's genuinely impacted by the threat

### Chapter 3

**10:44** · act apd-29 dubbed by crowdstrike as teleparticle rebellium by microsoft dark halo by velec city unc 2452 by fireeye all these and more are used to refer to the attackers behind the solarwinds hack to understand the sophistication and the extreme cautious nature of these attackers we need to get back into the timeline

**11:09** · initial statements made on the 13th of december 2020 pointed to its earliest compromise placed somewhere in between march and june of the same year due to the updates being deployed within this time frame however a month later sudarka ramakrishna the ceo of solarwinds would release an article on the solarwinds block site along with a timeline that suggested that the attackers may have entered all the way back in september of 2019.

**11:34** · this timeline also matches up to the one provided by microsoft in their deep dive of the attack from september of 2019 to december of 2020.

**11:43** · it took 15 months since entry for the first reported detection it has also been said that the attackers may have been lurking in the solarwinds office 365 email accounts that entire time but time has revealed more and it's got a little bit more convoluted the timelines presented by these organizations is possibly somewhat accurate however the fact that the attack is very recent and investigation is still ongoing brings more and more information

**12:08** · to the table as we go and therefore the timeline can often be altered in the process during the rsa conference in may of 2021 just a month prior to the release of this video laura ketzel the vice president and group director forester had a session with sudha ramakrishna ceo of solarwinds and here's what he had to say it was a very difficult thing to uncover but as we've been looking back into our

**12:35** · history and we have stumbled upon and as is the case with many investigations uh some old configuration of code where we were able to track down what exactly the attackers did and this was to give you a perspective we were assessing hundreds of terabytes of data

**12:56** · and thousands of build systems virtual build systems across the environment just to give you a perspective and what we have found more recently is that the attackers may have been in our environment as early as january 2019.

**13:13** · we publish obviously that it was in the september october time frame but as we look back they were doing very early recon activities in january of 2019 which explains i would say what they were able to do in september october of 2019 as well got it okay so even since january of 2019 that puts the

**13:37** · attackers in the solarwind system for almost two years and there's really no confirmation that this was the date or month of infiltration it's just what the investigation has revealed so far i don't need to tell you how much is capable in that time frame just imagine if an attacker was watching your every move on your computer for two straight years watching waiting and possibly stealing

**13:59** · data and now imagine this same scenario with an organization that provides a service to customers across the world four-fifths of the fortune 500 and multiple branches of the us government including the u.s energy department responsible for the united states nuclear arsenal it truly is a terrifying thought that the threat actors were able to look for so long without tripping any major wires

**14:22** · especially in companies that even specialize in security taking a look at the methods employed by the attackers reveals how exactly this was possible there's been four malware variants discovered ever since the solarwinds hack came to light we have sunspot sunburst teardrop

**14:40** · and raindrop sunburst in this context is not referring to the attack itself but to an element of the attack as a whole the entire attack including sunspot teardrop and raindrop are all part of the sunburst supply chain attack sunspot refers to the malware that was used to place the sunburst backdoor into the orion platform within solarwinds

**15:01** · the way it worked was quite remarkable you see when building software there is something called the compilation process is at this time the written code goes from high level language which is language that is easily comprehensible by human beings to low level or machine language which is better understood by computers this is also known as source code and executable or object code

**15:24** · before it goes through this process code is often audited there's many reasons for this one of which is to ensure that the code has not been tampered with in any way and so the attackers designed sunspot to catch the process msbill.exe which essentially calls out

**15:40** · that the audit of the code is completed and that the code is about to be turned from source code to object code it is at this final moment when it cannot be caught that sunspot switches the developer's code with the malicious code instead it is then compiled and the malicious code is injected successfully into the solarwinds update and solarwinds oblivious to it makes the update available to all its customers

**16:04** · once the sunburst backdoor reached the client's network it did a few things to stay undetected it waited for a period of 12 to 14 days before starting to do anything malicious this is because new updates can sometimes be monitored for issues in order to not affect business continuity it then disabled all antivirus and forensic tools that could detect the malware once it has successfully disabled them it communicates with what's known as the command and control or c2 server to send information such as

**16:32** · the ip address operating system version usernames all which allows the perpetrators to identify which organizations the compromised computer belongs to using the ip address the malware decides whether it wants to act passively actively or to entirely disable itself

**16:49** · if the address corresponds to one which the attackers want to pursue further it assigns a unique c2 server to the victim and then the attackers begin to manually intervene and perform hands-on keyboard attacks according to the timeline the hands-on keyboard attack starts somewhere during may with which they attempt to escalate privilege and take control of higher value accounts steal credentials and assets then

**17:13** · in around june is where teardrop and raindrop come in there are notable differences between teardrop and raindrop but their primary function is the same to place what is known as a cobalt strike beacon a very popular pen testing tool designed to detect network vulnerabilities and has often been used in malware before to find newer and more dangerous ways to exploit their victims around three to four days after the attack became public fireeye along with

**17:39** · microsoft and godaddy worked together in order to produce a kill switch a method to shut the malware down if you recall depending on the dns response sent from the victim the malware may disable itself experts at godaddy took advantage of this and discovered that if the victim responded with an ip address from the microsoft ip range it would prompt the malware to switch to a disabled state and so godaddy manipulated the dns to always respond with an ip from the microsoft ip range this ended up becoming the kill switch

**18:10** · other than the methods mentioned the attackers used a host of other techniques to avoid detection such as only using us domains for the victims command and control server to communicate with in order to raise minimal suspicion if it was trying to communicate with a server outside the country this would have immediately been a red flag they also used the gold and saml technique the first of its kind seen in the wild that allowed the attackers to impersonate any user with any privilege

**18:36** · and completely bypass multi-factor authentication by forging a response from the authentication server to make it seem as if their identity was verified it is clear how well planned and sophisticated the attack was the true danger of this attack is in the questions that it leaves behind there's still new information that is being revealed and it has been said the scope of the attack and exactly how much information was revealed or stolen will be left to uncover for years to come

**19:02** · even to this date there is no confirmation on how the attacker initially breached solarwinds to implant the sunspot malware there's been a few theories including the embarrassing case of an intern at solarwinds who protected a file server in the company with the password solarwinds123 which

**19:18** · was discovered in 2019 by an independent security researcher by the name of venut kumar who brought it to their attention and this password has been said to have been in use since 2017 well after the intern had left the organization however there's still nothing that points to this being the cause of the infection

**19:39** · so mr ramakrishna reclaiming my time i've got a stronger password than solarwinds123 to stop my kids from watching too much youtube on their ipad you and your company were supposed to be preventing the russians from reading defense department email

### Chapter 4

**20:03** · on january 5th 2021 the cisa along with the fbi nsa and the odni stated that the attack was likely russian in origin few months later on april 15 2021 the white house under the biden administration released a statement officially attributing the solarwinds hack to the russian foreign intelligence service svr expressing that they have high confidence in their assessment

**20:29** · in this statement they also introduced multiple new sanctions as response to the hack as well as in response to other conflicts with russia they exposed several technology companies that they believed to be supporting russian intelligence services in their cyber criminal activities and even issued warnings about dealing with any organizations that store user

**20:48** · data in russia or receive any type of remote technical support from russian personnel president biden spoke of his conversation with the russian president vladimir putin where he said i was clear with president putin that we could have gone further but i chose not to do so i chose

**21:05** · to be proportionate however russia completely denied any involvement in the hack the director of the russian foreign intelligence services called the claims a bad detective novel and even said that he would be flattered if they were involved in the attack due to its sophistication but that they couldn't take credit for it shortly after the sanctions were announced the russian deputy foreign minister conveyed to the u.s ambassador that the sanctions will be met with a series of retaliatory measures

**21:33** · the united states has stood its ground saying that there has been compelling evidence and that the hack has matched many years of russian foreign intelligence activity of course even if russia were truly involved it's highly unlikely that they'd come right out and say it considering the implications but on the

**21:49** · other hand with the limited information provided to the public as to the precise reason behind the attribution it's hard for us to come to a warranted conclusion the best we can do is make up our own hypothesis whatever said and done one thing is for sure nation state hacks have become increasingly prevalent and something to be very worried about

**22:10** · we live in an age where data and information can often be more powerful than weaponry and it wouldn't be a surprise if such hacks can bring the possibility of war on to the table luckily this attack did not employ any sabotage but mostly consisted of information gathering it's hard to

**22:26** · imagine that the repercussions would have been so lenient if there were any serious sabotage involved the extent of this attack is also something to be wary about security companies like malwarebytes and mimecast who had no relation to the solarwinds supply chain attack also found traces of apt-29 in their

**22:44** · systems possibly due to compromise within microsoft and there have been recent cases of cyberattack that ties to the solarwinds hack as well it seems that security has now reached a point where the measures you take to keep your system secure may not be enough anymore and that every application every code and every tool that you utilize designed by any external party can threaten your data security which is a terrifying realization to a majority of organizations worldwide because they simply cannot function without such vendors nor should they be expected to it's like

**23:16** · you're driving on the road on your lane at the right speed in a vehicle that you deem to be in perfect condition but all it takes is someone else to come along doing all the wrong things and thank you for watching \[Music\]

### Song

**23:56** · \[Music\]

**24:38** · \[Music\]

**25:34** · \[Music\] so \[Music\] you