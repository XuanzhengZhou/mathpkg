---
role: proof
locale: en
of_concept: theorem-94
source_book: gtm077
source_chapter: "30"
source_section: "Second Type of Decomposition Theorem for Rational Primes"
---

# Proof of Theorem 94

The proof is along the lines of Minkowski's contribution to the geometry of numbers. To begin with we ask: "What can we say about the quantities $\varkappa$ if the $n$ inequalities

$$|L_p(x)| \leq \varkappa_p \quad (p = 1, \ldots, n)$$

have no solution in rational integers $x_q \neq 0$?" We show that under these conditions $\varkappa_1 \cdot \varkappa_2 \cdot \cdots \cdot \varkappa_n < |D|$.

To this end, we consider the parallelotope in the space of $n$ dimensions with Cartesian coordinates $x_1, \ldots, x_n$ such that

$$|L_p(x)| \leq \frac{\varkappa_p}{2} \quad (p = 1, 2, \ldots, n)$$

and think of the same parallelotope displaced parallel to itself so that its center (the point $0, \ldots, 0$) corresponds to all lattice points $g_1, \ldots, g_n$, where the $g_i$ run through all rational integers. In this way we have infinitely many parallelotopes $\Pi_{g_1, \ldots, g_n}$.

Consequently the sum of the volumes of all the $\Pi$ which belong to a definite square $|x_q| \leq L$ ($q = 1, 2, \ldots, n$) must be less than the volume $(2L)^n$ of this square, from which the assertion follows immediately. To see this we first let $c$ be a number such that the coordinates of all points of the initial figure $\Pi_{0, \ldots, 0}$ are all $\leq c$ in absolute value. Then in any case all $\Pi_{g_1, \ldots, g_n}$ such that

$$|g_q| \leq L \quad (q = 1, \ldots, n)$$

belong to the square $|x_q| \leq L + c$. Hence if $L$ is a positive rational integer, then there are $(2L + 1)^n$ such $\Pi_{g_1, \ldots, g_n}$ and their total volume is

$$(2L + 1)^n J \leq (2L + 2c)^n,$$

where $J$ is the volume of a single $\Pi$. After division by $L^n$ and passage to the limit as $L \to \infty$ it follows that

$$J \leq 1.$$

On the other hand we have

$$J = \int \cdots \int_{|L_p(x)| \leq \varkappa_p/2} dx_1 \cdots dx_n = \frac{1}{|D|} \int \cdots \int_{|y_p| \leq \varkappa_p/2} dy_1 \cdots dy_n = \frac{\varkappa_1 \varkappa_2 \cdots \varkappa_n}{|D|}.$$

Thus if these inequalities cannot be solved in integers except $0, \ldots, 0$, then $\varkappa_1 \cdots \varkappa_n \leq |D|$.

By contraposition: if $\varkappa_1 \cdots \varkappa_n \geq |D|$, there must exist a nonzero integer solution.
