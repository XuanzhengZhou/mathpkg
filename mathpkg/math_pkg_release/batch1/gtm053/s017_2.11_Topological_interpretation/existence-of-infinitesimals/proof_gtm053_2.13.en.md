---
role: proof
locale: en
of_concept: existence-of-infinitesimals
source_book: gtm053
source_chapter: "2"
source_section: "2.13"
---

Let ${^*\mathbf{R}}$ be a nonstandard model of the reals. Since ${^*\mathbf{R}}$ is not isomorphic to $\mathbb{R}$, there exists an element $\gamma \in {^*\mathbf{R}}$ that is not equal to the interpretation of any standard real $r \in \mathbb{R}$.

Define the Dedekind cut of $\gamma$:
$$[\gamma]^- = \{q \in \mathbb{Q} : q \leq \gamma\}, \qquad [\gamma]^+ = \{q \in \mathbb{Q} : q > \gamma\},$$
where we identify each rational $q$ with its image under the unique embedding $\mathbb{Q} \hookrightarrow {^*\mathbf{R}}$.

**Case 1:** $[\gamma]^- = \varnothing$. Then $\gamma < q$ for every $q \in \mathbb{Q}$. In particular, $\gamma < 0$, so $-\gamma > 0$ and $-\gamma > q$ for all $q \in \mathbb{Q}$ (since $\gamma < -q$ for all $q > 0$). Set $\alpha = -\gamma^{-1}$. Then $\alpha > 0$. For any positive integer $n$, we have $1/n \in \mathbb{Q}$ and $-\gamma > 1/(1/n) = n$, so $\gamma^{-1} > -1/n$, giving $\alpha = -\gamma^{-1} < 1/n$. Thus $0 < \alpha < 1/n$ for all $n$.

**Case 2:** $[\gamma]^+ = \varnothing$. Then $\gamma \geq q$ for every $q \in \mathbb{Q}$ (in fact $\gamma > q$ for all $q$). Set $\alpha = \gamma^{-1}$. Then $\alpha > 0$, and for any $n$, $\gamma > n$, so $\alpha = \gamma^{-1} < 1/n$. Hence $0 < \alpha < 1/n$.

**Case 3:** Both $[\gamma]^-$ and $[\gamma]^+$ are nonempty. The pair $([\gamma]^-, [\gamma]^+)$ is a Dedekind cut of $\mathbb{Q}$ in the standard sense, and therefore determines a unique standard real number $r \in \mathbb{R}$. By construction, $r = \sup [\gamma]^- = \inf [\gamma]^+$.

Since $\gamma \neq r$ (as $\gamma$ is not standard), we have either $r < \gamma$ or $r > \gamma$.

- If $r < \gamma$, set $\alpha = \gamma - r > 0$. For any $\varepsilon > 0$ standard, $r + \varepsilon \in \mathbb{Q}$ falls into $[\gamma]^+$ (by definition of the infimum), so $r + \varepsilon > \gamma$, giving $\alpha = \gamma - r < \varepsilon$. Taking $\varepsilon = 1/n$ yields $0 < \alpha < 1/n$ for all $n$.

- If $r > \gamma$, set $\alpha = r - \gamma > 0$. By a symmetric argument, for any $\varepsilon > 0$, $r - \varepsilon < \gamma$, so $\alpha = r - \gamma < \varepsilon$. Again $0 < \alpha < 1/n$ for all $n$.

In all cases, we have constructed $\alpha$ satisfying $0 < \alpha < 1/n$ for every positive integer $n$.
