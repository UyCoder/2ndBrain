---
title: "How the NSA Hacked Huawei: Operation Shotgiant"
source: "https://www.youtube.com/watch?v=aQNgelm7JeE"
author:
  - "[[Cybernews]]"
published: 2025-07-17
created: 2026-05-05
description: "How do you hack the largest tech corporation in China? Well, if you are the National Security Agency of the United States, you just… send a phishing email. A..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=aQNgelm7JeE)

## Transcript

### Intro

**0:00** · 2010, somewhere in Iran, a computer of a prominent Iranian politician.

**0:06** · He's having a regular workday, emails, scheduling, the usual stuff.

**0:10** · But there's one thing the owner of this device didn't notice.

**0:14** · His computer has been thoroughly hacked.

**0:17** · All of his traffic is about to get monitored.

**0:19** · Here's how.

**0:21** · The Internet traffic from this computer is going through a brand new router.

**0:24** · The office just received a bunch of these, and the IT department set them up yesterday.

**0:29** · The routers are made by Huawei.

**0:31** · The sourcing was crucial.

**0:32** · Huawei is a Chinese company.

**0:34** · This should be safer for the regime, which isn't exactly friendly with the West.

**0:38** · CIA and the likes can't force it to give up the data of its customers, or at least that's how the logic goes.

**0:44** · The routers came straight from the factory, and in the mind of Iranians, this is as tamperproof as you can get.

**0:51** · But it's not true.

**0:52** · In the programs that were just installed, deep in the code, there is a bug.

**0:57** · A small vulnerability, a mistake which is extremely easy to miss if you don't know precisely what to look for.

**1:04** · Normally, if you want to connect to one of these routers, you would have to know the password.

**1:09** · But thanks to this mistake in the code, the password has a bypass.

**1:13** · All you have to know is a simple command, a master password, so to speak.

**1:18** · The router's software is hard-coded with it.

**1:20** · Anyone who knows this command can just skip regular authentication and immediately gain administrator privileges.

**1:27** · That's exactly what someone just did.

**1:29** · Straight in front of the politician's eyes, an unknown hacker triggered the vulnerability and granted himself access to the router.

**1:36** · The hacker escalated his privileges to administrator and began installing sophisticated monitoring software on the router.

**1:43** · From now on, all the traffic that goes through the device will get intercepted.

**1:48** · Every email sent, every website visited, all of that gets carefully documented and reported to a command and control server.

**1:55** · The brand new router is now the perfect surveillance tool, and this Iranian politician is not the only victim.

**2:02** · Thousands of people across the world, everyone who uses this Huawei equipment is susceptible to the same bug, the same vulnerability, and a lot of them get the same treatment of privilege escalation and monitoring software.

**2:15** · You might think that Huawei is responsible for that.

**2:18** · After all, the company shipped the equipment.

**2:20** · It had to have full knowledge of what was happening.

**2:23** · And this might be true.

**2:24** · You've probably heard that a lot of governments reported being spied on by China through Huawei equipment.

**2:30** · But in this particular case, somebody else was involved.

**2:34** · Huawei itself, the most powerful Chinese tech company at the time, was hacked.

**2:39** · It was penetrated by an attacker with the precise purpose of getting access to computers like this, and thousands of other ones.

**2:46** · This event later became known as Operation ShotGiant, and it was one of the most ambitious espionage efforts of the National Security Agency of the United States.

**2:56** · One of the most elaborate hacking operations of our time, and one which changed the world to the point that there was, No Rollback.

### Chapter 1: Baseline

**3:07** · This is China in the 1970s, and this is China in the mid-2010s.

**3:13** · Yeah, the whole country basically exploded with money.

**3:16** · A couple of decades, and a backwater turned into a superpower.

**3:20** · People call this the Chinese economic miracle.

**3:23** · To this day, economists argue over what it really was and how it worked, but the broad strokes are mostly undisputed.

**3:30** · A series of deep reforms in the 1970s injected a massive dose of free market into what was a planned economy, allowing the state to reap the benefits of carefully reined-in capitalism.

**3:42** · You've seen the manifestation of this miracle in its purest form.

**3:45** · I mean, this.

**3:47** · For a couple of decades, made in China was on everything because, well, everything was manufactured in China.

**3:54** · The country became the world's assembly line, courtesy of its most abundant resource, cheap labor.

**3:59** · But pumping out millions of metric tons of kipple wasn't China's final goal.

**4:04** · More of a stepping stone, really.

**4:05** · Right from the start, it was trying to branch into the natural evolution of regular industry, high-tech manufacturing.

**4:12** · Huawei is the prime example of that.

**4:14** · It was founded in the early 1980s as a reseller of phone switchboards.

**4:19** · These things.

**4:20** · The company did well, got a few government grants, and began churning out its own products.

**4:25** · As the story goes, in 1997, its founder went to the United States for the first time.

**4:31** · He visited Bell Labs and was gobsmacked by the efficiency and the order of this world-class company.

**4:37** · He decided to copy the structure and the management style of Western tech giants for his startup.

**4:42** · Foreign advisors were invited.

**4:44** · Local views on how a business should be run were rejected, and every spare penny was invested in the research and development.

**4:50** · How much of that is true, and whether Huawei just implemented the best practices of Western corporate propaganda is a question we won't be able to answer.

**4:58** · But the company really did see success, moderate at first and a meteoric one in the 2000s.

**5:04** · Its rise was massively tight to China's export push.

**5:08** · The internal market for communication equipment in the country was still tiny, and selling abroad was the only way to grow.

**5:14** · And so Huawei grew.

**5:16** · By 2005, more than half of its sales were outside of China.

**5:20** · At the time, it was mostly selling communications equipment to other businesses, and its customers included some of the largest mobile companies worldwide.

**5:28** · Huawei exported everything from modems to submarine cables, and didn't miss a single chance to branch out into a new product category.

**5:36** · In the span of just a few years, its size tripled, and so did its revenue.

**5:41** · It was already among the largest technology companies in the world, and on its way to becoming the largest.

**5:47** · But then, some skeletons began poking out of the closet, and a lot of people who depended on its products suddenly got very uneasy.

### Chapter 2: Trigger

**5:56** · Huawei was hit with the first of its major scandals in 2003.

**6:00** · Cisco Systems, one of the industry players Huawei tried to uproot, sued for intellectual property theft.

**6:06** · Well, this is a very mild way to put it.

**6:09** · Basically, Huawei copied Cisco software for some of its routers and switches, and the manuals, too.

**6:14** · Word for word, even including spelling mistakes.

**6:18** · A while later, Motorola accused Huawei of sending an employee to infiltrate them.

**6:23** · According to court documents, the employee spent several years copying blueprints of Motorola's base stations and sending them directly to Huawei's founders, only for Huawei to manufacture direct copies.

**6:34** · In 2008, a worker at Nortel, one of the largest telecommunications companies at the time, discovered that almost the whole fleet of computers, as workplace was infected.

**6:44** · The hackers were imaging entire hard drives and sending the images to their handlers in China.

**6:49** · They weren't even hiding their IPs and kept discussing their work on random Chinese forums.

**6:54** · You guessed it. In several years, direct copies of Nortel's equipment were being manufactured by Huawei.

**7:00** · Except that Nortel didn't have the time to sue anyone.

**7:02** · It couldn't compete with Huawei's cheaper products and went bankrupt.

**7:06** · Before Chinese company Huawei became the largest telecommunications equipment manufacturer in the world, a Canadian company, Nortel, was on top.

**7:16** · All of these stories were just a fraction of the whole avalanche of Chinese industrial espionage operations conducted at the time.

**7:23** · If you want to hear about the most famous one, we've got a video for you, Operation Shady Rat, check it out next.

**7:30** · We post videos like this every month or so.

**7:32** · So if you're into hacking documentaries, subscribe to our channel and help us make more.

**7:37** · Thanks.

**7:38** · These cases of Chinese industrial espionage are not an excuse for what happened later, far from it.

**7:44** · Instead, they're important because they set the scene for the attitude towards Huawei at the time.

**7:50** · That attitude was also shaped by another thing, Huawei's alleged ties to the Chinese military, government, and the Communist Party.

**7:58** · The founder of Huawei started his engineering career in the army.

**8:02** · The army was also one of the first customers of Huawei, and kept buying its communications equipment for years to come.

**8:08** · Based on this, some in the West were alleging that the entire company is under direct control of the military.

**8:14** · The accusations were a bit of a stretch, but Huawei's response didn't help.

**8:19** · For years, it refused to reveal its ownership structure, only stating, in the best traditions of communist propaganda, that it is fully owned by its employees.

**8:28** · At the same time, Huawei was receiving a lot of support from the Chinese government.

**8:33** · A lot.

**8:34** · Loans, contracts, a direct line of communication.

**8:38** · The Communist Party understood that tech giants are of the utmost importance to the success of the Chinese economic miracle.

**8:45** · The government even kept denying all of the allegations of industrial espionage to the outside world.

**8:50** · Meanwhile, inside, copying Western technology wasn't just accepted, it was encouraged and glorified, presented as a way to repay the West for past humiliations.

**9:00** · Say whatever you want, seeing all of that was quite unsettling for any user of Huawei technology, especially as Huawei was quickly climbing towards becoming the biggest tech brand in the entire world.

**9:11** · The analysts who saw its relations with the military and the government were worried.

**9:15** · As the logic went, even if Huawei is completely independent from the government and the party, wouldn't it at least want to repay with kindness?

**9:24** · The company was now managing terabytes upon terabytes of data flowing out into and between American and European countries.

**9:32** · The Communist Party could ask Huawei to maybe take a peek or force it to give up some of the data on the pretext of national security.

**9:40** · Would it do that, though? Nobody knew.

**9:43** · If only there was a way to understand how Huawei really works, what is happening inside its management structure, what are the motivations of its executives, and what are their relations with the Communist Party of China.

**9:55** · Of course, to get that information, somebody would have to infiltrate the company, thoroughly hack it at its highest management level.

**10:03** · A difficult task, almost impossible.

**10:06** · But the American government had somebody who specialized in the impossible.

### Chapter 3: Execution

**10:11** · And so Operation ShotGiant was launched.

**10:16** · It was performed by TAO, Tailored Access Operations, the secretive cyber espionage arm of the National Security Agency, and without much doubt, one of the most elite hacking units in the world.

**10:27** · With rare exceptions like Stuxnet, TAO wasn't after destroying things.

**10:32** · It was what people in the know, call Advanced Persistent Threat.

**10:36** · After infiltrating its target, it persisted, loitered there, keeping watch, observing.

**10:43** · Most state-sponsored threat actors are like that.

**10:46** · And for decades, TAO was the most advanced, persistent, and threatening of them all.

**10:51** · Which is why when Uncle Sam really, really needed to get some exclusive knowledge, TAO was who it called.

**10:59** · Now, back in the late 2000s, TAO was a complete secret.

**11:03** · NSA largely managed to keep information about its elite hacking units under wraps.

**11:08** · But it all changed in 2013 when one person decided to spill the secret.

**11:13** · It was Edward Snowden, arguably the most famous and important whistleblower of all time.

**11:19** · A lot of the documents he leaked had something to do with TAO, and a lot of those documents contained details on some pretty heavy stuff.

**11:26** · But the few pages describing Operation Shot Giant were still among the heaviest.

**11:32** · Those pages were from top secret slides the NSA made for Five Eyes, a collection of Intelligence Agencies from allied countries.

**11:40** · Unfortunately, the slides come without any context.

**11:43** · Some of the information is also censored, which doesn't help, but the remaining information gives us enough pointers to figure out what happened.

**11:50** · Most importantly, we know the objectives of the operation.

**11:54** · First and foremost of those objectives was finding out if Huawei engages in spying on behalf of the Chinese government.

**12:01** · The second objective was to gain more information on the company itself, decipher Huawei's mysterious organizational structure, relationships within it, even the plans for the future.

**12:12** · With the first two objectives completed, the NSA would have complete access to one of the largest tech companies in the world.

**12:18** · Why waste the opportunities and not do something useful with it?

**12:22** · The third objective was to use Huawei's potential for filling intelligence gaps the NSA had, poke around the most sensitive parts of the company, decipher its encryption protocols, get a glimpse of its research and development plans, take a good look at its supply chain.

**12:37** · Finally, with all of this completed, the most ambitious part could be launched, using Huawei to reach otherwise unreachable targets.

**12:45** · Particularly in unfriendly countries.

**12:48** · That part is rich.

**12:51** · After seeing this objective, a lot of people interpreted as the NSA trying to install its own backdoors into Huawei's equipment, which is a valid way to look at it, but not the only way.

**13:02** · Let's return to that later.

**13:04** · Meanwhile, how would TAO reach its objectives, and how did it all pan out in the end?

**13:10** · Well, we don't know for sure, but the third side from the Snowden leaks gives us a hint.

**13:15** · It shows the emails of Ren Zhengfei, the CEO and founder of Huawei, and Sun Yafang, the chairwoman at the company.

**13:23** · It also shows their social circle, the people they communicated with via email.

**13:28** · According to additional details provided by Spiegel, a German newspaper, Snowden shared his leaks with, the NSA infiltrated an email server at Huawei's central office in Shenzhen.

**13:38** · There, the hackers kept intercepting all internal communications within Huawei and scanning them for important details.

**13:45** · We don't know how precisely that was done, but we can take a wild guess.

**13:49** · For example, TAO might have used its tool of choice for breaching confidential communications, Fox Acid.

**13:57** · Initially, it was developed specifically for infiltrating Al-Qaeda, and then branched out into a full-on toolkit that leveraged bugs in popular browsers.

**14:05** · The deployment of Fox Acid would begin with a phishing message, which convinced the target to click on a link.

**14:11** · The link would lead to a custom malicious page, which installed a backdoor in the browser.

**14:16** · Then, depending on the target system and the mission, the MSA could use a variety of specialized tools to intercept, monitor, and even modify the traffic that the target sent and received.

**14:27** · Fox Acid may have been used to breach the executives at Huawei, but TAO might have deployed something else as well.

**14:34** · All we know is that it succeeded.

**14:36** · That's the first two objectives of ShotGiant covered.

**14:40** · How about the other ones?

**14:42** · At one point, the NSA's operatives admitted that through this operation, they managed to get a hold of more information on Huawei than they knew what to do with.

**14:50** · They even got access to the source code of Huawei products, which granted them the ability to not only reverse engineer them, but also to dissect them for any vulnerabilities.

**14:59** · And this is where things get pretty complicated.

### Chapter 4: Post Mortem

**15:03** · Initially, it seemed that we were never going to know if the NSA found any dirt on Huawei.

**15:07** · In the early 2010s, various institutions across the world launched their own investigations into the company.

**15:13** · As a rule, they didn't provide any concrete evidence on either its ties to the government or spying operations, but recommended or even demanded, avoiding Huawei products anyway.

**15:24** · In 2013, the former chief of the NSA came out saying that he had seen backdoors in Huawei equipment with his own eyes.

**15:31** · It was around the same time the details about Operation ShotGiant got leaked, so his words appeared to have quite a bit of weight.

**15:37** · In response, Huawei fired back.

**15:39** · It called the allegations baseless, began revealing more information about its structure, and even went on to undergo security assessments in the attempt to prove that the NSA does not know what it's talking about.

**15:50** · Was that right, though?

**15:51** · And also, did the NSA really manage to turn Huawei into its own spying apparatus?

**15:56** · You see, here's the fun part about deliberate backdoors.

**15:59** · They usually aren't labeled as deliberate.

**16:02** · In almost all cases, they're nearly indistinguishable from your regular old bugs.

**16:06** · And ever since the early 2000s, researchers discovered a lot of those bugs in Huawei's equipment.

**16:12** · Some of them allowed intercepting traffic, escalating privileges, conducting denial of service, and doing all other things a malicious actor or a hostile government would find extremely useful.

**16:22** · Just like many companies whose income depended on reputation, Huawei generally did not pass on the chance of fixing revealed vulnerabilities.

**16:29** · Especially when the press looked bad.

**16:31** · It's pretty much impossible to say if any of these vulnerabilities were deliberate, if they were intentional backdoors or just honest mistakes Huawei's coders made.

**16:40** · And since the NSA had priority seat access to lots of Huawei products since 2009, it's entirely possible that it knew some of those vulnerabilities and even use them for its own advantage, like in the speculative but plausible scenario we showed in the intro.

**16:55** · In 2020, the White House reiterated once again, it saw the backdoors in Huawei equipment, and it knew about them since Operation ShotGiant.

**17:03** · But once again, concrete examples were not provided.

**17:06** · Instead, the officials pointed to Chinese laws that mandate companies to share intelligence information with the government.

**17:12** · And that is true.

**17:13** · Chinese National Intelligence law indeed obligates all citizens and organizations sharing information which relates to national security.

**17:21** · But national security is a vague definition.

**17:25** · The NSA conducted Operation ShotGiant for the purpose of national security, too.

**17:29** · It acted under the American law, just like Huawei would have acted under Chinese law, had any of those backdoors been intentional.

**17:37** · In the end, the real results of operations like this are hard to quantify.

**17:41** · Somewhere deep in the NSA's archives, there probably lay multiple reports with in-depth assessments of the conclusions of Operation ShotGiant presented to the American government.

**17:50** · Maybe TAO hackers really found out that Huawei's vulnerabilities are deliberate, that they're just secret backdoors left there for the purpose of the Chinese government.

**17:59** · Maybe the NSA used some of those vulnerabilities to breach the targets that would have been untouchable otherwise, or maybe not.

**18:07** · We probably will never know.

**18:09** · Unless the government declassifies something, it has no intention to declassify, or another whistleblower manages to sneak out another trove of leaked data.

**18:18** · Operation ShotGiant showed how vulnerable our digital infrastructure really is.

**18:23** · Huawei, the crown jewel of the Chinese economy, was breached.

**18:26** · Its top management was put under surveillance, and nobody managed to stop this attack.

**18:32** · Nobody knew about it until its operation details got leaked.

**18:35** · Sure, Huawei probably isn't the first tech giant to be penetrated in such a way, but the ingenuity and persistence with which it was done left the cyber world in awe.

**18:45** · In this sense, Operation ShotGiant was the harbinger of countless similar far-reaching attacks that came later, like the one on SolarWinds, which saw hackers intercepting communications at the highest reaches of the American government.

**18:58** · Should it be the next cyber attack we tackle in the next installment of No Rollback, or would you prefer something else?

**19:04** · Let us know in the comments.

**19:05** · Thank you for watching this video.

**19:07** · We hope you enjoyed it, and we'll see you in the next video.