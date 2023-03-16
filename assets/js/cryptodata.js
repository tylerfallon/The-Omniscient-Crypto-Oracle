async function initcryptodata() {
  console.log('test1')
  let response = await fetch('/getcryptodata')
  const cryptodata = await response.json();
  return cryptodata;
}

async function updateCryptoPrice() {
  let cryptoDataUpdated = await initcryptodata();
  document.querySelector('#cryptoprice').innerHTML = '$' + cryptoDataUpdated.price;
}

updateCryptoPrice();




async function initcryptopercentchange() {
  console.log('test2')
  let response = await fetch('/getpercentchange')
  const cryptodata = await response.json();
  return cryptodata;
}

async function updatePercentChange() {
  let percentChangeUpdated = await initcryptopercentchange();
  document.querySelector('#btcpercentchange').innerHTML = percentChangeUpdated.price + '%';
}

updateCryptoPrice();
updatePercentChange();