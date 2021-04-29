async function getCountryName(code) {
//   // write your code here
//   // API endpoint: https://jsonmock.hackerrank.com/api/countries?page=<PAGE_NUMBER>

  let page_number = 1;
  let has_country_name = false;
  while (has_country_name == false) {
    await https.get(`https://jsonmock.hackerrank.com/api/countries?page=${page_number}`, (resp) => {
        let data = '';

        resp.on('data', (chunk) => {
            data += chunk
        })

        resp.on('end', () => {
            console.log(JSON.parse(data).explanation)
        })
    }).on('error', (err) => {
        console.log("ERROR:" + err.message)
    })

    has_country_name = true
}
    
}

