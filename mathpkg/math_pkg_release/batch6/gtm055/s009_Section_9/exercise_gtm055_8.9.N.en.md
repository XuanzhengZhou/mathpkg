---
role: exercise
locale: en
chapter: "8"
section: "9"
exercise_number: N
---

Let $(X, \mathbf{S}, \mu)$ be a measure space, and suppose given a $\sigma$-ring $\mathbf{S}_0$ contained in $\mathbf{S}$ with the property that every set in $\mathbf{S}$ is almost equal $[\mu]$ to some set in $\mathbf{S}_0$. (In other words, for each set $E$ in $\mathbf{S}$ there is a set $E_0$ in $\mathbf{S}_0$ such that $\mu(E \nabla E_0) = 0$.) Show that every function measurable $[\mathbf{S}]$ on $X$ is equal a.e. $[\mu]$ to a function that is measurable $[\mathbf{S}_0]$. Hence for every integrable function $f$ on $(X, \mathbf{S}, \mu)$ there is a function $f_0$ on $X$ that is equal to $f$ a.e. $[\mu]$ such that $f_0$ is integrable $[\mu|\mathbf{S}_0]$ on $(X, \mathbf{S}_0)$ and such that
$$\int_X f d\mu = \int_X f_0 d(\mu|\mathbf{S}_0).$$
(Hint: Show that if $f$ is measurable $[\mathbf{S}]$ and if $\varepsilon > 0$, then there exists a function $f_\varepsilon$ that is measurable $[\mathbf{S}_0]$ and possesses the property that $|f - f_\varepsilon| \leq \varepsilon$ a.e. $[\mu]$. Construct a sequence of functions.)
