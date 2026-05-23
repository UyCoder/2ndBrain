---
title: "China Nexus Barracuda Hack - Threat Talks Cybersecurity Podcast"
source: "https://www.youtube.com/watch?v=4X9AmBhOmSA"
author:
  - "[[Threat Talks]]"
published: 2024-08-13
created: 2026-05-05
description: "The name is Bond,.. James Bond. 🍸How do James Bond’s spy skills compare to modern cyber espionage? The Nexus Barracuda Hack was performed by highly skilled, Chinese cyber attackers, who exploited"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=4X9AmBhOmSA)

The name is Bond,.. James Bond. 🍸  
How do James Bond’s spy skills compare to modern cyber espionage?  
  
The Nexus Barracuda Hack was performed by highly skilled, Chinese cyber attackers, who exploited a zero-day vulnerability in Barracuda’s Email Security Gateway (ESG). 🚨  
  
Join Lieuwe Jan Koning, Rob Maas and Luca Cipriano to find out about the strategies the attackers used, how their tactics could’ve been countered, and whether or not stopping James Bond-level spies is an achievable goal for cybersecurity experts.  
  
🔔 Follow and Support our channel! 🔔  
\===  
► YOUTUBE: https://youtube.com/@ThreatTalks  
► SPOTIFY: https://open.spotify.com/show/1SXUyUEndOeKYREvlAeD7E  
► APPLE: https://podcasts.apple.com/us/podcast/threat-talks-your-gateway-to-cybersecurity-insights/id1725776520  
  
👕 Receive your Threat Talks T-shirt  
https://threat-talks.com/the-evolution-of-cyber-warfare/  
  
🗺️ Explore the Hack's Route in Detail 🗺️  
https://on2it.s3.amazonaws.com/20240719\_Threat-Talks\_Infographic-Cyberwarfare.pdf  
  
🕵️ Threat Talks is a collaboration between @ON2IT and @AMS-IX  
  
#cybersecurity #threatintelligence #CyberEspionage #ON2IT #ThreatTalks

## Transcript

### Introduction to threat talks

**0:00** · Welcome to a James Bond movie.

**0:02** · Except this James Bond is not actually flying into your country to spy on you.

**0:07** · And this time, James Bond speaks Chinese, but he is still very clever and very effective as we will learn.

**0:14** · Thank you for joining, this is Threat Talks from the Security Operations Center floor at ON2IT and my name is Lieuwe Jan Koning and the subject of today is the China Nexus Barracuda Hack.

**0:24** · Let's get on to it. Welcome to Threat Talks.

**0:27** · Let's delve deep into the dynamic world of cybersecurity.

**0:31** · Let me briefly introduce my two guests of today.

**0:33** · On my left side is Luca Cipriano, he is a Threat Intel Specialist, and he's going to tell us everything about this Bond guy.

**0:40** · And on my right side, it's Rob Maas.

**0:42** · He's Field CTO of ON2IT and his job is to make sure that James Bond doesn't have a chance.

**0:48** · Rob. I'm not going to be doing a good job here.

**0:51** · 26 movies and he wins every time? He's going to lose everything.

**0:54** · Even when he dies he comes back.

**0:55** · Yeah he always comes back, so.

**0:56** · We still have work to do. Well. Let's see.

**0:59** · And before I forget, there will be an infographic, as you're used to, and you might need it today, because we're going to talk about advanced persistent threats.

**1:07** · And they are advanced.

**1:08** · They are persistent and are clearly a threat.

**1:11** · So it can be complicated at times, but we'll do our best to explain them as easy as much to consume for you as possible.

**1:19** · Luca, it's the China Nexus Barracuda attack.

**1:22** · Tell me it's China.

**1:25** · Well, yes.

### Analyzing the China nexus

**1:27** · I mean, China Nexus.

**1:29** · So what's the China Nexus?

**1:30** · With China Nexus, we do not refer to a specific APT but the Nexus is more of a group of state sponsored actors, so it can be like hacker groups, but also like security contractors, as we know, that operate... You seem quite confident that it is China, because typically it's really hard to figure out who is behind something.

**1:57** · Why are you confident?

**1:58** · Well, there are some hints here, or some studies that have been done, so thanks to CTI, we can give an answer to this.

**2:08** · So, first of all, is that, there were no .. so Mandiant observed that between January 20 to January 22, there were close to no actions and these dates correspond with .. Chinese New Year.. the Chinese New Year.

**2:25** · Exactly. So, as you know they work for the government, probably they were on a holiday or whatever.

**2:30** · But also, this specific attacker has been named as UNC4841.

**2:39** · UNC stands for unknown, because well, they didn't attribute a specific group, but they know that they used infrastructures that have been already used by other Chinese attackers since 2019 already.

**2:55** · And aside from that, also analyzing the backdoors on malware, they found some similarities with codes of malware utilized by attackers from China.

**3:07** · So some .. So you might say that the weapons they use seem to be produced in China.

**3:12** · And they... Already attributed to Chinese, so all these together, led \[us\] to confidently say that, and aside from that, also the target.

**3:23** · So the target was espionage. We're talking about email.

**3:25** · And they were targeting Western, governments and agencies.

**3:31** · So, also given the targets.. So and the Barracuda, Rob, what is Barracuda?

**3:36** · What was the attack-ee here?

**3:38** · In this case, it was on the barbecue... Barracuda.

### Barracuda attack mechanics

**3:43** · That's very American.

**3:44** · It was on a Barracuda email security gateway, which is there to filter out spam and email containing, for example, viruses.

**3:54** · So it's there to protect you against these spam emails. And the attacks we've seen indeed that were Western companies, Western governments, and they got in there and that's ...

**4:06** · Yeah, correct.

**4:08** · So how did they do this, Luca?

**4:11** · So first of all, I would like to say that this is a really sophisticated attack, the attackers, they had good knowledge about the product but also, if you look at the time they have been dwelling there, it's quite long. So just to give like an idea, on the 18th of May, Barracuda realized that there was some anomalous traffic, and the 23rd of May, they published the zero day for the first time, but when they then did the investigation and the forensic investigation, they found out the initial foothold, was already in 2022 October.

**4:49** · So they were already in the system for a long time.

**4:52** · And this outlines how dangerous APTs are.

**4:56** · They have a long dwelling time and they try to be as stealthy as possible.

**5:02** · This specific attack targets a zero day in the Barracuda ESG appliance, which is a common injection vulnerability.

**5:10** · So how does this work?

**5:12** · Barracuda uses an antivirus, open source, that's called Amavis to scan the attachments in the email.

**5:20** · This antivirus uses Perl. And the vulnerability is, in fact, that Perl has a function called, ... sorry, there's a function in PERL called qx{}, which when it scans the attachment, which are .tar or .zip, so archive attachment, it will return in a variable, the $f, also the file name of the file names that are contained in the archive.

**5:47** · And there was a lack of checks on what was passed, then the file name is passed as a command with escape possibilities.

**5:57** · So they could use, it could trigger a common injection.

**6:02** · So for clarity, this was a vulnerability in the Barracuda device.

**6:06** · So, again, a security device that's supposed to protect us, that contains a vulnerability that they somehow found a way to exploit. Yes.

**6:12** · And the funny thing about that is that, the attacker, in this case, they had to make the email as suspicious as possible, because they wanted Barracuda to check it.

**6:22** · So the emails are poorly crafted with maybe some mistakes or obviously, scammy or spammy.

**6:29** · So in this way the Barracuda will send it to the antivirus and they will check the contents. Hey Rob, you're always telling your customers and us to, hey, make sure you filter the obvious bad stuff.

**6:41** · It looks like you shouldn't do that all the time.

**6:44** · Luckily, I also always tell never rely on just one layer of defense.

**6:49** · So you should have multiple layers of defense.

**6:51** · And in this case, this layer, so the spam filtering and the antivirus is failing, because there's a vulnerability at that time a zero day vulnerability, within the appliance.

**7:00** · So it's really hard to defend on the device itself, but you can put some measures in place around it, which we will discuss in a bit, to hopefully prevent or at least make it more difficult for the attackers to get into your network.

**7:14** · Fascinating this.

### Persistence and evasion

**7:17** · So they send us this, on purpose spam thing.

**7:20** · We've been talking about AI trying to make spam more sophisticated..

**7:24** · And how to bypass it.

**7:25** · Actually, this is the other way around. This is not needed.

**7:27** · Can AI help here? Yeah. Make it really bad. Yeah.

**7:32** · Well, so at this point, we have this scam email that passes by, the content of the archive, the .tar, or the .zip, it is not important, the important \[part\] is the file name of one of the files that is in the archive.

**7:46** · So now we know that we have these escape possibilities, because of the lack of input validation.

**7:53** · And what happened is that, the file name of the file containing the archive contains a base64 encoded payload command, that what it does, it uses open SSL to start the client and initiate a connection to the C2 server from the attacker.

**8:13** · So that's.. So, from the Barracuda appliance to some random IP somewhere in probably China or China's control machine. Well, yeah. Chinese control machine. Yes.

**8:25** · Rob. Yeah. Here we can already do two things.

**8:27** · First it starts, that there is an email with an archive.

**8:31** · So maybe the question is, should you allow archives in email, or should you allow files in email at all?

**8:37** · I think it's bad practice, but still, a lot of companies will do it.

**8:40** · And the reason for that is because if the email is delivered, it's already on your endpoint.

**8:44** · And from there, an attacker has a lot of access.

**8:47** · No attachments will be difficult. For a lot of companies it will be difficult. ... different attachments, maybe?

**8:53** · Yeah, .zip files, .tar files, I would always try to block them. We used to block executables, so why not some other files that try to hide what they have inside them, Yeah, but a calendar inite, for example, is really hard... Calendar invites would be an exception indeed.

**9:11** · Or the logo. I mean, if I go to our marketing department and tell them, hey, I'm not going to put in a picture..

**9:17** · A picture in the footer, yeah, I have my own opinions about that.

**9:20** · You can just ask .. Yeah, that would be a good way.

**9:26** · No, but blocking attachments, especially in this case, archives, would have helped. You can do that already on the firewall, the layer before the Barracuda, if that's needed.

**9:38** · The second thing you can do here is limit the connection from the Barracuda.

**9:43** · Why should it go outside to all addresses?

**9:46** · And what kind of ... Because it needs to send email?

**9:48** · Yeah, but then you make a policy that is only allowed to send email.

**9:51** · So making sure that is on that service port, 25, 587, also I can debate if Barracuda should send email, because it is a spam filter for incoming email.

**10:01** · Yeah, I guess maybe it's a bit difficult for companies also, when you need to get, for example, updates or maybe, yeah.

**10:10** · You don't know what is the legitimate traffic?

**10:12** · It's hard to be granular at that level.

**10:15** · So, it can be done, but no.. It can be done, you should monitor if... So.

**10:20** · The best way, the vendors tells you, hey, this is what connections you need to open up in your firewall.

**10:27** · You see, it more and more. Yeah. So it isn't ... If that was available...

**10:31** · So that was really difficult to address. If that isn't available then the best way is to just monitor the traffic for a couple of days.

**10:37** · And of course, hope you don't get abused in that period and then create rules.

**10:41** · Our internal IT department is doing exactly this all the time.

**10:44** · I mean, there's a new, we have some kind of chat server that needs to send out push notification, for example.

**10:50** · And then we debate where exactly does it need to go, how safe is this, should we add a proxy in there?

**10:54** · That's how it should be. And it's not rocket science, it will take time, that's maybe the biggest challenge here, but it is not that difficult, I think.

**11:02** · Okay. Yeah. Well, too bad for you, we're done. Oh, well.

### Post-exploitation activities

**11:07** · Well, so at this point, what happened is that attacker starts with Wget to download the backdoors and payloads, additional backdoors and payloads.

**11:19** · So in this case, they did a lot. Really a lot.

**11:22** · They also Trojanized legitimate modules, just adding snippets of codes.

**11:28** · So they really did a lot of things. I kind of .. Again, on the Barracuda box. Still trying to get in the heart of the network on the Barracuda.

**11:37** · Yes, in the Barracuda and actually, the...

**11:42** · That's good that you mentioned it, because they did not went into the network after, like in some cases they did, but this was espionage.

**11:49** · They were interested in the email. They wanted to read. They wanted information.

**11:53** · So they did not need to go deep in the network to do things.

**11:56** · But they just wanted to have mostly a backdoor to monitor the communications. So there was no need for, maybe it in some cases.. Maybe good to mention here that email is used for everything, so also for a lot of sensitive communication. Yeah. Yeah, yeah.

**12:11** · And of course moving then deeper in the network makes you more noisy.

**12:15** · And it's better to just limit there. So less chances to get caught.

**12:19** · But anyway, so what are we doing now? What are we doing?

**12:22** · What are they doing now?

**12:22** · They're downloading extra payloads. And as I mentioned, it did a lot.

**12:26** · They did a lot, but I kind of narrow it down to the three main backdoors that they got. They were named SEASPY, SALTWATER and SANDBAR.

**12:39** · So the SEASPY is a really important one, because what it does, it establishes a pick up filter on a port TCP 25 and TCP 587.

**12:48** · So it starts to.. Ports that have to do with sending email over the SMTP protocol. Yes.

**12:52** · And it was installed under the name Barracuda mail service.

**12:56** · So also trying to make it blend. The SALTWATER is a module for the... Wait one moment. So what happens there?

**13:06** · There is a ... they capture all the traffic, and therefore that is probably in an early stage on the network interface.

**13:13** · Yeah. They capture all the traffic that goes in the port.

**13:16** · And now the extra backdoors, they do other things, which the SALTWATER, for example, it goes on the SMTP daemon and it allows functionalities of download, upload file, execute commands and all this kind of thing.

**13:31** · So that's how they can pass them the pick up and everything.

**13:36** · So they can send a command via email to them and then it will also ...

**13:39** · Also retrieve files and download ... And send an email to the box and with a command they say, hey, get me this file and it will deliver the file through that C2 channel.

**13:48** · Yes. And, the next one, the really important one is SANDBAR. And the SANDBAR is a rootkit.

**13:56** · So the rootkits, rootkits are extremely bad.

**14:00** · They're the most dangerous, because they are really at the kernel level.

**14:04** · So they're at the lowest level, and they can do basically everything on the machine. When there's a rootkit, it can, the rootkit usually survives also reboots. It's there.

**14:17** · But the most important thing is that it can hide processes.

**14:21** · Because a rootkit puts itself on top of the kernels, on top of the operating system, so first you boot the rootkit and then the bootkit, like a VM runs the actual OS, right? There are different, there's like bootkit or.. Yeah, but anyway, they're different.

**14:34** · But yes, indeed it goes on the kernel level so it can hide all of the... Control everything.

**14:39** · So, do you know Matrix, the Matrix, the movie?

**14:44** · It's a documentary.

**14:45** · Yes. When Neo passes by, and there's the cat, and then he says, oh, déja vu again, the cat.

**14:50** · That's basically the rootkit. It changes something in the matrix, but you don't know anymore what is changed.

**14:55** · You can't rely on your tools anymore.

**14:57** · So if you do 'ps' to list the processes that are running.. You just.. Off.

**15:01** · Yeah, it's not reliable, because now that one is your new normal.

**15:05** · So, maybe a little bit of sidestep, but if you do threat hunting, how do you...

**15:11** · That's the ... It's really difficult. It's extremely difficult.

**15:15** · You need to do like a really in-depth forensic analysis to understand and the more sophisticated, the more difficult it is to check it. And here we reach the point where, Barracuda said due to all these problems, it's too complex.

### The RMA and hidden backdoors

**15:30** · So we need to issue an RMA, because you can't remediate it, it is too much in depth into your device.

**15:36** · It's too sophisticated, so they said, okay, RMA is like, change your device.

**15:40** · We're going to.. Yeah, return material.

**15:41** · Yeah. Yes. And, you do this when your hard drive is broken for example, ship it back and you'll get a new one. Yeah.

**15:46** · So what happened is... So, Rob, you get the new device, what's the first thing you're going to do when you get the new device?

**15:52** · I put back my backup so I can quickly be back up and running.

**15:57** · Don't you think that they know that?

**16:00** · So that's funny, because, this is what happened... You find that funny?

**16:04** · But you got the new device, and then, of course, Rob puts in the backup and at a certain point, exploit starts again.

**16:11** · So what happened?

**16:13** · A new zero day? Is something, well, what's happening?

**16:15** · Well, they missed a passive backdoor a passive backdoor which was implanted in the MySQL database.

**16:23** · And this vector was designed to trigger for when a device is reissued or just somebody is putting it back up.

**16:32** · Right. You got a brand new device. Nothing on it.

**16:34** · Factory default. So you're putting your backup and your backup is...

**16:38** · So my settings export off the Barracuda. Yes.

**16:40** · And then, as I mentioned, the first signs of attack were October 22nd.

**16:46** · So, 2022.

**16:47** · So they were already there for a long time, they planted it way before.

**16:51** · So how do you know what is your clean backup at this point?

**16:56** · How do you know they were not already there?

**16:57** · Because of course, you start to realize it when they get noisy, but probably they have been stealthy for a long time.

**17:03** · And they implanted this, they thought about this, and it was there.

**17:07** · Yeah. So from the attacker's perspective, first thing you do is make sure you have persistence.

**17:11** · You don't do anything bad yet.

**17:12** · Try to be as much off the radar as possible.

**17:14** · Only activate the spying once you know for sure that when they return... In this case, they really did it, really good, yeah.

### Defense strategies

**17:23** · James Bond can learn two or three things, right?

**17:26** · So this backdoor is... It's like a sleeper cell.

**17:30** · Yeah, yeah, exactly.

**17:31** · So this vector is called the depth chart or a submarine.

**17:35** · and, what it does, it's in the configuration, in one of the configuration file, and it has a trigger when one of the line from the configuration gets deleted, which this happens, of course, when you install, when you put your backup in, because of course, your configuration changes.

**17:51** · And what it does, as soon as it triggers, it writes to disk a base64 encoded script that contains a shell script and an installer.

**18:02** · But since you can't really run commands from database, what they did, they named it with the same name of an argument that is legitimately called by the Barracuda with a function.

**18:14** · So when that function starts to do legitimate things, it calls that argument.

**18:18** · And that argument is the file that... Yeah, so side effect of something else then triggers execution of this just installed malware.

**18:25** · Yeah. Indeed.

**18:27** · Well Rob, tell me, what are we going to do against? Update your device.

**18:32** · Yeah. Well. Eventually... made it.

**18:35** · So. Yeah.

**18:36** · No, so there's not much we can do on the device itself.

**18:39** · Like stated before, because you cannot install an EDR solution that can then detect abnormal behavior or function for example.

**18:47** · But what we can do is still making sure that connections are limited, that will help in all stages, because in the end, payloads need to be downloaded.

**18:56** · Data that is being gathered needs to be sent out, so there's always some kind of communication channel.

**19:02** · That's what we can try to block with firewalls.

**19:05** · In this case, also, the Barracuda has solved problems, they have fixed the vulnerabilities, so updating is a good solution now, but, yeah, of course, you first have to know what the vulnerabilities are before you can start working on a patch.

**19:21** · And then of course, release it. And..

**19:23** · That's all depending on what what Barracuda does.

**19:26** · I mean, suppose I am a CISO and I want to, I realize that there's APTs out there, I cannot wait for the patch to be there, because they have already been in my environment for a long time.

**19:38** · Is there anything, any strategy that I can apply, to ...?

**19:41** · to be sure? So we come back to the Zero Trust strategy, so make sure you have small segments.

**19:46** · The Barracuda in itself doesn't need to talk to your whole network hopefully, only to clients that need to receive the email.

**19:54** · So you can make already strict policies around it and also vice versa.

**19:58** · So clients that connect to your Barracuda, also very limited on application protocol.

**20:04** · Outgoing connections we already discussed: make them very specific, but also, when this whole Threat Intel process was going on, we got a lot of information about IOCs and we can also block the known bad IPs, for example, as a simple step which you can implement in your firewalls.

**20:20** · Yeah.

**20:20** · So figuring out, doing all this Threat Intel, learns us a lot about the steps that attackers do and therefore we can come up with strategies.. Better strategies, better prevention.

**20:29** · And Zero Trust is such a thing that is really, really effective.

**20:32** · And makes it also very digestible, so, you know where to focus on.

**20:36** · All right, gentlemen, this was an awesome story.

### Conclusion and resources

**20:40** · \[I'm\] maybe a little bit more afraid, maybe.

**20:43** · And I'll, look at James Bond a little bit differently next time.

**20:46** · I think we have won for now, but there will definitely be a new James Bond stepping up. As far as we know, we have won.

**20:52** · Probably next week.

**20:54** · So, if you want to read more about this, we have, like I said before, we have some infographics prepared for you that lay out, all the things we talked about in more detail, even more detail than we had time to discuss about today.

**21:06** · And well, thank you, thank you to Rob, to Luca, for explaining this to us.

**21:10** · And thank you, listeners, for tuning in.

**21:12** · We'd love to hear your feedback.

**21:14** · Email us at the team@threat-talks.com and we'll reward you with a t shirt if you have good feedback for us, that we can make this this Threat Talks better with, And if you want to see more, learn more, please like us because it helps us spread the word.

**21:30** · Subscribe to this channel.

**21:31** · So you are sure that next time you'll hear about Ethan Hunt, for example.

**21:36** · Thank you very much. See you next time.

**21:39** · Thank you for listening to Threat Talks, a podcast by ON2IT cybersecurity and AMS-IX.

**21:44** · Did you like what you heard?

**21:45** · Do you want to learn more? Follow Threat Talks to stay up to date on the topic of cybersecurity.