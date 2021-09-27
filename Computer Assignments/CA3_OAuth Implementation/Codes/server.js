const axios = require('axios')
const express = require('express')
const app = express()
const port = 8589;
const clientID = '9151a1308bb204f757a5'
const clientSecret = 'fbec814d389c0899c65e8e039e6fbdc057b5db58'
const authorize_uri = 'https://github.com/login/oauth/authorize';
const redirect_uri = 'http://127.0.0.1:8589/oauth/redirect';

app.get('/oauth/redirect', async (req, res) => {
  console.log(`Github code is: ${req.query.code}`);
  const requestToken = req.query.code;
  console.log('authorization code:', requestToken);

  const tokenResponse = await axios({
    method: 'post',
    url: 'https://github.com/login/oauth/access_token?' +
      `client_id=${clientID}&` +
      `client_secret=${clientSecret}&` +
      `code=${requestToken}`,
    headers: {
      accept: 'application/json'
    }
  });

  const accessToken = tokenResponse.data.access_token;
  console.log(`access token: ${accessToken}`);

  const result = await axios({
    method: 'get',
    url: `https://api.github.com/user`,
    headers: {
      accept: 'application/json',
      Authorization: `token ${accessToken}`
    }
  });
  console.log(result.data);
  const name = result.data.name;

  res.send(result.data)
});

app.use(express.static('HTML'))

app.get('/', (req, res) => {
  res.send()
})
app.listen(port, () => {
  console.log(`server is listening on port: ${port}`)
});