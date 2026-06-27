---
role: proof
locale: en
of_concept: family-to-function-lemma
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Family of Sets to Real-Valued Function Lemma

**Lemma 2 (Family of Sets to Real-Valued Function).** Suppose that for each member $t$ of a dense subset $D$ of the positive reals $F_t$ is a subset of a set $X$ such that

(a) if $t < s$, then $F_t \subset F_s$; and
(b) $\bigcup \{F_t: t \in D\} = X$.

For $x$ in $X$ let $f(x) = \inf \{t: x \in F_t\}$. Then $\{x: f(x) < s\} = \bigcup \{F_t: t \in D \text{ and } t < s\}$ and $\{x: f(x) \leq s\} = \bigcap \{F_t: t \in D \text{ and } t > s\}$ for each real number $s$.

*Proof.* The calculation is direct. The set $\{x: f(x) < s\} = \{x: \inf \{t: x \in F_t\} < s\}$, and since the infimum is less than $s$ iff some member of $\{t: x \in F_t\}$ is less than $s$, the set $\{x: f(x) < s\}$ is the set of all $x$ such that for some $t$, $t < s$ and $x \in F_t$; that is, $\bigcup \{F_t: t \in D \text{ and } t < s\}$. This establishes the first equality.

To prove the second notice that $\inf \{t: x \in F_t\} \leq s$ if for each $u$ greater than $s$ there is $t < u$ such that $x \in F_t$. Conversely, if for each $t$ in $D$ such that $t > s$ it is true that $x \in F_t$, then $\inf \{t: x \in F_t\} \leq s$ because $D$ is dense in the set of positive numbers. Consequently the set $\{x: f(x) \leq s\} = \bigcap \{F_t: t \in D \text{ and } t > s\}$.

