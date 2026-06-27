---
role: proof
locale: en
of_concept: "schrder-bernstein-if-and-are-cardinal-numbers-such-that"
source_book: gtm025
source_chapter: "Unknown Chapter"
source_section: "4.7"
---

Let $U$ and $V$ be sets such that $\bar{U} = u$ and $\bar{V} = v$. By hypothesis there exist one-to-one functions $f$ and $g$ such that $domf = U$, $rngf \subset V$, $domg = V$, and $rngg \subset U$. Define a function $\varphi$ on $\mathcal{P}(U)$ into $\mathcal{P}(U)$ by the following rule:

$$\varphi(E) = U \cap \left[ g(V \cap (f(E))') \right]'.$$

(1)

It is easy to see that

$$E \subset F \subset U \text{ implies } \varphi(E) \subset \varphi(F).$$

(2)

Define $\mathcal{D} = \{E \in \mathcal{P}(U) : E \subset \varphi(E)\}$. Notice that $\varnothing \in \mathcal{D

Proof. Let $U$ and $V$ be sets such that $\bar{U} = u$ and $\bar{V} = v$. Let $\mathfrak{F}$ denote the family of all one-to-one functions $f$ such that $domf \subset U$ and $rngf \subset V$. It is easily seen that $\mathfrak{F}$ is a family of finite character so, by Tukey's lemma (3.8), $\mathfrak{F}$ contains a maximal member $h$. We assert that either $domh = U$ or $rngh = V$. Assume that this is false. Then there exist $x \in U \cap (domh)'$ and $y \in V \cap (rngh)'.$ But then $h \cup \{(x,y)\} \in \mathfrak{F}$, contradicting the maximality of $h$. Thus our assertion is true. If $domh = U$, then $h$ shows that $u \leq v$. If $rngh = V$, then $h^{-1}$ shows that $v \leq u$.
