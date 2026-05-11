---
title: "China is Already Inside your infrastructure"
source: "https://www.youtube.com/watch?v=Vj5Z7RYMACY"
author:
  - "[[Threat Talks]]"
published: 2026-03-03
created: 2026-05-05
description: "China is Already Inside your infrastructure. And the EU is done ignoring it.In this exclusive first discussion of the upcoming EU Cybersecurity Act revision, Bart Groothuis, MEP, joins Lieuwe-Jan"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=Vj5Z7RYMACY)

China is Already Inside your infrastructure.  
  
And the EU is done ignoring it.  
  
In this exclusive first discussion of the upcoming EU Cybersecurity Act revision, Bart Groothuis, MEP, joins Lieuwe-Jan Koning, CTO and Co-Founder, to explain why vendor dependency is now a board-level security risk.  
  
Groothuis breaks down how the revised EU Cybersecurity Act will shift Europe from soft guidance to hard enforcement - introducing formal “high-risk vendor” treatment inside critical infrastructure.  
  
This isn’t about secret backdoors.  
  
It’s about who controls the next update.  
Who enters your data center.  
And who can one day - switch off the grid.  
  
The revision brings non-technical risk - state influence, intelligence laws, geopolitical leverage - directly into cyber certification decisions. That means supply chain risk is no longer theoretical. It’s regulatory.  
  
And the impact goes far beyond telecom.  
Energy. Cloud. Transport. Enterprise IT.  
  
If your infrastructure depends on a vendor tied to a high-risk state, this conversation matters.  
  
Timestamps (MM:SS)  
00:00 Opening & guest intro: MEP Bart Roos - rapporteur on EU legislation  
01:23 What the CSA revision targets - certification, telecoms, cloud  
09:11 Non-technical risk: intelligence laws, vendor-state ties, 5G implications  
15:10 What’s new in the Security Act Revision, 4G vs 5G - why virtualisation changes the security model  
17:17Energy, inverters, and real-world dependency risks - blackouts  
21:53 What organisations & buyers should do now (roadmaps, phasing out risk)  
25:53 Final call to action & closing  
  
Key Topics Covered  
• Why the EU Cybersecurity Act revision treats non-technical vendor risk as policy, not just code review.  
• The difference between technical vulnerabilities and vendor/state dependencies (intelligence laws, personnel access).  
• 5G’s virtualised architecture: “winner takes all” risks and the limits of code audits.  
• Practical next steps for CISOs: vendor inventory, risk-based roadmaps, procurement levers and phasing strategies.  
  
Related ON2IT content & explicitly referenced resources  
\- ON2IT website: https://on2it.net/  
\- Threat Talks website: https://threat-talks.com/  
\- European Commission - Cybersecurity Act overview: https://digital-strategy.ec.europa.eu/en/policies/cybersecurity-act  
\- Proposal for a Regulation for the EU Cybersecurity Act: https://digital-strategy.ec.europa.eu/en/library/proposal-regulation-eu-cybersecurity-act  
  
  
🔔 Follow and Support our channel! 🔔  
\===  
► YOUTUBE: https://youtube.com/@ThreatTalks  
► SPOTIFY: https://open.spotify.com/show/1SXUyUEndOeKYREvlAeD7E  
► APPLE: https://podcasts.apple.com/us/podcast/threat-talks-your-gateway-to-cybersecurity-insights/id1725776520  
  
👕 Receive your Threat Talks T-shirt  
https://threat-talks.com/  
  
🗺️ Explore the Hack's Route in Detail 🗺️  
https://threat-talks.com  
  
🕵️ Threat Talks is a collaboration between @ON2IT and @AMS-IX

## Transcript

### Opening & guest intro: MEP Bart Roos - rapporteur on EU legislation

**0:00** · Help! China is in my infrastructure. Welcome to Threat Talks. My name is Lieuwe Jan Koning, and here from the Security Operations Center at ON2IT, we bring you the next episode.

**0:08** · Let's get onto it. Welcome to Threat Talks. Let's delve deep into the dynamic world of cybersecurity.

**0:14** · Let me introduce my guest of today. I'm really excited he is here because this is a man who has not a lot of time on his mind because he is a member of the European Parliament. His name is Bart Groothuis, and he is part of the Renew Europe group. Bart, welcome. Good morning. Hello.

**0:32** · Good morning. Many people in the cyber industry already have heard your name or know about you, and that is for a very good reason. Because Bart has been instrumental in the NIS2 legislation, he was actually appointed by the European Parliament as the rapporteur. And what that means is that while you lead new legislation from A to Z, if I summarize it, so there's a lot of things that we actually have to thank Bart for.

**0:59** · And many of the good things that we are doing right now with NIS2 and the broader reach that it has, we now reap the fruits of. But of course, well, we're not going to talk too much about NIS2 today because Bart has been working in the past years on the next steps already. And that's what we're going to talk today about, because there's an upcoming revision of the CSA, the Cybersecurity Act, coming up in our European Parliament. And we would like to know everything there is to tell about this.

### What the CSA revision targets - certification, telecoms, cloud

**1:29** · So I'm really excited to have this conversation with you, Bart. So yeah , could you explain to me, what is this revision all about? Mainly about certification, how Europe certifies: cloud certification, product certification, telecommunications certification.

**1:45** · So it's a powerful instrument. And mainly, I think the main problem that we've had is that it's been seen as a mere technical instrument. But as you know, it's becoming more and more political as well. Also because, I think mainly China offers low cost solution inside a critical infrastructure. And I guess we don't want to be too dependent on them. And those reasons we will elaborate on. But I mean, the reason that we certify is we certify our products in a critical infrastructure so we can live prosperously, and safe and secure.

**2:18** · So you're talking about products? Is that also vendors? it might also be vendors. Yes. This is the realisation..

**2:25** · The European Commission is now, because they put forward this legislation, the European Commission has finally realised there are high risk vendors inside our critical infrastructure. And high risk vendors has not just to do with technical issues, it also has to do with non-technical issues. Non- technical issues such as the 2017 intelligence legislation in China, which compels any Chinese company wherever in the world to do what the services, what the Chinese state wants of them. And that is a problem in itself.

**2:57** · That the Chinese state operates very differently than many other countries and that vendors from China have a specific risk, a non-technical risk profile we have to address in our certification. This legislation is being used for that. Okay, so I remember that we had some discussions over here about 5G network for telecommunication. Can we take that as an example? And could you educate us on what those risks then are? Because you mentioned technical risk, but especially I'm interested in the non-technical ones then.

**3:29** · Let's just say Huawei, for example. Huawei is by far the most important together with ZTE telecommunications infrastructure provider outside Nokia and Ericsson.

**3:43** · And the problem is this, we've been focusing in Europe, but also in the US, too much on a secretive backdoor. Have the Chinese inserted a secretive backdoor in Huawei routers? That was a debate. And that's a completely wrong debate. I 've been trying to convince my political colleagues of that wrong debate because you're always one software update away from disaster. You know, there's hundreds of millions of rules of code inside of a router. You can always insert new backdoors there.

**4:14** · The question isn't whether Huawei has done that in the past 20 years, whether they could do or will do in the next 20 or 30 years. So what you're saying is we may certify and analyze the source code or the firmware of those devices right now and conclude there is no backdoor. But the point is, with a flip of a switch, they can probably install it everywhere at once and then we have it. Exactly. And the United Kingdom has a testing center.

**4:39** · And I think that's flawed, too. They shouldn't have done that. That's ridiculous. Looking, reviewing millions of lines of code. That's not the issue. Yeah, you have to review the code that hasn't \[been\] written yet. And that's by definition impossible. Gotcha. And another non-technical risk then comes. And if you're a telecommunication provider, but we'll come to later to other forms of society as well in other products. But let me just focus now, for example, on telecommunications.

**5:09** · If you deliver yourself to Huawei, then for the outroll of the product, you're dependent on Chinese nationals that enter your data center for maintenance, but also for innovation, for backups , for you have risk, cybersecurity risk you cannot manage technically. But it's important that you understand if Chinese nationals enter your data center, they enter the core of the telecommunication infrastructure. What is there to, how can you have technical measures? And in 4G, in 4G, Huawei is manageable.

**5:42** · And that is because, for example, if you have a government infrastructure in The Hague or in Washington DC or wherever, you can say we want to have trusted vendors putting up an antenna. You can look at the traffic which goes through, you can do DPI, you can have a security rules and you can really, you can hire a company, you can see how to mitigate cybersecurity risk from a technical point of view. But in 5G, it's very different.

**6:16** · 5G means the antenna layer of a telecommunications provider is being virtualized. It means the winner takes all. It means that there's only one vendor you will choose. And if one vendor introduces such risks to the core of your telecommunication infrastructure, you have a problem for billing, for cold data records, etc. So there's no mitigation option anymore. We should make a decision.

**6:44** · I want to make sure that I fully understand what you're saying. So for 4G, it's an antenna, you know who built it and whose data runs over it.

**6:49** · But with 5G, it's a virtual thing. So vendors can pop in and out of that antenna then? Is that how I should look at it? Yeah, it's a virtualized layer inside the infrastructure and architecture of a telecommunication provider. That's why in 2020, the European Commission came forward with a 5G toolbox saying where can we allow risky vendors, China, Huawei, ZTE, inside of 5G? Because not all is critical, but maybe in 5G more is critical.

**7:21** · The question is, where is it critical? And that was an exercise that has been done by the European Commission. And it was a very good crafted, well crafted piece. But it was soft law. It wasn't hard law. So it gave telecommunications providers in this case guidance, where can we and how to handle it? Now, years after, together with my colleagues ... So soft law just means that nobody's really enforced to use it. So it's more of an advice, it 's optional, but it's not like the European Commission can with that say, you got to use this kind of equipment or this vendor and not that one.

**7:56** · That wasn't the power of it. Exactly. And then what happened was we asked the European Court of Auditors, we have that at our disposal as members of parliament, and they can review that. And we asked them to put down, put forward a review of that soft law. And they said it's a rackety patchwork of policies. Almost half of the member states have actually put forward real good policies to address the Huawei issue, and the other half hasn't. So that's a problem as such, and we should do something about that.

**8:27** · And they said, come up with hard law. Sent several letters to the European Commission. We've sent pressure and pressure all over again. And what they thought is we should actually put that in the Cybersecurity , Act. And this is why this revision is here.

**8:45** · And the Cybersecurity Act is like, there's no optional thing in there. So that's the right place to put it in. But before we dive into that a little bit more, you said telecommunication, but it's not just that. The first thing that springs to mind with me, Chinese cars, for example, they are everywhere, or solar panels. Is that also what you're concerned about?

**9:04** · Sure. Sure. And we'll come to that. But first, back to Huawei, it's not just there's a technical risk or there's a non-technical risk. There's also a legal risk, like I said, the 27th intelligence that, but it's also a political strategic military risk. Because 5G, and we'll come back to the other products, that is not just the nerve center of our future societies. It's also a political military strategic battlefield.

### Non-technical risk: intelligence laws, vendor-state ties, 5G implications

**9:29** · And you either take control of critical components of your telecommunications backbone, or you become the signals intelligence colony of another country.

**9:41** · And what many say is that, well, everyone spies, so why bother taking care about looking at China?

**9:50** · And I say, well, that's true. And even the Dutch- But there's a difference. Open your doors, or at least make it difficult.

**9:58** · The lesson shouldn't be everyone spies, so why bother? I mean, there's several in open source, there's several cases of the Dutch and the Germans together spying on crypto AG and a Swiss company, which provides telecommunication encryption. And apparently those countries spied and were able to intercept and decrypt much of the many of the telecommunications traffic that has been flowing. Well, the lesson shouldn't be everyone spies, so why bother?

**10:26** · But if even a small country like the Netherlands is tempted to do so, do you really believe that China won't misuse the power of owning someone's telecommunications backbone?

**10:40** · Come on. This is critical, right? And the same goes to answer your question for other parts of the infrastructure. This is serious. This is serious shit. This is real problem we have to address.

**10:52** · And I mean, just one step back out of the technical, I was raised by senior diplomats at the Ministry of Foreign Affairs who taught me geography, but geography is the most important asset for geopolitics. China's far and away, Russia's more near, concentrate on that. But I said, it's not.

**11:12** · Your times have changed. Technology is more decisive in geopolitics than geography. Far away geographical bodies are now like next door, thanks to the digital- They're not even next door. They're inside your home, inside your car, in your critical infrastructure. This is decisive.

**11:33** · This is a decisive moment in history. Are we being colonized or not? Do we want to be coerced or not? And this is why I am so eager to get this revision of the CSA done, because we finally make hard legislation to get this through in Europe.

**11:49** · And we're the first of a kind. We're the first in the world to have this sort of legislation.

**11:54** · And I commend it. it's a blueprint for how this should be done. Yeah. So it makes me realize I wouldn't allow a spy like a person in my house sitting there all the time. But in fact, I'm already doing it because of my maybe solar panels or my phone, right? And that's how we should think about it. That's so true. I've been very, very active in parliament in the past years. Especially on Russia, China, Iran and North Korea. Because these countries have something in common, right?

**12:24** · They have this legislation, this non-technical risk. They have companies in place that want to penetrate our critical infrastructure. They are able and willing to project an authoritarian view of the world inside our own backyard. They are the ones who aggressively try to pursue and dump below cost price inside our critical infrastructure products that actually they control. And the most critical, for example, is energy, like you just mentioned.

**12:51** · And then, if you look at politicians in Brussels or in The Hague or wherever, they say, we do not buy Russian gas anymore. We never want to be again dependent on a tyrant or not a dictator like Putin. We've seen what he's done.

**13:07** · It's not a commercial project, most \[ \] do, It's a coercion project. And I commend them for that. Yeah, that actually makes me realize gas doesn't actually get a software update that we should be scared about. That's true. So we're becoming more dependent on software updates inside our energy infrastructure because we need batteries and we need control panels. We need inverters to convert the energy from solar panels to our grid. And the list goes on and on. And this is the problem, of course.

**13:37** · And we've seen in Portugal, France, and parts of Spain last year, the two and a half gigawatts fell off the grid, and entire parts of Europe experienced a blackout.

**13:51** · And this is a problem as such. And if two and a half gigawatts can provide a blackout, then imagine how much of the more than 200 gigawatts that Huawei controls with this inverter business in Europe. They don't just control it.

**14:07** · They own it. They dumped it. There's below cost price. And I'm not saying it's not good material, but it's a dependency that we've introduced on Huawei. And the reason I'm also saying this is because I see in open source, many of the Chinese research universities, they do research on how to create blackouts inside the European or American electricity market. And it's not about how do we solve it? How do we build resilience? It's about how to shut it down.

**14:35** · This is what the universities in China are studying. There's more than a dozen studies I found online. It's not healthy. We shouldn't- It doesn't take a spy to know this. Yeah, well, it's important that we know what the threat is, and we shouldn't be naive. We were too naive on gas in Russia, but we're going from one dependency, from one autocrat to dependency on the other autocrat. And this is why the Cybersecurity Act comes in. This is where it helps to actually mitigate those risks.

**15:05** · So what is new at this revision that - It's super clear why it's needed, super clear - So how do you do it? Well, the 5G toolbox, for example, is a good example.

### What’s new in the Security Act Revision, 4G vs 5G - why virtualisation changes the security model

**15:21** · That has been revised. It's technically tested.

**15:24** · And we know it's not implemented right. So we make it obligatory. And the European Commission will come forward with proposals to push Huawei out of European critical infrastructure. And I commend that. And the Chinese are doing the same with European producers. Less than 5% of the market share in China is by Nokia and Ericsson. They won't allow our products in their market. This is just mirroring what they are doing for the same reasons we are doing it.

**15:55** · The only problem is we are lagging behind. But then the question is, if you have 5G, what do we do with inverters?

**16:05** · What do we do with the battery control? What do we do with cars, like you said? What do we do with other parts and transport? And this is next onthe menu. This is in the CSA. But I'm critical about the speed with which we can deliver that. So this is in the revision. Parliament still has to decide what to do with it. My main spear point will be speed. Speed is of the essence. And speed is powerful. Do you mean speed of passing this legislation or what's right after that?

**16:33** · Well, the speed of the legislation is slow because there's so many process steps in between. Studies.

**16:42** · Studies by member states, studies by the European Commission, impact assessments, all sorts of delegations, delegated powers to the commission to come up with acts. It might take years to come up with something. That's not what I want. I want to deliver with the speed of light. Because China is... And the problem is that the European Commission knows this is highly political. Like I just said, this technology is geopolitics.

**17:10** · But this is why I got into parliament. This is the reason why people elected me because I believe this is what I should do. What does the commission need to do today, tomorrow? Well, put off firm, I mean firm rules for our critical infrastructure.

### Energy, inverters, and real-world dependency risks - blackouts

**17:26** · If you conjointly can shut down the European electricity grid, that's just, I think it's an un- imaginable threat. It sounds like a no-brainer, honestly. It's a no-brainer. It's a no-brainer.

**17:39** · And I would say it's another no-brainer because of industrial policy. We have a couple of European producers of inverters, PV inverters, but they're bleeding. But they're good, but they're bleeding because the Chinese always outcompete them. It's not just because they have cheaper products, it's because they overproduce and they subsidize, the government subsidizes it and they dump it on our market. We are being deindustrialized on a huge scale, faster than we can imagine.

**18:08** · It's also industrial policy for our industries and businesses here in Europe to thrive. So it's not just cybersecurity.

**18:15** · Yeah. Imagine what would happen if like a French company would be subsidized by the French government to put this equipment on the European market. Then I'm sure there's lots of rules against that and that won't happen. But the Chinese do and we let it happen.

**18:30** · Exactly. This is crazy. So yeah. So as a citizen, what can I do? Who should I vote for, for example?

**18:39** · You apparently. Vote for whoever you want, but don't vote for, I mean, vote for everyone, but vote for some, for people who want to solve problems and not just... And I believe that if we solve this one, it's good for our industry, it's good for our security, it might also cost money.

**18:58** · I should be honest with anyone who votes, voted for me, it could cost us money. It's more expensive to do it ourselves because the Chinese dumped very cheap equipment. But in the short term, geopolitical costs in the short term are often very low, but in the long term, what you pay is...

**19:16** · That's the problem. In the long term, you can be coerced and your political sovereignty is at stake.

**19:22** · What if China would seize Taiwan? What if we would have countermeasures against China?

**19:30** · They could shut down our entire industry. Is this something that we think is okay? I don't.

**19:36** · And I understand that the cost will be there, but the long-term costs are much higher.

**19:41** · So what's the force then that limits the European Commission in actually doing the light speed as you propose? That's the member states. The member states with the large dependencies on China, they fear retaliation, they fear that they are being coerced again, and this is the problem.

**19:59** · And it's mainly Germany, Spain. Those countries have huge dependency on.. Germany, on export to China and Spain nowadays from foreign direct investments in Spain. Those are the problems that we face. And I guess that for my country, the Netherlands, we can't accept it. We are very dependent on Chinese exports as well, but I guess that a good conversation with the Chinese is possible to say, this is what you do to our vendors. We just mirror what we do.

**20:29** · And I guess that it's possible to do. Yeah. So there's a lot of work for the European Commission, but especially then in making deals between the member states and make sure they were all aligned. Does it require all member states to agree on this? Or can it also be like a super majority or a regular majority?

**20:55** · Yeah. No, it's everybody. This is majority voting.

**20:58** · Yes. But even that is difficult then.

**21:02** · It's doable, but you see in the way that the European Commission has crafted this legislation, they take into account the fears of many member states. We're in parliament. We have a different role to play when it comes to European legislation. This is the good thing. It's never a hundred percent the member states. It's not just the commission. It's also elected representatives from the parliament who together make legislation which works. I have to explain to my constituents, to my voters, what we've done.

**21:36** · And it's not just the member states deciding or saying they want to be nice and kind to each other. We're not. I'm very curious how this all works out. And we'll follow it like really closely because it's so important. What I would like to shift into a little bit is what can we do? What can organizations do? I mean, voters we talked about a little bit, but organizations, I mean, I'm guessing that there's also buying power within companies, for example, and companies move more quick. What can we do?

### What organisations & buyers should do now (roadmaps, phasing out risk)

**22:07** · Well, companies of course have to assess what kind of products they have in their critical infrastructure. The NIS2, like you've mentioned in the first bit, that it says you have a responsibility to look at the vendors, the Cyber Resilience Act on critical hard and software. It was an opportunity to push out risky vendors, but they didn't. They do ask anyone to say, look at risky vendors from risky countries. So how do we know what those risky vendors and risky products are?

**22:34** · Is that something that - That's been defined in this new law and this new revision for the first time, there's two things, risky vendors, either black or a white list and the risky countries, let's say high risk countries who have this non-technical element of risk inside the vendors because of coming from the country.

**22:56** · The relationship between companies who operate in China and with their government and the communist party is so incomparable with how businesses in Europe work with their governments. Those are separate entities, private and public, that is really, but in China it's not , it's inter-merged. It's also, if you look at the number of, I mean, employees from the Chinese intelligence community who work at the large Chinese tech firms, the overlap is huge.

**23:30** · It's not just that the CEO knows that it's being coerced by the Chinese communist party, it's also lower in the organization. There's an overlap between employees. There's also a non-technical risk. And we've seen Huawei and others also cooperating with other companies who have a real, real bad view of what is morally correct to do.

**23:51** · APT3, for example, is just a Chinese hackers group.

**23:56** · It's been documented in open source. They worked with Boyusec on software vulnerabilities in Huawei, which they also leveraged against targets in Europe, hundreds of them. And we shouldn't ignore these facts. They're already in open source. So.

**24:13** · So new legislation will make it really tangible what those countries or territories are and what the products are. And so it will become much easier. There's no excuse not knowing who to avoid. Correct? So that's what every company then should make a roadmap. It's not easy to phase out maybe. Say you are a telco, you have your Huawei, what would you do? Now, that's the main problem for many of the member states. It will cost too much. So phasing out is a huge cost issue.

**24:41** · The Canadian government recently over a couple of years said, okay, we'll help you with that. If it's the cost issue, we'll help you transferring to Nokia, Ericsson.

**24:53** · Wait, so the Canadian government thinks it's of their interest probably to help the European Union in this journey. Wow.

**25:02** · And the same will go for inverters, batteries, etc. We have to have a program that phases out and where to phase out and where not... That is inside this. And I think that the technical community, the nerds, they should be making this certification. They should be in the driver's seat selling where it introduces an unacceptable risk versus okay, this is doable. This is mitigation we can handle. It's not about completely decoupling from China. It's about accepting where can you accept a risk, where not. This is the key.

**25:37** · It's risk based. It's not an anti-China agenda.

**25:40** · It is really about ourselves. It's not about Chinese people or China as a starting point, but it's about the risk that their infrastructure actually poses on us. And that's what we need to find. It could be true for any country in the world. Well, they have a specific legislation, 2017. But if any other country would pass the same legislation, we would do the same to them.

### Final call to action & closing

**26:09** · Yeah. So that's why we introduce a list of high risk countries. And it's also true for Iran.

**26:16** · And it's also true for Russia. And it's also true for the DPRK, Korea. So those are objective criteria. Yes. So are there enough alternatives then on this? I mean, in IT, I mean, you mentioned the tech people, it's full of nerds here. And we always look at the EU alternative software, etc. And everybody uses their own, preferably their own mail server, for example. So I know they exist. Are they known enough, you think? I guess they are, Lieuwe Jan.

**26:47** · But the problem is, they've been pushed out of the market for too long. And we haven't had the opportunity to really develop it. And I guess the same will happen in many of them. The trend, the global trend I see in politics is demand politics. You create demand by setting rules, setting standards.

**27:08** · And setting standards is also industrial policy.

**27:12** · And creating a European sovereign demand for products will be the trend in the next couple of years. So we should do the same. All right.

**27:20** · So what sectors bother you most? So those in our audience work for companies, is that in the energy sector, for example, is that, do you have some priorities? You must have one.

**27:33** · Well, I guess that the energy sector is utmost importance together with communication sector.

**27:39** · And then we have transport as well. But the main focus should be telecommunications first, and then we tackle the energy grid. Because we're electrifying as a continent, less and less dependent on molecules, more and more on electrics.

**27:55** · And that means the management will be done digitally, accessible from wherever on the planet.

**28:02** · And at their time of choosing, they can create a blackout. And we do not accept such dependencies in a critical infrastructure. It's about critical infrastructure as a first move. But if you're worried about espionage, if you're worried about other forms that those countries can hit you, of course you have a different risk appetite and calculus accordingly. Yeah. Okay. So act accordingly. Yeah. Thank you very much. I mean, this is a clear call to action to everybody really, both in legislation.

**28:32** · And thank you for doing all that work and making sure that our future laws are actually protecting us better.

**28:39** · And a clear call to action to everybody who makes decisions on procurement, and especially in telecom and in energy sectors to act now and to make sure that you look at this list of companies of territories, of countries that we should avoid for these very well voiced reasons.

**29:01** · Bart Groothuis, thank you so much for your time and for explaining this all. And we wish you all the best in making sure that this legislation passes as quickly as possible. Thank you so much.

**29:10** · You're welcome. And to my viewers, thank you very much for tuning in today. If you thought this was really interesting, please approve us with a like we'd appreciate that. And next week, there will be another episode of Threat Talks in your inbox. Hope to see you there. Bye bye.