---
title: "Your Phone is the Perfect Witness (And the Police Know It)"
source: "https://www.youtube.com/watch?v=FZJT81N_sDM"
author:
  - "[[Bilawal Sidhu]]"
published: 2026-06-12
created: 2026-06-13
description: "Most people think surveillance means cameras on street corners.They're wrong.Your phone knows where you sleep, where you work, where you travel, and everywhe..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=FZJT81N_sDM)

## Transcript

### Intro

**0:01** · Right now in towns across the country, people are losing their minds over Flock cameras.

**0:10** · License plate readers bolted onto traffic poles scanning \[music\] every single car that passes by. The pushback is real and the concern is fair.

**0:19** · Well, some communities around the country are coming together to fight against \[music\] what they say is a concerning form of surveillance.

**0:25** · That the surveillance that these Flock \[music\] cameras are doing is not normal. It's not something that people would tolerate.

**0:33** · But while everyone's been arguing about these cameras on poles, your phone has been logging far more than any of them ever could. Where you slept last night, where you ate lunch, how long you sat at your ex's apartment. These aren't just snapshots, these are patterns, a continuous record of your life.

**0:53** · And right now, the Supreme Court is actually debating whether taking all of that data that your phone collects is fair game for law enforcement. \[music\] The tool for this is called a geofence warrant. The police draw a circle on a map. They ask for everyone's data in that circle, not just the suspect, everyone who was in that area at a particular \[music\] time. And whether they're allowed to do that is setting in front of nine justices right now. And I mean, think about it. Phones are better witnesses than cameras. They're more \[music\] accurate, more numerous, and most of us can't leave home without one.

**1:25** · So, instead of asking, can they actually do this, let's walk through what they actually get in a \[music\] geofence warrant layer by layer.

### BIG TECH & SOCIAL - THE HISTORIC GOLDMINE

**1:36** · All right, so the thing about drawing a circle on a map is that it doesn't have to land on just one company. The same warrants can hit Google, Snapchat, Uber, Yahoo, basically any company holding location data. Same circle, different snapshots, all very useful. But if we take a step back, the original target and the historic goldmine has always been Google's \[music\] location history.

**2:00** · Back when this was on by default, Google had a database of every \[music\] place every Android user had ever been.

**2:07** · Internally, Google called this sensor vault. So, if you wanted to know who was within 250 m of a bank robbery between 4:45 and 5:15 on a Tuesday, that was the best place to ask. But, it wasn't just Google. The same circle can pull basically any app that pings your location while you're using it. I mean, even think about Yahoo. Like your beloved and news app is also collecting your location. And then there's Snap Map, a literal heat map of where everyone's \[music\] posting in real time.

**2:34** · Like people are opting into this surveillance for fun and maybe a little bit of utility. I mean, you open this app, you zoom into your block, and that's what's going on in the bar right now. Pan to a different city and watch dots light up around the venue. We literally built our own dragnet and called it a feature. So, here's how this worked. When Google would get a geofence warrant, they built a three-step process \[music\] for responding to them. First, they would share an anonymized list of devices. Law enforcement would take a look at that and try to narrow it down.

**3:03** · And then, and only then, would Google unmask the names of the people that were in \[music\] that circle. Say what you will about Google, but they were trying to build in restraint. I want you to remember this pattern because it's going to show up again.

### Layer 2: Google's surprising move

**3:19** · Now, Google's the real OG here, and they realized that by aggregating all of this user data and putting in one place means that government and law enforcement across the world is going to be very interested in getting access to it. So, in late 2023, Google did something that genuinely shifted this architecture.

**3:36** · Your location timeline, basically every place you've ever been, every commute, every restaurant, used to live \[music\] on Google servers. Now, it lives on your phone. It's auto-deleted every 3 months by default. And if you back it up to the cloud, Google encrypts it with a key that only your device holds, meaning that even Google can't read your \[music\] location data. So now, if a police department draws a circle on a map and sends Google a geofence warrant, "Give us every single account that pinged last Tuesday." Increasingly, Google's answer is, "We don't have that anymore."

**4:07** · Now, here's the clever part. Obviously, Google makes money off of ads, and with this move of location history on device, ad targeting critically didn't break. Their search relevance didn't break. They still know what to show you because targeting is mostly contemporaneous. They have your location while you're searching. Google realized that that historical trail was never the moat. It was just a liability. In other words, keep the derived signal, but dump this honeypot \[music\] of location data.

### Layer 3: carriers and ride-sharing apps

**4:39** · Take Apple for instance. Apple officially returns zero data on geofence warrants. They never built the equivalent of sensor vault, this one centralized location that housed all of their user data. Similar to what Google does now, their location stack was designed for on-device storage and anonymity from day one. So if you have an iPhone, you're probably thinking, "Oh, I'm totally safe." But you're not safe. And this is because your phone is still pinging cell towers every few seconds, regardless of the operating system it runs.

**5:07** · Cell phone carriers can be subpoenaed \[music\] for this tower triangulation data covering anyone in that area \[music\] at the time. And if you use ride-sharing apps, Uber and Lyft is also collecting your data, and you could end up inside that circle. \[music\] Basically, this whole iPhone saves you idea collapses very quickly once you remember that you're using a phone on a physical network that knows where you are by virtue of the service that it gives you.

### Layer 4: vehicles as surveillance

**5:36** · And look, your phone is not the only device that's tracking you. You've got modern Fords, GMs, Toyotas. Basically, every car built in the last decade collects something called telematics data. This is stuff like speed, location, hard braking events, and sometimes even cabin audio. And that data in many cases goes back to the manufacturer. In a similar fashion, the police can subpoena the OEM directly and get all of that data.

**6:02** · So, as privacy research Chris Gilliard put it, modern vehicles are rolling surveillance devices. You know what else is a roaming surveillance device? Self-driving cars.

### Layer 5: Waymo and the digital twin city

**6:16** · Waymo cars roam Phoenix, LA, San Francisco, Austin every block at all hours. And now we're not just talking about RGB cameras, we're talking about lidar, laser 3D reconstructions constantly recording everything. And unlike Tesla, which is the next layer and we'll get to it, Waymo uploads everything to the cloud. They're an Alphabet subsidiary, so the data sits on Google's infrastructure, which means Waymo is fully subject to geofence warrants. Take for example a hit-and-run case in 2019 in Chandler, Arizona.

**6:48** · Detectives served Waymo for video of the suspect vehicle delivered May 22nd, 2019. Then they submitted a Google geofence warrants on the same case signed by Maricopa County Judge on July 16th, 2019 to identify the driver. We're talking about Waymo footage and a Google geofence warrants on the same investigation. The police are already running this play. Now, Waymo's stated policy is very similar to what Google said.

**7:13** · Yes, we'll cooperate with valid warrants, but we'll narrow the scope when the request is overbroad and occasionally object entirely. Now, it's worth noting that Waymo does blur the faces and license plates in the data that they use for their own research, but not in the footage that they hand over to the police. Now, look, this is better than rubber stamping every single request that these companies get, but it's a policy, not an architecture. And as we well know, policies can change.

### Layer 6: Tesla, and what happens when the architecture fights back

**7:47** · Now, what about Tesla? There's so many of these things on the road, and as I mentioned in previous videos, they're sort of like Street View cars. Tesla pulls a partial version of this trick.

**7:57** · The car reports constantly through its 8-plus cameras, but Tesla doesn't upload that footage to the cloud. The full imagery sits on a USB drive in the glove box. So, trip logs, telemetry, and fleet learning clips do end up going to Tesla servers \[music\] and can be subpoenaed. I mean, think of it like this. Basically, the location history of where you drove is completely fair game. But, the ubiquitous surveillance footage, the part that actually matters if the authorities want to use your car to surveil other people, stays local.

**8:24** · The standard geofence warrant does not work on Tesla's camera footage, \[music\] because there's nothing on Tesla's servers to subpoena. So, police do the next obvious thing. In 2024, Oakland police obtained warrants in at least three cases to physically tow and impound innocent bystanders' Teslas, because in these cases, the car may have witnessed a shootout or burglary nearby. So, essentially, your car gets seized as evidence because of where it was parked.

**8:52** · The data that lives on our USB drive is in the glove box, so they take the whole damn vehicle. And, this is the escalation pattern. Because there are so many entities that actually track and monitor our movements, if cloud data gets locked down, you go subpoena the carrier. If a carrier start locking it down, you subpoena the OEM of your vehicle. If they lock it down, take the damn device itself. The legal mechanism keeps adapting to the architectural changes that these companies are making.

### The Mosaic Theory

**9:22** · So, notice what we just did. We didn't walk through one warrant. We walked through the entire stack. Phone pings, social location, carrier triangulation, vehicle telematics, Waymo footage, Tesla cameras. Each layer technically operates on its own legal mechanism. Each layer on its own is even defensible. But the question we should really be asking isn't whether any single layer is reasonable and acceptable. The question is what happens when you add them up. So legal scholars have a name for this.

**9:53** · They call it the mosaic \[music\] theory. The idea is very simple. A single tile is meaningless. A thousand tiles from all sorts of sources fused together is a portrait. So a cop on a corner writing down license plates is a tile. An AI \[music\] fusing every single camera, every single cell ping, every Waymo recording, every car telematics feed \[music\] across the city for 60 days is a portrait of the lives of its citizens.

**10:19** · And that's the question the Supreme Court of the United States \[music\] is grappling with, whether they realize it or not.

**10:30** · All right, so let's get into the legal arguments. For my non-US audience, the Fourth Amendment in the United States basically is in place to prevent unlawful search and seizure. Basically, the cops can't just come into your house and start rifling through all your stuff. So the general argument for allowing public surveillance despite the Fourth Amendment is as follows. If you're outside in the public sphere, everything is fair game. You have no reasonable expectation of privacy.

**10:54** · That's why Google can drive a Street View car down your block. And even the controversial Flock cameras live inside this doctrine, though it's starting to crack. The original rule was about what could be seen in a moment, a snapshot.

**11:08** · License plates on a freeway, faces in a crowd. Once you start making that snapshot continuous and start aggregating all these cameras across the city, that's where the lawsuits are starting to push back. But if you think about it, a geofence warrant breaks that line entirely. A circle on a map doesn't care if you're outside or inside. It can pull data from people in their living rooms, their bedrooms, their offices, at church. In fact, the geofence warrant in the case the Supreme Court is hearing right \[music\] now swept a 17.5 acre radius around a Virginia bank.

**11:39** · That radius included a church. People at \[music\] worship were inside the dragnet. And that's what's different about this case. The oral arguments were April 27th, just a week or so ago as we're recording this video, and a ruling is expected this summer. Now, the case stems from a 2019 bank robbery in suburban Richmond.

### Chatrie v. United States

**12:04** · Police basically used the geofence warrant to ask Google for every device within 150 m of the bank for the hour around the robbery. And just like Google's old tiered approach, they ended up getting 19 anonymized accounts back. Then law enforcement narrowed it to nine, then to three, and then they finally unmasked the actual names. One of them was Okello Chatrie, and he's been challenging the warrant ever since.

**12:27** · \[music\] And by the way, the case only made it to the Supreme Court because the lower courts can't agree. The fifth course ruled in a separate \[music\] case in 2024 that these geofence warrants are completely unconstitutional. The fourth circuit, upon hearing Chatrie's case, was split seven to seven on whether a search even occurred. \[music\] In other words, saying that this is completely fair game. And that's the conflict the Supreme Court is taking up.

### The Honest Case for Geofence Warrants

**12:52** · So, before we get to the critique, the case for geofence warrants deserves to be made more cleanly. I mean, if you think about it, a geofence warrant isn't an officer kicking down a door. There's a real crime that took place. There's a judge that signed off on a warrant. And there's a specific time window and a radius involved. Compared to physically searching someone's home, the intrusion is minimal. You're getting slivers of derived data that we voluntarily share with a private company that's retrieved through a judicial process.

**13:20** · This isn't law enforcement going to Google being like, "Hey, give us a location history of anyone because we think something may have potentially happened. The warrant is anchored to a real event, not a fishing expedition. So, if the data gets misused, that's not a flaw in the warrant, that's a flaw and oversight, and the answer is deterrent penalties that are severe enough to bankrupt and jail any official who abuses this kind of a warrant. Basically, law enforcement would say, "Don't ban the tool, police the tool." So, that's one side of the argument, and it totally makes sense.

**13:52** · But, what the institutionalist position misses is the mosaic. The geofence warrant authorizes one circle around one crime for one time window. But, what it actually unlocks is starting a thread. So, for example, once John Doe is unmasked through the circle, the police can pivot to Flock camera networks. And in those case, no warrants are currently needed.

### The mosaic counter-argument

**14:14** · They can go back in time 60 to 90 days and pull every single vehicle movement, his family's vehicle movements, known associates vehicle movements, start cross-referencing that with social media metadata, cell tower triangulation, every public-facing data feed \[music\] that exists because, let's be honest, open-source intelligence itself is powerful. And now, think about it, none of those secondary pulls were authorized by the original judge. Each one technically operates inside its own legal carve out.

**14:43** · So, the opposing case that's being made is that the original warrants was reasonable, but this cascade is not. And honestly, that's the part that erodes the police the misuse argument as well. Like, we only find out about misuse that gets caught, right?

**14:58** · Like, we've got cases on record with police chiefs that are spying on their ex-wives using Flock cameras, police officers running plates on people they know, or people that they want to date. Now, these are the cases that audit surface, and thank God there are audit logs. But, unaudited misuse is by definition invisible, and deterrent penalties only deter what actually gets discovered.

### The question SCOTUS isn't quite asking

**15:24** · Now, here's where it gets really strange. Even the staunchest defenders of geofence warrants, including some who think that Shatree warrant should be upheld, concede that secondary uses of geofence derived data should require separate warrants. The original circle is one search. Pivoting the 60 days of flock history is a different search entirely, and a judge should have to sign off on both of them. So, if you accept that, you have accepted the mosaic \[music\] critique. You've accepted that the real risk isn't in any single warrant.

**15:54** · It's the cascade and ill-tailored tapestry, once put together, \[music\] that creates a clearer picture than you could possibly imagine. But alas, the existing legal framework doesn't have a mechanism for this cascade. There is no mosaic warrant.

**16:10** · There is no judge that reviews the composite. Each downstream pull happens in its own legal silo, which means the question the Supreme Court is being asked, "Was this one warrant constitutional?" isn't actually the question that matters. The question that actually matters is whether American law is built for a world where one warrant unlocks a hundred derived searches that no judge ever sees. And that question is going to be answered in Shatree either way. It just won't be on the first page.

### The First Amendment Angle

**16:42** · Now, most reporting frames this as a privacy case, but it's also a speech case. The Knight First Amendment Institute, the Reporters Committee, the Brennan Center, and others have filed amicus briefs warning that the geofence warrants threaten journalism, protest, and religious assembly. Basically, you can have this dragnet that sweeps anyone who visits a newsroom, \[music\] anyone marching outside a courthouse, anyone gathered at a place of worship.

**17:06** · The concern being that if the government can ID everyone in those circles, the chilling effect on association is not theoretical. It is structural. But also think about where this can go. The Brennan Center brief warned \[music\] about the next step. And it's the line that should land the hardest. If a circle on a map is constitutional, what about a circle around a search query?

**17:29** · Imagine a reverse search warrant flagging every single account that Googled or Chat GPT'd a specific term last week. Every account that watched a specific video. The list goes on and honestly, it's the same legal architecture. It's just a very different trail. That's what's actually being decided this summer. Not just whether the police can pull cell phone pings around a bank, but whether the government can run a dragnet across any digital trail that you leave. And the answer scales to every search, every video, every conversation you've ever had with a machine.

**17:59** · And that is the most challenging thing about the world we live in. We opt into more forms of data collection every single year, which means this mosaic gets bigger and bigger. Legal frameworks have definitely not caught up and the court is about to decide not this mosaic, but one single tile and call it the answer. So, no matter what you think, you should at least be aware the next time you're trying to have a debate about surveillance, you might be worried about the wrong thing. Now, let me tell you the rabbit hole goes much deeper.

**18:27** · So, if you're interested in understanding other forms of surveillance that exist both in orbits and using radio frequency, including your Wi-Fi by the way, you want to check out these two videos over here. Balavo signing off and I'll see y'all in the next one. Cheers.