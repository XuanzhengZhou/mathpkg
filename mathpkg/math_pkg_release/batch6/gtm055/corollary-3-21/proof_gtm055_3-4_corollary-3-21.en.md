---
role: proof
locale: en
of_concept: corollary-3-21
source_book: gtm055
source_chapter: "3-4"
source_section: "Section 05_Section_5"
---

Proof. It suffices to prove the first assertion of the corollary. The condition is clearly necessary

of $X$ into $\Pi = \prod_{\gamma} Y_{\gamma}$ is a homeomorphism of $X$ onto the subspace $F(X)$. (Such a mapping is called a topological embedding of $X$ in $\Pi$.)

**Example S.** A very important application of the foregoing construction arises when $X$ is a completely regular space. In this case let $\mathcal{F}$ denote the collection of all continuous mappings of $X$ into the unit interval $[0, 1]$, and note that the complete regularity of $X$ ensures that the topology inversely induced on $X$ by $\mathcal{F}$ coincides with the given topology. Moreover, the fact that $X$ is Hausdorff assures that $\mathcal{F}$ is separating on $X$. Thus we obtain the following result (Tihonov): If we write

$$F(x) = \{f(x)\}_{f \in \mathcal{F}}, x \in X,$$

then $F$ is a topological embedding of $X$ in $\Pi = \prod_{f} Y_{f}$, where $Y_{f} = [0, 1]$ for every $f$ in $\mathcal{F}$. Since $\Pi$ is a compact Hausdorff space (Th. 3.15), this construction shows that an arbitrary completely regular space can be topologically embedded in a compact Hausdorff space. Conversely, it is clear that every subspace of a compact Hausdorff space is completely regular (Prop. 3.4).

**PROBLEMS**

A. (i) The weight of a topological space $X$ is the minimum cardinal number that a base for the topology on $X$ can have. (Thus the second axiom of countability requires the weight of a space to be a countable cardinal number.) Show that if the weight of $X$ is an infinite cardinal number $c$ and if $\mathcal{B}$ is an arbitrary base for $X$, then $\mathcal{B}$ contains a base $\mathcal{B}_0$ having cardinal number $c$. (Hint: Recall Problem 1T.)

(ii) If $X$ is a topological space and $x$ is a point of $X$, then a neighborhood base at $x

sets in $\mathbb{R}$ are the closed intervals $[a, b]$, $a < b$. Show that the Cantor set (Ex. J) is perfect.

(iii) A point $x$ in a topological space $X$ is a condensation point of a set $A \subset X$ if the intersection $V \cap A$ is uncountable for every neighborhood $V$ of $x$. Show that if $X$ is a Hausdorff space satisfying the second axiom of countability, and if $F$ is a closed subset of $X$, then $F$ can be expressed as the (disjoint) union of two sets $A$ and $B$, where $A$ is a countable set while $B$ is a (perfect) set having the property that every point of $B$ is a condensation point of $B$. In particular, every closed set in $\mathbb{R}^n$ can be so expressed. (Hint: Set $B$ equal to the set of all condensation points of $F$.)

C. Let $K$ be a compact subset of a Hausdorff space $X$, and let $y$ be a point of $X$ such that $y \notin K$. Show that there exist disjoint open sets $U$ and $V$ in $X$ such that $K \subset U$ and $y \in V$. (Hint: For each point $x$ of $K$ there exist disjoint open sets $U_x$ and $V_x$ such that $x \in U_x$ and $y \in V_x$, and some finite collection of the sets $U_x$ suffices to cover $K$.) Use this fact to prove Propositions 3.2 and 3.4.

D. (i) It is clear that an ordinal number segment $W(\beta)$ has a greatest element if and only if $\beta$ is of the form $\alpha + 1$, in which case $W(\beta) = W(\alpha) \cup \{\alpha\}$. Show that an ordinal number segment $W(\beta)$, $\beta > 0$, is compact in the order topology if and only if $W(\beta)$ contains a greatest element, or, equivalently, if and only if $\beta$ is not a limit ordinal. Use this fact to show

(The ternary expansion (2) is not always unique since each triadic fraction $r = m/3^n$, $0 < r < 1$, possesses two ternary expansions, one ending in a sequence of zeros, the other in a sequence of twos. Every other real number in $[0, 1]$ has a unique ternary expansion.) Verify that the set $F_1$ in Example J consists precisely of those real numbers $t$ in $[0, 1]$ such that $\varepsilon_1 \neq 1$ in the representation (2). (If $t$ is a triadic fraction and therefore has two ternary expansions, then $t \in F_1$ if $\varepsilon_1 \neq 1$ in either of its expansions.) Pursue this line of reasoning to show that the Cantor set coincides with the set of all those numbers in the unit interval possessing a ternary expansion in which no digit $\varepsilon_n$ is equal to one. (Such expansions are sometimes said to be "one-free.")

F. Let $x$ be a point in a compact Hausdorff space $X$, and let $D$ denote the intersection of all of the closed-open subsets of $X$ that contain $x$. Show that $D$ coincides with the connected component of $x$, and use this fact to prove Proposition 3.14. (Hint: The hard part is to show that $D$ is connected. Suppose that $D = D_1 \cup D_2$, where $D_1$ and $D_2$ are closed and disjoint. Let $U_1$ and $U_2$ be disjoint open sets such that $D_i \subset U_i$, $i = 1, 2$ (Prop. 3.4). There exists a closed-open set $E$ such that $D \subset E \subset U_1 \cup U_2$.)

G. Show that the intersection of an arbitrary nonempty collection of topologies on a set $X$ is again a topology on $X$. Use this fact to prove that the collection of all topologies on $X$ is a complete lattice in the inclusion ordering. Show, in other words, that for an arbitrarily given family $\{\

J. It is well known that an infinite sequence $\{x_n\}$ in a topological space $X$ converges to a limit $y$ if and only if every subsequence of $\{x_n\}$ possesses a subsequence that converges to $y$. (Proof?) Show that it is also the case that a net $\{x_\lambda\}_{\lambda \in \Lambda}$ in a topological space $X$ converges to a limit $y$ if and only if every subnet of $\{x_\lambda\}$ possesses a subnet that converges to $y$.

K. Suppose that $X$ is a topological space that is not Hausdorff. Show that there exists a net in $X$ that converges to two distinct points of $X$. (Hint: Let $x$ and $y$ be distinct points of $X$ that do not possess disjoint neighborhoods, and turn the product $N(x) \times N(y)$ into a directed set.)

L. Every convergent sequence in $\mathbb{C}$ is bounded. Give an example of a net in $\mathbb{C}$ that converges but is not bounded.

M. Let $a$ and $b$ be real numbers, $a < b$, and let $f$ be a monotone real-valued function defined on $[a, b]$. Show that $f(c-) = \lim_{t \downarrow c} f(t)$ exists for every $a < c \leq b$, and likewise that $f(c+) = \lim_{t \downarrow c} f(t)$ exists for every $a \leq c < b$ (see Example P). Thus $f$ is continuous except for “jump” discontinuities. At each point $t$, $a < t < b$, let us define the jump in $f$ to be

$$\delta_t = |f(t+) - f(t-)|,$$

and set $\delta_a = |f(a+) - f(a)|, \delta_b = |f(b) - f(b-)|$. Show that

$$\sum_{a \leq t \leq b} \delta_t \leq |f(b) - f(a)|.$$

In the same vein verify that if $f$ is an arbitrary function of bounded variation on $[a,

According to this definition of limit, a function $f$ defined on a subset $A$ of a topological space $X$ possesses a limit at a point $x_0$ of $A$ when and only when $f$ is continuous at $x_0$ relative to $A$, in which event

$$\lim_{x \to x_0} f(x) = f(x_0).$$

In some contexts it is desirable to relax this rather stringent requirement. The slightly different definition of limit that the reader may have encountered elsewhere (notably in his elementary calculus textbook) corresponds in our notation to

$$\lim_{x \to x_0} f(x).$$

O. If $X$ is a topological space and $\{x_\lambda\}_{\lambda \in \Lambda}$ is a net in $X$, then a point $y$ in $X$ is a cluster point of $\{x_\lambda\}$ if for every neighborhood $V$ of $y$ and every $\lambda$ in $\Lambda$ there exists an index $\lambda'$ in $\Lambda$ such that $\lambda' \geq \lambda$ and $x_{\lambda'} \in V$.

(i) Let $\{x_\lambda\}_{\lambda \in \Lambda}$ be a net in a topological space $X$, and for each $\lambda$ in $\Lambda$ let $T_\lambda = \{x_\lambda' : \lambda' \geq \lambda\}$. Show that $y$ is a cluster point of the net $\{x_\lambda\}$ if and only if $y \in T_\lambda^-$ for every $\lambda$ in $\Lambda$.

(ii) Show that if $X$ is a Hausdorff space and a net $\{x_\lambda\}$ in $X$ converges to a limit $x_0$, then $x_0$ is the unique cluster point of the net $\{x_\lambda\}$.

P. A point $y$ in a topological space $X$ is a cluster point of a net $\{x_\lambda\}_{\lambda \in \Lambda}$ in $X$ if and only if some subnet of $\{x_\lambda\}$ converges to $y$. (Hint: Turn the product $\Lambda \times \mathcal{N}(y)$ into a directed set.) If $X$

finite intersection property and is directed under inverse-inclusion. For each $G$ in $\mathcal{G}$ choose a point $x_G$ in $G$, and consider the net $\{x_G\}_{G \in \mathcal{G}}$.

S. A collection $\mathcal{U}$ of subsets of a set $X$ is called an ultrafilter on $X$ if (a) $\mathcal{U}$ has the finite intersection property, and (b) $\mathcal{U}$ is maximal with respect to possessing the finite intersection property (in the inclusion ordering on the power class on the power class on $X$).

(i) Verify that if $\mathcal{U}$ is an arbitrary ultrafilter on a set $X$, and if $A$ is a subset of $X$ such that $A \cap E \neq \emptyset$ for every set $E$ in $\mathcal{U}$, then $A \in \mathcal{U}$. Show also that $\mathcal{U}$ is closed with respect to the formation of finite intersections, i.e., show that if $E_1, \ldots, E_n$ are sets belonging to $\mathcal{U}$, then $E_1 \cap \cdots \cap E_n$ belongs to $\mathcal{U}$.

(ii) Prove that a topological space $X$ is compact if and only if every ultrafilter on $X$ possesses an adherent point. (Hint: Use Zorn's lemma and Problem Q.)

T. Let $\mathcal{U}$ be an ultrafilter on a topological space $X$, and let $f$ be a continuous mapping of $X$ into a compact space $Y$. Show that there exists a point $y_0$ in $Y$ such that $f^{-1}(V) \in \mathcal{U}$ for every neighborhood $V$ of $y_0$ in $Y$, and use this fact to prove Theorem 3.15. (Hint: Choose $y_0$ to be an adherent point of the collection $\{f(E) : E \in \mathcal{U}\}$ of subsets of $Y$, and apply part (i) of Problem S. The hard part of the proof of Tihonov's theorem consists in showing that the product $X = \prod_{\gamma} Y_{\gamma}$ of

plank, is a locally compact Hausdorff space that is not normal. (The Tihonov plank is thus also an example of a completely regular space that is not normal.)

W. Let $X$ be a locally compact Hausdorff space. Show that there exists a compact Hausdorff space $\hat{X}$ such that $\hat{X}$ contains $X$ as a subspace and such that $\hat{X} \setminus X$ is a singleton $\{\omega\}$. Show also that $\hat{X}$ is unique in the sense that, if $\hat{X}$ is another compact Hausdorff space such that $\tilde{X}$ contains $X$ as a subspace and such that $\tilde{X} \setminus X$ is a singleton $\{\omega'\}$, then the identity mapping on $X$ extends to a homeomorphism between $\hat{X}$ and $\tilde{X}$ carrying $\omega$ to $\omega'$. The (essentially unique) space $\hat{X}$ is called the one-point compactification of $X$, and the point $\omega$ is known as the point at infinity in $\hat{X}$. Show that the one-point compactification $\hat{\mathbb{C}}$ of the complex plane $\mathbb{C}$ is homeomorphic to the two-dimensional sphere

$$S_2 = \{(x, y, z) \in \mathbb{R}^3 : x^2 + y^2 + (z - 1)^2 = 1\}.$$

(For this reason $\hat{\mathbb{C}}$ is frequently called the complex or Riemann sphere. The point at infinity in $\hat{\mathbb{C}}$ is denoted by $\infty$. It is important to note the distinction between the element $\infty$ of $\hat{\mathbb{C}}$ and the elements $\pm \infty$ of $\mathbb{R}^3$.)

4 Metric spaces

We assume the reader to be familiar with the notion of a metric space, and with the elementary concepts associated with the theory of metric spaces. In this chapter we briefly review some of these concepts, largely to fix notation and terminology. (An exception is our treatment of the theory of Baire categories; we do not assume any prior knowledge of this topic.) In particular, the reader is assumed to be acquainted with the notion of a bounded set, the diameter of a bounded set $A$ (notation: diam $A$), the distance between a point $x$ and a set $A$ (notation: $d(x, A)$), and the distance between two sets $A$ and $B$ (notation: $d(A, B)$), in a metric space. The reader is also assumed to be familiar with the notion of the metric topology on a metric space, and with the elementary properties of a metric space regarded as a topological space. In particular, the following result is assumed known (see Problem 3I).
