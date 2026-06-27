---
role: proof
locale: en
of_concept: support-of-distribution-defined-by-function
source_book: gtm012
source_chapter: "4"
source_section: "§4. Characterization of distributions of type L'"
---

# Proof of Support of a distribution defined by a function

**Proposition (Exercise 5).** Let $F \in \mathcal{L}'$ be a distribution defined by a locally integrable function $f: \mathbb{R} \to \mathbb{C}$ satisfying the conditions (3) and (4) of §3, i.e.,

$$F(u) = F_f(u) = \int_{-\infty}^{\infty} f(t) u(t) \, dt, \quad u \in \mathcal{L}.$$

Then

$$\operatorname{supp}(F) = \operatorname{supp}(f).$$

*Proof.* Recall the definitions. The support of a function $f$ is

$$\operatorname{supp}(f) = \overline{\{t \in \mathbb{R} : f(t) \neq 0\}}.$$

The support of a distribution $F \in \mathcal{L}'$ is the complement of the largest open set on which $F$ vanishes: we say $F$ vanishes on an open set $U \subset \mathbb{R}$ if $F(u) = 0$ for every $u \in \mathcal{L}$ with $\operatorname{supp}(u) \subset U$. Then $\operatorname{supp}(F)$ is the complement of the union of all such open sets.

**Step 1: $\operatorname{supp}(F) \subset \operatorname{supp}(f)$.**

Let $x \notin \operatorname{supp}(f)$. Then there exists an open neighborhood $U$ of $x$ such that $f(t) = 0$ for all $t \in U$. For any test function $u \in \mathcal{L}$ with $\operatorname{supp}(u) \subset U$, we have

$$F(u) = \int_{-\infty}^{\infty} f(t) u(t) \, dt = \int_U f(t) u(t) \, dt = 0,$$

since $f \equiv 0$ on $U$. Thus $F$ vanishes on $U$, which implies $x \notin \operatorname{supp}(F)$. Taking complements yields $\operatorname{supp}(F) \subset \operatorname{supp}(f)$.

**Step 2: $\operatorname{supp}(f) \subset \operatorname{supp}(F)$.**

We prove the contrapositive. Suppose $x \notin \operatorname{supp}(F)$. Then there exists an open neighborhood $U$ of $x$ such that $F(u) = 0$ for all $u \in \mathcal{L}$ with $\operatorname{supp}(u) \subset U$. This means

$$\int_U f(t) u(t) \, dt = 0 \quad \text{for all } u \in \mathcal{L} \text{ with } \operatorname{supp}(u) \subset U.$$

By a standard lemma (the fundamental lemma of the calculus of variations for the space $\mathcal{L}$), this implies that $f(t) = 0$ for almost every $t \in U$. Since the function $f$ is continuous (as a consequence of conditions (3)-(4) of §3 — they imply $f$ is continuous on the complement of a discrete set), we actually have $f(t) = 0$ for all $t \in U$. Hence $x \notin \operatorname{supp}(f)$. Taking complements gives $\operatorname{supp}(f) \subset \operatorname{supp}(F)$.

**Step 3: Conclusion.**

From Steps 1 and 2 we obtain $\operatorname{supp}(F) = \operatorname{supp}(f)$. $\square$
