---
role: proof
locale: en
of_concept: normal-cone-characterization
source_book: gtm036
source_chapter: "23"
source_section: "23.1"
---

If $C$ is normal, there is a constant $k$ (the reciprocal of the constant $e$ of the definition) such that, if $x$ and $y$ are positive and $\|x + y\| < 1$, then either $\|x\|$ or $\|y\|$ is less than $k$. If $z$ is a member of $(S + C) \cap (S - C)$, then $z = u + x = v - y$ for some $x$ and $y$ in $C$ and $u$ and $v$ in $S$. Then $\|(x + y)/2\| \leq 1$, and hence either $\|x/2\| < k$ or $\|y/2\| < k$. [The remainder of the proof is missing from the source text due to OCR gaps.]

Conversely, suppose $(S + C) \cap (S - C)$ is bounded. If $\{y: -x \leq y \leq x\}$ is bounded for some $x$, then there exists $r > 0$ such that $x + rS + C \subset C$. Hence $\{y: -x \leq y \leq x\} = (-x + C) \cap (x - C) \supset (rS + C) \cap (-rS - C)$. If $\{y: -x \leq y \leq x\}$ is bounded, then $(rS + C) \cap (-rS - C)$ is bounded, which implies $(S + C) \cap (S - C)$ is bounded by scaling.
