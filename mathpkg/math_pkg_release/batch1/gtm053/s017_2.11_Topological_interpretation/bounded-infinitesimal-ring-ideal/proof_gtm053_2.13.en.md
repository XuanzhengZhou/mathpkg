---
role: proof
locale: en
of_concept: bounded-infinitesimal-ring-ideal
source_book: gtm053
source_chapter: "2"
source_section: "2.13"
---

Recall that $B = \{\gamma \in {^*\mathbf{R}} : [\gamma]^- \neq \varnothing \text{ and } [\gamma]^+ \neq \varnothing\}$ is the set of bounded elements, and $\mu = \{\alpha \in {^*\mathbf{R}} : \alpha = 0 \text{ or } \forall n \in \mathbb{N}_{>0},\, |\alpha| < 1/n\}$ is the set of infinitesimals.

**$B$ is a ring.** Let $\gamma_1, \gamma_2 \in B$, so there exist $p_1, p_2, q_1, q_2 \in \mathbb{Q}$ with $p_i < \gamma_i < q_i$. Then $p_1 + p_2 < \gamma_1 + \gamma_2 < q_1 + q_2$, so $\gamma_1 + \gamma_2 \in B$. Also $-q_1 < -\gamma_1 < -p_1$, so $-\gamma_1 \in B$. For multiplication, the bounds depend on signs, but since each $\gamma_i$ is bounded by rationals, their product is also bounded by products of rational bounds (taking absolute values and using $|\gamma_1\gamma_2| < \max(|p_1|,|q_1|) \cdot \max(|p_2|,|q_2|)$). Also $1 \in B$ and $0 \in B$. Thus $B$ is a subring of ${^*\mathbf{R}}$ containing $\mathbb{R}$.

**$\mu$ is an ideal of $B$.** First, $\mu \subseteq B$: for any $\alpha \in \mu$, we have $-1 < \alpha < 1$, so $\alpha \in B$. Let $\alpha, \beta \in \mu$. For any $n$, $|\alpha| < 1/(2n)$ and $|\beta| < 1/(2n)$, so $|\alpha + \beta| \leq |\alpha| + |\beta| < 1/n$. Thus $\alpha + \beta \in \mu$. Also $-\alpha \in \mu$ and $0 \in \mu$. So $\mu$ is an additive subgroup of $B$.

Let $\alpha \in \mu$ and $b \in B$. Since $b$ is bounded, there exists $q \in \mathbb{Q}$ with $|b| < q$. For any $n$, $|\alpha| < 1/(n \lceil q \rceil)$, so $|\alpha b| < q / (n \lceil q \rceil) \leq 1/n$. Thus $\alpha b \in \mu$. This shows $\mu$ absorbs multiplication by elements of $B$, hence $\mu$ is an ideal of $B$.

**$\mu$ is maximal.** Consider the quotient ring $B / \mu$. Every bounded element $\gamma \in B$ defines a Dedekind cut with both sides nonempty, which determines a unique standard real $r = \operatorname{st}(\gamma)$. The difference $\gamma - r$ is infinitesimal (as shown in the proof of the existence of infinitesimals), so $\gamma \equiv r \pmod{\mu}$. Thus the map $\mathbb{R} \to B / \mu$ given by $r \mapsto r + \mu$ is surjective. It is injective because if $r_1 \neq r_2$ are distinct standard reals, then $|r_1 - r_2|$ is a positive standard real, so $r_1 - r_2 \notin \mu$. Hence $B / \mu \cong \mathbb{R}$. Since $\mathbb{R}$ is a field, $\mu$ is a maximal ideal.
