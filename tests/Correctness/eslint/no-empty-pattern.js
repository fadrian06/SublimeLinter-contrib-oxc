var {} = foo;
var [] = foo;
var {a: {}} = foo;
var {a: []} = foo;
function foo({}) {}
function foo([]) {}
function foo({a: {}}) {}
function foo({a: []}) {}
