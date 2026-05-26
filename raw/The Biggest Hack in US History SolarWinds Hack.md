---
title: "The Biggest Hack in US History: SolarWinds Hack"
source: "https://www.youtube.com/watch?v=Eq6ATHhBezw"
author:
  - "[[Cybernews]]"
published: 2025-08-22
created: 2026-05-05
description: "At one point in 2019, somebody managed to hack the entire government of the United States and some of the country’s biggest corporations in one sweeping atta..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=Eq6ATHhBezw)

## Transcript

### Intro

**0:00** · Imagine you're a guard at the White House.

**0:03** · You monitor security cameras.

**0:05** · Of course, you're not just a security guard.

**0:08** · You're a member of the Secret Service.

**0:10** · You went through a tough selection process and grueling training, but you still don't have their complete trust.

**0:16** · As you monitor the cameras, you yourself are being monitored by your coworkers and superiors.

**0:21** · There is a sophisticated system in place to make sure the Office of the President of the United States is safe.

**0:26** · And those superiors?

**0:28** · Well, they're monitored too.

**0:29** · Not for safety, but for convenience.

**0:32** · The information they work with is handled by special management software.

**0:35** · It makes sure everybody's on the same page and that any anomalies and intrusions are handled correctly.

**0:41** · But there is a level above even that.

**0:44** · It appears this system is monitored too.

**0:47** · Somebody has access to every bit of data that goes around the White House like it's their very own server, and that somebody is not a high-level officer or security chief or even the President.

**0:59** · It's an intruder, somebody who just got into the White House network monitoring system and took it over.

**1:06** · This was done through a back door, an access point that gave the intruder direct access to the whole system.

**1:13** · For months, the door to the White House was wide open.

**1:16** · The attackers could get inside and see whatever they wanted whenever they wanted.

**1:21** · Unfortunately, unlike your position as the White House security guard, this attack was not fictional.

**1:27** · It was real.

**1:29** · We know about it because in due course, despite all the precautions on the attacker's part, the back door was discovered.

**1:36** · It turned out that the security system and the White House at large was not the only thing compromised this way.

**1:42** · Pretty much every branch of the American government and military, and thousands of the largest companies in the world had the same backdoor in their systems, and every single one of them was delivered with the same software: SolarWinds.

**1:57** · It didn't take long for revelations to sink in and for the cybersecurity community to understand how deep the rabbit hole went.

**2:04** · Today, several years later, this attack is already remembered as one of the largest cyber espionage scandals in history.

**2:12** · The story of how one company led to the entire government being compromised, the story of the SolarWinds hack, and how after it happened, there was no rollback.

### Baseline

**2:26** · The high-tech world we live in is incredibly complicated.

**2:29** · There are thousands of companies that offer niche products for almost anything.

**2:33** · Most people have never heard of them despite relying on services those companies provide.

**2:38** · Just think of a device you're watching this video on.

**2:41** · Most likely, you bought it from a store.

**2:44** · To get there, that device had to be transported through a number of warehouses, logistics hubs, ports, and terminals.

**2:50** · Before that, it had to be assembled.

**2:53** · Its components were manufactured in different factories by different companies that have very little to do with each other.

**2:59** · Each of those companies may have employed their own contractors who designed and produced some minor parts, and each of those contractors may have had all kinds of partnerships and subcontractors of their own.

**3:12** · While your device has only one name printed on its body, the name hides dozens, maybe hundreds, maybe even thousands of other names, countless major and minor companies that have been involved in a mind bogglingly complicated process to get this one device in front of you.

**3:28** · The same goes for software that runs on this device.

**3:32** · How many apps are there?

**3:34** · Do you know what each of them does, and how many companies that make those apps rely on other companies that make their software?

**3:41** · This is the reality of modern-day supply chains.

**3:44** · They're so complicated, no single person can really comprehend them.

**3:48** · Everybody relies on everybody else.

**3:50** · It's the price we pay for casually using things that would have been considered pure magic just a century ago.

**3:57** · A byproduct of this situation is an abundance of incredibly powerful and incredibly important names that you've never heard of.

**4:05** · Companies instrumental in keeping things running.

**4:08** · The device you're looking at right now, the website that serves you this very video, the channel that created it.

**4:13** · Like and subscribe by the way.

**4:15** · All of them use hundreds of tools to make their lives easier.

**4:19** · There's just no other way to survive in the modern economy.

**4:22** · Now, imagine a fault in one of those tools.

**4:25** · Not an accident, but a deliberate act of sabotage.

**4:29** · One of the gazillion companies in the supply chain has been compromised.

**4:33** · What happens next?

**4:35** · The compromise reverberates through the whole chain.

**4:38** · The clients of the company don't notice the sabotage because they have their own problems to worry about.

**4:43** · The problems travel down the chain, infecting everything downstream.

**4:47** · You didn't do anything wrong.

**4:48** · The company that supplied the product did nothing wrong either.

**4:51** · But its vendor's, vendor's, vendor was hacked, and so you get hacked as well.

**4:57** · This is called a supply chain attack, and it's hands down one of the most insidious and dangerous kinds of attacks there is.

**5:04** · It's also one of the most popular.

**5:06** · Chances are, if, for example, your personal data has ever been stolen by hackers, they got it through a supply chain.

**5:12** · A company that held it was infected through another company that didn't do its due diligence, one of its vendors who didn't, or somebody else down the chain.

**5:22** · In many, many cases where governments or large corporations get hacked, it was a supply chain attack.

**5:28** · In 2022, the personal IDs of nearly every single Chinese citizen, over a billion of them, were leaked on a Dark Web forum because a developer contracted by the Chinese police left a bug in the database.

**5:41** · In 2017, the world's most damaging cyberattack known as NotPetya, happened because a Ukrainian tax accounting software company was breached and spread the infection to all its clients.

**5:52** · From what we know, Stuxnet, the most advanced cyber weapon of its time, was most likely delivered through a compromised supply chain: a water pump infected by malware and sold by a man who turned out to be a spy.

**6:05** · Some of the biggest and best known cyberattacks in history were supply chain attacks.

**6:10** · A lot of them were perpetrated by the United States government, and in the particular case of SolarWinds, the United States government was on the receiving end of this treatment.

### Trigger

**6:20** · SolarWinds is based in Texas.

**6:22** · It's not a small company by any stretch.

**6:24** · It's valued at around $4 billion, so similar in size to something like Craigslist or Vinted.

**6:30** · But unlike these companies, barely anybody has heard of SolarWinds because the company just doesn't deal with an average consumer.

**6:37** · All of its services are aimed at other companies.

**6:40** · SolarWinds builds software for them, management software, specialized programs designed for specialized work.

**6:47** · No matter who makes your hardware, NPM can make it easy to reduce outages and help quickly detect, diagnose, and resolve performance issues.

**6:56** · View traffic, configuration, and performance details for on-prem, hybrid, and cloud services using critical path hop-by-hop analysis with NetPath.

**7:05** · As you can see, these aren't the products your average consumer might buy.

**7:09** · Noob-friendly and foolproof they are not.

**7:12** · But software like this is crucial to manage the mess inside multi-billion-dollar corporations.

**7:18** · SolarWinds found itself a niche as one of countless links in worldwide supply chains.

**7:23** · By 2019, its tools were used at 425 of the Fortune 500 companies, every single one of the top 10 American telecommunications providers, all branches of the US military, and even the Office of the President of the United States.

**7:39** · This is just the first few paragraphs of the full customer list on the SolarWinds website.

**7:45** · For managers at SolarWinds, this list probably looked like a great idea.

**7:49** · After all, wouldn't you want to brag if you sold your software to the White House?

**7:54** · But not everyone saw it this way.

**7:56** · It's almost certain that in 2018, this very web page caught the attention of a different kind of audience, a group of people who found it useful for entirely different reasons, a threat actor that didn't hesitate to use it not as a list of achievements, but as an invitation, one they were more than happy to accept.

### Execution

**8:16** · Here's what, to our knowledge, could have happened next.

**8:19** · Full disclosure, we don't know the exact way hackers initially got into SolarWinds' systems, and SolarWinds claims it doesn't know either.

**8:27** · But it almost certainly involved a zero-day vulnerability, brute force or phishing, or all the above.

**8:33** · We also know about at least one other attack perpetrated by the same hackers and performed at almost the same time.

**8:40** · That attack involved, you've guessed it, a zero-day vulnerability and phishing.

**8:45** · Now, just to visualize how insidious the breach of SolarWinds was, let's speculate a bit and pretend that it saw the use of the same tools and techniques as the other attack.

**8:55** · In that case, it would have went like this.

**8:58** · In early 2019, an employee at SolarWinds gets a message on LinkedIn.

**9:02** · The contents of the message may look like this, or this, or even this.

**9:08** · The message contains a link.

**9:10** · The employee clicks on it.

**9:12** · It's easy to look at it and laugh, but believe it or not, the link has absolutely zero red flags.

**9:17** · It looks legitimate.

**9:18** · No pop-up ads, no weird redirects, just a regular website.

**9:23** · There's very little the attacked person can do in this situation.

**9:26** · Anybody can be phished this way because it's a zero-day attack.

**9:30** · The link uses a yet unknown vulnerability in Apple Safari, a vulnerability that won't get discovered and patched until 2021.

**9:38** · Basically, it exploits a bug in the browser's same origin policy, a function that allows sharing scripts across the websites you visit.

**9:46** · Thanks to this function, you don't have to log into a website every time you open a new page.

**9:50** · The malicious file downloaded through this bug pretends being the next page and gobbles up all the cookies saved in the browser.

**9:57** · Logins to Facebook, LinkedIn, Microsoft, Google.

**10:01** · Nearly every system the SolarWinds employees had access to is now accessible to the hackers.

**10:07** · At least that's what the same attackers did to multiple other high-profile victims at the same time.

**10:12** · The same attack vector could have been used to breach SolarWinds too.

**10:16** · If so, it was most likely performed several times, over and over again, until the hackers got enough credentials to pierce the entire system of SolarWinds.

**10:25** · In a matter of several months, the company's network was hacked through and through.

**10:30** · This is when the mayhem began.

**10:32** · Had the attackers been a regular hacker, a hacktivist, or a cybercriminal cartel, they could have used this access to wreak havoc across the world.

**10:40** · They could have stolen the data of thousands of companies shared through the networks and devices monitored by SolarWinds.

**10:46** · They could have bricked those networks with an encryptor or a wiper, but they didn't.

**10:51** · Instead, they played the long game.

**10:54** · They zeroed in on Orion.

**10:56** · It was one of the most popular products at SolarWinds, a platform with tools your average network engineer wouldn't know how to tie their shoes without.

**11:04** · The attackers gained access to SolarWinds' systems that pushed out updates for the software, and they implanted a Trojan there.

**11:11** · So along with new updates, every single Orion user got a back door, a program that would allow direct access to their system.

**11:19** · It looked like a regular update file, a DLL file you would find in Orion.

**11:23** · But the primary job of that file was to regularly communicate with a command and control server of the attackers and also mask their communication as just regular traffic.

**11:33** · The DLL would basically have two stages of activity.

**11:37** · In the first stage, it would call up to the server and the server would respond in several predetermined ways.

**11:43** · If the masterminds behind the malware heard the call and deemed the target to be worthy of further penetration, the server would order the malware to transition into the second stage: hands-on access.

**11:55** · Usually, the next step was to load some additional malware, which would make spying or exfiltrating files easier.

**12:01** · Sometimes this malware was completely custom, tailor-made for a particular target.

**12:06** · Creating something like this was time-consuming and resource-intensive, though.

**12:10** · Sometimes, the hackers were a bit more creative.

**12:13** · For at least several targets, they used a set of tools taken directly from Cobalt Strike, penetration testing software many companies use to check their networks for security holes.

**12:22** · These tools were scavenged, modified, and used to further backdoor the device or obfuscate the traffic.

**12:29** · That's right.

**12:29** · The threat actor disassembled a legitimate security tool and pieced together a nasty malware.

**12:35** · What's even more insidious is that the hackers also found a way to use SolarWinds' authentication system in this process.

**12:41** · The malicious code, the infected DLL they pushed out, was signed by SolarWinds and marked as safe.

**12:48** · No antivirus could have protected against it, and detecting this kind of attack was extremely difficult.

**12:54** · Just imagine it, 425 of the Fortune 500 companies, every single one of the top 10 American telecommunications providers, all branches of the US military, and even the Office of the President of the United States.

**13:10** · One update, and a Trojan sits in all of their systems.

**13:14** · Infecting all of these targets one by one would take years and require hundreds of unique vulnerabilities and exploits.

**13:21** · But with a supply chain attack, one vulnerability was enough to rule them all.

**13:25** · Well, this really sounds quite dramatic, and it definitely did sound like that when the attack was discovered in late 2020.

**13:32** · In reality, the attackers didn't have an Orion-like overview of all of their victims.

**13:37** · From what we know about it, each attacked network had to be attended separately and loaded with malware best adapted for that particular system.

**13:45** · While the resources and manpower behind this attack were undeniably massive, the attackers couldn't pump out terabytes of data from all the victims at once.

**13:53** · They had to carefully choose what breaches they wanted to exploit and what data they wanted to download.

**14:00** · Out of the total of 300,000 SolarWinds customers, around 33,000 used Orion.

**14:06** · Out of those, around 18,000 downloaded one of the infected updates.

**14:10** · Out of those, at least several dozen had their data stolen by the attackers.

**14:15** · We can only speculate who those several dozen were, although the clues we have point to them being the highest echelons of the American government.

**14:23** · After all, Orion was used by the White House, the Department of Defense, and the National Security Agency.

**14:29** · Simply put, there's just no data more valuable than that anywhere else in the world.

### Post Mortem

**14:36** · So it's safe to say that pretty much the entire top of the American government was compromised.

**14:41** · Their information sharing networks were breached for approximately a year.

**14:45** · A portion of the sensitive information the departments and the agencies shared with one another had been siphoned through a back door in SolarWinds' software.

**14:53** · As you might have guessed, the institutions that were on the receiving end of this attack are not keen on saying what exact data was leaked and how deep inside the government the attackers infiltrated.

**15:03** · Did it lead to NSA spies getting exposed?

**15:06** · Were the Pentagon's war plans stolen?

**15:08** · Did the hackers access security feeds from the restrooms at the White House?

**15:12** · Most likely, we'll never know, because not only is this information a national secret, it's extremely embarrassing for all parties involved.

**15:20** · A part of this embarrassment was that the backdoor wasn't discovered by government employees.

**15:24** · Neither NSA's hackers nor DOD's Cyber Command were the ones to find this hack.

**15:29** · Instead, it was a cybersecurity company, FireEye, one of SolarWinds' clients.

**15:34** · The man often credited with this discovery is their former engineer, Stephen Eckels.

**15:39** · Where my journey started was we started up an internal incident response investigation at then FireEye, now Mandiant, as part of Google.

**15:49** · Remember Cobalt Strike, the repurposed cybersecurity testing tool?

**15:53** · FireEye detected its use on their network.

**15:56** · Our incident response team started digging into our environment, and they were able to trace at least the Cobalt Strike activity back to a SolarWinds appliance.

**16:05** · Obviously, our incident response team started looking into this appliance, and eventually they imaged this machine, and they sent it off for analysis to Flare, which is the reversing team that I'm a part of.

**16:17** · Our Flare team, myself and two other reverse engineers, we started taking apart the appliance, trying to figure out was this anomalous activity or not?

**16:26** · We ended up noticing that some of the code around network activity had domains that linked to avsvmcloud.com, which was a suspicious domain that we had noted from network log analysis.

**16:40** · We reached out to SolarWinds, and we asked them, "Hey, do you guys know what avsvmcloud is?

**16:45** · Is it part of your product or not?"

**16:46** · They were like, "No, it is not."

**16:49** · That started to really ring some alarm bells for us.

**16:52** · As we started reverse engineering this plugin, we realized that it had some encoded strings and some other quite suspicious-looking stuff.

**16:59** · It ended up being a back door.

**17:02** · We analyzed that DLL in a mad run over the course of 2 or 3 days, and we had a public blog out, notifying that this was a supply chain breach of SolarWinds just over 2 days later.

**17:17** · This is the blog post with details of the attack Stephen and his colleagues detected.

**17:22** · It doesn't mince words.

**17:24** · Anybody familiar with the reach and the client list of SolarWinds didn't have any illusions.

**17:28** · It was a globe spanning infiltration campaign.

**17:31** · An unknown threat actor used a supply chain attack to compromise some of the most important institutions in the United States.

**17:38** · Something had to be done.

**17:40** · So the engineers went to work.

**17:41** · Pretty quickly, they discovered a way to stop the attack, a technique that would throw the malware into an infinite loop, distracting it from keeping the back door to the victim's machines open.

**17:51** · That was the part that I found most interesting.

**17:54** · We realized pretty early in reversing the malware that there was a state transition table that was encoded as various subdomains of responses that we get back from the DNS call logs.

**18:05** · What we eventually realized was there was a block of IP ranges where if it got a DNS, a record resolution to one of these IPs within the block, the malware would actually write a little config flag that would turn itself off, or at least not a lot of upgrades to second stage HGPs, C2 for on-keyboard activity.

**18:25** · When we realized that, we were able to actually reach out to Microsoft who this IP block belonged to.

**18:32** · We were able to say, "Hey, we would really like to change the DNS registration for this resolve for one of your IPs.

**18:39** · Can we work together and sync all this?"

**18:43** · In a day, we had sinkhole the avsvmcloud domain with the help of GoDaddy and Microsoft.

**18:50** · We had inoculated all the victims around the world from further malicious activity before the blog was even public.

**18:59** · We also got lots of data about how many machines were actually infected, how large of a scale is this.

**19:05** · That was a pretty critical part in understanding the severity and impact and also mitigating it before other security teams around the world had even woken up and read the blog.

**19:16** · When the teams did wake up, the scale of the whole thing hit them like a truck.

**19:21** · FireEye called this attack SUNBURST.

**19:23** · Microsoft, one of the companies we for sure know has been compromised, gave it another name, Solorigate.

**19:29** · There was a lot of celestial body-themed terminology thrown around, but none of that's really important.

**19:35** · What is important is that hours after being discovered, the attack made the news.

**19:40** · In an instant, SolarWinds stopped being an obscure company that supplied niche software to IT personnel and became the company through which the entire US government got hacked.

**19:51** · It was not pretty.

**19:53** · The company got dragged through the mud, some of it deserved, some of it not so much.

**19:58** · For one thing, the company's cybersecurity left a lot to be desired.

**20:02** · Its software didn't follow a lot of best cybersecurity practices.

**20:05** · Its updates still distributed the malware days after it was discovered.

**20:10** · In probably the most comical turn of events in this entire story, the CEO blamed the entire attack on an intern who used a weak password.

**20:18** · I personally did not enjoy seeing the SolarWinds123 framing.

**20:24** · I thought it was immature.

**20:26** · Entertaining, for sure, makes for some good memes.

**20:30** · But that's not an effective way to build a security posture.

**20:34** · The reality is you had a private company that was attacked by a nation state.

**20:38** · There's no real expectation of security in those situations.

**20:44** · You have to assume that breaches will happen eventually and have a defense in-depth posture.

**20:51** · This is exactly what happened in this case.

**20:53** · When we were a security firm, we had our own internal telemetry and all other security protocols.

**20:59** · Eventually, there was a breach, and we detected it, we investigated it, and we found one of the world's largest supply chain attacks.

**21:06** · That's how it's supposed to work.

**21:07** · Framing an intern or blaming a password as SolarWinds123 is not effective in mitigating a nation-state attack.

**21:17** · To be fair, there isn't much evidence that the breach was made through a weak password.

**21:22** · Knowing what we know now about both SolarWinds and the other attacks perpetrated by the same hackers, the breach was probably more complicated and much more advanced.

**21:31** · An attack performed by a determined threat actor with tools and infrastructure that are out of reach for your ordinary hackers.

**21:38** · Now, who that attacker was is another question entirely.

**21:42** · There's just no way around it.

**21:44** · Every single agency and company that investigated this breach said that it had been conducted by the Russian intelligence services.

**21:51** · The FBI, NSA, CISA, and the United Kingdom's NCSC all put the blame on APT-29, a hacking group also known as Cozy Bear.

**22:02** · We can be pretty certain this group is a part of the SVR, the Russian Foreign Intelligence Service.

**22:07** · FireEye, Google, and SolarWinds itself, as well as a number of other security companies that were breached, agree with this conclusion.

**22:14** · They say that tools, techniques, and infrastructure used in this attack were the exact same ones Cozy Bear used in its previous campaigns.

**22:22** · I don't do attribution myself, personally, but we track lots of activity as uncs, unconfirmed groups over time.

**22:31** · Then based on multiple incidents over time, we can build a set of TTPs, tactics, techniques, and procedures, and we can start to map out infrastructure, domain overlaps, certificate reuse, all kinds of things.

**22:46** · We can get internal telemetry from various customers that we do instant response for, where we can see, "Okay, what malware was used?

**22:54** · Is this malware a variation of one that we've seen before?

**22:56** · If it is a variation, then okay, it's probably the same group.

**23:01** · This code is private."

**23:02** · There's a lot of disjoint small indicators that you build over time, and we get a pretty good visual of how they operate from working all these distinct IRs and collaborating with government agencies.

**23:16** · You can build a cohesive picture that gives you pretty strong confidence that, "Hey, this is the group you're dealing with."

**23:23** · Even Kaspersky, the famous and controversial Russian cybersecurity company, did call out its own government for this attack in a roundabout way.

**23:31** · It published a paper highlighting a curious piece of evidence.

**23:35** · Turns out, parts of the algorithm used in breaching SolarWinds came from Turla, one of the oldest and best-known tools of Russian intelligence services.

**23:44** · Turla dates back to the late 1990s, and we know for sure that it belonged to Russia, because back then, the Russian government actually admitted that it used it to hack American infrastructure.

**23:53** · It's a crazy story we might go into in another episode of No<i> Rollback.</i> But for now, one thing is clear.

**23:59** · The SolarWinds breach was one of the rare cases where almost everybody agreed on who did it.

**24:05** · One of the people who did not agree with that was the President of the United States, Donald Trump.

**24:10** · He downplayed the significance of the attack, contradicted the conclusions of his own administration, and hinted that SolarWinds might have been breached by China, not Russia, which might have looked baseless given the previously disclosed information.

**24:23** · Except that mere days later, Microsoft confirmed that at the same time SUNBURST was happening, SolarWinds was breached by a second threat actor.

**24:32** · This breach was dubbed Supernova.

**24:34** · It used a completely different method and didn't go as deep as the first one.

**24:38** · It was also attributed to Spiral, a Chinese state-sponsored threat actor, and helped it exfiltrate tons of credentials from SolarWinds' networks.

**24:47** · Yeah, when it rains, it pours.

**24:49** · To this day, the SolarWinds cyberattack remains one of the most thorough cases of a government being hacked.

**24:55** · All that remained for the victims was to learn from the consequences and try not to repeat the same mistakes again.

**25:02** · The biggest one for me was seeing that there was congressional hearings.

**25:05** · You had our CEO at the time, Kevin Mandia.

**25:09** · You had the Microsoft CEO and the SolarWinds CEO testifying in front of Congress on how did this happen and how can we prevent this.

**25:17** · That was quite unique.

**25:18** · We deal with a lot of high-profile cybersecurity incidents all the time, and I have never seen that before myself.

**25:25** · We really don't know how deep the attack went, and if things like the White House security cameras were infiltrated, although we do know that the White House network monitoring tools were compromised for sure.

**25:35** · Sure, in theory, the systems that handle the camera feeds should have been air-gapped, so not reachable from the Internet at large and thus completely safe.

**25:44** · But were they?

**25:45** · What else was not safe, and maybe has been exploited by hackers?

**25:50** · In any case, this was quite a wake-up call for the American government.

**25:54** · I think around a year later, we saw an executive order, 14028, go out about pardoning the government's cybersecurity defense and how we restructure some of these government agencies to handle better information, collaboration, and sharing, specifically between the public and private sector.

**26:11** · That was a big change.

**26:13** · You saw CISA gain a lot more central role in organizing and disseminating information.

**26:20** · Then we also right after had a whole bunch of companies saying, "Hey, can you please verify our software supply chain?"

**26:27** · That's obviously a big ask, right?

**26:28** · You need to continuously evaluate what are your software dependencies and have they been updated?

**26:36** · Are they secure?

**26:37** · It's a big ask to do something like that.

**26:40** · But you did start to see people considering, "Hey, what is my software supply chain?"

**26:45** · That in and of itself was a difference.

**26:51** · On top of it all, this attack gave us another glimpse into the perpetual cyberwar happening out there, beneath the surface of the Internet we browse every day.

**27:00** · Attacks like this happen a lot and get discovered with a frightening regularity.

**27:05** · Do you have a personal favorite?

**27:06** · Let us know in the comments.

**27:08** · We might look at it in the next episode of No<i> Rollback,</i> the series dedicated to revealing the events that changed the cyber world to the point of no return.

**27:17** · Thanks for watching, and bye.