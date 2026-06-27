---
role: proof
locale: en
of_concept: well-ordering-of-ordinals
source_book: gtm053
source_chapter: "1"
source_section: "7"
---

**(a)** We must verify conditions (a), (b), and (c) of Section 4. The first of them follows immediately from the definition of an ordinal.

To prove the second condition, we consider two ordinals $\alpha$ and $\beta$. By Lemma 5, there exists an isomorphism $f$ of one of them, say $\alpha$, onto either $\beta$ or an initial segment of $\beta$. We show that then $\alpha = \beta$ or $\alpha \in \beta$. To do this, we prove that $f(\gamma) = \gamma$ for all $\gamma \in \alpha$. In fact, if $\gamma_1$ is the minimal element with $f(\gamma_1) \neq \gamma_1$, then $f(\gamma_2) = \gamma_2$ for all $\gamma_2 \in \gamma_1$. Since $f$ is an isomorphic embedding of $\alpha$ with respect to the ordering $\in$, and since $\gamma_1$ and $f(\gamma_1)$ are both the sets of their $\in$-predecessors, we must have $\gamma_1 = f(\gamma_1)$, a contradiction. Thus $f$ is the identity on $\alpha$. If the image of $f$ is $\beta$, then $\alpha = \beta$; if the image is an initial segment of $\beta$, then $\alpha \in \beta$.

**(b)** Any well-ordered set $X$ is isomorphic, by Lemma 5, to a unique ordinal $\alpha$ (if $X$ were isomorphic to two different ordinals, those ordinals would be comparable by $\in$, contradicting the trichotomy of Lemma 5). Similarly, $X$ is isomorphic to the set of ordinals $\{\gamma \in \mathrm{On} \mid \gamma < \alpha\}$, which is precisely the initial segment below $\alpha \cup \{\alpha\}$.
