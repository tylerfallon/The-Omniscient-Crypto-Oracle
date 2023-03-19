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

async function initethdata() {
  console.log('ethprice')
  let response = await fetch('/getethcryptodata')
  const ethdata = await response.json();
  return ethdata;
}

async function updateETHPrice() {
  let ETHDataUpdated = await initcryptodata();
  document.querySelector('#ethcryptoprice').innerHTML = '$' + ETHDataUpdated.price;
}



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


async function initMarketType() {
  console.log('test3')
  let response = await fetch('/getmarkettype')
  const cryptodata = await response.json();
  return cryptodata;
}

async function updateMarketType() {
  let marketType = await initMarketType();
  document.querySelector('#bullvsbear').innerHTML = marketType;
}

// d3.csv("filename").then(data=>{
//   console.log(data);
// })

updateCryptoPrice();
updatePercentChange();
updateMarketType();
updateETHPrice() 