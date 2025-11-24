from . import models
from . import wizard  # <-- زيد هادي 
from . import controllers  # <-- زيد هادي 

'''
fetch('/library/books', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    jsonrpc: "2.0",
    method: "call",
    params: {}
  })
})
.then(response => response.json())
.then(data => console.log(data.result));

'''