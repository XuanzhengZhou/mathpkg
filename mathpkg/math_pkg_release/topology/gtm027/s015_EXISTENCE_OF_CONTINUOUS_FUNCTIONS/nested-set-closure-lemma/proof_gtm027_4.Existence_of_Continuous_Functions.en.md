---
role: proof
locale: en
of_concept: nested-set-closure-lemma
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Nested Set Closure Lemma

Assume the hypotheses of Lemma 2 and suppose additionally that each $F_t$ is open and $F_t^{-} \subset F_s$ whenever $t < s$. Then for each real $s$, the set $\{x: f(x) < s\}$ is open and $\{x: f(x) \leq s\}$ is closed.

In view of the previous lemma, $\{x: f(x) < s\} = \bigcup \{F_t: t \in D \text{ and } t < s\}$, which is the union of open sets $F_t$ and is therefore open.

With reference again to the previous lemma, $\{x: f(x) \leq s\} = \bigcap \{F_t: t \in D \text{ and } t > s\}$, and the proof will be complete if we show this set is identical with $\bigcap \{F_t^{-}: t \in D \text{ and } t > s\}$. Since $F_t \subset F_t^{-}$ for each $t$, surely

$$\bigcap \{F_t: t \in D \text{ and } t > s\} \subset \bigcap \{F_t^{-}: t \in D \text{ and } t > s\}.$$

On the other hand, for each $t$ in $D$ with $t > s$ there is $r$ in $D$ such that $s < r < t$, and hence such that $F_r^{-} \subset F_t$. Consequently

$$\bigcap \{F_t^{-}: t \in D \text{ and } t > s\} \subset \bigcap \{F_t: t \in D \text{ and } t > s\}.$$

The reverse inclusion follows. Thus $\{x: f(x) \leq s\}$ is an intersection of closed sets and is therefore closed.
