---
role: proof
locale: en
of_concept: "let-be-a-locally-compact-hausdorff-space-and-4"
source_book: gtm025
source_chapter: "Integration Theory Continued"
source_section: "20.47"
---

Let $I$ be constructed from $L$ as in (20.46). By F. Riesz's representation theorem (12.36), there exists a measure $\iota$ on $X$ as in §9 such that

$$I(f) = \int_X f d\iota$$

for all $f \in \mathfrak{C}_{00}(X)$. It follows that

$$\iota(X) = \bar{I}(1) = \sup\{I(f) : f \in \mathfrak{C}_{00}^+, f \leq 1\}$$

$$\leq \sup\{|I(f)| : f \in \mathfrak{C}_0, \|f\|_u \leq 1\}$$

$$= \|I\| = \|L\|.$$

Thus $\iota$ is a finite measure. We know (13.21) that $\mathfrak{C}_{00}$ is a dense linear subspace of $\mathfrak{L}_1(X, \mathcal{M}_i, \iota)$. It follows from (20.46.i) that, relative to the $\mathfrak{L}_1$ norm, $L$ is a bounded linear functional of norm $\leq 1$ on

in the $\mathfrak{L}_1(X, \mathcal{M}_i, \iota)$-norm on $\mathfrak{C}_0$ and agree on the $\mathfrak{L}_1$-dense subspace $\mathfrak{C}_{00}$. All that remains is to show that $\mu$ is regular. Let $E \in \mathcal{M}_i$ and $\varepsilon > 0$ be given. Since $\iota$ is regular and finite, there exist a compact set $F$ and an open set $U$ such that $F \subset E \subset U$ and $\iota(U \cap F') < \varepsilon$. Thus if $A \in \mathcal{M}_i$ and $A \subset U \cap F'$, then

$$|\mu(A)| = \left| \int_A \bar{g} d\iota \right| \leq \iota(A) \leq \iota(U \cap F') < \varepsilon.$$

Hence $\mu \in M(X)$ and the proof is complete. $\square$

(20.48) Riesz Representation Theorem. Let $X$ be a locally compact Hausdorff space. Then the mapping $T$ defined by

$$T(\mu) = L_\mu$$

[see (20.45)] is a norm-preserving linear mapping of $M(X)$ onto $\mathfrak{C}_0(X)^*$. Thus $M(X)$ is a Banach space, and $M(X)$ and $\mathfrak{C}_0(X)^*$ are isomorphic as Banach spaces.

Proof. The fact that $T$ is a norm-preserving mapping from $M$ into $\mathfrak{C}_0^*$ is (20.45). It follows from (20.47) that $T$ is onto $\mathfrak{C}_0^*$. It is trivial that $T$ is linear. Since $T$ is both linear and norm-preserving, $T$ is one-to-one and preserves Cauchy sequences. Thus, since $\mathfrak{C}_0^*$ is complete, so is $M$. $\square$

(20.49) Exercise. Let $X$ be a

(d) If $v \in M(X)$ and $v = v_1 + v_2$ is the Lebesgue decomposition of $v$ with respect to $\iota$, then $v_j \in M(X)$ ($j = 1, 2$).

(20.52) Exercise. More on the structure of $\mathfrak{C}_{00}(X)$ and $\mathfrak{C}_0(X)$. (a) Let $X$ be a nonvoid locally compact Hausdorff space, and let $M$ be a multiplicative linear functional on $\mathfrak{C}_0(X)$. By this we mean that $M$ satisfies (9.1.i) and (9.1.ii), that $M \neq 0$, and that $M(fg) = M(f)M(g)$ for all $f, g \in \mathfrak{C}_0(X)$. Prove that there is a point $a \in X$ such that $M(f) = E_a(f) = f(a)$ for all $f \in \mathfrak{C}_0(X)$. [Hints. It is convenient to prove first that $M$ is continuous. In fact, we have $|M(f)| \leq \|f\|_u$ for all $f \in \mathfrak{C}_0$. To see this, assume that $M(f) = \alpha$ where $|\alpha| > \|f\|_u$. Let $g = -\sum_{k=1}^{\infty} \alpha^{-k}f^k$. The series converges uniformly and so $g \in \mathfrak{C}_0$. Check that $\alpha^{-1}f + g - \alpha^{-1}fg = 0$. Then one has $0 = M(0) = \alpha^{-1}M(f) + M(g) - \alpha^{-1}M(f)M(g) = 1 + M(g) - M(g) = 1$.

Now knowing that $M$ is bounded, we apply (20.47) to write

$$M(f) = \int_X f \, d\mu = \int_X f \bar{g} \, d\iota$$

where $\mu \in M(X)$, $\i

and left ideals disappears, of course, and we use the term "ideal". An ideal is called maximal if the only ideal containing it properly is the entire algebra. In the commutative Banach algebra $\mathfrak{C}_0(X)$, every set $\{f \in \mathfrak{C}_0(X) : f(a) = 0\}$ is a closed maximal ideal. Furthermore, every maximal ideal [not assumed a priori to be closed] in $\mathfrak{C}_0(X)$ has this form. [All assertions are simple to verify except the last, for which the following hints are offered. If $\mathfrak{I}$ is an ideal in $\mathfrak{C}_0(X)$ and if there is a point $a \in X$ such that $f(a) = 0$ for all $f \in \mathfrak{I}$, then $\mathfrak{I}$ can be maximal only if $\mathfrak{I} = \{f \in \mathfrak{C}_0(X) : f(b) = 0\}$ for some $b \in X$. If $\mathfrak{I}$ is an ideal such that for all $a \in X, f(a) \neq 0$ for some $f \in \mathfrak{I}$, then a simple compactness argument, and the fact that $f \in \mathfrak{I}$ if $f \in \mathfrak{I}$, show that $\mathfrak{I} \supset \mathfrak{C}_{00}(X)$. Consider the algebra $\mathfrak{S} = \mathfrak{C}_0(X)/\mathfrak{I}$. It is a linear space over $K$ and also an algebra with no proper ideals at all. This implies that $\mathfrak{S}$ is a field or is $K$ as a linear space with all products equal to 0. Let $\tau$ denote the canonical mapping of $\mathfrak{C}_0(X)$ onto $\mathfrak{S}$: $\tau(f) = f + \mathfrak{I}$ for all $f \in \mathfrak{C}_0(X)$. If $\mathfrak{S}$ is a field, let $h$

(iii) $(P, P')$ is a Hahn decomposition for $\eta_s$;
(iv) $f = \infty$ on $B \cap P$ and $f = -\infty$ on $B \cap P'$.

It is obvious that this definition agrees with (19.43) in the case that $\eta \ll \mu$ [$\eta_s = 0$]. In this case we merely take $B = P = \emptyset$.

To see that such derivatives exist, let $B$ be any set in $\mathcal{A}$ such that (ii) holds $[\eta_s \perp \mu]$, let $(P, P')$ be any Hahn decomposition for $\eta_s$ (19.6), and let $f_0$ be any LEBESGUE-RADON-NIKODYM derivative of $\eta_a$ with respect to $\mu$ [apply (19.24) to $\eta_a^+$ and $\eta_a^-$ to obtain $f_0^+$ and $f_0^-$]. Now define $f$ by

$$f(x) = \begin{cases} f_0(x) & \text{for } x \in B', \\ \infty & \text{for } x \in B \cap P, \\ -\infty & \text{for } x \in B \cap P'. \end{cases}$$

Since $f = f_0 \mu$-a.e., it is clear that $f$ is a derivative.

The following lemma characterizing derivatives will be very useful. It has the advantage that it makes no mention of Lebesgue or Hahn decompositions.
