---
title: "China Just Automated Cyberattacks With AI"
source: "https://www.youtube.com/watch?v=siZaZf3lK_8"
author:
  - "[[Marcus Hutchins]]"
published: 2025-11-17
created: 2026-05-05
description: "Anthropic has just detected the first recorded fully AI automated cyberattack. Chinese state-sponsored hackers used it to automate intrusions into company ne..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=siZaZf3lK_8)

## Transcript

### Introduction

**0:00** · Hey everyone. So, I've been wanting to talk about this for a few days now. It's Anthropic's new report about Chinese nation state hackers using their large language model to fully automate cyber attacks. Now, people have been running pretty wild with these claims. So, I wanted to talk about different aspects of it. Now, let's start with the report itself. This report sort of frames itself as a cyber threat intelligence report.

### What The Report Claims

**0:23** · Um, typically from a report like this, you would expect information that would allow you to recreate or at least find similar activity, whereas they've left no indicators of compromise, no detailing of the tooling used, no prompts. The report is basically completely devoid of anything that would lead me to consider it a threat intelligence report. Now, with that said, it does offer some insights. They basically talk about the fact that the attackers had automated cyber attacks uh basically from end to end.

**0:51** · Everything from the reconnaissance phase to the uh triaging vulnerabilities for the writing exploits and in the lateral movement and uh data exfiltration. Now anthropic did specifically say that there was a human in the loop. Basically certain steps required human intervention so that a human could actually review the output which makes sense because large language models do have a tendency to hallucinate a lot. So you want to make sure it's actually operating on real information and not something that it made up. But for most intents and purposes, this attack was fully automated end to end.

### Debunking Hype & Misinformation

**1:26** · Now, where people have gone a little bit crazy with this is the idea that oh my god, AIS are hacking people. They're developing cyber attacks that now bypass all the existing defenses. They can outsmart the defenders. They can outsmart the defenders security tools.

**1:41** · And this implies none of that. In fact, Anthropic specifically states that the attackers were not using the AI for novel capabilities. That is like building new cyber attacks that haven't been seen before, which is a capability they just don't have. Um, they were essentially just automating existing attacks.

**2:00** · Now, just the way that large language models work kind of rules out the possibility of them doing novel cyber attacks because large language models don't really exhibit novel capabilities. they sort of just learn from what's on the internet and then they can recreate it. So if an attack was not already publicly well doumented, the large language model is going to struggle with it or not even know of its existence at all.

**2:22** · Now, Anthropic actually specifically said that they were using a lot of open- source tooling which most of the readers decided to just ignore and sort of run with this idea of, oh my god, the AI is like making up new malware and new exploits and it's all of security is dead. What do we do? Um whereas what Anthropic said is that they were taking open source tools such as like open source vulnerability scanners, open source uh vulnerability proof of concepts, um open-source malware, and they were basically making uh MCP agents that run using Claude.

**2:55** · Now, if you're not familiar with MCP, it stands for model context protocol. And basically, the simplest explanation of it I can give is it allows agents to talk with the large language model. So imagine you build a Python script or some other script. It can basically call out to the large language model and ask it a question uh ask it for some kind of information. The large language model can then respond back and the agent can then do a task based on that response.

### How They Automated Cyberattacks

**3:24** · And basically this kind of mitigates the problem with large language models in that they can't actually do anything on their own. So Claude itself can't hack any systems. It doesn't even have the capability to make outbound internet connections. All it can do is search the web. So in order to actually do the hacking, you would need to write an agent uh that is able to perform some kind of external task. So it sounds like what the attackers actually did was they broke the attack down into stages.

**3:53** · So they had an agent which performs reconnaissance and it sort of interacts with Claude to sort of uh digest that information or maybe pick targets out of that information and then it passes on to the next step which does a vulnerability scan and that would be a vulnerability scanning agent which sort of talks with Claude and it sort of works through what it found and then the next step would actually build exploits for the vulnerability.

**4:18** · Now, while Anthropic implied they were explicitly using public tooling, public tooling doesn't necessarily get you the whole way there because if I go and get an exploit proof of concept from GitHub or exploit DB, there are going to be subtle differences in every network that might cause it to fail. So, we need some way to sort of catalog the differences and then customize our exploit payload uh to that specific network. And that is uh typically a human task.

**4:44** · Uh and a human operator would be responsible for sort of triaging the information that came from that network and then customizing their exploit payload and customizing uh their malware to that specific target.

**4:58** · And it seems like what they've done is they've actually automated this with Claude. Now the biggest question I personally had is what specifically are they automating that couldn't be automated with scripts? A lot of scanners can be automated with scripts.

### Why Did They Need AI?

**5:12** · A lot of exploit generators can be automated with scripts. A lot of malware generators can be automated with scripts. What was it specifically that Claude offered that they could not do with an automated script? And of course, Anthropic just didn't answer this. They glossed over that entire part of the equation, which kind of really annoyed me cuz that is really the only thing I wanted to know from that report because we see this with ransomware actors every day.

**5:38** · Most networks are similar enough that their operators literally just run through scripts that say try this, try this, try this, do this, do that, do this. If this doesn't work, do this. And there isn't really any need for human intelligence. Why couldn't they just fully script the attacks with a Python script? Like what did they need AI for?

### Why Did They Use US LLMs?

**5:58** · Now, my second biggest question was why did they use Claude? Because the agent itself is not doing any of the hacking.

**6:05** · It's just coordinating their tools which are hosted on their systems. So there's no sort of like illusion where it looks like Claude is accessing their systems rather than some random server controlled by a Chinese nation state actor. So why specifically did they choose to use a US-run large language model which is being audited by the company for this exact kind of activity rather than using one of their own models? Like China has large language models, they have Deep Seek.

**6:35** · They most likely have internal ones. Why didn't they use their own model? Why did they take the risk getting caught using a US model? And I say risk getting caught.

**6:47** · They did get caught. So, why did they go and get caught using a US model when they have their own? Now, I'm purely just speculating here, but this could be anything from maybe their models lack certain capabilities that they needed for this specific cyber attack, or maybe they just don't have permission to uh abuse local models. Um, because a lot of Chinese cyber attacks are actually sort of uh farmed out to private companies.

**7:12** · Where the US has private defense contractors that might make weapons on behalf of the US government, China has private cyber contractors who perform cyber attacks on behalf of the Chinese government. So since uh Deepseek is a private company, and this could be another private company who's been contracted to do cyber attacks, they may not have permission to abuse Deep Seek's infrastructure.

**7:34** · Now, these are questions that could have been quite easily answered if Anthropic had given us any information at all because the chances are some other cyber threat intelligence company is tracking that thread actor and they could answer those questions.

**7:47** · They could say who are they? Uh which company do they work for or do they actually work for the Chinese state? But unfortunately, Anthropic's threat intelligence report was devoid of any threat intelligence. So, we just can't do that. Which brings me on to my next segment. What actually are the implications of this? Because if you've been on social media for the past couple of days, you've seen people absolutely running with this claim. Cyber security is over. That all of the hacks are automated now. What are we going to do?

### The Implications For Defenders

**8:15** · All of the technologies are now obsolete. And of course, it's all nonsense, right? They've simply just automated attacks with existing tooling, which means the defenses are the same defenses that we always had for that tooling. The issue is actually that most companies do not have even the most basic defenses which is why this works.

**8:36** · It doesn't matter if a human is running the tools or a claude is running the tools or a bash script is running the tools. The issue is most organizations do not implement appropriate defenses against these tools. So all of the answers are the same answers that we've had for the past 10, 20, 50 years. Patch your systems, segment your networks.

**8:57** · Don't use admin credentials on random endpoints. It's like all of the basics that no one ever actually took the time to implement. Now, most likely the reason the thread actors chose to try and automate their systems with AI is so that they could do more attacks at once.

**9:12** · They could have higher bandwidth, higher capacity. And for the average organization, this doesn't really matter because thread actors are either trying to hack your organization or not trying to hack your organization. how many organizations they're trying to hack at the same time is completely irrelevant.

**9:30** · Your job is to still just secure your network against thread actors and the AI automation is entirely irrelevant to you. Although there is one caveat I might add, which is if the automation is leading to a quicker attack process, they're going quicker from initial entry to full network compromise. then that could change some decision- making on the organization's end because a lot of organizations still when they receive an alert from their EDR or their NDR or their sock, they then go and investigate it.

**10:00** · They'll go and check is this a false positive or is this a real thing that I need to be worried about? But if an automated agent is just say blasting through your network in like less than an hour, maybe less than 30 minutes, maybe even a couple of minutes, then you don't really have time to make those decisions. You would be better off just quarantining a system the second that an alert is raised and then doing the opposite. Instead of asking is this malicious activity that we need to care about, you should be asking is this a legitimate activity that we need to allow?

**10:30** · Because a lot of sock response times are actually too slow for even nonAI automated attacks. I've tracked ransomware attacks for a long time and we've seen ransomware actors blast through a company's entire network from initial access to full networkwide ransomware in less than 30 minutes. So assuming your sock gets an alert anywhere during that process, they have 30 minutes or less to respond.

**10:53** · And if that system goes unquarantined and that attack continues, by the time the sock even gets to investigating the initial intrusion, the network is toast. Whereas if that system were to trigger alert automatically get quarantined that would give the sock time to actually investigate the activity. Now this is making a lot of assumptions that this AI attack is actually faster than say a scripted ransomware attack. But I think it is important to have a think about that.

**11:22** · Think about how long does it take your sock to respond to an alert and is that going to stand up to an automated cyber attack? Because in a lot of cases the answer is going to be no. Which brings me on to my next point, which is if you're a managed sock, a sock that offers sock services to a multitude of

**11:42** · organizations, assuming that this AI use is allowing the attackers to attack more organizations at once, you could presumably see your volume of alerts increase, the volume of cyber attacks you have to handle at once increase, and you are again going to have to make those decisions of are we responding too slow? Because if you're one sock protecting one organization, it's entirely possible you could get your response time down to like a couple of minutes.

**12:08** · Whereas if you're a massive sock protecting thousands of organizations and your alert volume doubles or triples or quadruples, then you're going to really struggle to get to all of those alerts in a meaningful amount of time. Now, just based on what I've seen on the cyber thread intelligence side with pre-AII ransomware actors, I really think most socks are actually going about it wrong.

**12:32** · You won't believe the amount of times that I have witnessed a ransomware actor attacking a company's network. I've reached out and I've warned whoever I could get a hold of, usually the CISO or their head of sock, and I've been like, "Look, you have a ransomware actor in your network right now. They're pivoting through your network. You need to lock it down." and they've gone and they've quarantined the affected system and they've looked at their sock alerts and they've been like, "Oh, thank you, but we actually already knew about this attack. See, we had this alert in our sock system."

**13:01** · And I'm like, firstly, a thank you would be nice, but also there was no way you were going to get to that alert before they had your entire network ransomed. And a lot of organizations are just under this delusion that just because they detected some activity and they got that alert in their sock dashboard that means they're fine. That means that that system is going to get quarantined fast enough before the attacker jumps to another system or does a full networkwide compromise. And in most cases that is just not the case.

**13:32** · We know it's not the case because we see how much money ransomware actors are making. I believe in one year lockbit made a billion dollars in ransoms. So if those sock alerts were working, they would not be ransoming so many organizations that they're making a literal billion dollar a year. Anyway, that's a rant for another day.

**13:53** · I hope this video has been super informative and if it has been a like and subscribe super helps out my channel and I will hopefully have another video out shortly because I do actually have a backlog of things I want to talk about for probably the first time in the history of my YouTube channel. So, I'll see you all soon and enjoy the holidays.