---
role: proof
locale: en
of_concept: proposition-49
source_book: gtm026
source_chapter: "1"
source_section: "3.30"
---

The proof is essentially the same in all cases. A finitely-generated $\mathbf{T}$-algebra $(\bar{Q}, \xi)$ is necessarily finite and we may define subsets $S_n, Q_n$ according to the following inductive scheme:

$$S_0 = \langle \emptyset \rangle$$

$Q_n$ is the set of minimal elements of $\bar{Q} - S_n$ if $S_n \neq \bar{Q}$, and need not be defined if

finite suprema (recall that $X$ has only one element here). It is easy to check that the $\mathbf{T}$-algebra $(Y^{X^*}, \theta_\#)$ of 3.18 is just the product $\mathbf{T}$-algebra $(Y, \theta)^{X^*}$ (see exercise 3).

Let us compute the realization $\bar{M}$ of 3.23. Here, $\bar{Q}$ is the image of $\bar{f}$: $X^*T \longrightarrow Y^{X^*}$ which, thinking of $\bar{f}$ as $(f^\#)_\#$, is just the closure under nonempty unions of the $X^*$-closure of $f \in Y^{X^*}$. Recalling from 2.3 that the $X$-dynamical structure on $Y^{X^*}$ is $g$, $x \longmapsto L_x.g$ (where $X = \{x\}$), the $X^*$-closure of $f$ is routinely computed:

$$f = a/b/c/d//ab/ac/ad$$
$$fx = b/c/d//ab/ac/ad$$
$$fx^2 = c/d//ab/ac/ad$$
$$fx^3 = d//ab/ac/ad$$
$$fx^{4+3k} = //ab/ac/ad$$
$$fx^{5+3k} = //ac/ad/ab$$
$$fx^{6+3k} = //ad/ab/ac$$

The inclusion relationships among $f, \ldots, fx^6$ are as shown below:

$$fx^4$$
$$fx^5$$
$$fx^6$$

It is clear from 3.25 that the join-irreducibles of $\bar{Q}$ are those elements of $f, \ldots, fx^6$ which cannot be written as the supremum of a subset of the remaining six. Checking that $fx^6 = f \cup fx^3$ (as remarked above, the semi-lattice structure in $Y^{X^*}$ is elementwise union), the join-irreducibles are then $Q = \{f, \ldots, fx^5\}$ as circled above

of $\bar{Q}$ a choice of representation as a supremum of elements of $Q$. To compute the corresponding $\lambda$-automaton with state set $Q$ as in 3.22 it is not necessary to know the value of $c$ on all elements of $\bar{Q}$ (which is fortunate since it requires considerable combinatorics to compute $\bar{Q}$). Thus, to define $\delta: Q \times X \longrightarrow QT$ we need only know the values of $c$ on elements of form $L_x.q$, that is, on the set $\{fx, \ldots, fx^6\}$. Recalling the proof of 3.23 (specifically, we refer to the formulas “$\tau_f = I\eta.r_f, \beta_f = \sigma_f.Y\Lambda$” of 2.18), $\bar{M}$ has $f \in \bar{Q}$ as initial state and has output map $g \longmapsto (\Lambda)g$; thus to define the initial state of the corresponding $\lambda$-automaton we need only the value of $c$ on $f$, and $c$ is not needed at all to define the output map. Of course, $qc = \{q\}$ (for $q$ in $Q$) is the only reasonable choice in view of the definition of “isolated element.” Moreover, $(fx^6)c = \{f, fx^3\}$ is forced since, as it happens, there is no other way to write $fx^6$ as a supremum of elements of $Q$. Hence there is only one $\lambda$-automaton which can be obtained as in 3.22 by scooping $\bar{M}$ (even though $c$ possibly extends in more than one way to $\bar{Q}$); it is given by:

$$f/\Lambda f = a \quad fx/b \quad fx^2/c \quad fx^3/d \quad fx^4/ab \quad fx^5/ac$$

It is already clear from 3.4 that $\bar{M}$ is not minimal in the sense of 3.27. Indeed, we can discover this five-state realization as follows. Let $\tilde{a}$ in $Y^{X^*}$ be constantly

corresponding $\lambda$-automaton is then

which is precisely the system of 3.4. The implicit $\lambda$-automaton $\bar{R}$ is not reachable as $\tilde{a}$ is not in $\bar{Q}$. The implicit $\lambda$-automaton $R^*$ which runs $R$ (3.20) is not reachable either since, e.g., $\{f, \tilde{a}\}$ cannot be reached. Nonetheless, $R$ is minimal (we leave to the reader the ad hoc argument that $f$ cannot be realized with only four states).
