# Эндпоинты
## 1. /scan
**Сканирует указанный диапазон IP-адресов на доступность.**

### Метод:
```
POST
```

### Заголовки: 
```
Content-Type: application/json
```

### Тело запроса (JSON): 
```
{
  "network": "<CIDR-сеть>",
  "verbose": <true | false>
}
```
### Пример запроса: 
```
curl -X POST http://localhost:3000/scan \
-H "Content-Type: application/json" \
-d '{"network": "192.168.0.0/24", "verbose": false}'
```
### Пример ответа:
```
[
    "[#] Available: 25-11-2024 13:50:27 - 192.168.0.1 (response time 0.0731s)",
    "[#] Available: 25-11-2024 13:50:27 - 192.168.0.101 (response time 0.0218s)"
]
```

## 2. /sendhttp
**Отправляет HTTP-запрос по указанному адресу.**

### Метод:
```
POST
```

### Заголовки:
```
Content-Type: application/json
```

### Тело запроса (JSON):
```
{
  "Header": "<Ключ заголовка>",
  "Header-value": "<Значение заголовка>",
  "Target": "<URL-адрес>",
  "Method": "<HTTP-метод>",
  "Payload": <Данные запроса (JSON или строка)>
}
```

### Пример запроса:
```
curl -X POST http://localhost:3000/sendhttp \
-H "Content-Type: application/json" \
-d '{
    "Header": "Content-type",
    "Header-value": "text/plain",
    "Target": "https://jsonplaceholder.typicode.com/posts/1",
    "Method": "GET",
    "Payload": null
}'
```

### Пример ответа:
```
{
    "status_code": 200,
    "headers": {
        "Date": "Mon, 25 Nov 2024 13:59:14 GMT",
        "Content-Type": "application/json; charset=utf-8",
        "Transfer-Encoding": "chunked",
        "Connection": "keep-alive",
        ...
    },
    "content": "{\n  \"userId\": 1,\n  \"id\": 1,\n  \"title\": \"sunt aut facere repellat provident occaecati excepturi optio reprehenderit\",\n  \"body\": \"quia et suscipit\\nsuscipit recusandae consequuntur expedita et cum\\nreprehenderit molestiae ut ut quas totam\\nnostrum rerum est autem sunt rem eveniet architecto\"\n}"
}
```

