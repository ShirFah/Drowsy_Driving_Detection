[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest -Method POST `
  -Headers @{"Authorization" = "Bearer c8865525096a4609ae836f36a7aa6eb5"} `
  -ContentType "application/json" `
  -Uri https://sms.api.sinch.com/xms/v1/61ff676f98204fd2b893452646b0dd2a/batches `
  -Body '{
    "from": "447520651118",
    "to": [ "972545746881" ],
    "body": "The driver is asleep"
  }'