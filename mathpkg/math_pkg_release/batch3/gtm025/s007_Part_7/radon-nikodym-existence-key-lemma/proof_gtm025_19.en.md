---
role: proof
locale: en
of_concept: radon-nikodym-existence-key-lemma
source_book: gtm025
source_chapter: ""
source_section: "19"
---

Define $L(f) = \int_X f d\nu$ on $\mathfrak{L}_2(\mu+\nu)$. By Holder, $|L(f)| \leq \|f\|_2 \cdot (\mu(X)+\nu(X))^{1/2}$, so $L$ is bounded. By Riesz representation, there exists $h \in \mathfrak{L}_2(\mu+\nu)$ with $L(f) = \int f \bar{h} d(\mu+\nu)$. One shows $h$ is real and $0 \leq h \leq 1$ $(\mu+\nu)$-a.e. The identity $\int f(1-h) d\nu = \int f h d\mu$ follows from the definition of $L$.
