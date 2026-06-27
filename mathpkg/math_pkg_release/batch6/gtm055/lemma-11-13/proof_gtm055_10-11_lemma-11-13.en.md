---
role: proof
locale: en
of_concept: lemma-11-13
source_book: gtm055
source_chapter: "10-11"
source_section: "Section 12_Section_12"
---

Proof. It suffices to show that if $\varepsilon$ is a given positive number, then there exists a positive number $\delta$ such that $|\alpha| < \delta$ implies $|\alpha x| < \varepsilon$. Moreover, for given $\varepsilon > 0$ we know that there exists $\delta > 0$ such that $|\alpha| < \delta$ and $|\alpha y| < \delta$ imply $|x + y| < \varepsilon$ (since the mapping $(x, y) \to x + y$ is continuous at $(0, 0)$). Hence, in particular, if $|\alpha| < \delta$, then $|2x| < \varepsilon$. In other words, the very special dilatation $x \to 2x$ is continuous. But then (by induction) all of the dilatations $x \to 2^n x$ are continuous. Choose $n$ so that $|\alpha| \leq 2^n$, and for given positive $\varepsilon$ choose a positive number $\delta$ such that $|\alpha| < \delta$ implies $|2^n x| < \varepsilon$. Then $|\alpha x| = |(\alpha/2^n)2^n x| \leq |2^n x|

Example I. The function $f(t) = t/(1 + t)$ is a strictly increasing, continuous function on the ray $[0, +\infty)$ that vanishes at $t = 0$ and satisfies the condition

$$f(s + t) \leq f(s) + f(t).$$

From these observations it follows at once that if $|I|$ is a given quasinorm on a linear space $\mathcal{E}$, then

$$|x|_0 = \frac{|x|}{1 + |x|}, \quad x \in \mathcal{E},$$

defines a new quasinorm on $\mathcal{E}$. The metric defined on $\mathcal{E}$ by $|I|_0$ is easily seen to be equivalent to the metric defined by the original quasinorm $|I|$, so the topologies induced by these two quasinorms coincide. Two quasinorms on the same linear space that induce the same topology are said to be equivalent. Thus the quasinorm $|I|_0$ is equivalent to the given one. (The reader may wish to consult Example 4A in connection with this example.)

Example J. If $\mathcal{E}_1, \ldots, \mathcal{E}_n$ are quasinormed spaces, then it is easily seen that

$$|(x_1, \ldots, x_n)| = \sum_{i=1}^{n}|x_i|$$

defines a quasinorm on $\mathcal{E}_1 + \cdots + \mathcal{E}_n$. Likewise, if $\{\mathcal{E}_n\}_{n=0}^{\infty}$ is an infinite sequence of quasinormed spaces, then

$$\{x_n\}_{n=0}^{\infty} = \sum_{n=0}^{\infty} \frac{1}{2^n} \frac{|x_n|}{1 + |x_n|}$$

defines a quasinorm on the full algebraic direct sum $\sum_{n \in \mathbb{N}_0} + \mathcal{E}_n$. Indeed, in both the finite case and the infinite case, conditions (i), (ii'') and (iii) in the definition of a quasinorm are trivial to verify directly (using the construction in

Example K. Let $(X, S, \mu)$ be a finite measure space (Ch. 7, p.118), let $M$ denote the linear space of all complex-valued measurable functions on $X$, and let $\dot{M}$ be the quotient space of equivalence classes $[f]$ of functions in $M$, where $f$ and $g$ are equivalent if and only if $f = g$ a.e. $[\mu]$ (see Chapter 7 for definitions). Using the same calculations as in Example I, it is easy to see that

$$|[f]| = \int_X \frac{|f|}{1 + |f|} d\mu, \quad f \in M,$$

defines a quasinorm on $\dot{M}$. If $f$ and $g$ are two functions in $M$, and if we write $E_\varepsilon = \{x \in X : |f(x) - g(x)| > \varepsilon\}$, then straightforward computation shows that

$$\frac{\varepsilon \mu(E_\varepsilon)}{1 + \varepsilon} \leq \int_{E_\varepsilon} \frac{|f - g|}{1 + |f - g|} d\mu$$

$$\leq \int_X \frac{|f - g|}{1 + |f - g|} d\mu \leq \varepsilon \mu(X \setminus E_\varepsilon) + \mu(E_\varepsilon),$$

and hence that

$$\frac{\varepsilon \mu(E_\varepsilon)}{1 + \varepsilon} \leq |f - g| \leq \varepsilon \mu(X \setminus E_\varepsilon) + \mu(E_\varepsilon).$$

It follows that if $f$ is a function in $M$ and $\{f_n\}$ a sequence of functions in $M$, then $|[f] - [f_n]| \to 0$ if and only if $\{f_n\}$ converges to $f$ in measure (Prob. 7X). For this reason the invariant metric defined on $\dot{M}$ by the quasinorm $||$ is known as the metric of convergence in measure.

Just as in the case of a normed space, completeness is an

then

$$|X_k - X_m| < \sum_{n=0}^{N} |x_n^{(k)} - x_n^{(m)}| + \frac{\varepsilon}{2}$$

for all $k, m$ in $\mathbb{N}$, from which it follows at once that there exists a positive integer $K$ such that $|X_k - X_m| < \varepsilon$ whenever $k, m \geq K$. It results from this analysis (and that in Example J) that if each of the spaces $\mathcal{E}_n$ is complete, and if $\{X_k\}$ is a Cauchy sequence with respect to the quasinorm (12), then $\{X_k\}$ is termwise convergent, and therefore convergent with respect to the quasinorm (12); consequently $\sum_{n \in \mathbb{N}_0} + \mathcal{E}_n$ is complete. Thus the direct sum of a finite or countably infinite number of $F$-spaces, as constructed in Example J, is an $F$-space. Finally, the space $\dot{\mathcal{M}}$ in Example K is complete in the quasinorm defined there by virtue of the properties of convergence in measure (see Problem 7X).

It is important to know that every normed space can be embedded isometrically and isomorphically as a dense linear manifold in a Banach space, and likewise that every quasinormed space can be similarly embedded in an $F$-space.
