convertCoin(10.25);
convertCoin(22.99);

convertCoin(159.79);
convertCoin(3159.69);

function convertCoin(input) {
  var result = [{
    'name': 'dollar',
    'amount': 0,
    'cent': 100
  }, {
    'name': 'half-dollar',
    'amount': 0,
    'cent': 50
  }, {
    'name': 'quarter-dollar',
    'amount': 0,
    'cent': 25
  }, {
    'name': 'dime',
    'amount': 0,
    'cent': 10
  }, {
    'name': 'nickel',
    'amount': 0,
    'cent': 5
  }, {
    'name': 'pennie',
    'amount': 0,
    'cent': 1
  }];

  remain = parseInt(input * 100);

  for (var i in result) {
    result[i]['amount'] = parseInt(remain / result[i]['cent']);
    remain -= result[i]['cent'] * result[i]['amount'];
    // console.log('---');
    // console.log(result);
  }
  console.log();
  console.log('input(cent)', parseInt(input * 100) ,'cents');
  for (var i in result) {
    if(result[i]['amount'] > 0)
    console.log(result[i]['amount'] + ' ' + result[i]['name']);
  }


}
