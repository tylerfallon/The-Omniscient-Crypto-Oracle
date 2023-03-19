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
  console.log('ethdata1')
  let response = await fetch('/getethdata')
  const ethdata = await response.json();
  return ethdata;
}

async function updateETHPrice() {
  let ETHDataUpdated = await initethdata();
  document.querySelector('#ethprice').innerHTML = '$' + ETHDataUpdated.price;
}

async function initltcdata() {
  console.log('ltcdata1')
  let response = await fetch('/getltcdata')
  const ltcdata = await response.json();
  return ltcdata;
}

async function updateLTCPrice() {
  let LTCDataUpdated = await initltcdata();
  document.querySelector('#ltcprice').innerHTML = '$' + LTCDataUpdated.price;
}

async function initdogedata() {
  console.log('dogedata1')
  let response = await fetch('/getdogedata')
  const dogedata = await response.json();
  return dogedata;
}

async function updateDOGEPrice() {
  let DOGEDataUpdated = await initdogedata();
  document.querySelector('#dogeprice').innerHTML = '$' + DOGEDataUpdated.price;
}

async function initXRPdata() {
  console.log('XRPdata1')
  let response = await fetch('/getXRPdata')
  const XRPdata = await response.json();
  return XRPdata;
}

async function updateXRPPrice() {
  let XRPDataUpdated = await initXRPdata();
  document.querySelector('#xrpprice').innerHTML = '$' + XRPDataUpdated.price;
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

async function initethpercentchange() {
  console.log('ETH percent change')
  let response = await fetch('/getethpercentchange')
  const ethchangedata = await response.json();
  return ethchangedata;
}

async function updateETHPercentChange() {
  let percentETHChangeUpdated = await initethpercentchange();
  document.querySelector('#ethpercentchange').innerHTML = percentETHChangeUpdated.price + '%';
}

async function initltcpercentchange() {
  console.log('LTC percent change')
  let response = await fetch('/getltcpercentchange')
  const ltcchangedata = await response.json();
  return ltcchangedata;
}

async function updateLTCPercentChange() {
  let percentLTCChangeUpdated = await initltcpercentchange();
  document.querySelector('#ltcpercentchange').innerHTML = percentLTCChangeUpdated.price + '%';
}

async function initDOGEpercentchange() {
  console.log('DOGE percent change')
  let response = await fetch('/getdogepercentchange')
  const dogechangedata = await response.json();
  return dogechangedata;
}

async function updateDOGEPercentChange() {
  let percentDOGEChangeUpdated = await initDOGEpercentchange();
  document.querySelector('#dogepercentchange').innerHTML = percentDOGEChangeUpdated.price + '%';
}

async function initXRPpercentchange() {
  console.log('XRP percent change')
  let response = await fetch('/getxrppercentchange')
  const xrpchangedata = await response.json();
  return xrpchangedata;
}

async function updateXRPPercentChange() {
  let percentXRPChangeUpdated = await initXRPpercentchange();
  document.querySelector('#xrppercentchange').innerHTML = percentXRPChangeUpdated.price + '%';
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

updateCryptoPrice();
updatePercentChange();
updateMarketType();
updateETHPrice()
updateDOGEPrice()
updateLTCPrice()
updateXRPPrice()
updateETHPercentChange();
updateLTCPercentChange();
updateDOGEPercentChange();
updateXRPPercentChange();