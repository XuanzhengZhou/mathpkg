---
role: exercise
locale: en
chapter: "16"
section: "Section 17_Section_17"
exercise_number: 12
---

L. Let $\mathcal{E}$ be a separated locally convex space. Show that all hyperplanes and all closed half-spaces of $\mathcal{E}$ are also weakly closed (see Example I).

Show that the sequence $\{\sigma_n\}_{n=1}^{\infty}$ of pseudonorms on $\mathcal{E}^*$ induces the weak* topology on every ball $(\mathcal{E}^*)_r$, $r > 0$, and use this fact to prove that the (relative) weak* topology on $(\mathcal{E}^*)_r$ is metrizable. Conclude that the (relative) weak* topology is metrizable and satisfies the second axiom of countability on bounded subsets of $\mathcal{E}^*$. (Hint: The closed ball $(\mathcal{E}^*)_r$, $r > 0$, is compact in the weak* topology by Alaoglu's theorem (Th. 15.11).)

It is easy to give an explicit formula for a metric that induces the relative weak* topology on the ball $(\mathcal{E}^*)_r$ of Problem N. Indeed,

$$\rho(f, g) = \sum_{n=1}^{\infty} \frac{1}{2^n} \frac{|f(x_n) - g(x_n)|}{1 + |f(x_n) - g(x_n)|}, \quad f, g \in (\mathcal{E}^*)_r,$$

defines such a metric (see Proposition 11.32). Similarly the formula

$$\rho(x, y) = \sum_{n=1}^{\infty} \frac{1}{2^n} \frac{|f_n(x - y)|}{1 + |f_n(x - y)|}, \quad x, y \in \mathcal{E}_r,$$

defines explicitly a metric on the ball $\mathcal{E}_r$ of Problem M that induces the relative weak topology there.
