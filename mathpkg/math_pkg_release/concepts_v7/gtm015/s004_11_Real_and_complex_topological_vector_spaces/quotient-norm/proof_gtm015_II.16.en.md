---
role: proof
locale: en
of_concept: quotient-norm
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "16. Normed spaces, Banach spaces"
---

# Proof of the Quotient Norm

**Theorem (16.7).** Let $E$ be a normed space and let $M$ be a closed linear subspace of $E$. For $u \in E/M$ define

$$\|u\| = \inf \{ \|x\| : x \in u \}.$$

Then $\|u\|$ is a norm on $E/M$, and the norm topology on $E/M$ coincides with the quotient topology.

*Proof.* **Norm properties:**
- $\|\theta\| = \inf \{\|x\| : x \in M\} = 0$ since $\theta \in M$, and $\|\theta\| = 0$.
- If $\|u\| = 0$, then there exist $x_n \in u$ with $\|x_n\| \to 0$, so $x_n \to \theta$. Since $M$ is closed, $u = M = \theta_{E/M}$, establishing positive definiteness.
- Absolute homogeneity: $\|\lambda u\| = \inf\{\|\lambda x\| : x \in u\} = |\lambda| \inf\{\|x\| : x \in u\} = |\lambda| \|u\|$.
- Triangle inequality: For $u, v \in E/M$ and any $x \in u$, $y \in v$,

$$\|u + v\| \leq \|x + y\| \leq \|x\| + \|y\|.$$

Taking $\inf$ over $x \in u$, $y \in v$ yields $\|u + v\| \leq \|u\| + \|v\|$.

**Topology:** The quotient map $\pi: E \to E/M$ satisfies $\|\pi(x)\| \leq \|x\|$, so it is continuous. By definition of the quotient topology, a set is open in $E/M$ iff its preimage under $\pi$ is open in $E$. The norm-open balls in $E/M$ have preimages that are open (as unions of translates of $M$ with open balls in $E$), and conversely, any quotient-open set is norm-open because for any $u$ with $\|u\| < r$, one can find $x \in u$ with $\|x\| < r$. Thus the topologies coincide. $\square$
