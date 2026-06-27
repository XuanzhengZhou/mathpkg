---
role: proof
locale: en
of_concept: submartingale-closure-theorem
source_book: gtm046
source_chapter: "IX"
source_section: "32.3"
---

Let $Y \in L_r$ close $\{X_n\}$. Set $B_n = [|X_n| > c]$ so that $B = [\sup |X_n| > c] = \bigcup B_n$. Since $c^r PB \leq \int_B |Y|^r \leq E|Y|^r < \infty$ and $\int_B |X_n|^r \leq \int_B |Y|^r$, it follows that as $c \to \infty$, $PB \to 0$ and the $|X_n|^r$ are uniformly integrable. By the $L_r$-convergence theorem, $X_n \xrightarrow{r} X$.

Conversely, if the $|X_n|^r$ are uniformly integrable for some $r \geq 1$, then $E|X_n| \leq E^{1/r}|X_n|^r$ are uniformly bounded. Therefore $X_n \xrightarrow{\text{a.s.}} X$ and $X_n \xrightarrow{r} X$.

For the nearest property: letting $m \to \infty$ in the closing inequality $\int_{B_n} X_{n+m} \leq \int_{B_n} Y$ gives $\int_{B_n} X \leq \int_{B_n} Y$ on every $\mathcal{B}_n$. By the extension theorem, this holds on the generated $\sigma$-field $\mathcal{B}$, so $X \leq E^{\mathcal{B}} Y$ a.s. and $X$ is the nearest closing random variable.
