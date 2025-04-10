window.MathJax = {
  tex: {
    inlineMath: [ ["\\(","\\)"] ], // Looks for \( ... \)
    displayMath: [ ["\\[","\\]"] ], // Looks for \[ ... \]
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex" // Crucial: Only process elements with this class
  },
  // Optional but good defaults
  chtml: {
    matchFontHeight: true
  },
  loader: {
    load: ['input/tex', 'output/chtml']
  }
};
// console.log("MathJax Config Loaded"); // Uncomment for debugging