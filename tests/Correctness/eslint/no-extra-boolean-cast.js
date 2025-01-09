var foo = !!!bar;
var foo = Boolean(!!bar);

if (!!foo) {
}
if (Boolean(foo)) {
}

// with "enforceForLogicalOperands" option enabled
if (!!foo || bar) {
}
