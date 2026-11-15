---
layout: page
permalink: /interests/
title: interests
description: Some themes that appear across my work. Contact me if you want to chat more about any of them!
nav: true
nav_order: 3
---

{% capture text %}
Voting rules are usually designed by hand and then analyzed to see which axioms they satisfy. Much of my work turns this around: choose which properties matter then search for, or learn rules that have these properties.

In [What Voting Rules Actually Do](/publications/#Caiata_Armstrong_Larson-Arxiv-2025) (AAAI 2026) we measure how often multi-winner voting rules violate axioms and show that learned rules result in far fewer violations. [DeepVoting](/publications/#Matone_Deepvote_2026) (NeurIPS 2026) shows that by formulating rule output as a lottery we can train novel rules that replicate the behaviour of existing rules while largely not violating axioms that the original rule does violate. On the theory side, [Optimal Voting](/publications/#Armstrong_Optimal_Voting_preprint) finds the positional scoring rules which maximize social welfare across the power mean family; in some cases these rules look very different than known scoring rules.

**Future:** I am interested in understanding what data is needed to learn voting rules: Can we find embeddings which allow efficiently learning to replicate voting rules? Can we generate a single model which learns something general about preference aggregation and can perform many different social choice functions?
{% endcapture %}
{% include interest_section.liquid
  title="Optimizing Social Choice Functions"
  image="assets/img/interests/input_features.png"
  alt="Features and size of common input features when learning social choice functions."
  caption="Features and size of common input features when learning social choice functions."
  side="left"
  text=text
%}

{% capture text %}
Ideas from social choice impact many aspects of our world beyond just political elections. I am particularly interested in settings where learned mechanisms can safely improve on existing systems, and metrics that capture novel behaviours.

**Recommender systems.** Envy-freeness, has been used to measure fairness in recommender systems. Bossiness describes whether one agent can influence decisions made for other users. In our position paper [Envy-Free but Still Unfair](/publications/#aird2025envy) and in upcoming work up we show that these metrics provide intuitive and reliable measures of fairness in recommender systems when used appropriately.

**Peer review.** [Micro reviews](/publications/#Armstrong_Micro_Review_preprint) are an alternative to traditional bidding in which each reviewer's reaction to an abstract serves as a weak estimate of paper quality, drawing on the Condorcet Jury Theorem. We develop [rule-picking rules](/publications/#Berker_Armstrong_Conitzer_Shah-Arxiv-2025) (ICLR 2026) which show learned ranking rules provide more consistency than traditional methods in settings such as peer review.

**Future:** Recommender systems can use *reranking* agents, with preferences aggregated by social choice, to provide fairness guarantees. We can replace existing aggregation methods with learned mechanisms. Micro reviews present an opportunity to blend human taste with LLM review -- maintaining human control while improving peer review quality.


{% endcapture %}
{% include interest_section.liquid
  title="Applications of Social Choice"
  image="assets/img/interests/ef_bossiness_example.png"
  alt="Envy and bossiness among agents in a recommender system. (unpublished preprint)"
  caption="Envy and bossiness among agents in a recommender system. (unpublished preprint)"
  side="right"
  text=text
%}

{% capture text %}


My interest in AI and collective decision-making began with questions about how AI affects society. In 2019 I contributed to work on how [AI could drive societal transfomation](/publications/#Parson_Lempert_Armstrong_Crothers_DeChant_Novelli_2019), [design principles for an AI policy analyst](/publications/#Armstrong_Beretta_Crothers_Karlin_Kim_Longo_Powell_Sanders), and how [machine learning might strengthen democracy](/publications/#Armstrong_Larson_2019). More recently, our [AIES 2025 paper](/publications/#AIES-2025) studies the political and demographic biases exhibited by large language models, using Moral Foundations Theory to ground results in comparison with human data.

I have also spent several years contributing to the [teaching](/teaching/) of ethical and legal issues in AI. This primarily involved leading seminar style discussions around the social implications of computing, discrimination in computing, and broad ethical issues at both the undergraduate and graduate level.

**Future:** I look forward to teaching more ethics courses (or [teaching ethics in other CS courses](https://arxiv.org/abs/1808.05686)). I am interested in applying social choice ideas to provide reliable and fair aggregation of output from agents in swarms.
{% endcapture %}
{% include interest_section.liquid
  title="AI Safety and Ethics"
  image="assets/img/interests/moral_radar_persona.png"
  alt="Comparison of LLMs prompted to act liberal vs conservative. (AIES 2025)"
  caption="Comparison of LLMs prompted to act liberal vs conservative. (AIES 2025)"
  side="left"
  text=text
%}

{% capture text %}
I enjoy building spaces where researchers from different communities can meet. In 2024 I started the Workshop on Social Choice and Learning Algorithms (SCaLA) to bring together researchers in machine learning and computational social choice, and have run it for three years: at [AAMAS 2024](https://sites.google.com/view/scala24/), [IJCAI 2025](https://sites.google.com/view/scala25/), and [IJCAI 2026](https://sites.google.com/view/scala26/home).

I am also an organizer of the [Games, Agents, and Incentives Workshop](https://gtep-workshops.github.io/gaiw2026/) (GAIW) in 2026 and 2027. In 2026 I ran a trial of [micro reviews] and found that the process provides real benefit during the full review period; we plan to repeat this experiment in 2027. At GAIW we have used micro reviews as part of the reviewing process, which lets us try out new ideas about peer review with a real community of authors and reviewers.

**Future:** I plan to continue organizing these venues and encouraging scientific community. I aim to continue experimenting with novel forms of peer review to better understand how peer review can survive in the age of LLMs.
{% endcapture %}
{% include interest_section.liquid
  title="Building Scientific Community"
  image="assets/img/interests/scala25.jpg"
  alt="Participants at the SCaLA workshop in 2025."
  caption="Participants at the SCaLA workshop in 2025."
  side="right"
  text=text
%}
