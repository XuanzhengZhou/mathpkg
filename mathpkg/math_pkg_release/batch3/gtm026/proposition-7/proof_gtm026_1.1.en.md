---
role: proof
locale: en
of_concept: proposition-7
source_book: gtm026
source_chapter: "1"
source_section: "1.6"
---

Suppose $p_i: A \longrightarrow A_i$ and $q_i: B \longrightarrow A_i$ are both products of $(A_i)$. Consider the unique induced maps as shown below:

Then $(fg)p_i = f(gp_i) = fq_i = p_i = (\text{id}_A)p_i$ for all $i \in I$, which proves $fg = \text{id}_A$. Similarly, $gf = \text{id}_B$. Therefore $f$ is an isomorphism transforming one set of projections into the other (which would seem to be as isomorphic as two products could possibly be without being equal).

Two things are worth noticing in the above proof: it works for all universal properties; it required two of the three category axioms.

Because of 1.6, we can think in terms of the product of $(A_i)$ and write it as $\prod A_i$. In practice, "$\prod A_i$" is either any convenient choice of—or the isomorphism class of all—$I$-tuples $p_i: A \longrightarrow A_i$ with the universal property; for most categorical purposes, these distinctions do not matter. In some contexts, the notation "$\prod A_i$" means just the object $A$, e.g. as in "consider $p_j: \prod A_j \longrightarrow A_j$" which is synonymous with "let $p_i: A \longrightarrow A_i$ be a product of $(A_i)$".

The "size" of a product is the size of $I$. The smallest product is the empty product (i.e., $I$ is empty), which it is standard to call a terminal object of $\mathcal{

and so on accordingly as $\prod A_i$ exists for finite families, for countable families, et cetera.

Several examples follow and more appear in the exercises.

1.7 Example. Set has products, the usual ones. The category of finite sets and functions has finite products (the usual ones). The fact that an infinite product (in the usual sense) of finite sets is not necessarily finite strongly suggests but does not prove that finite sets does not have products. To justify our intuition, notice that morphisms $1 \rightarrow X$ are essentially the same thing as elements of $X$. Using the universal property of a product, this proves that the elements of $\prod A_i$ are indeed in bijective correspondence with the elements of the usual product.

1.8 Example. The category of topological spaces and continuous functions has products; one provides the usual cartesian product set with what is normally called the product topology, or the topology of pointwise convergence. A net $(a_i, \alpha)$ converges to $(a_i)$ in $\prod A_i$ if and only if for all $i, a_i, \alpha$ converges to $a_i$. This statement both characterizes the product topology and amounts to the universal property.

1.9 Example. The category of metric spaces and distance-decreasing maps (we call the function $f:(X, d) \rightarrow (X', d')$ distance decreasing if for all $x, y \in X$, $d'(xf, yf) \leq d(x, y)$) has finite products and many other—but not all—products. Since all constant functions are distance decreasing, we can use the one-element metric space as in 1.7 to argue that if $(A, d) = \prod (A_i, d_i)$ $A$ must be the usual product of the sets $A_i$. Because projections must be distance decreasing, we must have $d((a_i), (b_i)) \leq \sup(d_i(a_i, b_i): i \in I)$. It is now easy to prove that $\prod (A_i, d_i)$ exists if and only if $\sup(d_i(a_i, b_i): i \in I)$ is finite for every pair $(a_i), (b_i)$ in the usual product set $A$; and then $(A, d)$ is the product where $d$

Although 1.4.27 was nominally restricted to Set, the reasoning there is perfectly general and proves that $(A, \xi)$ is a T-algebra. It remains to establish the universal property. Suppose we have given T-homomorphisms $f_i:(B, \theta) \longrightarrow (A_i, \xi_i)$. There exists a unique $\mathcal{K}$-morphism $f:B \longrightarrow A$ such that $f.p_i = f_i$ for all $i$. In the diagram below, we must show that the leftmost square commutes given that all the outer rectangles do. But this follows immediately from the universal property, since the leftmost square is commutative followed by each $p_i$.

The above proposition is our first encounter with "categorical universal algebra."

In all of the examples of products so far, there is no evidence that the underlying set of the product structured set, when it exists, is not always the usual product set. The following is such a counterexample.

1.12 Example. Consider the category whose objects are metric spaces with base point $(X, d, \bar{x})$ (the "base point" $\bar{x}$ is simply an arbitrary element of $X$) and distance-decreasing base-point preserving (i.e., $xf = x'$) functions. Every family $(X_i, d_i, \bar{x}_i)$ has a product $(X, d, x)$ where $X$ is the subset of the usual product of the $X_i$ consisting of all tuples $(x_i)$ with the property that $\text{Sup}(d_i(x_i, \bar{x}_i))$ is finite. As in 1.9, $d$ is defined by $d((x_i), (y_i)) = \text{Sup}(d_i(x_i, y_i)): i \in I$ which is guaranteed to be finite by the definition of $X$ and the fact that each $d_i$ satisfies the triangle inequality. $(\bar{x}_i)$ provides the base point. The projections are the restrictions of the usual ones. In general, $X$ is a proper subset of the usual product set.

1.13 Equalizers. Given sets $A_1, A_2$ and two functions $f, g:A_1 \long

tained in $A, h$ is defined by $a'h = a'i'$. Given morphisms $f, g: A_1 \rightarrow A_2$ in a category $\mathcal{K}$, an equalizer of $(f, g)$ is an object $E$ and a morphism $i: E \rightarrow A$ with the following universal property:

(1) $i.f = i.g$

(2) Given $i'$ with $i'.f = i'.g$, there exists unique $h$ with $h.i = i'$.

By the same sort of reasoning as in 1.6, equalizers are unique up to isomorphism. We speak of the equalizer of $f$ and $g$ and write $\text{eq}(f, g)$ to denote any convenient representative of—or the entire isomorphism class of—all equalizers $i: E \rightarrow A$ of $f, g: A_1 \rightarrow A_2$. $\mathcal{K}$ has equalizers if $\text{eq}(f, g)$ exists for every pair $f, g: A_1 \rightarrow A_2$.

Most categories of sets with structure have equalizers via the appropriate "substructure" on the subset of points on which $f$ and $g$ agree. For topological spaces, use the relative topology. For metric spaces (either 1.9 or 1.12) just restrict the metric to the subset. For groups and homomorphisms, the subset in question is a subgroup. The latter, or course, is another instance of categorical universal algebra.
