---
role: proof
locale: en
of_concept: submartingale-closure-theorem
source_book: gtm046
source_chapter: "IX-X"
source_section: "31-32"
---

1\textdegree\ Let $Y \in L_r$ close $\{X_n\}$. Set $B_n = [|X_n| > c]$ so that $B = [\sup |X_n| > c] = \bigcup B_n$. Since $c^r PB \leq \int_B |Y|^r \leq E|Y|^r < \infty$ and $\int_B |X_n|^r \leq \int_B |Y|^r$, it follows that, as $c \to \infty$, $PB \to 0$, and by letting $m \to \infty$, $\int_{B_n} X_n \leq \int_{B_n} X = \int_{B_n} E^{\mathcal{B}_n} X$. Therefore, $X_n \leq E^{\mathcal{B}_n} X$ a.s., that is, the submartingale sequence is closed on the right by $X$. If a r.v. $Y$ also closes the sequence on the right, then by letting $m \to \infty$, $\int_{B_n} X \leq \int_{B_n} Y$. Therefore, on every $\mathcal{B}_n$ and hence on $\bigcup \mathcal{B}_n$, the indefinite integral of $Y - X$ determines a $\sigma$-finite measure on $\mathcal{B}$. Thus, $X \leq E^{\mathcal{B}} Y$ a.s. and hence the submartingale $X_1, X_2, \cdots, X$ is closed on the right by $Y$; that is, $X$ is the "nearest" of the closing r.v.'s.
