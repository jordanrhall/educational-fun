# Some Basic Math Commands

The nice thing about Markdown is the incorporation of stylized mathematical typesetting. Via https://gitlab.com/gitlab-org/gitlab-foss/-/issues/33573, "The markdown guide for gitlab specifies a math mode that uses KaTeX to render math expressions using LaTex.
This used to work until recently but seems to be broken on the current release."

The rendering is still going to respect almost all of the syntax (commonly) used in LaTeX.

To write some math in-line, just wrap the "TeX" code in dollar signs (on outside) and single quotes (inside of dollar signs). 

For example, the standard form of a line in 2-space is given by $`ax + by + c = 0`$, where $`a,b,c`$ are real numbers, $`x`$ is (traditionally) an independent real-valued variable and $`y`$ a dependent real-valued variable.

To have display an equation more prominantly and in the center of the page, use

```math
ax + by + c = 0.
```

