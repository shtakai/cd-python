var fact = function (n) {
  if (n == 1) {
    return 1;
  }
  return n * fact(n-1)
}



console.log( fact(7));
console.log( fact(10) == 10*9*8*7*6*5*4*3*2*1);
