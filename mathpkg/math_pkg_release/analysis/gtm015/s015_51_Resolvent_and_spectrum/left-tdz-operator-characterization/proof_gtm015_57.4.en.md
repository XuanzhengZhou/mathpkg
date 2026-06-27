---
role: proof
locale: en
of_concept: left-tdz-operator-characterization
source_book: gtm015
source_chapter: "57"
source_section: "57.4"
---

# Proof of Left topological divisors of zero in L(E)

(57.4) Theorem. Let $E$ be a normed space and let $T \in \mathcal{L}(E)$. The following conditions on $T$ are equivalent:

(a) $T$ is a left TDZ in $\mathcal{L}(E)$;

(b) there exists a sequence of vectors $x_n$ in $E$ such that $\|x_n\| = 1$ and $Tx_n \rightarrow \theta$;

(c) $T$ is not bounded below (40.28).

Proof. The equivalence of (b) and (c) is obvious from the definitions.

(b) implies (a): Let $x_n$ be a sequence of unit vectors such that $Tx_n \rightarrow \theta$, let $f \in E'$ with $\|f\| = 1$ (40.10), and, for each $n$, define $S_n \in \mathcal{L}(E)$ by the formula

$$S_n x = f(x)x_n \quad (x \in E).$$

Clearly $\|S_n\| = \|f\| \|x_n\| = 1$. Moreover,

$$TS_n x = f(x)Tx_n \quad (x \in E),$$

therefore $\|TS_n\| = \|f\| \|Tx_n\| \rightarrow 0$. Thus $T$ is a left TDZ in $\mathcal{L}(E)$.

(a) implies (b): Let $S_n$ be a sequence in $\mathcal{L}(E)$ such that $\|S
