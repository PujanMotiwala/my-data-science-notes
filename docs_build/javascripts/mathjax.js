// docs/javascripts/mathjax.js
window.MathJax = {
    tex: {
      inlineMath: [["\\(", "\\)"]], // Use \( ... \) for inline
      displayMath: [["\\[", "\\]"]], // Use \[ ... \] for display
      processEscapes: true,
      processEnvironments: true
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    }
  };