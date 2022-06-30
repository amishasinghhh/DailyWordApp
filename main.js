const axios = require('axios').default;
process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';
axios.get('https://krdict.korean.go.kr/api/search?certkey_no=3971&key=92425B7F6398BF034955A47FC88B8D6B&type_search=search&part=dfn&q=%EB%82%98%EB%AC%B4&sort=popular&translated=y&trans_lang=1')
  .then(function (response) {
    // handle success
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });