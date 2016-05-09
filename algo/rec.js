var fact = function (n) {
  return (n == 1) ? 1 : n * fact(n-1);
}



console.log( fact(7));
console.log( fact(10) == 10*9*8*7*6*5*4*3*2*1);
