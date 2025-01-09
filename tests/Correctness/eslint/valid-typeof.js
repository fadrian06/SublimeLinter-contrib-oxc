// requireStringLiterals: false
// incorrect:
typeof foo === "strnig";
// correct:
typeof foo === "string";
typeof foo === baz;

// requireStringLiterals: true
// incorrect:
typeof foo === baz;
