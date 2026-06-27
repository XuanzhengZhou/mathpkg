---
role: proof
locale: en
of_concept: let-z-be-such-that
source_book: gtm001
source_chapter: "17"
source_section: ""
---

OF LEMMA 17.23** (cf($\kappa$) = $\omega$ case). We want to show that there exists $Z$, an elementary submodel of $L_\kappa$, such that

(1) $X \subseteq Z, \bar{Z} = \bar{X}$; and

(2) If $\Pi \subseteq Z$ is a $Z$-well-founded $\kappa$-direct limit system, then $\Pi$ is well

Let $Z = \bigcup_{\alpha < \aleph_1} Z_\alpha$. Then $Z \prec L_\kappa$, $X \subseteq Z$ and $\overline{Z} = \overline{X}$. We want to show that $(2')$ holds for this $Z$. Let $\Pi \subseteq Z$ be a countable $Z$-well-founded $\kappa$-direct limit system. Then $\Pi \subseteq Z_\alpha$ for some $\alpha < \aleph_1$. If $\Pi$ were not well founded, then $\Pi$ would not be $Z_{\alpha+1}$-well-founded, and hence not $Z$-well-founded. This is a contradiction. Thus the lemma has been proved in the case where $\text{cf}(\kappa) = \omega$.

From now on, we assume that $\text{cf}(\kappa) > \omega$. From (3) of Lemma 17.22, we see that $X$ is unbounded in $\kappa$. We may assume that $X$ is closed in $\kappa$, (if necessary, consider the closure of $X$ in place of $X$).

EXERCISE

We denote the closure of $X$ by $C(X)$. Prove $\overline{X} = \overline{C(X)}$.

Let $S = \{\lambda \in X | \text{cf}(\lambda) = \omega\}$.
