---
role: proof
locale: en
of_concept: proposition-9-13
source_book: gtm040
source_chapter: "9"
source_section: "1. Potentials"
---

We first compute the action of $P$ on ${}_0 N$:
$$(P {}_0 N)_{ij} = \sum_{k} P_{ik} \, {}_0 N_{kj} = \begin{cases}
0 & \text{if } j = 0 \text{ since } {}_0 N_{k0} = 0 \\
{}_0 \bar{N}_{0j} = \frac{\alpha_j}{\alpha_0} & \text{if } i = 0 \text{ and } j \neq 0 \\
{}_0 N_{ij} - \delta_{ij} & \text{if } i \neq 0 \text{ and } j \neq 0.
\end{cases}$$

Then
$$((I-P){}_0 N)_{ij} = \begin{cases}
0 & \text{if } j = 0 \\
-\alpha_j/\alpha_0 & \text{if } i = 0 \text{ and } j \neq 0 \\
\delta_{ij} & \text{if } i \neq 0 \text{ and } j \neq 0.
\end{cases}$$

By Lemma 9-11, ${}_0 N f$ is finite-valued, hence associativity holds in $(I-P){}_0 N f$. We find
$$((I-P){}_0 N f)_i = \begin{cases}
\sum_{j \neq 0} \delta_{ij} f_j = f_i & \text{for } i \neq 0 \\
\sum_{j \neq 0} (-\frac{\alpha_j}{\alpha_0}) f_j = \frac{1}{\alpha_0}(\alpha_0 f_0) = f_0 & \text{for } i = 0,
\end{cases}$$
where we used $\alpha f = 0$ to obtain the last equality. Thus $(I-P){}_0 N f = f$. Hence
$$(I + P + \cdots + P^{n-1})f = (I + P + \cdots + P^{n-1})(I-P){}_0 N f = (I - P^n){}_0 N f = {}_0 N f - P^n({}_0 N f).$$
Taking limits as $n \to \infty$ gives the result.
