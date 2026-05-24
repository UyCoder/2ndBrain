---
title: "Lecture 1: Introduction to Individual Decision-Making"
source: "https://www.youtube.com/watch?v=WRibE2nt8wM"
author:
  - "[[MIT OpenCourseWare]]"
published: 2026-05-18
created: 2026-05-23
description: "MIT 14.12 Economic Applications of Game Theory, Fall 2025 Instructor: Ian Ball View the complete course: https://ocw.mit.edu/courses/14-12-economic-applications-of-game-theory-fall-2025/YouTube Pla"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=WRibE2nt8wM)

MIT 14.12 Economic Applications of Game Theory, Fall 2025  
Instructor: Ian Ball  
View the complete course: https://ocw.mit.edu/courses/14-12-economic-applications-of-game-theory-fall-2025/  
YouTube Playlist: https://www.youtube.com/playlist?list=PLUl4u3cNGP63quuKvMHCt3cmTmt0O2qpv  
  
In this first lecture of the course, Ian Ball explains the basics of game theory, which is a mathematical framework to analyze decision-making when the outcome depends on the actions of other people. In simpler terms, it's interactive decision-making.  
  
License: Creative Commons BY-NC-SA  
More information at https://ocw.mit.edu/terms  
More courses at https://ocw.mit.edu  
Support OCW at http://ow.ly/a1If50zVRlQ  
  
We encourage constructive comments and discussion on OCW’s YouTube and other social media channels. Personal attacks, hate speech, trolling, and inappropriate comments are not allowed and may be removed. More details at https://ocw.mit.edu/comments.

## Transcript

**0:00** · \[SQUEAKING\] \[RUSTLING\] \[CLICKING\] IAN BALL: OK, great.

**0:10** · So let's now say a little bit about what this course is.

**0:13** · This is a course on game theory or on the economic applications of game theory.

**0:17** · So I think a natural starting point is to ask what is game theory.

**0:21** · Well, here's two definitions, both from people who've won the Nobel Prize for their work in game theory.

**0:27** · The first is by Roger Myerson, who says that game theory is the study of mathematical models of conflict and cooperation between intelligent, rational decision makers.

**0:40** · Robert Aumann, also a Nobel laureate, gives just a briefer definition, which I think encapsulates the key ideas.

**0:47** · It's interactive decision theory.

**0:49** · It's about people making decisions when their decisions interact.

**0:53** · What does it mean for people's decisions to interact?

**0:55** · Well, I think the best way to see it is just an example.

**0:57** · So we're going to play a game as a class to see what it means to be a hopefully rational and intelligent interacting decision maker.

**1:03** · And then after that, I'll get into the formal material on the board.

**1:06** · So to play games in the class, we're going to use a platform called Moblab.

**1:10** · So let me just describe the game and then I'll hit Begin.

**1:12** · You're each going to be assigned a random number between 1 and 100.

**1:15** · It's going to be an integer.

**1:16** · And then you're each going to make a guess, which is also a number between 1 and 100.

**1:20** · The winner of the game-- I'm sorry, there's no real prizes but pride-- the winner of the game is the person who guesses closest to 2/3 of the average of everyone's number in the class.

**1:30** · AUDIENCE: The number they guess or the number they were assigned?

**1:33** · IAN BALL: The number they guess.

**1:34** · So you're assigned a number.

**1:35** · Only you know that.

**1:36** · No one else knows that number.

**1:37** · You're going to make a guess.

**1:38** · And the winning guess is the guess that's closest to 2/3 of the average of everyone in the class's guess.

**1:44** · Yes.

**1:44** · AUDIENCE: Is everyone's number drawn from a uniform distribution?

**1:46** · IAN BALL: Yes.

**1:47** · Any other questions?

**1:48** · Yes.

**1:49** · AUDIENCE: What's the range again?

**1:49** · IAN BALL: 1 to 100.

**1:50** · Yeah.

**1:51** · Any other questions?

**1:52** · I think these details should be there, but sometimes they're a little imprecise in the way they write it.

**1:57** · OK, so let's begin.

**2:04** · All right.

**2:05** · Here we are.

**2:07** · So let's see.

**2:08** · So here on the horizontal axis are the guesses that people made.

**2:12** · Again, to clarify, not the numbers you got, but the guesses that people are making.

**2:15** · And on the vertical axis, we're showing the percentage of people who made that particular guess.

**2:20** · So we have a few.

**2:20** · It's a bit maybe hard to see with the color, but we have a few summary statistics here.

**2:24** · We see that the average was 36 roughly.

**2:29** · And that's the dotted purple line here.

**2:31** · And the winning guess was the guess that was closest to 2/3 of 36, so about 24.

**2:38** · And we see that guess is here.

**2:40** · Does anyone want to share their thought process?

**2:44** · Maybe someone who was quite high up here, what they were thinking.

**2:48** · Or low?

**2:49** · Anyone who's willing to share what they were thinking about?

**2:54** · What about the winner?

**2:55** · They should be able to come forward.

**2:56** · Who won?

**2:57** · Yes.

**2:58** · You won.

**2:58** · OK, tell me, what was your reasoning?

**3:00** · AUDIENCE: I wouldn't replicate the strategy.

**3:02** · I think it's not the best idea.

**3:03** · But what I did was put the mean of a uniform distribution from 0 to 100 would probably be around 50.

**3:09** · IAN BALL: Yeah.

**3:10** · AUDIENCE: I'd take 2/3 of that.

**3:11** · But I thought probably other people would be thinking the same thing.

**3:15** · So I downscaled it a bit more by 2/3.

**3:17** · IAN BALL: Great.

**3:18** · Great.

**3:19** · So you're showing the foundation of game theoretic reasoning, what we talked about, interactive decision making.

**3:23** · You didn't just think about your number.

**3:24** · You had to think about other people's numbers.

**3:26** · And then you had to think about what other people will do given the numbers that they got.

**3:29** · And you adjusted your strategy accordingly.

**3:31** · And in this case, it worked out pretty well.

**3:33** · Anyone else want to share maybe a bid they're happy with, a bid they feel they made a mistake on?

**3:39** · Any other thoughts?

**3:42** · Yes.

**3:43** · AUDIENCE: I did 26.

**3:44** · IAN BALL: 26, OK.

**3:45** · So you were pretty close, yeah?

**3:46** · AUDIENCE: Yeah.

**3:47** · I thought maybe something like 30, and then figured that I was probably wrong in whatever reason I would have, so I just lowered it.

**3:52** · IAN BALL: OK that's fair.

**3:54** · I mean, maybe they don't want to out themselves, but I'm kind of curious.

**3:56** · People that guessed very high, any reasoning about that?

**3:59** · No, maybe they don't want to say anything.

**4:00** · OK, let's play it one more time and see what happens.

**4:06** · Ah, so quite different this time.

**4:09** · So now the average was 21 and the winning choice was 14.

**4:15** · That's interesting.

**4:16** · So this happens every year.

**4:17** · So people are very consistent.

**4:19** · So the distribution has changed a bit.

**4:21** · So some people must have decided to bid less this time.

**4:24** · Anyone who bid less this time, do they want to share why?

**4:29** · Very quiet.

**4:31** · Anyone?

**4:33** · AUDIENCE: It's basically tho idea that you would keep getting 2/3 and 2/3 and 2/3 of what you previously thought like would be a good guess.

**4:42** · IAN BALL: OK.

**4:43** · Can you say a little more?

**4:44** · So you thought something was a good guess, and now you're bidding even less.

**4:47** · And why is that?

**4:48** · AUDIENCE: Like I initially thought something was a good guess.

**4:50** · And then I was like, OK, but if I think this, then what if other people think the same?

**4:54** · So I'm going to give 2/3 of that.

**4:56** · But then 2/3 again of that.

**4:58** · And then I'm going to give 2/3 of that.

**4:59** · IAN BALL: Right.

**5:00** · So what we see is that interactive decision making sometimes creates this regress.

**5:04** · So first, I have to think about my number.

**5:06** · That's certainly relevant.

**5:07** · Then I have to try to think about what other people are going to do.

**5:10** · So I have to think about what number they have.

**5:12** · But now I have to put myself in the shoes of those other people and say, what are they bidding?

**5:15** · What are they going to guess?

**5:17** · Well, they're thinking about what I'm doing.

**5:19** · But when they try to think about what I'm doing, they have to think about what I think about what they're doing.

**5:22** · So I have think about what would they think about what I think what they think.

**5:24** · And all of a sudden, it gets very, very hard.

**5:26** · And this is exactly what game theory is trying to address.

**5:28** · I think for a while historically, if you go back to the history of thought, people thought, it's just an infinite regress.

**5:33** · There's no way we can try to analyze games like this.

**5:36** · And game theory is a formal way to try to think about this kind of reasoning process.

**5:40** · This also happens every year.

**5:42** · A lot of people shift to 100 after we talk about it.

**5:45** · Why?

**5:47** · I think some people are kind of mischievous.

**5:48** · They want to try to shift the results and get it wrong.

**5:51** · So I think this highlights a really important thing about game theory, that when we study game theory and when we analyze a game, a really important modeling choice is writing down what people's preferences actually are, what people want.

**6:03** · So if you analyze this game assuming that people's goal was to win, your predictions might be wrong if some people's goal is not actually to win.

**6:10** · So I think some people's goal might be to make my prediction look a little silly or to make their friends laugh or to mess with things.

**6:16** · That's fine.

**6:17** · That's their preference.

**6:18** · But we need to make sure we accurately capture people's preferences when we model games.

**6:23** · Because if we don't, our predictions are obviously going to be wrong.

**6:26** · Another thing, though, that we have to keep in mind is, especially when comparing the results we get in a lab or in a classroom setting to the real world, is that the stakes really matter.

**6:34** · So we have a lot of students-- maybe a few students who are kind of mischievous.

**6:37** · If you won $10 for guessing, well, I think some of those students wouldn't be so mischievous.

**6:42** · And if you won $100,000 for winning, I think very few students would be mischievous.

**6:46** · And I think once we get high enough, essentially no students would be mischievous.

**6:50** · So the stakes and what you actually get for winning are going to affect the preferences that people have in this game.

**6:56** · So let's move on.

**6:58** · The plan is to move on to the formal analysis, unless there are any questions about this game.

**7:03** · I should say this is sometimes called the Keynesian beauty contest.

**7:06** · So if you want to google it or read about it, that's what it's often called.

**7:09** · Yes.

**7:09** · AUDIENCE: So the average wasn't the average of numbers randomly assigned by the game to everyone, but the average of the choices?

**7:18** · IAN BALL: Exactly right.

**7:19** · So with this many people, the average of the numbers that people got is almost certain to be very close to 50.

**7:24** · But this average is the average choice, so the average guess of people in the class.

**7:29** · And that's why when we move from the first round to the second round, I didn't see all the realizations, but it's likely that the average number that people received was basically the same in the two rounds.

**7:39** · But the average guess changed dramatically because people behaved differently in the second round after we had this discussion.

**7:45** · And we could keep doing this.

**7:46** · We have limited class time.

**7:47** · But my guess if we played this 10 times, we might see people getting very, very close to 0.

**7:51** · And my guess is then some people at 100 to mess with things.

**7:55** · Was there a question here or comment?

**7:57** · Yeah.

**7:58** · AUDIENCE: I didn't get a number.

**7:59** · It was just guest.

**8:00** · I don't know if there was a big number assigned to it.

**8:03** · IAN BALL: Oh, maybe I'm-- oh yeah, you're right.

**8:05** · Sorry.

**8:05** · There's no number.

**8:06** · Yeah, good point.

**8:07** · I'm getting ahead to the next game we play.

**8:09** · You're right.

**8:09** · Sorry.

**8:09** · You weren't assigned a number.

**8:11** · Yeah, sorry.

**8:12** · That was very confusing.

**8:14** · We play another game where you get a number, and fair enough.

**8:16** · Yeah, you don't get a number.

**8:18** · There's no uniformity.

**8:19** · Yeah, fair enough.

**8:19** · OK, I'm getting ahead of myself.

**8:22** · Thanks for the clarification.

**8:25** · OK, let us get to the board.

**8:50** · There we go.

**8:51** · So on the problem set, you'll analyze a variant of this game where you'll get a number.

**8:54** · So that'll be coming.

**9:10** · Let's open this up.

**9:32** · OK, so let's get started.

**9:35** · So first let me say a little bit more about what we said was the definition of game theory which we said was the study of interacting rational decision makers.

**10:03** · So let's break down each of the terms in this definition.

**10:06** · Let's go backwards from easiest to hardest.

**10:10** · So I think the basic thing is that we're studying decision makers.

**10:13** · We're studying people who make decisions.

**10:15** · And that means people are making choices.

**10:17** · So another good word for decision that we'll use a lot in the course is people are making either choices or we might also call it actions.

**10:26** · And game theory is a very abstract, general mathematical theory that applies to a huge range of choices and actions.

**10:33** · So in the game you just played, where you chose a number to guess, that was an example of a choice.

**10:39** · Whether you go to MIT is another example of a choice or action that we could analyze in game theory.

**10:44** · What price a firm sets is another example of a choice.

**10:49** · Which country you move to, what job you choose, how many hours a week you work, these are all these different questions-- what platform a political party chooses coming up to an election, who someone votes for, these are all actions or choices that people make.

**11:03** · And the generality and abstractness of game theory is what allows it to be applied to so many different settings.

**11:08** · And throughout the course, we're going to talk about various applications of game theory, mainly within economics, but also to some things beyond economics, like political science and political bargaining.

**11:19** · What does rational mean?

**11:20** · So this is certainly a sticking point of game theory.

**11:23** · If you've mentioned game theory to someone, whenever I'm on a plane and people ask me what I do and I say I'm a game theorist, I always get the same response.

**11:29** · But aren't people not rational?

**11:30** · You probably don't get asked about game theory on planes as much as I do, but maybe someday you will.

**11:37** · And I want to be cautious about how we interpret rationality.

**11:41** · In some contexts, this is a very bad assumption.

**11:43** · There's no question about that.

**11:46** · But in other contexts, I think it's a better assumption than people might think.

**11:51** · And the reason for that is that the way we use the term rationality within game theory is a bit different than the way we use it colloquially in everyday language.

**11:59** · So what you might often hear someone on the street say is, it's so irrational for this person to like this political candidate.

**12:10** · In our model of rational choice, we would never say someone's preferences are irrational.

**12:15** · If that's what they like, that's what they like.

**12:17** · So rationality, I think a better way to think of it is it's really about consistency.

**12:24** · The agents in the models that we study are going to act towards achieving some consistent objective.

**12:30** · You might disagree with the objective they have.

**12:32** · They might like a different flavor of ice cream or a different political candidate or put different weight on income and leisure.

**12:38** · That's fine.

**12:39** · We don't all have to have the same preferences, but the assumption is that people consistently act with an eye towards these preferences that they do have.

**12:48** · So sometimes, there's a phrase that we say and I like to say is that preferences cannot be irrational.

**13:01** · What can be rational in the context of game theory choices giving preferences.

**13:06** · So liking chocolate ice cream is not irrational.

**13:09** · Even if you really like vanilla, if your friend likes chocolate, that's fine.

**13:12** · But if your friend likes chocolate and they choose vanilla, we would call that choice irrational because they're not maximizing their objective.

**13:19** · Now, consistency-- now I've shifted the goalposts.

**13:23** · Instead of trying to defend rationality as a game theory assumption, I'm now trying to mention consistency.

**13:28** · Again, sometimes it applies, sometimes it doesn't.

**13:31** · My guess is your preferences today as 20-year-olds are very different from the preferences you had 18 years ago.

**13:37** · So if we're looking at a model of people's choices over life, this probably isn't a very good description, or at least we might need to enrich the model to capture that.

**13:44** · But if we're looking at your choices or preferences today and tomorrow, it probably is a pretty good assumption.

**13:51** · And then interacting.

**13:53** · This is the key thing that distinguishes game theory from a lot of other decision problems that we study in economics.

**13:59** · And it's exactly what we saw in this first game.

**14:01** · It's that multiple people are making decisions.

**14:04** · But it's more than that.

**14:05** · There are a lot of situations where we all make decisions, but there's no interaction between the decisions.

**14:10** · So we don't really have to take into account what decisions other people make.

**14:13** · What distinguishes game theory and what I mean by interacting decisions is that when I'm choosing what decision to make myself, I have to take into account what other people are going to do.

**14:22** · Because what other people do affects my preferences.

**14:26** · So this is often called-- the situation is often called strategic interdependence.

**14:38** · What's best for me depends upon what other people do.

**14:43** · So a classic example where this is used would be penalty kicks or tennis serves.

**14:47** · Should the shooter shoot left or right?

**14:49** · Well, there's no inherent reason to shoot left or right.

**14:52** · But whether they should shoot left or right depends upon which way the goalie is going to dive or which way the tennis serve receiver is planning to play.

**14:59** · The best action for one player depends upon what other people are doing.

**15:02** · And that's going to be what we study today.

**15:06** · So that's this course.

**15:08** · What about this class today?

**15:09** · We're actually going to drop interacting and just study a single rational decision maker.

**15:15** · That's going to be our baseline for today.

**15:17** · Because before we can study how rational decision makers interact, we have to study how rational decision makers act in isolation.

**15:25** · So today-- and then the rest of the course will be about interaction-- today we're going to study what's called individual decision making.

**15:35** · Of course, up here, we still have individuals.

**15:38** · But the key is that they're interacting with other individuals.

**15:41** · So maybe individual is not the best term, but this is what's used.

**15:43** · We're going to study individual decision making.

**15:50** · I want to make one final comment about the scope of game theory, which is the question of who's taking these actions.

**15:57** · We often think of it as an individual making choices.

**16:00** · But it can be applied much more broadly.

**16:02** · So there's a lot of applications of game theory to evolution, where we think of animals or species kind of collectively taking actions.

**16:08** · We might also think about firms or organizations, governments taking actions, committees taking actions.

**16:14** · And I think now with the rise of artificial intelligence, there's a lot of interest in thinking of the agents in our models as being an LLM or some algorithm that's taking an action and interacting with people.

**16:25** · So one view that is kind of becoming common, we can debate about it, is that the rationality assumptions of game theory become more useful and more compelling in a world of artificial intelligence.

**16:35** · We can debate about that, but that's a view that some people express.

**16:39** · OK, so here we are, individual decision making.

**16:43** · Let's start with a very simple problem-- a simple what I might call decision or choice problem.

**16:54** · Nothing deep here.

**16:55** · Nothing that interesting about the problem.

**16:57** · But I just want to show how we can set it up.

**16:59** · So let's say that you're choosing between three things.

**17:02** · Let's say you're at a cafe and it's coffee, espresso, and tea.

**17:05** · So we have three choices-- Coffee which I'll label C, espresso which I'll label E, and tea, which I'll label T.

**17:19** · And let's not think about prices.

**17:20** · Of course, maybe coffee is cheaper.

**17:22** · But for now, let's not think about prices.

**17:23** · You just get a choice.

**17:24** · Your friend's paying.

**17:25** · You're choosing between these three things.

**17:28** · The first component that we need to think about in this decision problem is, what are these preferences?

**17:32** · Remember, we said that we're studying decision makers who consistently maximize some of preference.

**17:37** · So we need to specify this agent's preferences.

**17:44** · And in this case, their preferences are going to specify some ordering among these three choices.

**17:50** · So a great way to represent this in this context would be C better than E better than T.

**17:57** · So these are probably my preferences.

**17:59** · What does this mean?

**18:00** · It means I prefer drinking coffee to drinking espresso.

**18:04** · I prefer drinking espresso to drinking tea.

**18:07** · And the way I've written this suggests transitivity, which you will assume that if I prefer coffee to espresso and espresso to tea, then I must also prefer coffee to tea.

**18:16** · I won't write that out explicitly, but that's implied by this.

**18:19** · And there's an implicit transitivity assumption that we're making.

**18:25** · But I think this actually raises kind of a difficult philosophical question.

**18:28** · What does it mean to prefer coffee to espresso?

**18:30** · What is a preference?

**18:32** · Philosophers talk about this.

**18:34** · Maybe people who study cognitive sciences go to the lab and they try to measure people's brain activity and say, oh, when you drink coffee, a different neuron activates.

**18:42** · Philosophers will get into these long debates about what it means to have a preference.

**18:46** · In economics, we take a much more operational view of preferences.

**18:50** · What does it mean?

**18:50** · And it's almost tautological.

**18:52** · What does it mean that I prefer coffee to espresso?

**18:55** · It means when I'm faced with a choice between coffee and espresso, I choose coffee.

**18:59** · That's all it means.

**18:59** · So this is the decision based view of preferences that's predominant in economics.

**19:04** · So let's say what is the meaning of this?

**19:12** · The meaning is that if I'm given a choice between coffee and espresso, I choose coffee.

**19:21** · I'm not going to be too precise here.

**19:22** · We might argue about strict preferences versus weak preferences.

**19:26** · And maybe we can be indifferent between things.

**19:28** · But for now, let's just think about strict preferences.

**19:31** · And preferences are a pairwise object, right?

**19:34** · So a preference says for any two things, which do I prefer between them?

**19:37** · So one way of thinking about what we mean by preferences is we're describing what an agent would choose from any pair or any menu containing two items.

**19:46** · And then from that primitive preference, we can talk about what they would choose in richer problems.

**19:52** · Now, an issue is that these little squiggly inequality signs are kind of messy to deal with.

**19:58** · So it often becomes more convenient in economics to use a utility representation of preferences.

**20:03** · So let me go to a new board for this.

**20:05** · And this didn't go all the way up.

**20:07** · Let's see.

**20:08** · There we go.

**20:12** · And I'll define the word ordinal in a second.

**20:14** · But I'm going to talk about an ordinal utility representation of preferences.

**20:31** · Why do we use this?

**20:32** · Well, it's just more convenient.

**20:34** · Especially when we have a lot of things, specifying all my pairwise preferences between these things can get kind of cumbersome.

**20:40** · So what we do is we just specify a function called a utility function.

**20:44** · So let's give just an example here.

**20:46** · So maybe my utility function is u of C equals 5, u of E equals 4, and u of T equals 1.

**20:59** · This should be one utility representation of these preferences.

**21:03** · Why do these utilities represent these preferences?

**21:06** · Well, do I prefer C to E?

**21:08** · Yes, because the utility assigned to C is higher than the utility assigned to E.

**21:13** · Do I prefer E to T?

**21:15** · Well, yes, because the utility assigned to E is strictly greater than the utility assigned to T.

**21:21** · And if we have a utility function like this, you can check that our induced preferences are going to satisfy transitivity as well.

**21:27** · Because if one number is bigger than another and that other number is bigger than a third number, then the first number is bigger than the third number.

**21:35** · But we have an issue here that this is only a representation.

**21:39** · So I can also write down an alternative utility function.

**21:41** · Maybe I'll call this u1.

**21:44** · Let me now write down a utility function u2 that's this.

**21:59** · What about these preferences?

**22:00** · Are these the same preferences or are these different preferences than the first utility function?

**22:06** · What do people think?

**22:07** · I don't think there's really one right answer.

**22:11** · AUDIENCE: In a marginal sense, it's the same.

**22:13** · IAN BALL: The same, right?

**22:14** · So it is true that if this were my utility representation, it still says I prefer C to E, I prefer E to T, and I prefer C to T. So this is an alternative representation of the same preferences.

**22:27** · And this is what we mean by an ordinal utility representation.

**22:31** · Only the order matters.

**22:34** · Let me say this.

**22:46** · And because only the order matters, that has a few implications.

**22:49** · The first is that there's many utility representations of the same preferences.

**22:58** · Many ordinal representations.

**23:12** · And a second I think more subtle point is that the units and the values in the utility function don't have meaning.

**23:27** · In fact, what are the units of utility functions?

**23:29** · They don't really have a unit that makes sense.

**23:31** · Sometimes we call the units utils.

**23:37** · But from a purely preference standpoint, you might look at this and you might say, oh, I like C more in this world than in this world.

**23:44** · But no, the way we think about ordinal representations is that what matters are your preferences.

**23:50** · And there's a convenient mathematical way to represent them like this.

**23:53** · And this is another convenient mathematical way to represent them.

**23:56** · And they represent the same preferences.

**23:58** · And there's no meaning associated with these utility functions in this ordinal world.

**24:02** · Yes.

**24:03** · AUDIENCE: Would you have to specify a null option, then?

**24:05** · Let's say if the utility is negative 100 for T, would you have to specify that they could also choose nothing?

**24:12** · IAN BALL: Great, that's a good point.

**24:14** · So when we write a choice problem, it's really crucial-- and it's implicit in what I did, but I didn't say it explicitly, so thanks for bringing this up-- that I can make only one choice, and every possible choice is included.

**24:25** · So if you have four options, if only three of them are included, that's not going to capture your preference problem-- your choice problem.

**24:31** · So really, if I were being careful, probably this is actually a more complicated problem.

**24:35** · And there's a third option, which is not drinking any drink.

**24:38** · And I should really specify the utility here.

**24:40** · So in this simple thing I'm imagining for some reason you have to make one of these three choices.

**24:44** · But you're right.

**24:45** · In general, when we model a choice problem, it's important to capture every possible choice the agent could make.

**24:50** · On the other side, indeed, if it's possible for me to choose both coffee and espresso, then that needs to be formally modeled as another choice, the bundle where I get coffee and espresso, because that's a separate choice that I can make.

**25:02** · Good point.

**25:04** · OK, so this is ordinal utility representations.

**25:06** · And now I'm going to move to the opposite, cardinal representations.

**25:10** · And everything I said here is going to go the other way.

**25:12** · So let's be really clear.

**25:14** · Everything I just said is going to be wrong in a different context.

**25:16** · So let's be very careful.

**25:18** · So this is ordinal.

**25:21** · The issue is that often in game theory, we face decisions under uncertainty.

**25:27** · And when we face decisions under uncertainty, we need to model preferences a bit differently.

**25:32** · So let's now move to decisions under uncertainty.

**25:41** · What is a decision under uncertainty mean?

**25:43** · It means when I make a choice, I don't know exactly what the consequence of that choice will be.

**25:49** · When I buy an index fund or buy a stock, I don't know whether that stock is going to go up or down.

**25:54** · I can't choose-- of course, if I could choose the stock that made more money, I would choose that one.

**25:58** · But that's not my choice.

**25:59** · I'm choosing one stock that has some distribution over outcomes that I don't know what the outcomes will be.

**26:04** · And then I might choose another stock.

**26:05** · And again, I don't know exactly what the outcome of that stock will be.

**26:08** · And that's what we mean by uncertainty.

**26:11** · So let's look at, again, a very, very simple problem, not economically interesting, but just to convey the ideas, which is the choice of how to get home.

**26:18** · Let's say you're choosing whether to walk home or to take the subway.

**26:21** · So you can either walk home or take the subway.

**26:27** · Maybe we'll call that and we'll call this W.

**26:29** · And again, here we're assuming you have to get home.

**26:31** · Maybe there's a third option where you stay at work all day.

**26:33** · But we're not going to model that.

**26:41** · And now why is this a decision under uncertainty?

**26:43** · Well, you don't know what the weather is going to be like.

**26:45** · You have a long walk home, so the weather could change as you walk home.

**26:48** · And we're going to assume there's two ways the world could be again.

**26:51** · Weather it's more complicated, but this is a simplification of reality.

**26:54** · It could be sunny or it could be rainy.

**26:58** · Maybe we should really model every possible temperature and every possible level of precipitation, but we're not going to do that.

**27:04** · And the way things work is when it's sunny, you'd rather walk home and when it's rainy, you'd rather take the subway.

**27:13** · So maybe I'll write this over here.

**27:15** · If sunny, you prefer-- and I think sometimes I call this the T to avoid the S.

**27:25** · Let's call this the T. Maybe TA, just so we don't see the two S's.

**27:33** · Sunny, you prefer to walk home.

**27:35** · And if rainy, you prefer to take the T.

**27:42** · So how would you approach this problem?

**27:43** · And this is a very simple problem, a simple choice people make all the time.

**27:48** · How would you approach this?

**27:53** · What do you do when you-- do you just randomly go home or do you think a little bit?

**28:00** · What's relevant?

**28:01** · What do you need to know to approach this problem?

**28:03** · Yeah.

**28:04** · AUDIENCE: You check the weather app.

**28:05** · IAN BALL: You check the weather app.

**28:07** · And what does that tell you?

**28:08** · AUDIENCE: If it's sunny or rainy.

**28:09** · IAN BALL: OK.

**28:10** · And it might tell you-- and really, it might give you some-- or do you want to go ahead?

**28:14** · Yeah.

**28:14** · AUDIENCE: It'd be how likely it is.

**28:15** · IAN BALL: Yeah.

**28:16** · It's going to tell you-- it might say sun or rain, but also it might give you a likelihood of sun or rain.

**28:19** · And oftentimes, you're not certain if it's going to be sunny or rainy.

**28:22** · You have some uncertainty.

**28:23** · That's the key thing that we're having here.

**28:25** · So this problem, if you knew the weather, would be very easy.

**28:28** · If you knew for certain it was going to be sunny, we know you'd walk home.

**28:31** · And if you knew for certain it was going to rain, you'd take the T.

**28:33** · The issue is that you have uncertainty.

**28:35** · And indeed, when you check the weather app, what you do is you form beliefs.

**28:38** · And this is going to be kind of a foundational idea in this course, that in the face of uncertainty, what do you do?

**28:53** · You form beliefs.

**28:57** · So in game theory, we take a fundamentally Bayesian view of the world.

**29:00** · When we have uncertainty, we say, well, we don't know whether it's going to be sunny or rainy.

**29:04** · But we might say something like, there's a 20% chance that it's sunny.

**29:08** · So we'll assign beliefs.

**29:09** · And in this case, let's represent our belief by the probability p that it's sunny.

**29:15** · And then correspondingly, we have the probability 1 minus p that it's raining.

**29:21** · So these are my beliefs.

**29:23** · OK?

**29:23** · And now I'm going to fill in some utilities here.

**29:27** · I'm going to say 7, 2, 5, 5.

**29:35** · So this is a representation of my preferences.

**29:38** · And indeed, when it's sunny, I prefer walking to taking the T.

**29:41** · And when it's rainy, I prefer taking the T to walking.

**29:46** · So now we've written things down.

**29:48** · Now I'd ask again.

**29:49** · Now we've specified our beliefs, which would you choose?

**29:52** · How would you approach this choice?

**29:55** · AUDIENCE: Find an expected utility.

**29:56** · IAN BALL: So in this course, we're going to assume expected utility.

**29:59** · But I want to point out that that's not so obvious.

**30:01** · One thing you might say you might say, look, I'm an optimistic person.

**30:06** · If I walk, the best thing that can happen is I get 7.

**30:10** · If I take the T, the best thing that can happen is I get 5.

**30:12** · 7 is higher than 5.

**30:14** · I'm going to walk.

**30:15** · I'm an optimistic person.

**30:16** · You might say, I'm a pessimistic person.

**30:18** · I'm really afraid of the worst-case outcome.

**30:21** · So when I walk, I could get 2.

**30:23** · When I take the T, the worst I can get is 5.

**30:25** · That's better, so I'm going to take the T.

**30:27** · I think the view in game theory is that optimism and pessimism are better reflected in your beliefs.

**30:33** · And we're generally going to assume in this course expected utility.

**30:42** · But I want to point out that this is an assumption.

**30:44** · There's an axiomatic foundation.

**30:46** · So decision theorists think a lot about the question, why should we use expected utility?

**30:51** · Or more concretely, if we assume that agents use expected utility, what assumption are we making?

**30:56** · What does that mean about their behavior when we assume expected utility?

**30:59** · How restrictive is that assumption?

**31:01** · And there's an appendix in the lecture notes that's posted online where you can look at this axiomatic approach to expected utility theory.

**31:07** · But in this course, we're just going to take it as given that people always use expected utility.

**31:12** · So what does that mean?

**31:13** · It's two steps.

**31:16** · First, they form beliefs.

**31:27** · Now, how reasonable is it to think that people form beliefs about the thing they're uncertain about?

**31:31** · Well, I think it depends on the context.

**31:33** · In this problem, I think it's very reasonable.

**31:35** · You open your weather app.

**31:36** · It gives you some probability of rain or sun.

**31:39** · You might think, oh, I don't really trust the weather app.

**31:40** · It always overestimates or underestimates.

**31:42** · You might adjust.

**31:42** · But you'll form your belief.

**31:44** · But if I said, form your belief about what is the probability that in 15 years your income will be between these two numbers.

**31:54** · That's pretty hard to form beliefs about.

**31:56** · So I think this assumption that you start by forming beliefs about what you don't know is a very realistic assumption in very simple problems.

**32:03** · But as we get to very, very rich problems and complicated problems, you might worry that this is not a very well-founded assumption.

**32:09** · When we get to complicated choices, maybe your choice about what job to take today depend on your belief about how likely it is that you have a grandchild in 40 years who's short on money and needs the money that you saved based on your job today.

**32:23** · Or let's go deeper.

**32:24** · What's the probability that in 10 generations, your 10th degree grandchild is going to be short on money?

**32:31** · Wow, that's really hard to form beliefs about.

**32:32** · So in that context, maybe this is an unrealistic assumption, but it's going to be the assumption we make in this class.

**32:37** · And we're going to apply this to models where we think it's a reasonable assumption.

**32:40** · And then the next thing that you do, given that you formed your beliefs, is you compute your expected utility from each choice.

**32:55** · But now we have a bit of an issue.

**32:57** · Because I set up here when I talked about ordinal utility representations that the numbers didn't matter.

**33:04** · But now all of a sudden, the numbers will matter.

**33:06** · Because when I compute the expectation, my expected utility from walking, if 7 were 700, that's going to change my expected utility.

**33:15** · So we have to really crucially understand that in this model, these utilities are different.

**33:20** · These are no longer ordinal utilities.

**33:23** · So in the decision making under uncertainty-- so in this context, utility is cardinal as opposed to ordinal.

**33:43** · Ordinal means only the order matters.

**33:46** · That's where the word ordinal comes from.

**33:48** · Cardinal means the size or the actual numbers matter.

**33:52** · And the way we distinguish this is we say that this utility function here is a Von Neumann-Morgenstern utility function.

**34:12** · And basically, throughout this course, we're going to focus on this case of uncertainty.

**34:17** · And essentially, all the utility functions we work with are going to be cardinal utility functions or Von Neumann utility functions rather than ordinal utility functions.

**34:26** · And just to understand the landscape, up here, we didn't make any expected utility assumptions.

**34:33** · This was a very abstract approach to any preference problem.

**34:36** · When we're in the world of uncertainty and we restrict attention to expected utility preferences, in that more restricted environment, we're always going to work with what are called Von Neumann-Morgenstern utility functions, where the numerical value actually matters.

**34:51** · So let's see how we would approach this problem in this VNM context.

**34:56** · So we have two choices.

**34:58** · We have walking and taking the T.

**35:03** · And what I'm generally going to use is this Von Neumann-Morgenstern utility function u.

**35:07** · This is a small u.

**35:11** · But then when I compute expected utilities, your expected utility is going to be a big U.

**35:15** · So I'm going to now compute here U of walking and U of taken the T. And this is a big U.

**35:22** · And of course with handwriting, it's not obvious what it is.

**35:25** · So if you're ever unsure, you can ask me.

**35:27** · But let's make sure we understand that these functions are defined for different objects.

**35:32** · My cardinal utility tells me what is my utility from walking when it's sunny?

**35:38** · What is my utility from walking when it's rainy?

**35:40** · And it gives me these four numbers.

**35:42** · My big U, my expected utility, isn't assigned to a weather-choice pair.

**35:49** · It's assigned just to the choice.

**35:52** · So for my big U, I can say, what is my expected utility from walking?

**35:57** · My little you tells me my utility from walking in each state of the world.

**36:01** · So let's just compute this.

**36:02** · It's going to be quite easy.

**36:04** · The math here is not the point.

**36:05** · It's about conceptually.

**36:07** · So if I walk, well, with probability p I get 7 and with probability 1 minus p I get 2.

**36:13** · So my expected utility is p times 7 plus 1 minus p times 2.

**36:21** · And if I take the T, well, it's p times 5 plus 1 minus p times 5.

**36:30** · Well, this is easy, right?

**36:31** · The expectation of this is just going to be 5.

**36:33** · It's 5 either way.

**36:35** · So this is 5.

**36:38** · And then here what do I get?

**36:41** · I get 2.

**36:42** · Minus 2p, so plus 5p.

**36:48** · So which do I prefer?

**36:50** · Well, it depends on p, right?

**36:52** · If p is really, really small-- if p gets close to 0, then this becomes 2.

**36:57** · And I prefer 5 to 2.

**36:59** · So I prefer taking the T.

**37:01** · That makes sense.

**37:02** · If I look outside and it looks really, really rainy, I'm going to take the T. If p is really, really high-- well, let's say p is 1.

**37:09** · I know it's going to be sunny.

**37:10** · Then if I walk, I get 7.

**37:13** · Yes, if I walk, I get 7.

**37:15** · If I take the T, I get 5.

**37:17** · 7 is more than 5.

**37:19** · So therefore, I prefer to walk.

**37:22** · When will I walk rather than take the T?

**37:24** · Well, I have to compare these two numbers.

**37:25** · So when is 2 plus 5p greater than or equal to 5?

**37:29** · Let's ask that question.

**37:37** · Well, it's if 5p is greater than or equal to 3.

**37:40** · So if p is greater than or equal to 3/5, right?

**37:46** · All right?

**37:46** · Yeah.

**37:48** · I'm sure someone will check the math.

**37:54** · Yeah.

**37:56** · AUDIENCE: Why is it greater than 3/5?

**37:59** · IAN BALL: Ah, good point.

**38:00** · So when p is exactly 3/5, I'm indifferent between the two.

**38:04** · So I need some word for that.

**38:05** · So I guess I would say I weakly prefer walking to taking the T if p is greater than or equal to 3/5.

**38:12** · And I strictly prefer walking to taking the T if p is strictly greater than 3/5.

**38:18** · AUDIENCE: But wouldn't that make sense that the equal part would be for the T, not for walking?

**38:25** · IAN BALL: Sorry, say it again.

**38:27** · AUDIENCE: So since it's greater or equal, when this happens, we walk, right?

**38:32** · IAN BALL: Exactly.

**38:33** · Yeah.

**38:33** · AUDIENCE: So why are we putting equal in walking?

**38:37** · Is there like-- do we say like when it's equal, it's indifferent?

**38:41** · Do we decide which one?

**38:43** · IAN BALL: You're right.

**38:44** · So there's a bit of ambiguity there.

**38:45** · So maybe I'll put-- if this makes it-- let's say this, yeah.

**38:48** · I would say, let's focus on the case where p is not 3/5.

**38:51** · Then it's pretty clear.

**38:52** · When p is exactly 3/5, you're right, we wouldn't have an inherent preference for walking over taking the T. In that case, we would be indifferent between walking and taking the T.

**39:00** · So maybe I'll make a note up here and sometimes use a squiggle for that.

**39:03** · So we might say W squiggle T, I'm indifferent between walking and taking the T, exactly if p equals 3/5.

**39:17** · And in this case, it's a strict preference.

**39:19** · So here what this says, which I think is an intuitive model of decision making, that I'm going to choose to walk home when I check my weather app and I think it's sufficiently likely that it's sunny.

**39:28** · How sufficiently likely?

**39:29** · Well, in this case, it's exactly 60% chance of sun that makes it worth it for me to walk home.

**39:35** · Now, where did we get this number from?

**39:37** · It depended on the numerical values over here.

**39:41** · If these numerical values were different, if I made this 700, well, then I'm basically always going to walk home unless I'm absolutely certain, basically, it's going to rain.

**39:49** · So that again shows us that the cardinal values of these utility functions are going to affect the decisions that we make.

**39:56** · Any other question on this?

**39:57** · Yeah.

**39:58** · AUDIENCE: So in the case when it's equal, is there-- like, now we use expected utility.

**40:03** · So you can see which expected utility is bigger.

**40:07** · But in the case it's equal, is there a rule we should follow?

**40:10** · Or based on the numbers we have in the grid-- IAN BALL: No, I would say the right way to think about preferences-- I was being a little loose over there to make it quicker.

**40:18** · But I'd say really, there's three possibilities when you compare two things.

**40:22** · You can strictly prefer one to the other.

**40:24** · You can strictly prefer the other to the first one.

**40:26** · Or you can be indifferent.

**40:27** · There's really three possibilities.

**40:29** · And when I compare my expected utilities, there's again three possibilities.

**40:32** · Either one is strictly higher, the other is strictly higher, or we're exactly indifferent.

**40:36** · And in general, when people are indifferent, it's harder to make predictions about what they'll do.

**40:40** · They might randomize.

**40:41** · They might choose one.

**40:42** · They might choose the other.

**40:43** · We're not going to really take a strong stance on what people do in that case.

**40:45** · Thanks for clarifying.

**40:46** · Yeah.

**40:47** · Any other questions?

**40:50** · All right.

**40:50** · So now let's be a bit more formal.

**40:52** · This was a very simple example, but let's formalize this a bit.

**40:57** · I guess I have one more board.

**41:07** · So maybe I'll say VNM.

**41:09** · This is Von Neumann-Morgenstern that I said before.

**41:11** · And I'll call this the VNM setting.

**41:17** · So generally, this is the approach we're going to take in this course.

**41:20** · We're going to start with a really simple example to motivate the theory.

**41:23** · We're then going to present a more general abstract model.

**41:25** · And then we're going to go back to more concrete and more interesting applications that are more substantive.

**41:30** · So that's the three steps we'll take.

**41:31** · So what's the setting here?

**41:32** · Well, there's going to be a set Z, which we'll say is the-- and I'll call this Z1 through Zm.

**41:41** · And this is the set of maybe outcomes or consequences.

**41:49** · And we have to be really careful about how we define outcomes and consequences.

**41:53** · So in this game that we described, there are actually four outcomes-- I walk home in the sun, I walk home in the rain, I take the T in the sun, and I take the T in the rain.

**42:03** · It's important to understand the outcome has to capture everything about my choice.

**42:07** · It's not directly my choice.

**42:08** · I'm not directly choosing outcomes.

**42:10** · I'm choosing effectively lotteries over outcomes.

**42:13** · And the outcome has to capture everything that's relevant in the situation.

**42:17** · So we have this set of outcomes or consequences.

**42:20** · And then we have the Von Neumann-Morgenstern utility function little u.

**42:26** · Now, just as we saw over here, little u assigned a number to each of our four outcomes.

**42:31** · So U is going to be a function from Z to R.

**42:36** · So I'm going to use this function notation a lot in the course.

**42:39** · When I put a letter and then a colon, that means this is a function that assigns to every item in this set, every object in this set, something in this set.

**42:49** · So in this case, it assigns to every outcome Z is-- I'll write it like this underneath-- what we'll call u of Z. And u of Z is the cardinal Von Neumann-Morgenstern utility I get from the outcome Z.

**43:04** · Now, given the set of outcomes and my Von Neumann-Morgenstern utility, we can consider my expected utility.

**43:14** · Let me write it this.

**43:20** · So my expected utility is the big U.

**43:22** · And what is this going to be defined over?

**43:24** · It's really crucial that this is defined over a different set.

**43:27** · So what do I assign expected utilities to?

**43:32** · Yeah.

**43:32** · AUDIENCE: Would it be a set of actions?

**43:34** · IAN BALL: So in this context, it was a set of actions.

**43:37** · But in this abstract model-- good question.

**43:39** · Yeah.

**43:40** · AUDIENCE: Like the state you're in.

**43:41** · IAN BALL: So I would say-- may be a bit of a vague question.

**43:44** · I would say the set of lotteries over outcomes.

**43:48** · So let's be clear.

**43:49** · Here, you're right, we were choosing actions.

**43:51** · We chose whether to walk or take the MBTA.

**43:53** · But the way we think about those actions in this abstract setting is that each one corresponds to a lottery.

**43:58** · Walking is the lottery where with probability p, I walk in the sun, and with probability 1 minus p, I walk in the rain.

**44:06** · And similarly, the MBTA is a different lottery where with probability p, I get this outcome, and with probability 1 minus p, I get this outcome.

**44:13** · So we need some notation for lotteries.

**44:15** · I'm going to use throughout the course delta of Z.

**44:19** · I don't want the notation to scare people.

**44:21** · It's just going to make it easier for us to talk about things.

**44:23** · So Z is our set of outcomes.

**44:25** · Delta of Z is the set of lotteries over these outcomes.

**44:29** · So in this context where we only had two outcomes, a lottery just specified two numbers, p and 1 minus p.

**44:37** · And because those numbers sum to 1, it was really only one number that mattered.

**44:41** · Once we knew p, we were able to calculate 1 minus p.

**44:44** · But in general, we're looking at a situation where there are m outcomes instead of just two.

**44:49** · So what is a lottery?

**44:53** · So it contains what I'll call lotteries.

**44:57** · And again, I should be clear the use of lottery colloquially is different from in econ.

**45:01** · We're not literally talking about buying lottery tickets.

**45:04** · We're using this more abstractly.

**45:05** · It's a vector p that specifies the probability of each of these outcomes.

**45:13** · So p1 to pm.

**45:16** · The lottery says with probability p1, you get consequence Z1.

**45:20** · With probability pm, you get consequence Zm.

**45:24** · These are probabilities.

**45:25** · So what has to be true about them?

**45:27** · They have to be non-negative.

**45:28** · You can't have negative probabilities.

**45:30** · And they have to sum to 1.

**45:33** · So say p1 up to pm are greater than or equal to 0.

**45:41** · And p1 plus pm equals 1.

**45:50** · So delta of Z is the set of all of these probability vectors or lotteries that satisfy these properties.

**45:58** · And now our expected utility function u is a function from delta Z to R.

**46:07** · It says, for any lottery, what is my expected utility from that lottery?

**46:12** · So again, using the notation above, we would call a lottery p, and that would go to u of p.

**46:19** · So this distinction is crucial, right?

**46:21** · A VNM utility says for each outcome, what is my utility from that outcome?

**46:26** · And expected utility big U says for each lottery over outcomes, what is my expected utility from that lottery?

**46:33** · Yes, question?

**46:34** · AUDIENCE: Just to clarify, when we say lotteries, that's what we're modeling your decision as is opting into a specific lottery.

**46:41** · IAN BALL: So in the face of uncertainty, we're going to imagine that each choice that you make is going to induce some lottery of outcomes.

**46:49** · And we're going to represent the choice by that lottery.

**46:52** · This is an important point, because it could be that-- yeah, there's an embedded assumption there.

**46:56** · But I'll just say yeah, that's what we're assuming.

**46:57** · Yes.

**46:58** · AUDIENCE: Can you just say what u would be in this case?

**47:01** · IAN BALL: Yes.

**47:01** · So let me write the definition and then I'll give you an example.

**47:03** · Exactly.

**47:04** · AUDIENCE: The little one.

**47:05** · IAN BALL: Yeah.

**47:06** · Yeah, exactly.

**47:07** · So let's first give the general definition.

**47:09** · Then I'll go to this example.

**47:10** · So u of p equals what?

**47:12** · Well, I'm just going to sum over all the possible outcomes.

**47:16** · There are m outcomes.

**47:18** · So I'm going to take-- and let me not use summation notation, because I think that makes it just seem harder than it is.

**47:22** · So let me write p1 u of Z1.

**47:34** · So I'm saying with probability p1, I get outcome Z1.

**47:38** · And this is my utility.

**47:39** · And I sum it all the way up until I get to pn.

**47:42** · This is the probability of outcome n.

**47:44** · And I get utility this.

**47:46** · So if we wanted to really formally write this in the example over here-- so in the example, walking corresponded to a particular lottery, right?

**47:59** · Now, if I really want to write out the example, I need to write out all four of these things.

**48:03** · So maybe I'll call these Z1, Z2, Z3, Z4.

**48:11** · OK?

**48:11** · These are the four consequences of my actions.

**48:14** · Now, what is walking here?

**48:17** · We need to specify four numbers-- p1, p2, p3, p4.

**48:23** · What are these four numbers in this example?

**48:26** · Well, if I walk, I either get this box with probability p or this box with probability 1 minus p.

**48:34** · So of these four numbers, two of them are 0.

**48:37** · p3 and p4 are both 0.

**48:44** · Why?

**48:44** · Because it's impossible for me to get one of those consequences.

**48:49** · If I choose to walk home, there's no way-- oh, I got unlucky.

**48:52** · I'm now on the T. We're not imagining that can happen.

**48:55** · What can happen is you can either walk home when it gets wet or you walk home and you don't.

**48:59** · So we have Z1 is going to be p.

**49:05** · 1 minus p here.

**49:07** · And if we compute it, what is u of this particular p going to be?

**49:14** · Well, we go through and we get pu of Z1 plus 1 minus pu of Z2 plus 0 plus 0.

**49:23** · I'm not going to include the last two terms because they disappear.

**49:27** · And this is going to be exactly what we said before, p times 7 plus 1 minus p times 2.

**49:38** · Which we already computed.

**49:39** · Any questions on that?

**49:43** · Yes.

**49:44** · AUDIENCE: So when we're actually getting the value that goes from p to a real number, there's already an implicit choice, like here implicitly we're walking and we're not calculating this particular T.

**49:55** · IAN BALL: Yeah.

**49:55** · So what I would say is in principle, you can evaluate-- and this is the key distinction between preferences and choices.

**50:02** · In principle, you could say, if I were offered a lottery between these outcomes, this lottery versus this lottery, what would I prefer?

**50:09** · Those are your preferences.

**50:10** · But in reality, you're given a limited menu of lotteries that you can actually choose from.

**50:14** · And you're going to make a choice between those lotteries.

**50:16** · So I could say in my head, what would I prefer between a stock that always pays a return of 1,000% and a stock that always pays a return of negative 1,000%?

**50:23** · I know which one I'd prefer.

**50:25** · And I can compute my preferences.

**50:26** · But there may not actually be a company listed on the stock market that is going to give me that lottery.

**50:30** · In reality, I'm going to face a limited choice set, a limited menu of options.

**50:34** · Each of those options will induce a lottery, and I'll make a choice among this smaller collection of lotteries.

**50:38** · In this case, that collection had two lotteries, the walking lottery and the taking the T lottery.

**50:43** · AUDIENCE: When you're calculating this function, you've already chosen a lottery.

**50:48** · Or you calculate this function based off of that.

**50:50** · IAN BALL: I would say it's a function, so it's defined for every single lottery.

**50:53** · I can say for every single lottery what my expected utility is, even for lotteries that I may not have the option to choose in a given situation.

**51:01** · Yes.

**51:02** · AUDIENCE: So even though p is determined on our beliefs, when it's a function of big U, do we just take it as exogenous and optimize based off of the things that we can control?

**51:12** · IAN BALL: Good question.

**51:13** · So this is going to be a big difference between individual decision making and interactive decision making.

**51:17** · In individual decision making, all of this uncertainty is just going to be exogenous.

**51:21** · And that's the model I've written down.

**51:23** · But we'll see when we get to interactive decision making, well, how do I form beliefs about the choices that other people make?

**51:28** · And then we're going to have to impose more structure on these beliefs.

**51:31** · But for the individual context, we think of them as exogenous.

**51:33** · Through introspection, you form your beliefs about what nature does, not what other players do.

**51:37** · Yep.

**51:38** · Thank you.

**51:39** · OK, so one final thing in the last five minutes.

**51:42** · There's a special case, which is of a lot of importance.

**51:46** · And I'll say the key special case is going to be what we call money lotteries.

**52:00** · So these are more like the lotteries that you hear about in reality.

**52:04** · And why do I call it a special case?

**52:06** · Well, it's the special case where Z, the set of outcomes, is just a set of monetary rewards.

**52:12** · So I'll say Z is equal to R. And this means the real number line.

**52:17** · Now, before I said Z was finite.

**52:19** · Here I'm going to be a little loose and allow Z to be infinite.

**52:22** · So the outcome here is I get $1, I get $10, I get a billion dollars.

**52:26** · These are all outcomes.

**52:27** · So what is the lottery?

**52:28** · Let's consider two lotteries.

**52:31** · One lottery maybe pays $10.

**52:55** · So let's now consider two lotteries.

**52:57** · Now here, with infinitely many things, it could be more complicated.

**53:00** · But I'm going to look at lotteries where there's a small number of things that could actually happen.

**53:05** · So under this lottery, there's only two outcomes that could happen.

**53:07** · Every other outcome has probability 0.

**53:10** · Under this lottery, with probability 0.99, I get $10.

**53:15** · And with probability 0.01, I get nothing.

**53:18** · I get 0.

**53:19** · With this lottery, I get $1,000 with probability 0.01 and I get 0 with probability 0.99.

**53:26** · So two different lotteries.

**53:27** · They fit within our framework.

**53:29** · And we can compute our expected utility of these lotteries.

**53:31** · How?

**53:32** · Well, to do that, we need our VNM utility function, which is a function, remember from Z to R. But in this case, Z is just R. But let's understand, this is money and this is utility.

**53:53** · So which of these lotteries would you prefer?

**53:56** · There's no right answer.

**53:57** · Again, preferences are not irrational.

**53:59** · But what's your preference between these?

**54:06** · Yeah.

**54:07** · AUDIENCE: I like the first one.

**54:08** · IAN BALL: You like the first one?

**54:09** · OK.

**54:09** · I think most people would.

**54:10** · And why is that?

**54:12** · AUDIENCE: Because I don't know, it seems like 1,000 divided by whatever seems to be about 10, and then it feels more certain because it's 0.99.

**54:25** · But I don't know.

**54:25** · IAN BALL: Right.

**54:26** · So that's a great way of thinking about it.

**54:27** · So the first thing you might say is let's compare the expected values of these lotteries.

**54:31** · The expected value of this is exactly $10.

**54:34** · 100th of 1,000 has expected value $10.

**54:37** · What's the expected value of this?

**54:39** · It's $9.90.

**54:42** · So this has a lower monetary expected value.

**54:45** · But despite it having a lower monetary expected value, it might have a higher expected utility.

**54:50** · And many people would choose this lottery over this lottery exactly because of what you said, it's safer.

**54:57** · So what's key is through our Von Neumann-Morgenstern utility function u, when we evaluate lotteries, we don't just compare the expected monetary amount of the lotteries, we compare the expected utility between the lotteries.

**55:11** · And what you're describing is what a lot of people feature in this context is, I'll say often, u is a concave function.

**55:23** · So if I were to draw u for a lot of people, their u is something like this.

**55:29** · And when u is concave, it means people are what we call risk averse.

**55:37** · So in this case, you exhibited risk aversion.

**55:40** · You preferred this lottery to this lottery, even though it had a smaller expected value.

**55:48** · And if we want to formally define what does risk aversion mean, a risk averse person is someone who always prefers a certainty at the expected value of a lottery to the lottery itself.

**56:03** · So let me just write this mathematically and then explain it.

**56:12** · Someone is risk averse if deciding between a lottery p-- let's take this as an example.

**56:17** · This is one lottery p.

**56:19** · And another lottery that pays the expected value of p with certainty.

**56:23** · In this case, that would be exactly $10.

**56:26** · Someone who's risk averse would always prefer getting $10 for sure to getting a lottery whose expected monetary amount was $10.

**56:34** · And mathematically, that's captured by the concavity of the utility function here, u.

**56:40** · For this to be a strict preference, we need p to be non-degenerate.

**56:43** · 1p would be you get something with probability 1.

**56:45** · So as long as it's non-degenerate, this is the meaning of risk aversion.

**56:49** · And this kind of answers a puzzle, I mean, going back to the 1700s where people said, why would you choose this lottery over this one?

**56:55** · This one has a higher expected value.

**56:57** · And the answer is, well, your utility function is not the same as money.

**57:01** · You don't maximize expected money, you maximize expected utility.

**57:04** · And some people's utilities can be concave like this.

**57:08** · So let me stop there and I will see everyone next week.