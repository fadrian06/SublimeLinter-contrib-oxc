function* quux(foo) {
  yield foo;
}

/**
 * @yields {undefined}
 * @yields {void}
 */
function* quux(foo) {}
