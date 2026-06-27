---
role: proof
locale: en
of_concept: unique-representation-in-associated-graded
source_book: gtm004
source_chapter: "VIII. Spectral Sequences"
source_section: "2. Filtered Differential Objects"
---

# Proof of Unique Representation of Elements in the Associated Graded Object

**Statement.** Let $M$ be a module equipped with a filtration

$$\cdots \subseteq M^{(p-1)} \subseteq M^{(p)} \subseteq \cdots \subseteq M, \qquad -\infty < p < \infty,$$

satisfying the adequate filtration conditions

$$\text{(i)} \quad \bigcap_{p} M^{(p)} = 0, \qquad \text{(ii)} \quad \bigcup_{p} M^{(p)} = M. \tag{2.8}$$

Then every non-zero element $x \in M$ is represented by a unique homogeneous non-zero element in the associated graded object $Gr(M) = \bigoplus_p M^{(p)}/M^{(p-1)}$, and conversely, every homogeneous non-zero element of $Gr(M)$ represents a non-zero element of $M$.

**Proof.** Let $x \in M$, $x \neq 0$.

*Existence and uniqueness of the representing degree.* By condition (ii), there exists some integer $q$ such that $x \in M^{(q)}$. Let

$$p = \min\{\, r \in \mathbb{Z} \mid x \in M^{(r)} \,\}.$$

This minimum exists because the set of integers $r$ with $x \in M^{(r)}$ is non-empty (by condition (ii)) and is bounded below: if it were not bounded below, then $x \in M^{(r)}$ for arbitrarily small (i.e., arbitrarily negative) $r$. Since the filtration is increasing, $x \in M^{(r)}$ for arbitrarily small $r$ forces $x \in M^{(r)}$ for *all* $r$ (as $M^{(s)} \subseteq M^{(t)}$ when $s \leq t$). But then $x \in \bigcap_r M^{(r)} = 0$ by condition (i), contradicting $x \neq 0$. Hence the set is bounded below, and the minimum $p$ is well-defined.

By construction, $x \in M^{(p)}$ but $x \notin M^{(p-1)}$. Therefore the residue class

$$\bar{x} = x + M^{(p-1)} \in M^{(p)}/M^{(p-1)}$$

is non-zero. This homogeneous element of degree $p$ in $Gr(M)$ represents $x$.

*Uniqueness.* If $x$ were also represented by a homogeneous element of a different degree $q \neq p$, say $x \in M^{(q)}$ with non-zero image in $M^{(q)}/M^{(q-1)}$, then $x \notin M^{(q-1)}$ and $x \notin M^{(p-1)}$. Without loss of generality $p < q$. Since $x \in M^{(q)} \subseteq M^{(p)}$ (filtration is increasing), we have $x \in M^{(p)}$, but then $x \in M^{(q-1)}$ (since $p \leq q-1$), contradicting that the image in $M^{(q)}/M^{(q-1)}$ is non-zero. Hence the representing degree $p$ is unique.

*Converse.* If $\bar{y} \in M^{(p)}/M^{(p-1)}$ is a non-zero homogeneous element, then any lift $y \in M^{(p)}$ is non-zero in $M$ and satisfies $y \notin M^{(p-1)}$. By condition (i), $y \neq 0$ in $M$, and $\bar{y}$ is precisely the unique representing element of $y$ constructed above.

*Conclusion.* Under conditions (2.8), the correspondence $x \mapsto \bar{x}$ defines a bijection between non-zero elements of $M$ and non-zero homogeneous elements of $Gr(M)$. All that is lost in the passage from $M$ to $Gr(M)$ is the information about the module extensions — we cannot recover how $M^{(p-1)}$ is embedded in $M^{(p)}$ from $Gr(M)$ alone.
