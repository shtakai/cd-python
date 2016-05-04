



var users = [
  {
  'id': 1,
  'first_name': 'Johnny',
  'last_name': 'Rotten',
  'created_at':'2012-12-31 23:59:59',
  'updated_at':'2012-12-31 23:59:59'
  },
  {
  'id': 2,
  'first_name': 'Amy',
  'last_name': 'Brown',
  'created_at':'2012-12-31 23:59:59',
  'updated_at':'2012-12-31 23:59:59'
  },
  {
  'id': 3,
  'first_name': 'Alice',
  'last_name': 'Roh',
  'created_at':'2012-12-31 23:59:59',
  'updated_at':'2012-12-31 23:59:59'
  },
];

var usersHaveBooks = [
  {
    'id':1,
    'user_id':1,
    'book_id':1,
    'created_at':'2012-12-31 23:59:59',
    'updated_at':'2012-12-31 23:59:59'
  },
  {
    'id':2,
    'user_id':1,
    'book_id':2,
    'created_at':'2012-12-31 23:59:59',
    'updated_at':'2012-12-31 23:59:59'
  },
  {
    'id':3,
    'user_id':1,
    'book_id':3,
    'created_at':'2012-12-31 23:59:59',
    'updated_at':'2012-12-31 23:59:59'
  },
  {
    'id':4,
    'user_id':2,
    'book_id':2,
    'created_at':'2012-12-31 23:59:59',
    'updated_at':'2012-12-31 23:59:59'
  },

];

var books = [
  {
  'id': 1,
  'book_title': 'Grapes of Wrath',
  'book_subject': 'The hard life during the depression',
  'created_at':'2012-12-31 23:59:59',
  'updated_at':'2012-12-31 23:59:59'
  },
  {
  'id': 2,
  'book_title': 'Metamorphosis',
  'book_subject': 'The degradation of humanity, reflected in a single man',
  'created_at':'2015-01-12 23:59:59',
  'updated_at':'2015-01-12 23:59:59'
  },
  {
  'id': 3,
  'book_title': 'The Coming Plague',
  'book_subject': 'Infectious diseases',
  'created_at':'2015-01-12 23:59:59',
  'updated_at':'2015-01-12 23:59:59'
  },
];








console.log(innerjoin(users, books, usersHaveBooks));


function innerjoin(users, books, usersHaveBooks){
    var resultArr = [];
    //console.log("usersHaveBooks", usersHaveBooks);
    for(var i in usersHaveBooks){
         var usersHaveBook = usersHaveBooks[i];
         var user_id = usersHaveBook.user_id;
         var user = users[user_id - 1];
         var book_id = usersHaveBook.book_id;
         var book = books[book_id - 1];
         if( user != null && book != null ){
            resultArr.push([user, book, usersHaveBook ]);
         }

    }
    return resultArr;



}
