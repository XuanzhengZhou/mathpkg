---
role: proof
locale: en
of_concept: quotient-banach-algebra
source_book: gtm015
source_chapter: "52"
source_section: "52.4"
---

# Proof of Quotient of a Banach algebra by a closed ideal

(52.4) Lemma. If $I$ is a closed, proper ideal of $A$, then $A/I$ is a Banach algebra with unity element $1+I$, $\|1+I\| = 1$. The canonical mapping $\pi: A \rightarrow A/I$ is continuous, with $\|\pi\| = 1$.

Proof. Suppose $u, v \in A/I$. If $x \in u$ and $y \in v$ then $xy \in uv$, therefore

$$\|uv\| \leq \|xy\| \leq \|x\| \|y\|;$$

varying $x$ and $y$, it results that $\|uv\| \leq \|u\| \|v\|$. Combining this with the preliminary remarks, we see that $A/I$ is a Banach algebra with unity element $\pi(1) = 1+I$.

The inequality $\|\pi(x)\| \leq \|x\|$ is immediate from $x \in \pi(x)$, thus $\pi
